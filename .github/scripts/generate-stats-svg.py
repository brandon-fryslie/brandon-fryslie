#!/usr/bin/env python3
"""
Generate the daily GitHub stats data + a fallback stats card.

Picks 4 metrics (from 8) with varying time periods each day (seeded by the date) and
queries GitHub for their exact values. It then writes two things:

  * assets/daily-stats.json — the *data seam*: the four exact values, labels, and
    periods. This is the source of truth the doodle job's Claude reads to author a
    fresh, radically-different-each-day stats card. The verify step
    (`--verify-svg PATH`) checks that authored card against this JSON, so a wrong or
    missing number fails the run instead of shipping.

  * a deterministic fallback SVG (`--svg-out PATH`) — an always-valid, always-legible
    animated dark card (palette + motif seeded off the date). It backstops the
    creative step: if the LLM-authored card can't be made legible/accurate, the job
    falls back to this. Never a broken card. [LAW:no-silent-failure]

Data sourcing — read this before touching a query:

  * Pure counts (commits, PRs, reviews, issues) come from the REST *search* API's
    `total_count`, which is accurate at any magnitude. Only *retrieving items* past
    1000 is capped; the count itself is not.

  * Enumeration metrics (days active, active repos, languages) do NOT use search.
    Search caps item retrieval at 1000 results, which silently truncated these to a
    fraction of reality (e.g. Days Active 1y read 101 when the truth was 252). They
    now come from the GraphQL `contributionsCollection` — the same data that draws
    the profile contribution graph — which is exact and includes org repos. Its only
    limit is a 1-year span per query, so all-time is stitched from consecutive
    ≤1-year windows. See GitHubData.contribution_scope. [LAW:one-source-of-truth]
"""

import argparse
import hashlib
import json
import math
import os
import random
import sys
from datetime import datetime, timedelta, timezone
from urllib.parse import quote

try:
    import requests

    HAS_REQUESTS = True
except ImportError:
    import urllib.error
    import urllib.request

    HAS_REQUESTS = False

# ─── Configuration ──────────────────────────────────────────

USERNAME = "brandon-fryslie"
STATS_PATH = "assets/daily-stats.svg"
JSON_PATH = "assets/daily-stats.json"
API_TIMEOUT = 30  # seconds
GRAPHQL_URL = "https://api.github.com/graphql"
FONT = (
    "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
)

# Dark-profile chrome to match the doodle above it and GitHub's dark README.
BG = "#0d1117"
CARD = "#11161d"
BORDER = "#21262d"
TITLE = "#e6edf3"
LABEL = "#9aa4b2"
SUB = "#6e7681"
TRACK = "#1c2430"

# ─── Time Periods ───────────────────────────────────────────

PERIOD_DAYS = {"7d": 7, "30d": 30, "1y": 365, "all": None}
PERIOD_LABELS = {"7d": "7 Days", "30d": "30 Days", "1y": "1 Year", "all": "All Time"}

# ─── Metric Definitions ────────────────────────────────────
# Each metric: (display_label, list_of_valid_periods)

METRIC_DEFS = {
    "languages":     ("Languages",     ["30d", "1y", "all"]),
    "commits":       ("Commits",       ["7d", "30d", "1y", "all"]),
    "prs_merged":    ("PRs Merged",    ["7d", "30d", "1y", "all"]),
    "reviews":       ("Code Reviews",  ["30d", "1y", "all"]),
    "active_repos":  ("Active Repos",  ["7d", "30d", "1y"]),
    "days_active":   ("Days Active",   ["30d", "1y"]),
    "longest_streak": ("Longest Streak", ["1y"]),
    "issues_closed": ("My Issues Closed", ["30d", "1y", "all"]),
}


# ─── Errors ─────────────────────────────────────────────────

class GitHubAPIError(RuntimeError):
    def __init__(self, url, status, body):
        super().__init__(f"POST/GET {url} failed with status {status}: {body[:300]}")
        self.url = url
        self.status = status
        self.body = body


class SearchIncompleteError(RuntimeError):
    """GitHub set incomplete_results=true — its search timed out, so total_count is
    partial and must not be trusted as a real value. Fail loud instead of reporting a
    wrong (often zero) number. [LAW:no-silent-failure]"""

    def __init__(self, path, query):
        super().__init__(f"/search/{path} returned incomplete_results for: {query}")


class GraphQLError(RuntimeError):
    def __init__(self, messages):
        super().__init__("GraphQL errors: " + "; ".join(messages))


# ─── REST API Layer ─────────────────────────────────────────

def api_get(endpoint, token):
    """Single GitHub REST GET. Returns parsed JSON; raises GitHubAPIError on non-2xx
    so a rate-limit (403) or search cap (422) surfaces instead of a silent '—'."""
    url = f"https://api.github.com{endpoint}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    if HAS_REQUESTS:
        resp = requests.get(url, headers=headers, timeout=API_TIMEOUT)
        if not (200 <= resp.status_code < 300):
            raise GitHubAPIError(url, resp.status_code, resp.text)
        return resp.json()
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=API_TIMEOUT) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise GitHubAPIError(url, e.code, body) from e


def search_total_count(path, query, token):
    """total_count from a GitHub search endpoint. Accurate at any magnitude (the 1000
    cap only limits item *retrieval*, not the count). Loud-fails on incomplete_results
    so a timed-out search can't masquerade as a real number. [LAW:no-silent-failure]"""
    encoded_q = quote(query, safe="+:")
    data = api_get(f"/search/{path}?q={encoded_q}&per_page=1", token)
    if data.get("incomplete_results"):
        raise SearchIncompleteError(path, query)
    return data.get("total_count", 0)


# ─── GraphQL API Layer ──────────────────────────────────────

def api_graphql(query, variables, token):
    """POST a GraphQL query. Returns the `data` object; raises on transport errors or
    a top-level `errors` array (GraphQL returns 200 with errors). [LAW:no-silent-failure]"""
    body = json.dumps({"query": query, "variables": variables}).encode()
    headers = {
        "Authorization": f"bearer {token}",
        "Content-Type": "application/json",
    }
    if HAS_REQUESTS:
        resp = requests.post(GRAPHQL_URL, headers=headers, data=body, timeout=API_TIMEOUT)
        if not (200 <= resp.status_code < 300):
            raise GitHubAPIError(GRAPHQL_URL, resp.status_code, resp.text)
        payload = resp.json()
    else:
        req = urllib.request.Request(GRAPHQL_URL, data=body, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=API_TIMEOUT) as resp:
                payload = json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            raise GitHubAPIError(GRAPHQL_URL, e.code,
                                 e.read().decode("utf-8", errors="replace")) from e
    if payload.get("errors"):
        raise GraphQLError([e.get("message", "?") for e in payload["errors"]])
    return payload["data"]


CONTRIB_QUERY = """
query($login:String!, $from:DateTime!, $to:DateTime!) {
  user(login:$login) {
    contributionsCollection(from:$from, to:$to) {
      contributionCalendar { weeks { contributionDays { date contributionCount } } }
      commitContributionsByRepository(maxRepositories: 100) {
        contributions { totalCount }
        repository { nameWithOwner primaryLanguage { name } }
      }
    }
  }
}
"""

REPO_MAX = 100  # commitContributionsByRepository ceiling; hitting it makes repo/lang counts a floor.


# ─── Date Helpers ───────────────────────────────────────────

def _iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def cutoff_iso(period):
    """ISO date string for period start, or None for 'all'."""
    days = PERIOD_DAYS[period]
    if days is None:
        return None
    return _iso(datetime.now(timezone.utc) - timedelta(days=days))


def date_qualifier(period, field="committer-date"):
    """Search query fragment like '+committer-date:>2024-...' or empty."""
    since = cutoff_iso(period)
    return f"+{field}:>{since}" if since else ""


def year_windows(start, end):
    """Yield consecutive (from, to) datetimes covering [start, end], each ≤ 364 days
    so no window trips GraphQL's 'must not exceed 1 year' limit. This is the workaround
    for the per-query span cap: all-time is the union over these windows.

    Windows are disjoint, not merely consecutive: the next one starts one second past the
    previous window's inclusive `to`, so they partition [start, end] at GitHub's 1-second
    timestamp granularity. [LAW:one-source-of-truth] a commit at a boundary instant belongs
    to exactly one window — otherwise the summing path (_repo_commit_counts) would count it
    in both and inflate the repo/language breakdowns."""
    step = timedelta(days=364)
    cur = start
    while cur < end:
        nxt = min(cur + step, end)
        yield cur, nxt
        cur = nxt + timedelta(seconds=1)


# ─── Cached Data Fetcher ───────────────────────────────────

class GitHubData:
    """Fetches and caches GitHub data. REST for pure counts and repo metadata;
    GraphQL contributions for exact enumeration metrics."""

    def __init__(self, token):
        self.token = token
        self._user = None
        self._contrib = {}  # (from_iso, to_iso) -> contributionsCollection

    # -- account (REST) --

    def user(self):
        if self._user is None:
            self._user = api_get(f"/users/{USERNAME}", self.token)
        return self._user

    def account_created(self):
        return datetime.strptime(
            self.user()["created_at"], "%Y-%m-%dT%H:%M:%SZ"
        ).replace(tzinfo=timezone.utc)

    # -- pure counts (REST search total_count) --

    def commit_count(self, period):
        q = f"author:{USERNAME}{date_qualifier(period)}"
        return search_total_count("commits", q, self.token)

    def pr_merged_count(self, period):
        since = cutoff_iso(period)
        q = f"author:{USERNAME}+type:pr+is:merged"
        if since:
            q += f"+merged:>{since}"
        return search_total_count("issues", q, self.token)

    def review_count(self, period):
        since = cutoff_iso(period)
        q = f"reviewed-by:{USERNAME}+type:pr+-author:{USERNAME}"
        if since:
            q += f"+updated:>{since}"
        return search_total_count("issues", q, self.token)

    def issue_closed_count(self, period):
        since = cutoff_iso(period)
        q = f"author:{USERNAME}+type:issue+is:closed"
        if since:
            q += f"+closed:>{since}"
        return search_total_count("issues", q, self.token)

    # -- enumeration metrics (GraphQL contributions) --

    def _contributions(self, from_iso, to_iso):
        key = (from_iso, to_iso)
        if key not in self._contrib:
            data = api_graphql(
                CONTRIB_QUERY,
                {"login": USERNAME, "from": from_iso, "to": to_iso},
                self.token,
            )
            self._contrib[key] = data["user"]["contributionsCollection"]
        return self._contrib[key]

    def _window_scope(self, from_iso, to_iso):
        """(active_dates, repos, languages, capped) for one ≤1-year window."""
        c = self._contributions(from_iso, to_iso)
        lo, hi = from_iso[:10], to_iso[:10]
        active = {
            d["date"]
            for w in c["contributionCalendar"]["weeks"]
            for d in w["contributionDays"]
            if d["contributionCount"] > 0 and lo <= d["date"] <= hi
        }
        by_repo = c["commitContributionsByRepository"]
        repos = {r["repository"]["nameWithOwner"] for r in by_repo}
        langs = {
            r["repository"]["primaryLanguage"]["name"]
            for r in by_repo
            if r["repository"]["primaryLanguage"]
        }
        return active, repos, langs, len(by_repo) >= REPO_MAX

    def contribution_scope(self, period):
        """Union of (active days, repos, languages, capped) over the period, stitched
        from ≤1-year windows so neither the search 1000-cap nor the GraphQL 1-year-span
        cap can truncate the answer. `capped` means a window hit the 100-repo ceiling,
        making repo/language counts a floor rather than an exact value."""
        now = datetime.now(timezone.utc)
        days = PERIOD_DAYS[period]
        start = self.account_created() if days is None else now - timedelta(days=days)
        active, repos, langs, capped = set(), set(), set(), False
        for f, t in year_windows(start, now):
            a, r, l, cap = self._window_scope(_iso(f), _iso(t))
            active |= a
            repos |= r
            langs |= l
            capped = capped or cap
        return active, repos, langs, capped

    # -- distributions for meaningful visualizations (the rich seam) --

    def calendar_year(self):
        """{start, counts}: chronological daily contribution counts for the last 365
        days — a universal time-series for heatmaps/sparklines. Same 1y window the
        enumeration metrics use, so it's already cached."""
        now = datetime.now(timezone.utc)
        c = self._contributions(_iso(now - timedelta(days=365)), _iso(now))
        days = sorted(
            (d for w in c["contributionCalendar"]["weeks"] for d in w["contributionDays"]),
            key=lambda d: d["date"],
        )
        if not days:
            return {"start": (now - timedelta(days=365)).strftime("%Y-%m-%d"), "counts": []}
        return {"start": days[0]["date"], "counts": [d["contributionCount"] for d in days]}

    def _repo_commit_counts(self, period):
        """(repo_full_name -> commit count, repo_full_name -> primary language) over the
        period, aggregated across ≤1-year windows."""
        now = datetime.now(timezone.utc)
        days = PERIOD_DAYS[period]
        start = self.account_created() if days is None else now - timedelta(days=days)
        counts, langs = {}, {}
        for f, t in year_windows(start, now):
            c = self._contributions(_iso(f), _iso(t))
            for r in c["commitContributionsByRepository"]:
                name = r["repository"]["nameWithOwner"]
                counts[name] = counts.get(name, 0) + r["contributions"]["totalCount"]
                lang = (r["repository"].get("primaryLanguage") or {}).get("name")
                if lang:
                    langs[name] = lang
        return counts, langs

    def repo_breakdown(self, period, top=6):
        """Top repos by commit count over the period: [{name, count}] (repo basename)."""
        counts, _ = self._repo_commit_counts(period)
        ranked = sorted(counts.items(), key=lambda kv: -kv[1])[:top]
        return [{"name": name.split("/")[-1], "count": n} for name, n in ranked]

    def language_breakdown(self, period, top=8):
        """Languages by commit count over the period: [{name, count}]."""
        counts, langs = self._repo_commit_counts(period)
        agg = {}
        for name, n in counts.items():
            lang = langs.get(name)
            if lang:
                agg[lang] = agg.get(lang, 0) + n
        ranked = sorted(agg.items(), key=lambda kv: -kv[1])[:top]
        return [{"name": name, "count": n} for name, n in ranked]


# ─── Metric Computation ────────────────────────────────────

def floor_str(n, capped):
    """A count that could be truncated by an upstream cap is a *floor*, not a truth.
    Render it 'n+' so an undercount can't pose as an exact value. [LAW:no-silent-failure]"""
    return f"{n}+" if capped else n


def compute_metric(name, period, data):
    """Compute a single metric value. Returns an int, an 'n+' floor string, or raises."""
    if name == "commits":
        return data.commit_count(period)
    if name == "prs_merged":
        return data.pr_merged_count(period)
    if name == "reviews":
        return data.review_count(period)
    if name == "issues_closed":
        return data.issue_closed_count(period)

    if name == "days_active":
        active, _, _, _ = data.contribution_scope(period)
        return len(active)  # calendar is exact; never capped
    if name == "active_repos":
        _, repos, _, capped = data.contribution_scope(period)
        return floor_str(len(repos), capped)
    if name == "languages":
        _, _, langs, capped = data.contribution_scope(period)
        return floor_str(len(langs), capped)

    if name == "longest_streak":
        # Longest run of consecutive days with any contribution, over the same 365-day
        # calendar the heatmap already draws (cached — no extra API call). A measure of
        # sustained activity, not the one-click vanity of "repos created" it replaced.
        counts = data.calendar_year()["counts"]
        best = run = 0
        for c in counts:
            run = run + 1 if c > 0 else 0
            best = max(best, run)
        return best

    return 0


# ─── Daily Selection ────────────────────────────────────────

def build_metric_record(key, period, data):
    """Compute a metric AND attach the distribution that makes it visualizable:
    a `max` denominator (proportion/gauge) or a `breakdown` (category distribution).
    A metric with neither is a plain scalar. Returns the seam record; raises on a
    compute error so the caller can simply drop it from the day's candidates."""
    value = compute_metric(key, period, data)
    rec = {
        "key": key,
        "label": METRIC_DEFS[key][0],
        "period": PERIOD_LABELS[period],
        "value": str(value),
    }
    if key == "days_active":
        rec["max"] = PERIOD_DAYS[period]          # 30 or 365 — days-active out of N
    elif key == "languages":
        rec["breakdown"] = data.language_breakdown(period)
    elif key == "active_repos":
        rec["breakdown"] = data.repo_breakdown(period)
    return rec


def pick_daily_pool(date_str):
    """Assign each of the 8 metrics a period for the day (seeded). The full pool is
    computed, then relevance-filtered down to the 3-6 shown."""
    rng = random.Random(int(hashlib.md5((date_str + "::pool").encode()).hexdigest(), 16))
    return [(key, rng.choice(defs[1])) for key, defs in METRIC_DEFS.items()]


BORING_VALUES = {"0", "—"}


def select_daily_metrics(records, date_str):
    """Pick 3-6 metrics to feature: drop the boring ones (zero, or failed→absent), then
    a seeded count and subset so the card shows a different, relevant set each day.
    Varying the count is deliberate — a day with less to say shows fewer, bigger stats."""
    rng = random.Random(int(hashlib.md5((date_str + "::select").encode()).hexdigest(), 16))
    interesting = [r for r in records if str(r["value"]) not in BORING_VALUES]
    pool = interesting if len(interesting) >= 3 else records
    if not pool:
        return []
    count = rng.randint(min(3, len(pool)), min(6, len(pool)))
    return rng.sample(pool, count)


# ─── Daily Visual Theme ─────────────────────────────────────
# Palette + background motif are seeded off the date (independently of the metric
# pick) so the card's look changes every day while staying deterministic/reproducible.

PALETTES = [
    ("Ember",      "#ff7043", "#ffd166"),
    ("Aurora",     "#64ffda", "#48beff"),
    ("Synthwave",  "#ff5cf4", "#b06bff"),
    ("Solarflare", "#ffd166", "#ff8f1c"),
    ("Matrix",     "#7cff8a", "#38f9d7"),
    ("Glacier",    "#8ecae6", "#a2d2ff"),
    ("Magma",      "#ff6b6b", "#ffa45b"),
    ("Ultraviolet","#a78bfa", "#f472b6"),
    ("Citrus",     "#c8f560", "#4dd4ac"),
    ("Coral",      "#ff8fab", "#ffc2a1"),
]
MOTIFS = ["constellation", "sonar", "waves", "grid"]


def pick_daily_theme(date_str):
    """(rng, (name, c0, c1), motif) for the date. Same rng drives motif placement so
    the whole card is one reproducible composition.

    STATS_THEME_SALT (env) perturbs the seed. Default empty = today's deterministic
    pick. The doodle job's legibility self-review bumps it (1, 2, ...) to re-roll a
    different palette/motif when a rendered card reads poorly — the deterministic analog
    of the doodle reviewer's "rewrite with a different approach, don't patch"."""
    salt = os.environ.get("STATS_THEME_SALT", "")
    rng = random.Random(int(hashlib.md5((date_str + "::theme" + salt).encode()).hexdigest(), 16))
    return rng, rng.choice(PALETTES), rng.choice(MOTIFS)


# ─── SVG helpers ────────────────────────────────────────────

def bar_magnitude(value):
    """Numeric magnitude of a display value for meter sizing. '252' -> 252,
    '55+' -> 55, '—' -> 0."""
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    return int(digits) if digits else 0


def motif_constellation(rng, w, h, color):
    """Scattered stars with faint links; each star twinkles on a prime-second cycle."""
    pts = [(rng.randint(24, w - 24), rng.randint(54, h - 14)) for _ in range(16)]
    out = []
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                   f'stroke="{color}" stroke-width="0.5" opacity="0.07"/>')
    for x, y in pts:
        r = rng.choice([1, 1.5, 2])
        dur = rng.choice([7, 11, 13])
        beg = round(rng.uniform(0, 4), 1)
        out.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" opacity="0.22">'
                   f'<animate attributeName="opacity" values="0.05;0.4;0.05" '
                   f'dur="{dur}s" begin="{beg}s" repeatCount="indefinite"/></circle>')
    return "".join(out)


def motif_sonar(rng, w, h, color):
    """Concentric rings pinging outward from one side, like a radar sweep."""
    cx = rng.choice([70, w - 70])
    cy = h // 2 + 12
    out = []
    for k in range(4):
        beg = round(k * 2.75, 2)
        out.append(
            f'<circle cx="{cx}" cy="{cy}" r="8" fill="none" stroke="{color}" '
            f'stroke-width="1" opacity="0">'
            f'<animate attributeName="r" values="8;{w // 2}" dur="11s" begin="{beg}s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="0.32;0" dur="11s" begin="{beg}s" repeatCount="indefinite"/>'
            f'</circle>'
        )
    return "".join(out)


def motif_waves(rng, w, h, color):
    """Layered sine curves drifting horizontally at different speeds."""
    out = []
    for k in range(3):
        base = 66 + k * 26 + rng.randint(-6, 6)
        amp = rng.choice([6, 8, 10])
        phase = rng.uniform(0, 6)
        pts, x = [], 0
        while x <= 2 * w + 20:
            y = base + amp * math.sin(x / 38.0 + phase + k)
            pts.append(f"{x},{round(y, 1)}")
            x += 20
        d = "M" + " L".join(pts)
        dur = [13, 17, 19][k]
        out.append(
            f'<g opacity="0.13"><path d="{d}" fill="none" stroke="{color}" stroke-width="1"/>'
            f'<animateTransform attributeName="transform" type="translate" '
            f'values="0 0;-{w} 0" dur="{dur}s" repeatCount="indefinite"/></g>'
        )
    return "".join(out)


def motif_grid(rng, w, h, color):
    """A faint technical grid drifting slowly sideways."""
    out = ['<g opacity="0.06">']
    for gx in range(0, w + 40, 40):
        out.append(f'<line x1="{gx}" y1="50" x2="{gx}" y2="{h}" stroke="{color}" stroke-width="0.5"/>')
    for gy in range(58, h, 22):
        out.append(f'<line x1="0" y1="{gy}" x2="{w}" y2="{gy}" stroke="{color}" stroke-width="0.5"/>')
    out.append('<animateTransform attributeName="transform" type="translate" '
               'values="0 0;-40 0;0 0" dur="31s" repeatCount="indefinite"/></g>')
    return "".join(out)


MOTIF_FNS = {
    "constellation": motif_constellation,
    "sonar": motif_sonar,
    "waves": motif_waves,
    "grid": motif_grid,
}


# ─── SVG Generation ─────────────────────────────────────────

def generate_stats_svg(stat_items, date_label, rng, palette, motif):
    """Render the animated stats card.

    stat_items: list of (value, label, period_label). value is int | 'n+' | '—'.
    """
    W, H = 800, 160
    pal_name, c0, c1 = palette

    motif_svg = MOTIF_FNS[motif](rng, W, H, c0)

    # Meter bars are log-scaled relative to the largest value on this card, so a 6000
    # and a 7 both read sensibly. Bars are decorative; the numbers carry the truth.
    mags = [bar_magnitude(v) for v, _, _ in stat_items]
    peak = max(mags) if mags else 0
    BAR_W = 108

    def bar_width(mag):
        if peak <= 0 or mag <= 0:
            return 0
        return round(BAR_W * math.log10(1 + mag) / math.log10(1 + peak))

    n = len(stat_items)
    # [LAW:no-silent-failure] This deterministic card is the reliable fallback path, so
    # it must render *something* even in the degenerate case where no metric survived
    # selection (every metric query transiently failed). max(n, 1) keeps the column math
    # total instead of dividing by zero; the empty-state cell says so honestly rather
    # than shipping a blank card. n == 0 is a real domain shape here, not a bug to hide.
    cw = W // max(n, 1)
    cells = []
    if not stat_items:
        cells.append(
            f'<text x="{W // 2}" y="96" font-family="{FONT}" font-size="15" fill="{SUB}" '
            f'text-anchor="middle">Live stats momentarily unavailable</text>'
        )
    for i, (value, label, period_label) in enumerate(stat_items):
        cx = i * cw + cw // 2
        delay = round(0.15 * i, 2)
        fw = bar_width(bar_magnitude(value))
        bx = cx - BAR_W // 2
        # Big number: base opacity 1 (so a static render — and any SMIL-blind viewer —
        # always shows it legibly); the animate only adds a staggered fade-in on load.
        cells.append(
            f'<text x="{cx}" y="96" font-family="{FONT}" font-size="30" fill="url(#num)" '
            f'font-weight="700" text-anchor="middle" opacity="1">{value}'
            f'<animate attributeName="opacity" from="0" to="1" begin="{delay}s" dur="0.7s" fill="freeze"/>'
            f'</text>'
        )
        # meter track + animated fill (base width = final so a static render still shows it)
        cells.append(
            f'<rect x="{bx}" y="108" width="{BAR_W}" height="5" rx="2.5" fill="{TRACK}"/>'
            f'<rect x="{bx}" y="108" width="{fw}" height="5" rx="2.5" fill="{c0}" opacity="0.9">'
            f'<animate attributeName="width" from="0" to="{fw}" begin="{delay + 0.2}s" '
            f'dur="1.2s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines="0.2 0.8 0.2 1"/></rect>'
        )
        cells.append(
            f'<text x="{cx}" y="132" font-family="{FONT}" font-size="12" fill="{LABEL}" text-anchor="middle">{label}</text>'
            f'<text x="{cx}" y="148" font-family="{FONT}" font-size="10" fill="{SUB}" text-anchor="middle">({period_label})</text>'
        )

    return f'''<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Live GitHub stats">
  <defs>
    <clipPath id="card"><rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="10"/></clipPath>
    <linearGradient id="num" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{c0}"/><stop offset="1" stop-color="{c1}"/>
    </linearGradient>
    <linearGradient id="edge" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{c0}"/><stop offset="1" stop-color="{c1}"/>
    </linearGradient>
  </defs>
  <rect width="{W}" height="{H}" rx="10" fill="{BG}"/>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="10" fill="{CARD}" stroke="{BORDER}" stroke-width="1"/>
  <g clip-path="url(#card)">{motif_svg}
    <rect x="0" y="0" width="{W}" height="3" fill="url(#edge)" opacity="0.85"/>
  </g>
  <circle cx="26" cy="25" r="3.5" fill="{c0}">
    <animate attributeName="opacity" values="1;0.25;1" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text x="40" y="30" font-family="{FONT}" font-size="14" fill="{TITLE}" font-weight="600">Live GitHub Stats</text>
  <text x="{W - 20}" y="30" font-family="{FONT}" font-size="12" fill="{SUB}" text-anchor="end">Updated {date_label}</text>
  <line x1="20" y1="44" x2="{W - 20}" y2="44" stroke="{BORDER}" stroke-width="1"/>
  <g>{"".join(cells)}
  </g>
  <text x="{W - 20}" y="154" font-family="{FONT}" font-size="9" fill="{SUB}" text-anchor="end" opacity="0.7">◆ {pal_name}</text>
</svg>'''


# ─── Main ───────────────────────────────────────────────────

def write_json(path, today, username, calendar, metrics):
    """Write the rich data seam the authored card visualizes: a universal 365-day
    contribution `calendar` (time-series) plus the 3-6 selected `metrics`, each with its
    exact value and any `max`/`breakdown` distribution."""
    # Keep the ~365 calendar counts on one line — this file is committed daily, and a
    # count-per-line array would make every diff 360+ lines of churn.
    counts = calendar.get("counts", [])
    payload = {
        "date": today,
        "generated_at": _iso(datetime.now(timezone.utc)),
        "username": username,
        "calendar": {**calendar, "counts": "__COUNTS__"},
        "metrics": metrics,
    }
    text = json.dumps(payload, indent=2).replace('"__COUNTS__"', json.dumps(counts))
    with open(path, "w") as f:
        f.write(text + "\n")


def _leading_number(raw, default=None):
    """Parse the leading numeric part of an SVG length ('340', '12px', '9.5') → float.
    SVG attributes here are bare numbers, but tolerate a trailing unit rather than
    crash on one."""
    num = "".join(ch for ch in str(raw) if ch.isdigit() or ch == ".")
    return float(num) if num else default


def _canvas_height(root):
    """The card's coordinate-space height — the value a text baseline is measured
    against for clipping. Prefer viewBox (a `<text y>` is in viewBox units); fall back
    to the height attribute. [LAW:one-source-of-truth] one canvas height, read from
    where the coordinates actually live. Returns None only if the SVG declares neither,
    which these cards always do."""
    vb = root.get("viewBox")
    if vb:
        parts = vb.replace(",", " ").split()
        if len(parts) == 4:
            return _leading_number(parts[3])
    return _leading_number(root.get("height", ""))


def _bottom_clip_violations(root, height):
    """Text baselines jammed against — or past — the bottom edge: the exact defect that
    shipped on 2026-08-01, a row placed at y == the viewBox height, whose descenders
    render below the canvas and clip. [LAW:verifiable-goals] make "the text fits in its
    frame" a machine-checked fact instead of a judgment the eye keeps missing on a
    downscaled render.

    Scoped deliberately to the bottom edge and to un-transformed text, because that is
    the signal we can read unambiguously: `y` is the baseline regardless of
    `text-anchor` (a reliable vertical position, unlike `x`, which an anchored element
    measures from its own edge), and skipping any text under a `transform` avoids false
    positives where the real position isn't cheaply resolvable. The visual self-review
    still covers the transformed and horizontal cases; this gate nails the common,
    unambiguous one."""
    ns = "{http://www.w3.org/2000/svg}"
    parent = {child: par for par in root.iter() for child in par}

    def transformed(el):
        cur = el
        while cur is not None:
            if cur.get("transform"):
                return True
            cur = parent.get(cur)
        return False

    out = []
    for el in root.iter(f"{ns}text"):
        baseline = _leading_number(el.get("y", ""))
        if baseline is None or transformed(el):
            continue
        fs = _leading_number(el.get("font-size", ""), 12.0)
        # Descenders drop ~0.2-0.3x the font size below the baseline; reserve at least
        # that much clear space (floor 6px) so glyph bottoms land inside the canvas.
        reserve = max(6.0, 0.3 * fs)
        if height - baseline < reserve:
            out.append(("".join(el.itertext()).strip()[:48], baseline, reserve))
    return out


def verify_svg(svg_path, json_path):
    """Accuracy + layout gate. Fails unless (1) every value in json_path is rendered as
    text in svg_path, and (2) no un-transformed text baseline is clipped by the bottom
    edge. The digit-boundary guard stops a value like '9' from matching spuriously
    inside another number ('1956'), so a wrong or dropped number can't slip through; the
    bottom-margin check stops an authored card from shipping with its last row cut off.
    [LAW:verifiable-goals] [LAW:no-silent-failure]"""
    import re
    import xml.etree.ElementTree as ET

    with open(json_path) as f:
        payload = json.load(f)
    root = ET.parse(svg_path).getroot()
    ns = "{http://www.w3.org/2000/svg}"
    rendered = "\n".join("".join(el.itertext()).strip() for el in root.iter(f"{ns}text"))

    errors = [
        f'missing/altered value: {m["label"]} ({m["period"]}) = {m["value"]}'
        for m in payload["metrics"]
        if not re.search(r"(?<!\d)" + re.escape(str(m["value"])) + r"(?!\d)", rendered)
    ]
    height = _canvas_height(root)
    if height is not None:
        for text, baseline, reserve in _bottom_clip_violations(root, height):
            errors.append(
                f'bottom-clipped text (baseline y={baseline:g} in a {height:g}px canvas '
                f'needs >={reserve:g}px clearance below): "{text}"'
            )

    if errors:
        print(f"ERROR: {svg_path} failed the stats-card gate vs {json_path}:",
              file=sys.stderr)
        for x in errors:
            print(f"  - {x}", file=sys.stderr)
        sys.exit(1)
    print(f"OK: all {len(payload['metrics'])} values render and no text is bottom-clipped "
          f"in {svg_path}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--svg-out", default=STATS_PATH,
                        help="path to write the fallback SVG (default: %(default)s)")
    parser.add_argument("--json-out", default=JSON_PATH,
                        help="path to write the metric data seam (default: %(default)s)")
    parser.add_argument("--theme-salt", default=None,
                        help="re-roll the fallback palette/motif to a different look")
    parser.add_argument("--verify-svg", metavar="PATH", default=None,
                        help="verify PATH renders every value in --json-out, then exit")
    args = parser.parse_args()

    # Verify mode is pure (no token, no network): read the JSON and the SVG, compare.
    if args.verify_svg:
        verify_svg(args.verify_svg, args.json_out)
        return

    if args.theme_salt is not None:
        os.environ["STATS_THEME_SALT"] = args.theme_salt

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN environment variable not set", file=sys.stderr)
        sys.exit(1)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    date_label = datetime.now(timezone.utc).strftime("%B %d, %Y")
    print(f"Date seed: {today}")

    data = GitHubData(token)

    # Compute the full pool, keeping each metric's supporting distribution; drop any that
    # fail to compute (a rate-limited metric is simply not a candidate, not a wrong "0").
    records = []
    for key, period in pick_daily_pool(today):
        try:
            records.append(build_metric_record(key, period, data))
        except Exception as e:
            print(f"Warning: failed to build {key} ({period}): {e}", file=sys.stderr)

    selected = select_daily_metrics(records, today)
    print(f"Selected {len(selected)} metrics: {[(r['key'], r['value']) for r in selected]}")

    calendar = data.calendar_year()
    print(f"Calendar: {len(calendar['counts'])} days from {calendar['start']}")

    os.makedirs(os.path.dirname(args.json_out) or ".", exist_ok=True)
    write_json(args.json_out, today, USERNAME, calendar, selected)
    print(f"  Rich data seam written to {args.json_out}")

    # Deterministic fallback card — renders the selected metrics as scalars, variable count.
    rng, palette, motif = pick_daily_theme(today)
    stat_items = [(r["value"], r["label"], r["period"]) for r in selected]
    os.makedirs(os.path.dirname(args.svg_out) or ".", exist_ok=True)
    with open(args.svg_out, "w") as f:
        f.write(generate_stats_svg(stat_items, date_label, rng, palette, motif))
    print(f"  Fallback SVG ({palette[0]}/{motif}) written to {args.svg_out}")


if __name__ == "__main__":
    main()

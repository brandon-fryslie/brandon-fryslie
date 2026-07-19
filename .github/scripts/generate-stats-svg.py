#!/usr/bin/env python3
"""
Generate daily stats SVG for GitHub profile.

Picks 4 random metrics (from 8) with random time periods each day,
queries GitHub API with pagination, and creates the stats card.
"""

import hashlib
import os
import random
import sys
from datetime import datetime, timedelta, timezone
from urllib.parse import quote

try:
    import requests

    HAS_REQUESTS = True
except ImportError:
    import json
    import urllib.error
    import urllib.request

    HAS_REQUESTS = False

# ─── Configuration ──────────────────────────────────────────

USERNAME = "brandon-fryslie"
STATS_PATH = "assets/daily-stats.svg"
API_TIMEOUT = 30  # seconds
FONT = (
    "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
)

# GitHub Primer dark palette — matches the #0d1117 profile chrome so the
# stats card sits flush with the surrounding dark banners instead of
# rendering as a light box on the dark profile.
BG = "#0d1117"
TEXT = "#e6edf3"
SECONDARY = "#8b949e"
ACCENT = "#58a6ff"
BORDER = "#30363d"
TERTIARY = "#6e7681"

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
    "repos_created": ("Repos Created", ["1y", "all"]),
    "issues_closed": ("My Issues Closed", ["30d", "1y", "all"]),
}


# ─── API Layer ──────────────────────────────────────────────

class GitHubAPIError(RuntimeError):
    def __init__(self, url, status, body):
        super().__init__(f"GET {url} failed with status {status}: {body[:300]}")
        self.url = url
        self.status = status
        self.body = body


def api_get(endpoint, token):
    """Make a single GitHub API GET request. Returns parsed JSON.

    On non-2xx, raises GitHubAPIError with the status code and body so callers
    can distinguish 422 (search past 1000 results) from 403 (rate limit)
    instead of getting a generic "—" with no signal.
    """
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


def api_paginate_list(endpoint, token):
    """Paginate a GitHub list endpoint (repos, etc) to exhaustion."""
    results = []
    sep = "&" if "?" in endpoint else "?"
    page = 1
    while True:
        data = api_get(f"{endpoint}{sep}page={page}&per_page=100", token)
        results.extend(data)
        if len(data) < 100:
            break
        page += 1
    return results


def search_total_count(path, query, token):
    """Get total_count from a GitHub search endpoint."""
    encoded_q = quote(query, safe="+:")
    data = api_get(f"/search/{path}?q={encoded_q}&per_page=1", token)
    return data.get("total_count", 0)


SEARCH_PAGE_CAP = 10  # GitHub search caps at 1000 results (10 pages * 100); page 11 returns 422.


def search_commit_items(query, token):
    """Paginate commit search up to the GitHub 1000-result cap.

    Going past page 10 returns 422 ('Only the first 1000 search results are
    available'), which previously turned every metric depending on this list
    into "—" once Brandon's commit volume in the period exceeded 1000.
    """
    encoded_q = quote(query, safe="+:")
    items = []
    for page in range(1, SEARCH_PAGE_CAP + 1):
        data = api_get(
            f"/search/commits?q={encoded_q}&per_page=100&page={page}", token
        )
        batch = data.get("items", [])
        items.extend(batch)
        if len(batch) < 100:
            break
    return items


# ─── Date Helpers ───────────────────────────────────────────

def cutoff_iso(period):
    """ISO date string for period start, or None for 'all'."""
    days = PERIOD_DAYS[period]
    if days is None:
        return None
    dt = datetime.now(timezone.utc) - timedelta(days=days)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def date_qualifier(period, field="committer-date"):
    """Search query fragment like '+committer-date:>2024-01-01T...' or empty."""
    since = cutoff_iso(period)
    return f"+{field}:>{since}" if since else ""


# ─── Cached Data Fetcher ───────────────────────────────────

class GitHubData:
    """Fetches and caches GitHub API data to avoid duplicate calls."""

    def __init__(self, token):
        self.token = token
        self._user = None
        self._repos = None
        self._commit_items = {}
        self._repo_language = {}

    def user(self):
        """Canonical /users/{username} payload — has public_repos as a single field."""
        if self._user is None:
            self._user = api_get(f"/users/{USERNAME}", self.token)
        return self._user

    def public_repo_count(self):
        """The truth-source count for public repos. Avoids list-endpoint pagination quirks."""
        return self.user().get("public_repos", 0)

    def repos(self):
        """Paginated repo list. Logs a warning if its length disagrees with public_repos
        so silent pagination caps surface instead of producing a wrong number."""
        if self._repos is None:
            self._repos = api_paginate_list(
                f"/users/{USERNAME}/repos", self.token
            )
            expected = self.public_repo_count()
            if expected and len(self._repos) != expected:
                print(
                    f"Warning: paginated repo list returned {len(self._repos)} but /users/{USERNAME}.public_repos = {expected}",
                    file=sys.stderr,
                )
        return self._repos

    def commit_items(self, period):
        """Fetch commit items for a period (cached). Needed for languages, active_repos, days_active."""
        if period not in self._commit_items:
            q = f"author:{USERNAME}{date_qualifier(period)}"
            self._commit_items[period] = search_commit_items(q, self.token)
        return self._commit_items[period]

    def repo_language(self, full_name):
        """Primary language for any repo by full_name (cached).

        Unlike repos(), which only lists repos Brandon *owns*, this resolves
        the language of repos he merely commits to — org repos like
        promptctl/* — so the Languages metric isn't blind to the org work
        that dominates his activity. Missing/errored repos resolve to None
        and are simply skipped by the caller.
        """
        if full_name not in self._repo_language:
            try:
                self._repo_language[full_name] = api_get(
                    f"/repos/{full_name}", self.token
                ).get("language")
            except GitHubAPIError as e:
                print(
                    f"Warning: could not resolve language for {full_name}: {e}",
                    file=sys.stderr,
                )
                self._repo_language[full_name] = None
        return self._repo_language[full_name]

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


# ─── Metric Computation ────────────────────────────────────

def compute_metric(name, period, data):
    """Compute a single metric value. Returns an int."""
    if name == "commits":
        return data.commit_count(period)

    if name == "prs_merged":
        return data.pr_merged_count(period)

    if name == "reviews":
        return data.review_count(period)

    if name == "issues_closed":
        return data.issue_closed_count(period)

    if name == "languages":
        # Distinct languages across every repo Brandon committed to in the
        # period — org repos included, resolved via repo_language() rather
        # than intersecting with the owned-repos list (which dropped all
        # org contributions and undercounted the total).
        items = data.commit_items(period)
        repo_names = {it["repository"]["full_name"] for it in items}
        langs = {data.repo_language(fn) for fn in repo_names}
        langs.discard(None)
        if period == "all":
            # Also fold in owned repos with no commits in the search window,
            # since the all-time commit search caps at 1000 results.
            langs |= {r["language"] for r in data.repos() if r.get("language")}
        return len(langs)

    if name == "active_repos":
        items = data.commit_items(period)
        return len({it["repository"]["full_name"] for it in items})

    if name == "days_active":
        items = data.commit_items(period)
        dates = set()
        for it in items:
            d = it.get("commit", {}).get("committer", {}).get("date", "")
            if d:
                dates.add(d[:10])
        return len(dates)

    if name == "repos_created":
        # Repos Brandon actually *created* — owned and non-fork. public_repos
        # (used before for all-time) counts forks and is a current-inventory
        # count, not a creation count, so it badly overstated this metric.
        since = cutoff_iso(period)
        created = [r for r in data.repos() if not r.get("fork")]
        if since is None:
            return len(created)
        return sum(1 for r in created if r["created_at"] > since)

    return 0


# ─── Daily Selection ────────────────────────────────────────

def pick_daily_metrics(date_str):
    """Deterministically pick 4 (metric_name, period) combos for a given date."""
    seed = int(hashlib.md5(date_str.encode()).hexdigest(), 16)
    rng = random.Random(seed)

    metric_names = list(METRIC_DEFS.keys())
    chosen = rng.sample(metric_names, 4)

    result = []
    for name in chosen:
        _, valid_periods = METRIC_DEFS[name]
        period = rng.choice(valid_periods)
        result.append((name, period))

    return result


# ─── SVG Generation ─────────────────────────────────────────

def generate_stats_svg(stat_items):
    """Generate the stats card SVG.

    stat_items: list of (value, label, period_label) tuples
    """
    width = 800
    height = 140
    date_str = datetime.now(timezone.utc).strftime("%B %d, %Y")

    stat_cells = ""
    cell_width = width // len(stat_items)
    for i, (value, label, period_label) in enumerate(stat_items):
        x = i * cell_width + cell_width // 2
        stat_cells += f'''
    <text x="{x}" y="76" font-family="{FONT}" font-size="28" fill="{ACCENT}" font-weight="600" text-anchor="middle">{value}</text>
    <text x="{x}" y="96" font-family="{FONT}" font-size="12" fill="{SECONDARY}" text-anchor="middle">{label}</text>
    <text x="{x}" y="112" font-family="{FONT}" font-size="10" fill="{TERTIARY}" text-anchor="middle">({period_label})</text>'''

    return f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{width}" height="{height}" rx="6" fill="{BG}" stroke="{BORDER}" stroke-width="1"/>
  <text x="20" y="30" font-family="{FONT}" font-size="14" fill="{TEXT}" font-weight="600">Live GitHub Stats</text>
  <text x="{width - 20}" y="30" font-family="{FONT}" font-size="12" fill="{SECONDARY}" text-anchor="end">Updated {date_str}</text>
  <line x1="20" y1="42" x2="{width - 20}" y2="42" stroke="{BORDER}" stroke-width="1"/>
  <g>{stat_cells}
  </g>
</svg>'''


# ─── Main ───────────────────────────────────────────────────

def main():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN environment variable not set", file=sys.stderr)
        sys.exit(1)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(f"Date seed: {today}")

    selections = pick_daily_metrics(today)
    print(f"Today's metrics: {[(n, p) for n, p in selections]}")

    data = GitHubData(token)

    # Compute the 4 selected metrics
    stat_items = []
    for name, period in selections:
        label, _ = METRIC_DEFS[name]
        period_label = PERIOD_LABELS[period]
        try:
            value = compute_metric(name, period, data)
        except Exception as e:
            print(f"Warning: failed to compute {name} ({period}): {e}", file=sys.stderr)
            value = "—"
        stat_items.append((value, label, period_label))
        print(f"  {label} ({period_label}): {value}")

    os.makedirs("assets", exist_ok=True)

    print("Generating stats SVG...")
    with open(STATS_PATH, "w") as f:
        f.write(generate_stats_svg(stat_items))
    print(f"  Written to {STATS_PATH}")


if __name__ == "__main__":
    main()

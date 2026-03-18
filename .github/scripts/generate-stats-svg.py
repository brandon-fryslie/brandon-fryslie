#!/usr/bin/env python3
"""
Generate daily stats SVGs for GitHub profile.

Picks 4 random metrics (from 8) with random time periods each day,
queries GitHub API with pagination, and creates both the
stats card and the data-driven tech constellation.
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
    import urllib.request

    HAS_REQUESTS = False

# ─── Configuration ──────────────────────────────────────────

USERNAME = "brandon-fryslie"
STATS_PATH = "assets/daily-stats.svg"
CONSTELLATION_PATH = "assets/tech-constellation.svg"
API_TIMEOUT = 30  # seconds
FONT = (
    "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
)

# GitHub Primer palette
BG = "#fafbfc"
TEXT = "#24292e"
SECONDARY = "#586069"
ACCENT = "#0366d6"
BORDER = "#e1e4e8"

# Language colors
LANG_COLORS = {
    "Python": "#3776AB",
    "JavaScript": "#F0DB4F",
    "TypeScript": "#3178C6",
    "Shell": "#4EAA25",
    "Go": "#00ADD8",
    "Java": "#ED8B00",
    "HCL": "#7B42BC",
    "Kotlin": "#7F52FF",
    "C": "#555555",
    "C++": "#F34B7D",
    "Ruby": "#CC342D",
    "PHP": "#777BB4",
    "Rust": "#DEA584",
    "CoffeeScript": "#244776",
    "Groovy": "#4298B8",
    "HTML": "#E34C26",
    "CSS": "#563D7C",
    "Vim Script": "#199F4B",
    "Clojure": "#DB5855",
}
DEFAULT_COLOR = "#8b949e"

LANG_DISPLAY = {
    "HCL": "Terraform",
    "Vim Script": "Vim",
}

# Constellation layout
SLOTS = [
    {"x": 100, "y": 60, "ly": 90},
    {"x": 240, "y": 52, "ly": 82},
    {"x": 380, "y": 58, "ly": 88},
    {"x": 520, "y": 46, "ly": 76},
    {"x": 660, "y": 56, "ly": 86},
    {"x": 190, "y": 128, "ly": 158},
    {"x": 400, "y": 134, "ly": 164},
]
CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (2, 6),
]
DOT_DURS = [7, 11, 13, 7, 11, 13, 17]
DOT_BEGINS = [0, 2, 4, 1, 3, 5, 7]
BREATH_DURS = [11, 13, 7, 17, 11, 19, 13]
BREATH_BEGINS = [0, 0, 0, 0, 3, 0, 5]

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

def api_get(endpoint, token):
    """Make a single GitHub API GET request. Returns parsed JSON."""
    url = f"https://api.github.com{endpoint}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    if HAS_REQUESTS:
        resp = requests.get(url, headers=headers, timeout=API_TIMEOUT)
        resp.raise_for_status()
        return resp.json()
    else:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=API_TIMEOUT) as resp:
            return json.loads(resp.read().decode())


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


def search_commit_items(query, token):
    """Paginate commit search to exhaustion."""
    encoded_q = quote(query, safe="+:")
    items = []
    page = 1
    while True:
        data = api_get(
            f"/search/commits?q={encoded_q}&per_page=100&page={page}", token
        )
        batch = data.get("items", [])
        items.extend(batch)
        if len(batch) < 100:
            break
        page += 1
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
        self._repos = None
        self._commit_items = {}

    def repos(self):
        if self._repos is None:
            self._repos = api_paginate_list(
                f"/users/{USERNAME}/repos", self.token
            )
        return self._repos

    def commit_items(self, period):
        """Fetch commit items for a period (cached). Needed for languages, active_repos, days_active."""
        if period not in self._commit_items:
            q = f"author:{USERNAME}{date_qualifier(period)}"
            self._commit_items[period] = search_commit_items(q, self.token)
        return self._commit_items[period]

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
        if period == "all":
            return len({r["language"] for r in data.repos() if r.get("language")})
        items = data.commit_items(period)
        repo_names = {it["repository"]["full_name"] for it in items}
        repo_langs = {
            r["language"]
            for r in data.repos()
            if r["full_name"] in repo_names and r.get("language")
        }
        return len(repo_langs)

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
        since = cutoff_iso(period)
        repos = data.repos()
        if since is None:
            return len(repos)
        return sum(1 for r in repos if r["created_at"] > since)

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

def generate_stats_svg(stat_items, top_languages):
    """Generate the stats card SVG.

    stat_items: list of (value, label, period_label) tuples
    top_languages: list of (lang_name, count) tuples for footer
    """
    width = 800
    height = 170
    date_str = datetime.now(timezone.utc).strftime("%B %d, %Y")
    lang_text = " / ".join(
        f"{LANG_DISPLAY.get(lang, lang)} ({count})"
        for lang, count in top_languages[:5]
    )

    stat_cells = ""
    cell_width = width // len(stat_items)
    for i, (value, label, period_label) in enumerate(stat_items):
        x = i * cell_width + cell_width // 2
        stat_cells += f'''
    <text x="{x}" y="76" font-family="{FONT}" font-size="28" fill="{ACCENT}" font-weight="600" text-anchor="middle">{value}</text>
    <text x="{x}" y="96" font-family="{FONT}" font-size="12" fill="{SECONDARY}" text-anchor="middle">{label}</text>
    <text x="{x}" y="112" font-family="{FONT}" font-size="10" fill="#8b949e" text-anchor="middle">({period_label})</text>'''

    return f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{width}" height="{height}" rx="6" fill="{BG}" stroke="{BORDER}" stroke-width="1"/>
  <text x="20" y="30" font-family="{FONT}" font-size="14" fill="{TEXT}" font-weight="600">Live GitHub Stats</text>
  <text x="{width - 20}" y="30" font-family="{FONT}" font-size="12" fill="{SECONDARY}" text-anchor="end">Updated {date_str}</text>
  <line x1="20" y1="42" x2="{width - 20}" y2="42" stroke="{BORDER}" stroke-width="1"/>
  <g>{stat_cells}
  </g>
  <line x1="20" y1="128" x2="{width - 20}" y2="128" stroke="{BORDER}" stroke-width="1"/>
  <text x="{width // 2}" y="150" font-family="{FONT}" font-size="11" fill="{SECONDARY}" text-anchor="middle">{lang_text}</text>
</svg>'''


def generate_constellation_svg(top_languages):
    """Generate the data-driven tech constellation SVG."""
    langs = top_languages[:7]
    num_langs = len(langs)
    date_str = datetime.now(timezone.utc).strftime("%b %d, %Y")

    counts = [count for _, count in langs]
    max_count = max(counts) if counts else 1
    min_count = min(counts) if counts else 1
    count_range = max(max_count - min_count, 1)

    def radius(count):
        return 12 + (count - min_count) / count_range * 10

    lines_svg = ""
    dots_svg = ""
    glows_svg = ""
    nodes_svg = ""
    labels_svg = ""

    for ci, (a, b) in enumerate(CONNECTIONS):
        if a >= num_langs or b >= num_langs:
            continue
        sa, sb = SLOTS[a], SLOTS[b]
        color = LANG_COLORS.get(langs[a][0], DEFAULT_COLOR)
        dur = DOT_DURS[ci % len(DOT_DURS)]
        begin = DOT_BEGINS[ci % len(DOT_BEGINS)]

        lines_svg += (
            f'    <line x1="{sa["x"]}" y1="{sa["y"]}"'
            f' x2="{sb["x"]}" y2="{sb["y"]}"/>\n'
        )
        dots_svg += f'''    <circle r="1.5" fill="{color}">
      <animate attributeName="cx" values="{sa['x']};{sb['x']}" dur="{dur}s" repeatCount="indefinite" begin="{begin}s"/>
      <animate attributeName="cy" values="{sa['y']};{sb['y']}" dur="{dur}s" repeatCount="indefinite" begin="{begin}s"/>
      <animate attributeName="opacity" values="0;0.7;0.7;0" keyTimes="0;0.1;0.9;1" dur="{dur}s" repeatCount="indefinite" begin="{begin}s"/>
    </circle>
'''

    for i, (lang, count) in enumerate(langs):
        if i >= len(SLOTS):
            break
        s = SLOTS[i]
        color = LANG_COLORS.get(lang, DEFAULT_COLOR)
        r = radius(count)
        glow_r = r + 12
        dur = BREATH_DURS[i % len(BREATH_DURS)]
        begin = BREATH_BEGINS[i % len(BREATH_BEGINS)]
        begin_attr = f' begin="{begin}s"' if begin else ""
        display = LANG_DISPLAY.get(lang, lang)

        glows_svg += f'''    <circle cx="{s['x']}" cy="{s['y']}" r="{glow_r:.0f}" fill="{color}" opacity="0.06">
      <animate attributeName="opacity" values="0.04;0.1;0.04" dur="{dur}s" repeatCount="indefinite"{begin_attr}/>
    </circle>
'''
        nodes_svg += f'''    <circle cx="{s['x']}" cy="{s['y']}" r="{r:.0f}" fill="{color}" opacity="0.85">
      <animate attributeName="opacity" values="0.75;0.95;0.75" dur="{dur}s" repeatCount="indefinite"{begin_attr}/>
    </circle>
'''
        nodes_svg += (
            f'    <text x="{s["x"]}" y="{s["y"] + 4}" font-family="{FONT}"'
            f' font-size="11" fill="white" text-anchor="middle"'
            f' font-weight="600">{count}</text>\n'
        )
        labels_svg += (
            f'    <text x="{s["x"]}" y="{s["ly"]}" font-size="11"'
            f' fill="#8b949e" text-anchor="middle">{display}</text>\n'
        )

    domains = (
        "Backend Systems · Platform Infrastructure · Access Control"
        " · Distributed Coordination · Developer Tooling · Compiler Design"
    )

    return f'''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#21262d" stroke-width="0.3"/>
    </pattern>
  </defs>

  <rect width="800" height="200" rx="8" fill="#0d1117"/>
  <rect width="800" height="200" rx="8" fill="url(#grid)" opacity="0.4"/>

  <!-- Updated {date_str} -->

  <!-- Connections -->
  <g stroke="#30363d" stroke-width="1" fill="none">
{lines_svg}  </g>

  <!-- Traveling dots -->
  <g>
{dots_svg}  </g>

  <!-- Node glows -->
  <g>
{glows_svg}  </g>

  <!-- Nodes with counts -->
  <g>
{nodes_svg}  </g>

  <!-- Labels -->
  <g font-family="{FONT}" text-anchor="middle">
{labels_svg}  </g>

  <!-- Domains -->
  <line x1="40" y1="175" x2="760" y2="175" stroke="#21262d" stroke-width="0.5"/>
  <text x="400" y="192" font-family="{FONT}" font-size="11" fill="#484f58" text-anchor="middle">{domains}</text>
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

    # Language stats for constellation + stats footer (always needed)
    repos = data.repos()
    lang_counts = {}
    for repo in repos:
        lang = repo.get("language")
        if lang:
            lang_counts[lang] = lang_counts.get(lang, 0) + 1
    top_languages = sorted(lang_counts.items(), key=lambda x: x[1], reverse=True)[:7]
    print(f"Top languages: {', '.join(f'{l} ({c})' for l, c in top_languages)}")

    os.makedirs("assets", exist_ok=True)

    print("Generating stats SVG...")
    with open(STATS_PATH, "w") as f:
        f.write(generate_stats_svg(stat_items, top_languages))
    print(f"  Written to {STATS_PATH}")

    print("Generating constellation SVG...")
    with open(CONSTELLATION_PATH, "w") as f:
        f.write(generate_constellation_svg(top_languages))
    print(f"  Written to {CONSTELLATION_PATH}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Generate daily stats SVGs for GitHub profile.
Queries GitHub API and creates both the stats card and
the data-driven tech constellation.
"""

import os
import sys
from datetime import datetime, timedelta
try:
    import requests
except ImportError:
    import urllib.request
    import json

# Professional color palette (GitHub Primer)
BG = "#fafbfc"
TEXT = "#24292e"
SECONDARY = "#586069"
ACCENT = "#0366d6"
BORDER = "#e1e4e8"

USERNAME = "brandon-fryslie"
STATS_PATH = "assets/daily-stats.svg"
CONSTELLATION_PATH = "assets/tech-constellation.svg"

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

# Brand colors for languages
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

# Display name overrides
LANG_DISPLAY = {
    "HCL": "Terraform",
    "Vim Script": "Vim",
}

# Node positions: 5 upper, 2 lower
SLOTS = [
    {"x": 100, "y": 60, "ly": 90},
    {"x": 240, "y": 52, "ly": 82},
    {"x": 380, "y": 58, "ly": 88},
    {"x": 520, "y": 46, "ly": 76},
    {"x": 660, "y": 56, "ly": 86},
    {"x": 190, "y": 128, "ly": 158},
    {"x": 400, "y": 134, "ly": 164},
]

# Connection pairs (slot indices)
CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (2, 6),
]

# Animation durations for traveling dots (prime numbers)
DOT_DURS = [7, 11, 13, 7, 11, 13, 17]
DOT_BEGINS = [0, 2, 4, 1, 3, 5, 7]

# Breathing durations for nodes
BREATH_DURS = [11, 13, 7, 17, 11, 19, 13]
BREATH_BEGINS = [0, 0, 0, 0, 3, 0, 5]


def github_api_get(endpoint, token):
    """Make a GitHub API request."""
    url = f"https://api.github.com{endpoint}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except NameError:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())


def get_stats(token):
    """Fetch stats from GitHub API."""
    stats = {
        "repos": 0,
        "stars": 0,
        "commits_30d": 0,
        "years_active": 0,
        "top_languages": []
    }

    repos = github_api_get(f"/users/{USERNAME}/repos?per_page=100", token)
    stats["repos"] = len(repos)
    stats["stars"] = sum(r.get("stargazers_count", 0) for r in repos)

    created_dates = [datetime.strptime(r["created_at"], "%Y-%m-%dT%H:%M:%SZ") for r in repos]
    if created_dates:
        earliest = min(created_dates)
        stats["years_active"] = (datetime.now() - earliest).days // 365

    since_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        commits = github_api_get(
            f"/search/commits?q=author:{USERNAME}+committer-date:>{since_date}&per_page=100",
            token
        )
        stats["commits_30d"] = commits.get("total_count", 0)
    except Exception as e:
        print(f"Warning: Could not fetch commits: {e}", file=sys.stderr)
        stats["commits_30d"] = 0

    lang_counts = {}
    for repo in repos:
        if repo.get("language"):
            lang = repo["language"]
            lang_counts[lang] = lang_counts.get(lang, 0) + 1

    stats["top_languages"] = sorted(lang_counts.items(), key=lambda x: x[1], reverse=True)[:7]

    return stats


def generate_stats_svg(stats):
    """Generate the stats card SVG."""
    width = 800
    height = 160
    date_str = datetime.now().strftime("%B %d, %Y")
    lang_text = " / ".join([f"{lang} ({count})" for lang, count in stats["top_languages"][:5]])

    stat_items = [
        (stats["repos"], "Repositories"),
        (stats["stars"], "Stars"),
        (stats["commits_30d"], "Commits (30d)"),
        (f"{stats['years_active']}+", "Years Active"),
    ]

    stat_cells = ""
    cell_width = width // len(stat_items)
    for i, (value, label) in enumerate(stat_items):
        x = i * cell_width + cell_width // 2
        stat_cells += f'''
    <text x="{x}" y="80" font-family="{FONT}" font-size="28" fill="{ACCENT}" font-weight="600" text-anchor="middle">{value}</text>
    <text x="{x}" y="102" font-family="{FONT}" font-size="12" fill="{SECONDARY}" text-anchor="middle">{label}</text>'''

    return f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{width}" height="{height}" rx="6" fill="{BG}" stroke="{BORDER}" stroke-width="1"/>
  <text x="20" y="30" font-family="{FONT}" font-size="14" fill="{TEXT}" font-weight="600">Live GitHub Stats</text>
  <text x="{width - 20}" y="30" font-family="{FONT}" font-size="12" fill="{SECONDARY}" text-anchor="end">Updated {date_str}</text>
  <line x1="20" y1="42" x2="{width - 20}" y2="42" stroke="{BORDER}" stroke-width="1"/>
  <g>{stat_cells}
  </g>
  <line x1="20" y1="118" x2="{width - 20}" y2="118" stroke="{BORDER}" stroke-width="1"/>
  <text x="{width // 2}" y="142" font-family="{FONT}" font-size="11" fill="{SECONDARY}" text-anchor="middle">{lang_text}</text>
</svg>'''


def generate_constellation_svg(stats):
    """Generate the data-driven tech constellation SVG."""
    langs = stats["top_languages"][:7]
    num_langs = len(langs)
    date_str = datetime.now().strftime("%b %d, %Y")

    counts = [count for _, count in langs]
    max_count = max(counts) if counts else 1
    min_count = min(counts) if counts else 1
    count_range = max(max_count - min_count, 1)

    # Node radius: 12-22px proportional to repo count
    def radius(count):
        return 12 + (count - min_count) / count_range * 10

    # Build SVG parts
    lines_svg = ""
    dots_svg = ""
    glows_svg = ""
    nodes_svg = ""
    labels_svg = ""

    # Connection lines and traveling dots
    for ci, (a, b) in enumerate(CONNECTIONS):
        if a >= num_langs or b >= num_langs:
            continue
        sa, sb = SLOTS[a], SLOTS[b]
        color = LANG_COLORS.get(langs[a][0], DEFAULT_COLOR)
        dur = DOT_DURS[ci % len(DOT_DURS)]
        begin = DOT_BEGINS[ci % len(DOT_BEGINS)]

        lines_svg += f'    <line x1="{sa["x"]}" y1="{sa["y"]}" x2="{sb["x"]}" y2="{sb["y"]}"/>\n'

        dots_svg += f'''    <circle r="1.5" fill="{color}">
      <animate attributeName="cx" values="{sa['x']};{sb['x']}" dur="{dur}s" repeatCount="indefinite" begin="{begin}s"/>
      <animate attributeName="cy" values="{sa['y']};{sb['y']}" dur="{dur}s" repeatCount="indefinite" begin="{begin}s"/>
      <animate attributeName="opacity" values="0;0.7;0.7;0" keyTimes="0;0.1;0.9;1" dur="{dur}s" repeatCount="indefinite" begin="{begin}s"/>
    </circle>
'''

    # Nodes: glow + circle + count label + name label
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

        # Count inside node
        nodes_svg += f'    <text x="{s["x"]}" y="{s["y"] + 4}" font-family="{FONT}" font-size="11" fill="white" text-anchor="middle" font-weight="600">{count}</text>\n'

        # Language name below
        labels_svg += f'    <text x="{s["x"]}" y="{s["ly"]}" font-size="11" fill="#8b949e" text-anchor="middle">{display}</text>\n'

    # Domains text
    domains = "Backend Systems · Platform Infrastructure · Access Control · Distributed Coordination · Developer Tooling · Compiler Design"

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


def main():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN environment variable not set", file=sys.stderr)
        sys.exit(1)

    print("Fetching GitHub stats...")
    stats = get_stats(token)

    print(f"Stats: {stats['repos']} repos, {stats['stars']} stars, "
          f"{stats['commits_30d']} commits (30d), {stats['years_active']} years")
    print(f"Top languages: {', '.join(f'{l} ({c})' for l, c in stats['top_languages'])}")

    os.makedirs("assets", exist_ok=True)

    print("Generating stats SVG...")
    with open(STATS_PATH, "w") as f:
        f.write(generate_stats_svg(stats))
    print(f"  Written to {STATS_PATH}")

    print("Generating constellation SVG...")
    with open(CONSTELLATION_PATH, "w") as f:
        f.write(generate_constellation_svg(stats))
    print(f"  Written to {CONSTELLATION_PATH}")


if __name__ == "__main__":
    main()

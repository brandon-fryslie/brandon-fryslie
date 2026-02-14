#!/usr/bin/env python3
"""
Generate daily stats SVG for GitHub profile.
Queries GitHub API for stats and creates a clean SVG with live data.
"""

import os
import sys
from datetime import datetime, timedelta
try:
    import requests
except ImportError:
    # Fallback to urllib if requests is not available
    import urllib.request
    import json

# Professional color palette (GitHub Primer)
BG = "#fafbfc"
TEXT = "#24292e"
SECONDARY = "#586069"
ACCENT = "#0366d6"
BORDER = "#e1e4e8"

USERNAME = "brandon-fryslie"
OUTPUT_PATH = "assets/daily-stats.svg"


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
        # Fallback to urllib
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

    # Get all repos
    repos = github_api_get(f"/users/{USERNAME}/repos?per_page=100", token)
    stats["repos"] = len(repos)
    stats["stars"] = sum(r.get("stargazers_count", 0) for r in repos)

    # Calculate years active (from earliest repo)
    created_dates = [datetime.strptime(r["created_at"], "%Y-%m-%dT%H:%M:%SZ") for r in repos]
    if created_dates:
        earliest = min(created_dates)
        stats["years_active"] = (datetime.now() - earliest).days // 365

    # Count commits in last 30 days
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

    # Get language stats (count repos per language)
    lang_counts = {}
    for repo in repos:
        if repo.get("language"):
            lang = repo["language"]
            lang_counts[lang] = lang_counts.get(lang, 0) + 1

    # Top 5 languages
    stats["top_languages"] = sorted(lang_counts.items(), key=lambda x: x[1], reverse=True)[:5]

    return stats


def generate_svg(stats):
    """Generate clean professional stats SVG."""
    width = 800
    height = 160

    # Format date
    date_str = datetime.now().strftime("%B %d, %Y")

    # Format top languages
    lang_text = " / ".join([f"{lang} ({count})" for lang, count in stats["top_languages"]])

    # Stat items
    stat_items = [
        (stats["repos"], "Repositories"),
        (stats["stars"], "Stars"),
        (stats["commits_30d"], "Commits (30d)"),
        (f"{stats['years_active']}+", "Years Active"),
    ]

    # Build stat cells
    stat_cells = ""
    cell_width = width // len(stat_items)
    for i, (value, label) in enumerate(stat_items):
        x = i * cell_width + cell_width // 2
        stat_cells += f'''
    <text x="{x}" y="80" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="28" fill="{ACCENT}" font-weight="600" text-anchor="middle">{value}</text>
    <text x="{x}" y="102" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="12" fill="{SECONDARY}" text-anchor="middle">{label}</text>'''

    svg = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{width}" height="{height}" rx="6" fill="{BG}" stroke="{BORDER}" stroke-width="1"/>

  <!-- Header -->
  <text x="20" y="30" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="14" fill="{TEXT}" font-weight="600">Live GitHub Stats</text>
  <text x="{width - 20}" y="30" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="12" fill="{SECONDARY}" text-anchor="end">Updated {date_str}</text>

  <!-- Divider -->
  <line x1="20" y1="42" x2="{width - 20}" y2="42" stroke="{BORDER}" stroke-width="1"/>

  <!-- Stats -->
  <g>{stat_cells}
  </g>

  <!-- Languages -->
  <line x1="20" y1="118" x2="{width - 20}" y2="118" stroke="{BORDER}" stroke-width="1"/>
  <text x="{width // 2}" y="142" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="11" fill="{SECONDARY}" text-anchor="middle">{lang_text}</text>
</svg>'''

    return svg


def main():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN environment variable not set", file=sys.stderr)
        sys.exit(1)

    print("Fetching GitHub stats...")
    stats = get_stats(token)

    print(f"Stats: {stats['repos']} repos, {stats['stars']} stars, "
          f"{stats['commits_30d']} commits (30d), {stats['years_active']} years")

    print("Generating SVG...")
    svg = generate_svg(stats)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    with open(OUTPUT_PATH, "w") as f:
        f.write(svg)

    print(f"SVG written to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

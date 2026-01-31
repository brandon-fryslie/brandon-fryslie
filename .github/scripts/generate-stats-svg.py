#!/usr/bin/env python3
"""
Generate daily stats SVG for GitHub profile.
Queries GitHub API for stats and creates an animated SVG matching the atelier aesthetic.
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

# Colors from atelier theme
IVORY = "#f5f0e8"
BURGUNDY = "#8b4049"
WARM_GRAY = "#6b5d47"
DARK = "#1a1a1a"

USERNAME = "brandon-fryslie"
OUTPUT_PATH = "assets/atelier-daily-art.svg"


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

    # Top 3 languages
    stats["top_languages"] = sorted(lang_counts.items(), key=lambda x: x[1], reverse=True)[:3]

    return stats


def generate_svg(stats):
    """Generate SVG with SMIL animations."""
    width = 1200
    height = 200

    # Format top languages
    lang_text = " · ".join([f"{lang} ({count})" for lang, count in stats["top_languages"]])

    svg = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Gradient background -->
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:{IVORY};stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ebe6dd;stop-opacity:1" />
    </linearGradient>

    <!-- Grid pattern -->
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{WARM_GRAY}" stroke-width="0.5" opacity="0.2"/>
    </pattern>
  </defs>

  <!-- Background -->
  <rect width="{width}" height="{height}" fill="url(#bg)"/>
  <rect width="{width}" height="{height}" fill="url(#grid)">
    <animate attributeName="opacity" values="0.3;0.5;0.3" dur="13s" repeatCount="indefinite"/>
  </rect>

  <!-- Border -->
  <rect x="2" y="2" width="{width-4}" height="{height-4}" fill="none" stroke="{BURGUNDY}" stroke-width="2"/>

  <!-- Title -->
  <text x="40" y="45" font-family="monospace" font-size="24" fill="{DARK}" font-weight="bold">
    Daily Statistics
  </text>
  <text x="40" y="70" font-family="monospace" font-size="14" fill="{WARM_GRAY}">
    Updated {datetime.now().strftime("%Y-%m-%d")}
  </text>

  <!-- Stats Grid -->
  <g transform="translate(40, 100)">
    <!-- Repos -->
    <text x="0" y="0" font-family="monospace" font-size="16" fill="{BURGUNDY}" font-weight="bold">
      {stats["repos"]}
      <animate attributeName="opacity" values="1;0.6;1" dur="7s" repeatCount="indefinite"/>
    </text>
    <text x="0" y="20" font-family="monospace" font-size="12" fill="{WARM_GRAY}">
      Repositories
    </text>

    <!-- Stars -->
    <text x="200" y="0" font-family="monospace" font-size="16" fill="{BURGUNDY}" font-weight="bold">
      {stats["stars"]}
      <animate attributeName="opacity" values="1;0.6;1" dur="11s" repeatCount="indefinite"/>
    </text>
    <text x="200" y="20" font-family="monospace" font-size="12" fill="{WARM_GRAY}">
      Stars
    </text>

    <!-- Commits -->
    <text x="400" y="0" font-family="monospace" font-size="16" fill="{BURGUNDY}" font-weight="bold">
      {stats["commits_30d"]}
      <animate attributeName="opacity" values="1;0.6;1" dur="13s" repeatCount="indefinite"/>
    </text>
    <text x="400" y="20" font-family="monospace" font-size="12" fill="{WARM_GRAY}">
      Commits (30d)
    </text>

    <!-- Years -->
    <text x="600" y="0" font-family="monospace" font-size="16" fill="{BURGUNDY}" font-weight="bold">
      {stats["years_active"]}+
      <animate attributeName="opacity" values="1;0.6;1" dur="17s" repeatCount="indefinite"/>
    </text>
    <text x="600" y="20" font-family="monospace" font-size="12" fill="{WARM_GRAY}">
      Years Active
    </text>
  </g>

  <!-- Languages -->
  <text x="40" y="170" font-family="monospace" font-size="12" fill="{WARM_GRAY}">
    Top Languages: {lang_text}
  </text>

  <!-- Animated accent line -->
  <line x1="0" y1="{height/2}" x2="{width}" y2="{height/2}" stroke="{BURGUNDY}" stroke-width="1" opacity="0.3">
    <animate attributeName="opacity" values="0.1;0.3;0.1" dur="11s" repeatCount="indefinite"/>
  </line>
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

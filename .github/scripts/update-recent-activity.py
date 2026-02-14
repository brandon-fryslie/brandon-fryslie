#!/usr/bin/env python3
"""
Update Recent Activity section in README.
Replaces content between comment markers with latest repo activity.
"""

import os
import re
import sys
from datetime import datetime

try:
    import requests
except ImportError:
    import urllib.request
    import json

USERNAME = "brandon-fryslie"
README_FILES = ["README.md"]
START_MARKER = "<!-- RECENT-ACTIVITY:START -->"
END_MARKER = "<!-- RECENT-ACTIVITY:END -->"


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


def get_recent_repos(token, limit=5):
    """Get the most recently pushed repos by the user."""
    repos = github_api_get(
        f"/users/{USERNAME}/repos?sort=pushed&direction=desc&per_page={limit + 5}",
        token
    )

    recent = []
    for repo in repos:
        # Skip forks unless they have significant activity
        if repo.get("fork") and repo.get("stargazers_count", 0) == 0:
            continue

        pushed_at = datetime.strptime(repo["pushed_at"], "%Y-%m-%dT%H:%M:%SZ")
        date_str = pushed_at.strftime("%b %d, %Y")

        recent.append({
            "name": repo["name"],
            "full_name": repo["full_name"],
            "description": repo.get("description") or "No description",
            "html_url": repo["html_url"],
            "pushed_at": pushed_at,
            "date_str": date_str,
            "stars": repo.get("stargazers_count", 0),
            "language": repo.get("language") or "Unknown"
        })

    return recent[:limit]


def format_activity_section(repos):
    """Format the activity section as markdown."""
    now_str = datetime.now().strftime("%B %d, %Y")
    lines = [
        START_MARKER,
        "",
        f"*Last updated {now_str} · 5 most recently active repositories*",
        ""
    ]

    for repo in repos:
        stars_text = f"⭐ {repo['stars']}" if repo['stars'] > 0 else ""
        parts = [repo['language'], stars_text, repo['date_str']]
        meta = " · ".join(filter(None, parts))

        lines.append(f"**[{repo['name']}]({repo['html_url']})** — {repo['description']}")
        lines.append(f"<br/><sub>{meta}</sub>")
        lines.append("")

    lines.append(END_MARKER)
    return "\n".join(lines)


def update_readme(file_path, new_content):
    """Update README file by replacing content between markers."""
    if not os.path.exists(file_path):
        print(f"Warning: {file_path} does not exist, skipping", file=sys.stderr)
        return False

    with open(file_path, "r") as f:
        content = f.read()

    # Check if markers exist
    if START_MARKER not in content or END_MARKER not in content:
        print(f"Warning: Markers not found in {file_path}, skipping", file=sys.stderr)
        return False

    # Replace content between markers
    pattern = f"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}"
    new_content_full = re.sub(pattern, new_content, content, flags=re.DOTALL)

    # Write back
    with open(file_path, "w") as f:
        f.write(new_content_full)

    print(f"Updated {file_path}")
    return True


def main():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN environment variable not set", file=sys.stderr)
        sys.exit(1)

    print("Fetching recent repository activity...")
    repos = get_recent_repos(token)

    print(f"Found {len(repos)} recent repos:")
    for repo in repos:
        print(f"  - {repo['name']} ({repo['date_str']})")

    print("\nGenerating activity section...")
    new_content = format_activity_section(repos)

    print("\nUpdating README files...")
    success_count = 0
    for readme_file in README_FILES:
        if update_readme(readme_file, new_content):
            success_count += 1

    if success_count == 0:
        print("\nError: No README files were updated", file=sys.stderr)
        sys.exit(1)

    print(f"\nSuccessfully updated {success_count} file(s)")


if __name__ == "__main__":
    main()

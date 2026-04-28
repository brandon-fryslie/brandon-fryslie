#!/usr/bin/env python3
"""Extract README marker contents into docs/daily.json.

This is the bridge between the constrained profile (markdown + sandboxed SVG)
and the unconstrained Pages site (HTML + JS + WebGPU). The same daily content
engine writes the README; this post-processing step harvests the marker
regions into a structured JSON file that the Pages site fetches at load.

Run after the narrative job finishes its README rewrite. Idempotent — safe
to invoke even if a marker is missing (emits an empty string for it).
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
README = REPO_ROOT / "README.md"
DOCS = REPO_ROOT / "docs"
OUTPUT = DOCS / "daily.json"

MARKERS = ("DAILY-DOODLE", "INTRO-PROSE", "RECENT-ACTIVITY", "SELECTED-PROJECTS")


def extract_marker(text: str, name: str) -> str:
    """Return content between <!-- NAME:START --> and <!-- NAME:END -->."""
    pattern = re.compile(
        rf"<!--\s*{re.escape(name)}:START\s*-->(.*?)<!--\s*{re.escape(name)}:END\s*-->",
        re.DOTALL,
    )
    match = pattern.search(text)
    return match.group(1).strip() if match else ""


def first_paragraph(markdown: str) -> str:
    """Pull the first non-empty paragraph for use as a tagline."""
    for block in markdown.split("\n\n"):
        line = block.strip()
        if line and not line.startswith("#") and not line.startswith("<"):
            # Strip italics and inline emphasis for a clean tagline
            line = re.sub(r"\*+([^*]+)\*+", r"\1", line)
            return line.split("\n")[0].strip()
    return ""


def main() -> int:
    if not README.exists():
        print(f"error: {README} not found", file=sys.stderr)
        return 1

    text = README.read_text(encoding="utf-8")
    sections = {name: extract_marker(text, name) for name in MARKERS}

    intro_md = sections["INTRO-PROSE"]
    activity_md = sections["RECENT-ACTIVITY"]
    projects_html = sections["SELECTED-PROJECTS"]
    doodle_html = sections["DAILY-DOODLE"]

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "tagline": first_paragraph(intro_md),
        "intro": {"markdown": intro_md},
        "activity": {"markdown": activity_md},
        # Projects are an HTML table in the source — pass through verbatim
        # rather than reformatting; the Pages JS handles either shape.
        "projects": {"html": projects_html, "markdown": projects_html},
        "doodle": {
            "html": doodle_html,
            # The doodle job mirrors the SVG into docs/assets/ so this stable
            # relative path resolves under GitHub Pages (which serves /docs/
            # as the site root and can't reach back to /assets/).
            "svg_path": "assets/daily-highlight.svg",
        },
    }

    DOCS.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(REPO_ROOT)} ({len(json.dumps(payload))} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

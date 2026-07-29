#!/usr/bin/env python3
"""Regenerate the previous-work index and README's PREVIOUS-WORK block from disk.

Whether a week is "in progress" or finalized, and what a finalized week's topic
line reads, are facts that already live in previous-work/<year>/<monday>.md —
this script derives both surfaces from that one source rather than tracking
either as a separately maintained flag that could drift from the files.

Run after the weekly-archive workflow finalizes a week's file.
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
PREVIOUS_WORK = REPO_ROOT / "previous-work"
PREVIOUS_WORK_README = PREVIOUS_WORK / "README.md"
README = REPO_ROOT / "README.md"

IN_PROGRESS_LINE = (
    "*In progress — the summary header is added when the week closes on Monday.*"
)
WEEK_FILE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})\.md$")
README_BLOCK_LIMIT = 7  # in-progress week (if any) + last ~6 finalized


def replace_marker(text: str, name: str, new_body: str) -> str:
    """Replace the content between <!-- NAME:START --> and <!-- NAME:END -->."""
    pattern = re.compile(
        rf"(<!--\s*{re.escape(name)}:START\s*-->\n).*?(\n<!--\s*{re.escape(name)}:END\s*-->)",
        re.DOTALL,
    )
    if not pattern.search(text):
        raise ValueError(f"marker {name} not found")
    return pattern.sub(lambda m: m.group(1) + new_body + m.group(2), text)


class Week:
    def __init__(self, path: Path):
        self.path = path
        m = WEEK_FILE_RE.match(path.name)
        self.monday = date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        lines = path.read_text(encoding="utf-8").splitlines()
        # Fixed template: line 0 is the title, line 1 blank, line 2 is either
        # the in-progress placeholder or the finalized bold topic line.
        placeholder_present = len(lines) > 2 and lines[2].strip() == IN_PROGRESS_LINE
        self.finalized = not placeholder_present
        self.topic = self._extract_topic(lines) if self.finalized else None

    @staticmethod
    def _extract_topic(lines: list[str]) -> str:
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("**") and stripped.endswith("**") and len(stripped) > 4:
                return stripped[2:-2]
        return "(untitled week)"

    @property
    def title(self) -> str:
        return self.monday.strftime("%B %-d")

    def summary_text(self) -> str:
        return self.topic if self.finalized else "*in progress*"


def discover_weeks() -> list[Week]:
    weeks = []
    for year_dir in sorted(PREVIOUS_WORK.glob("[0-9][0-9][0-9][0-9]")):
        if not year_dir.is_dir():
            continue
        for f in sorted(year_dir.glob("*.md")):
            if WEEK_FILE_RE.match(f.name):
                weeks.append(Week(f))
    weeks.sort(key=lambda w: w.monday, reverse=True)
    return weeks


def render_full_index(weeks: list[Week]) -> str:
    """The full, newest-first archive index for previous-work/README.md."""
    lines: list[str] = []
    for year in sorted({w.monday.year for w in weeks}, reverse=True):
        lines.append(f"## {year}")
        lines.append("")
        for w in weeks:
            if w.monday.year != year:
                continue
            rel = f"{w.monday.year}/{w.path.name}"
            lines.append(f"- **[Week of {w.title}]({rel})** — {w.summary_text()}")
        lines.append("")
    return "\n".join(lines).rstrip("\n")


def render_readme_block(weeks: list[Week]) -> str:
    """The compact, visible list for README.md's PREVIOUS-WORK marker."""
    lines = ["### Previous Engineering Work", ""]
    for w in weeks[:README_BLOCK_LIMIT]:
        rel = f"./previous-work/{w.monday.year}/{w.path.name}"
        lines.append(f"- **[Week of {w.title}]({rel})** — {w.summary_text()}")
    lines.append("")
    lines.append("[Full archive →](./previous-work/)")
    return "\n".join(lines)


def main() -> int:
    weeks = discover_weeks()
    if not weeks:
        print("No previous-work week files found — nothing to render.", file=sys.stderr)
        return 1

    pw_text = PREVIOUS_WORK_README.read_text(encoding="utf-8")
    pw_text = replace_marker(pw_text, "WORK-INDEX", "\n" + render_full_index(weeks) + "\n")
    PREVIOUS_WORK_README.write_text(pw_text, encoding="utf-8")
    print(f"wrote {PREVIOUS_WORK_README.relative_to(REPO_ROOT)} ({len(weeks)} weeks)")

    readme_text = README.read_text(encoding="utf-8")
    readme_text = replace_marker(readme_text, "PREVIOUS-WORK", "\n" + render_readme_block(weeks) + "\n")
    README.write_text(readme_text, encoding="utf-8")
    print(f"wrote {README.relative_to(REPO_ROOT)} PREVIOUS-WORK block")

    return 0


if __name__ == "__main__":
    sys.exit(main())

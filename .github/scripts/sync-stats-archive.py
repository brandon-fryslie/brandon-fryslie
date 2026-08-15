#!/usr/bin/env python3
"""Bring stats-archive/ and STATS.md into agreement with git history.

Every version of assets/daily-stats.svg that has ever been committed is a card
that was live on the profile for a day, so git history — not a bookkeeping file,
and not a copy-before-overwrite step in the workflow — is the authoritative
record of which cards existed. This script derives the archive tree from that
history and the gallery from the archive tree, which is what makes it safe to
run at any time: backfilling six months and archiving yesterday are the same
operation, and a run that was skipped, failed, or lost to a force-push heals on
the next one. There is deliberately no --backfill flag; there is nothing for it
to select.

The doodle archive works the other way round (the job copies the live SVG aside
and prepends a gallery entry), which is why its gallery can drift from its tree.
Do not "align" this script to that shape.

Cards are stamped with the commit's *author* date. The push loop in
daily-highlights.yml rebases on contention, which rewrites committer dates but
preserves author dates; stamping from the committer date would let an already
archived card reappear under a second name after any contended push.

Usage: python .github/scripts/sync-stats-archive.py
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = REPO_ROOT / "stats-archive"
GALLERY = REPO_ROOT / "STATS.md"

CARD_PATH = "assets/daily-stats.svg"
SEAM_PATH = "assets/daily-stats.json"
GALLERY_MARKER = "STATS-GALLERY"
CARD_WIDTH = 960  # matches the card's own <img> in README.md

# Legacy cards came from the deterministic generator, which renders each metric
# as a fixed trio of font sizes. Agent-authored cards (August 2026 onward) are
# freeform data-visualisations with no such convention — those carry the data
# seam instead, so nothing here has to guess at them.
LEGACY_TEXT = re.compile(r'<text[^>]*font-size="(\d+)"[^>]*>([^<]*)</text>')
LEGACY_VALUE_SIZE, LEGACY_LABEL_SIZE, LEGACY_PERIOD_SIZE = "28", "12", "10"
STAMP_FORMAT = "%Y-%m-%d-%H%M%S"


def git(*args: str) -> str:
    """Run a git command, or abort. Never let a failed read reach the archive."""
    done = subprocess.run(
        ["git", "-C", str(REPO_ROOT), *args], capture_output=True, text=True
    )
    if done.returncode != 0:
        sys.exit(f"ERROR: git {' '.join(args)} failed: {done.stderr.strip()}")
    return done.stdout


@dataclass(frozen=True)
class Metric:
    label: str
    value: str
    period: str
    maximum: int | None = None

    def render(self) -> str:
        of_max = f"/{self.maximum}" if self.maximum else ""
        period = f" ({self.period})" if self.period else ""
        return f"{self.label} {self.value}{of_max}{period}"


@dataclass(frozen=True)
class Card:
    """One historical stats card, already resolved to a single uniform shape.

    Both eras of card land here identically, so nothing downstream — archive
    writing, gallery rendering — has to know that legacy cards were parsed out
    of SVG text while modern ones came from the JSON data seam.
    """

    stamp: datetime
    commit: str
    svg: str
    metrics: list[Metric]
    source: str

    @property
    def name(self) -> str:
        return self.stamp.strftime(STAMP_FORMAT)

    @property
    def svg_path(self) -> Path:
        return ARCHIVE / f"{self.stamp:%Y}" / f"{self.stamp:%m}" / f"{self.name}.svg"

    @property
    def record_path(self) -> Path:
        return self.svg_path.with_suffix(".json")

    def record(self) -> dict:
        """The gallery's only input: the numbers, their provenance, and a way back.

        The full data seam is not copied here — it is already in git history at
        `commit`, and a second copy of it could only ever disagree with the first.
        """
        return {
            "stamp": self.name,
            "date": self.stamp.strftime("%Y-%m-%d"),
            "commit": self.commit,
            "source": self.source,
            "metrics": [
                {
                    "label": m.label,
                    "value": m.value,
                    "period": m.period,
                    **({"max": m.maximum} if m.maximum else {}),
                }
                for m in self.metrics
            ],
        }


def metrics_from_seam(seam_json: str) -> list[Metric]:
    seam = json.loads(seam_json)
    return [
        Metric(m["label"], str(m["value"]), m.get("period", ""), m.get("max"))
        for m in seam["metrics"]
    ]


def metrics_from_card_text(svg: str) -> list[Metric]:
    """Recover a legacy card's metrics from its own rendered text.

    Returns nothing rather than a partial reading: a caption assembled from
    mismatched labels and values would state numbers this profile never showed,
    which is worse than a card with no caption at all.
    """
    by_size: dict[str, list[str]] = {}
    for size, body in LEGACY_TEXT.findall(svg):
        by_size.setdefault(size, []).append(body.strip())

    values = by_size.get(LEGACY_VALUE_SIZE, [])
    # The card's own "Updated <date>" header shares the label font size.
    labels = [t for t in by_size.get(LEGACY_LABEL_SIZE, []) if not t.startswith("Updated ")]
    periods = by_size.get(LEGACY_PERIOD_SIZE, [])

    if not values or len(values) != len(labels):
        return []
    if periods and len(periods) != len(labels):
        return []
    # Legacy cards render the period already parenthesised ("(30 Days)") while the
    # data seam stores it bare ("30 Days"). Normalise here so a Metric means the
    # same thing whichever era produced it and rendering never has to ask.
    # February-era cards carry no period line; pair every label with a blank one.
    return [
        Metric(label, value, period.strip("()"))
        for label, value, period in zip(labels, values, periods or [""] * len(labels))
    ]


def read_history() -> list[Card]:
    """Parse every committed version of the card into resolved Card records."""
    log = git("log", "--format=%H %aI", "--reverse", "--", CARD_PATH).strip()
    if not log:
        sys.exit(f"ERROR: no commits touch {CARD_PATH} — wrong repo, or a shallow clone")

    cards: list[Card] = []
    for line in log.splitlines():
        commit, authored = line.split()
        svg = git("show", f"{commit}:{CARD_PATH}")
        if not svg.strip():
            sys.exit(f"ERROR: {commit} has an empty {CARD_PATH}")

        seam = git("show", f"{commit}:{SEAM_PATH}") if seam_exists(commit) else ""
        metrics = metrics_from_seam(seam) if seam else metrics_from_card_text(svg)
        source = "data-seam" if seam else ("card-text" if metrics else "none")

        cards.append(
            Card(
                stamp=datetime.fromisoformat(authored).astimezone(timezone.utc),
                commit=commit,
                svg=svg,
                metrics=metrics,
                source=source,
            )
        )
    return cards


def seam_exists(commit: str) -> bool:
    """Whether the data seam was committed alongside this card."""
    return (
        subprocess.run(
            ["git", "-C", str(REPO_ROOT), "cat-file", "-e", f"{commit}:{SEAM_PATH}"],
            capture_output=True,
        ).returncode
        == 0
    )


def write_archive(cards: list[Card]) -> int:
    """Materialise every card that is not on disk yet. Never overwrite one."""
    added = 0
    for card in cards:
        card.svg_path.parent.mkdir(parents=True, exist_ok=True)
        if card.svg_path.exists():
            if card.svg_path.read_text(encoding="utf-8") != card.svg:
                sys.exit(
                    f"ERROR: {card.svg_path.relative_to(REPO_ROOT)} differs from the card at"
                    f" {card.commit[:8]}. An archived card is immutable, so this means the"
                    " file was hand-edited or history was rewritten. Resolve deliberately."
                )
        else:
            card.svg_path.write_text(card.svg, encoding="utf-8")
            added += 1
        card.record_path.write_text(
            json.dumps(card.record(), indent=2) + "\n", encoding="utf-8"
        )
    return added


def load_records() -> list[dict]:
    """Read the archive tree back. The gallery is a function of disk, not of git.

    Rendering from the freshly-read tree rather than from the in-memory cards is
    what guarantees the page and the directory cannot disagree: if a file is not
    on disk, it is not in the gallery, and there is no third place to check.
    """
    records = [json.loads(p.read_text(encoding="utf-8")) for p in ARCHIVE.glob("*/*/*.json")]
    records.sort(key=lambda r: r["stamp"], reverse=True)
    return records


def render_entry(record: dict) -> str:
    stamp = datetime.strptime(record["stamp"], STAMP_FORMAT)
    heading = f"{stamp:%B %-d, %Y} · {stamp:%H:%M} UTC"
    metrics = [
        Metric(m["label"], m["value"], m.get("period", ""), m.get("max")) for m in record["metrics"]
    ]
    summary = " · ".join(m.render() for m in metrics)
    relative = f"./stats-archive/{stamp:%Y}/{stamp:%m}/{record['stamp']}.svg"

    # The caption below the image carries the numbers, so the alt text does not
    # repeat them — a screen reader would otherwise announce every figure twice.
    # An empty metric list yields an empty caption, which the join drops: the
    # entry's shape does not change with the card's era.
    caption = [summary] if summary else []
    return "\n\n".join(
        [
            f"## {heading}",
            f'<img src="{relative}" width="{CARD_WIDTH}"'
            f' alt="Live GitHub stats card for {stamp:%B %-d, %Y}">',
            *caption,
            "---",
        ]
    )


def replace_marker(text: str, name: str, body: str) -> str:
    """Swap a marker region's contents, or abort.

    Markers are matched at line start and must appear exactly once each: this
    file's own prose mentions them, and a substring match would silently target
    the sentence describing the contract instead of the region it describes.
    """
    start = re.compile(rf"^<!-- {re.escape(name)}:START -->$", re.M)
    end = re.compile(rf"^<!-- {re.escape(name)}:END -->$", re.M)
    if len(start.findall(text)) != 1 or len(end.findall(text)) != 1:
        sys.exit(f"ERROR: {name} markers must appear exactly once each, at line start")
    return text[: start.search(text).end()] + body + text[end.search(text).start() :]


def main() -> int:
    cards = read_history()
    added = write_archive(cards)

    records = load_records()
    if len(records) != len(cards):
        sys.exit(
            f"ERROR: archive holds {len(records)} cards but history has {len(cards)}."
            " The tree and git history must agree exactly."
        )

    body = "\n\n" + "\n\n".join(render_entry(r) for r in records) + "\n"
    GALLERY.write_text(
        replace_marker(GALLERY.read_text(encoding="utf-8"), GALLERY_MARKER, body),
        encoding="utf-8",
    )

    uncaptioned = sum(1 for r in records if not r["metrics"])
    print(
        f"archive: {len(cards)} cards ({added} newly written) · "
        f"gallery: {len(records)} entries ({uncaptioned} without metrics)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

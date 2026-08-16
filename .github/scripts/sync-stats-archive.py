#!/usr/bin/env python3
"""Bring stats-archive/ and STATS.md into agreement with git history.

Every version of assets/daily-stats.svg that has ever been committed is a card
that was live on the profile for a day, so git history — not a bookkeeping file,
and not a copy-before-overwrite step in the workflow — is the authoritative
record of which cards existed. This script derives the archive's slots from that
history and the gallery from the archive tree, which is what makes it safe to
run at any time: backfilling six months and archiving yesterday are the same
operation, and a run that was skipped, failed, or lost to a force-push heals on
the next one. There is deliberately no --backfill flag; there is nothing for it
to select.

History decides the slots; the tree owns their contents. A slot already holding
both its files is left exactly as it is, so remaster-stats-card.py can replace a
deterministic-era card with an authored one without the next morning's sync
quietly putting the old one back. See stats-archive/README.md.

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

sys.path.insert(0, str(Path(__file__).resolve().parent))
from stats_archive import (  # noqa: E402
    CARD_PATH,
    GALLERY,
    REPO_ROOT,
    SEAM_PATH,
    STAMP_FORMAT,
    all_records,
    card_record,
    metric_record,
    record_path,
    stamp_of,
    svg_path,
    write_record,
)
from stats_archive import metrics_from_seam as seam_metrics  # noqa: E402

GALLERY_MARKER = "STATS-GALLERY"
CARD_WIDTH = 960  # matches the card's own <img> in README.md

# Legacy cards came from the deterministic generator, which renders each metric
# as a fixed trio of font sizes. Agent-authored cards (August 2026 onward) are
# freeform data-visualisations with no such convention — those carry the data
# seam instead, so nothing here has to guess at them.
LEGACY_TEXT = re.compile(r'<text[^>]*font-size="(\d+)"[^>]*>([^<]*)</text>')
LEGACY_VALUE_SIZE, LEGACY_LABEL_SIZE, LEGACY_PERIOD_SIZE = "28", "12", "10"


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
        return stamp_of(self.stamp)

    @property
    def svg_path(self) -> Path:
        return svg_path(self.name)

    @property
    def record_path(self) -> Path:
        return record_path(self.name)

    def record(self) -> dict:
        """The gallery's only input. Shape owned by `stats_archive.card_record`, which
        the remaster path writes through too, so one schema serves both writers."""
        return card_record(
            self.name,
            self.commit,
            self.source,
            [metric_record(m.label, m.value, m.period, m.maximum) for m in self.metrics],
        )


def metrics_from_seam(seam_json: str) -> list[Metric]:
    return [
        Metric(m["label"], m["value"], m["period"], m.get("max"))
        for m in seam_metrics(json.loads(seam_json))
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
    """Fill in every card slot history knows about that the tree does not have yet.

    Write-once, per slot: a slot holding both its files is already materialised and is
    left exactly as it is. History supplies what is missing; it does not restate what is
    present.

    This is the seam that lets `remaster-stats-card.py` replace a deterministic-era card
    in place. Re-deriving an existing slot every run would undo each remaster on the next
    morning's sync — and worse, would re-caption the new card with the numbers the old
    one rendered, since the sidecar is where the gallery reads its figures from.

    The slot is the unit, not the file: a half-written slot (svg without sidecar, or the
    reverse) is re-derived whole rather than left in a state where the gallery can read
    one card's picture under another's numbers.
    """
    added = 0
    for card in cards:
        if card.svg_path.exists() and card.record_path.exists():
            continue
        card.svg_path.parent.mkdir(parents=True, exist_ok=True)
        card.svg_path.write_text(card.svg, encoding="utf-8")
        write_record(card.record_path, card.record())
        added += 1
    return added


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

    records = all_records()
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

#!/usr/bin/env python3
"""Layout of the stats card archive: where a card lives, and how its stamp is read.

Two scripts write into `stats-archive/` — `sync-stats-archive.py` materialises cards
out of git history, and `remaster-stats-card.py` replaces deterministic-era cards with
authored ones. Both need the same four facts: where the tree is rooted, how a stamp is
spelled, which two files a stamp resolves to, and what instant it names. Those facts
live here once. Two copies of a filename convention is two clocks, and the day they
disagree one script silently writes cards the other cannot find.
[LAW:one-source-of-truth]

Importable name (underscores, not hyphens) on purpose — the two callers are CLIs and
this is the library they share.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = REPO_ROOT / "stats-archive"
GALLERY = REPO_ROOT / "STATS.md"

CARD_PATH = "assets/daily-stats.svg"
SEAM_PATH = "assets/daily-stats.json"

STAMP_FORMAT = "%Y-%m-%d-%H%M%S"


def stamp_of(moment: datetime) -> str:
    return moment.strftime(STAMP_FORMAT)


def instant_of(stamp: str) -> datetime:
    """The UTC instant a stamp names — the moment that card's data described.

    Raises on a malformed stamp rather than returning a fallback: every caller uses the
    result to bound a data query, and a wrong instant would silently produce a card full
    of the wrong day's numbers. [LAW:parse-dont-validate]
    """
    return datetime.strptime(stamp, STAMP_FORMAT).replace(tzinfo=timezone.utc)


def svg_path(stamp: str) -> Path:
    moment = instant_of(stamp)
    return ARCHIVE / f"{moment:%Y}" / f"{moment:%m}" / f"{stamp}.svg"


def record_path(stamp: str) -> Path:
    return svg_path(stamp).with_suffix(".json")


def read_record(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_record(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")


def metric_record(label: str, value: str, period: str, maximum: int | None = None) -> dict:
    """One metric as the gallery stores it. A falsy `max` is omitted rather than stored
    as null, so `"max" in m` stays the question callers actually mean."""
    return {
        "label": label,
        "value": str(value),
        "period": period,
        **({"max": maximum} if maximum else {}),
    }


def card_record(stamp: str, commit: str, source: str, metrics: list[dict]) -> dict:
    """The sidecar for one archived card: the numbers, their provenance, and a way back.

    The full data seam is deliberately not copied in — for a history-derived card it
    already exists at `commit`, and a second copy could only ever disagree with the first.

    `source` names where these numbers were read from: `data-seam` (the machine-readable
    seam the card was drawn from), `card-text` (recovered from a deterministic card's own
    rendered text), or `none` (unrecoverable — the entry gets no caption rather than a
    wrong one).
    """
    return {
        "stamp": stamp,
        "date": instant_of(stamp).strftime("%Y-%m-%d"),
        "commit": commit,
        "source": source,
        "metrics": metrics,
    }


def metrics_from_seam(seam: dict) -> list[dict]:
    """Sidecar metrics read out of a `assets/daily-stats.json` data seam."""
    return [
        metric_record(m["label"], m["value"], m.get("period", ""), m.get("max"))
        for m in seam["metrics"]
    ]


def all_records() -> list[dict]:
    """Every archived card's sidecar, newest first. The tree is the only thing consulted:
    a card that is not on disk is not in the archive, and there is no second place to
    check."""
    records = [read_record(p) for p in ARCHIVE.glob("*/*/*.json")]
    records.sort(key=lambda r: r["stamp"], reverse=True)
    return records

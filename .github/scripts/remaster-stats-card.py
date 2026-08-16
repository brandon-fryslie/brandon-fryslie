#!/usr/bin/env python3
"""Replace a deterministic-era stats card with one authored from that day's real data.

The archive holds every card the profile has shown. The ones from before August 2026
came from the deterministic generator — a value, a label, a period, three font sizes,
repeated — while everything since is authored as a data-visualisation by the stats-card
agent. This script drives the second kind backwards over the first: it reconstructs the
day's numbers with `generate-stats-svg.py --as-of`, hands them to the same agent under
the same prompt the daily job uses, and drops the result into that day's archive slot.

The card that comes out is not the card that was live. It cannot be: GitHub's commit and
PR search index lags by minutes, so a card generated at 06:03 saw fewer commits than a
query for that same instant sees today. The reconstruction is the more accurate of the
two, not the more faithful one.

Three phases, because a workflow step runs between them:

    select   which slots still hold a deterministic card
    stage    prepare the working tree to author one, and report the instant it describes
    archive  move the authored card into its slot and put the working tree back

Nothing here authors anything or talks to GitHub — `generate-stats-svg.py` fetches the
data and the agent draws the card. This script only moves files into and out of the
places those two expect. [LAW:decomposition]
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from stats_archive import (  # noqa: E402
    CARD_PATH,
    REPO_ROOT,
    SEAM_PATH,
    all_records,
    card_record,
    instant_of,
    metrics_from_seam,
    read_record,
    record_path,
    svg_path,
    write_record,
)

# A card whose numbers were read from a data seam was drawn from that seam — that is
# what an authored card is. Everything else in the archive is a deterministic card
# waiting for its turn, and a remaster writes `data-seam`, so a slot leaves this set by
# being done rather than by being recorded as done. [LAW:one-source-of-truth]
AUTHORED_SOURCE = "data-seam"

# GitHub's ceiling on matrix jobs in one workflow run. A `select` that returned more
# would produce a matrix the workflow silently truncates.
MATRIX_MAX = 256

LIVE_CARD = REPO_ROOT / CARD_PATH
LIVE_SEAM = REPO_ROOT / SEAM_PATH


def git(*args: str) -> str:
    done = subprocess.run(
        ["git", "-C", str(REPO_ROOT), *args], capture_output=True, text=True
    )
    if done.returncode != 0:
        sys.exit(f"ERROR: git {' '.join(args)} failed: {done.stderr.strip()}")
    return done.stdout


def deterministic_stamps() -> list[str]:
    """Archived slots still holding a deterministic card, in the order a visitor meets
    them: newest first, the same order the gallery renders. The first boring card someone
    scrolling STATS.md reaches is the newest one, so that is the one worth fixing first.
    """
    return [r["stamp"] for r in all_records() if r.get("source") != AUTHORED_SOURCE]


def cmd_select(args: argparse.Namespace) -> None:
    """Print the stamps to remaster as a JSON array — the workflow's matrix input.

    `--stamp` narrows the candidates to ones you name; `--limit` caps however many
    survive. Naming a stamp that is already authored yields nothing for it, which is the
    honest answer: re-running a finished slot is not this script's job.
    """
    candidates = deterministic_stamps()
    chosen = [s for s in candidates if s in set(args.stamp)] if args.stamp else candidates

    unknown = sorted(set(args.stamp) - set(candidates))
    print(
        f"{len(candidates)} deterministic card(s) in the archive; "
        f"selecting {min(len(chosen), args.limit)}"
        + (f"; not awaiting remaster: {', '.join(unknown)}" if unknown else ""),
        file=sys.stderr,
    )
    print(json.dumps(chosen[: args.limit]))


def divergence_source(stamp: str) -> Path:
    """The card to put in front of the agent as "the previous card, do not repeat it".

    Its nearest *newer* neighbour, because remastering runs newest-first: that neighbour
    is both already in its final authored form and the card a visitor sees directly above
    this one in the gallery. Falling back to the older neighbour and then to the live card
    keeps this total — there is always some real card to diverge from.
    """
    stamps = sorted(r["stamp"] for r in all_records())
    at = stamps.index(stamp)
    newer = stamps[at + 1 :][:1]
    older = stamps[:at][-1:]
    return next(
        (p for p in [*(svg_path(s) for s in newer + older), LIVE_CARD] if p.exists())
    )


def cmd_stage(args: argparse.Namespace) -> None:
    """Put the working tree in the state the daily job leaves for the agent, and print
    the instant this card's data must describe.

    The agent's prompt names `assets/daily-stats.svg` and `assets/daily-stats.json` and
    is not parameterised by any of this — it is the single source of truth for the card's
    creative direction, shared verbatim with the daily job and the preview workflow. So a
    remaster is staged *into those paths* rather than the prompt being taught a second set.
    [LAW:one-source-of-truth]
    """
    instant = instant_of(args.stamp)
    if not record_path(args.stamp).exists():
        sys.exit(f"ERROR: no archived card at {record_path(args.stamp).relative_to(REPO_ROOT)}")

    source = divergence_source(args.stamp)
    LIVE_CARD.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"staged {source.relative_to(REPO_ROOT)} as the card to diverge from", file=sys.stderr)
    print(f"{instant:%Y-%m-%dT%H:%M:%SZ}")


def cmd_archive(args: argparse.Namespace) -> None:
    """Move the authored card into its archive slot, then restore the working paths.

    The seam's own `date` is checked against the stamp before anything is written: the
    agent is handed a card path and a data file and told to draw one from the other, and
    the one way that goes silently wrong is drawing the right picture for the wrong day.
    A mismatch here means the reconstruction step ran with the wrong `--as-of`, and
    writing it anyway would put numbers in the archive that belong to another date.
    [LAW:no-silent-failure]

    Prints the paths it wrote, one per line, on stdout; the human summary goes to stderr.
    Those paths are the caller's staging list, and they are this slot's alone — which is
    what lets several remasters run at once without two of them writing one file.
    """
    seam = json.loads(LIVE_SEAM.read_text(encoding="utf-8"))
    card = LIVE_CARD.read_text(encoding="utf-8")
    fallback = Path(args.fallback).read_text(encoding="utf-8")
    previous = read_record(record_path(args.stamp))

    # Everything needed is in memory now, so give the working paths back before deciding
    # anything. They are the daily job's files, borrowed as the agent's workspace; a
    # decision below that ends this run must not end it holding them.
    # [LAW:effects-at-boundaries]
    git("checkout", "HEAD", "--", CARD_PATH, SEAM_PATH)

    expected = instant_of(args.stamp).strftime("%Y-%m-%d")
    if seam["date"] != expected:
        sys.exit(
            f"ERROR: seam describes {seam['date']} but the slot is {expected}."
            " The reconstruction ran with the wrong --as-of; refusing to archive it."
        )

    # The agent is told to copy the deterministic fallback in rather than ship a card it
    # cannot make both accurate and legible. For the daily job that is the right answer —
    # the profile needs a card this morning. Here it is not an answer at all: the slot
    # already holds a card, and swapping one deterministic card for another achieves
    # nothing while marking the slot done, which would retire it from the pending set
    # forever. Fail instead, so the run goes red and the next dispatch retries the slot.
    # [LAW:no-silent-failure]
    if card == fallback:
        sys.exit(
            f"ERROR: the agent fell back to the deterministic card for {args.stamp}."
            " Nothing was remastered; leaving the slot pending for a later run."
        )

    svg_path(args.stamp).write_text(card, encoding="utf-8")
    write_record(
        record_path(args.stamp),
        # The commit carries over from the record being replaced: it is still the commit
        # that put a card in this slot and dated it, which is what the field has always
        # meant. Nothing else survives — these numbers and this picture are new.
        card_record(args.stamp, previous["commit"], AUTHORED_SOURCE, metrics_from_seam(seam)),
    )

    values = " · ".join(f"{m['label']} {m['value']}" for m in metrics_from_seam(seam))
    print(f"archived {svg_path(args.stamp).relative_to(REPO_ROOT)} — {values}", file=sys.stderr)

    # The two paths this run touched, for the caller to stage — stdout is the machine
    # channel here, as it is for `stage`. The workflow must not glob them back out of the
    # tree: a stamp resolves to files through `stats_archive`, and a second spelling of
    # that convention in YAML is the copy that eventually disagrees.
    # [LAW:one-source-of-truth]
    for path in (svg_path(args.stamp), record_path(args.stamp)):
        print(path.relative_to(REPO_ROOT))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="phase", required=True)

    p_select = sub.add_parser("select", help="print stamps awaiting remaster as JSON")
    p_select.add_argument("--limit", type=int, default=8,
                          help="most slots to return (default: %(default)s)")
    p_select.add_argument("--stamp", action="append", default=[],
                          help="restrict to this stamp; repeatable")
    p_select.set_defaults(func=cmd_select)

    p_stage = sub.add_parser("stage", help="prepare the working tree; print the as-of instant")
    p_stage.add_argument("stamp")
    p_stage.set_defaults(func=cmd_stage)

    p_archive = sub.add_parser("archive", help="move the authored card into its slot")
    p_archive.add_argument("stamp")
    p_archive.add_argument("--fallback", required=True, metavar="PATH",
                           help="the deterministic card this run generated; a result "
                                "identical to it means the agent fell back and the slot "
                                "must stay pending")
    p_archive.set_defaults(func=cmd_archive)

    args = parser.parse_args()
    if getattr(args, "limit", 0) > MATRIX_MAX:
        sys.exit(f"ERROR: --limit {args.limit} exceeds GitHub's {MATRIX_MAX}-job matrix ceiling")
    args.func(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())

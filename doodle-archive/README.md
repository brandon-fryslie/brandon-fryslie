# Doodle Archive

Historical record of every daily doodle that has appeared at the top of the GitHub profile README. Written by the `doodle` job in `.github/workflows/daily-highlights.yml`; not hand-edited.

## File layout

```
doodle-archive/
  YYYY/
    MM/
      YYYY-MM-DD-HHMMSS.svg   ← UTC timestamp at the moment of archival
```

- Filenames are the UTC timestamp (`date -u '+%Y-%m-%d-%H%M%S'`) at the moment of archival. The timestamp guarantees every entry has a unique name, so multiple `doodle` runs in the same calendar day accumulate side-by-side instead of overwriting each other.
- Year and zero-padded month directories keep any single directory browseable in the GitHub UI and `ls`.
- The SVG is the exact file that was at `assets/daily-highlight.svg` immediately before the archival run — copied verbatim, not re-rendered. Each SVG carries its metadata in HTML comments: `<!-- theme: ... -->` (a short label, used for the gallery heading) and `<!-- about: ... -->` (two short prose paragraphs — the occasion's story and the composition — rendered as a collapsed `<details>` block under the gallery image). Pre-August-2026 SVGs have only a theme comment, sometimes overloaded with the full write-up; the gallery job splits those instead.
- Older entries (before the timestamped layout existed) use the form `YYYY-MM-DD.svg`. Both forms are valid; the agent only writes the new form.

## How entries get added

Each `doodle` job run, before generating its new doodle:

1. Computes a UTC archival stamp: `STAMP=$(date -u '+%Y-%m-%d-%H%M%S')`.
2. Copies the *current* `assets/daily-highlight.svg` verbatim to `doodle-archive/YYYY/MM/$STAMP.svg`.
3. Prepends a corresponding entry to the gallery in [`DOODLES.md`](../DOODLES.md), immediately after the `<!-- DOODLE-GALLERY:START -->` marker.

Then it overwrites `assets/daily-highlight.svg` with today's new doodle. The archive is therefore additive: every run leaves a new file, and the gallery accumulates one entry per archived doodle in newest-first order. There is no idempotency check — the timestamp does the disambiguation.

If `assets/daily-highlight.svg` doesn't exist yet (very first run ever), the run just generates the first live doodle without archiving anything.

## Relationship to the gallery

[`DOODLES.md`](../DOODLES.md) at the repo root is the human-browsable gallery. Each archived SVG corresponds to a gallery entry. Hand-curated entries (e.g. the **Pinned** section) live *outside* the `<!-- DOODLE-GALLERY:START -->` / `<!-- DOODLE-GALLERY:END -->` marker pair and are never touched by automation.

## What this archive is not

- Not a workspace. Nothing should be edited in place — the only mutation is adding a new file. One-time legacy cleanup is the only allowed exception, and should be paired with a prompt change that explains why.
- Not a backup of the stats SVG. Only the creative doodle is archived; `assets/daily-stats.svg` is regenerated mechanically each run and has no historical interest.

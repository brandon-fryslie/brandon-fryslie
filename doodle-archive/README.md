# Doodle Archive

Historical record of every daily doodle that has appeared at the top of the GitHub profile README. Written by the `doodle` job in `.github/workflows/daily-highlights.yml`; not hand-edited.

## File layout

```
doodle-archive/
  YYYY/
    MM/
      YYYY-MM-DD.svg
```

- One SVG per day, named by the date the doodle was *displayed* on the profile (UTC).
- Year and zero-padded month directories keep any single directory under ~31 entries, so the archive stays browsable in the GitHub web UI and `ls` output indefinitely.
- The SVG is the exact file that was at `assets/daily-highlight.svg` on that date — copied verbatim, not re-rendered. The theme is identifiable from the `<!-- theme: ... -->` comment the prompt requires at the top of every doodle.

## How entries get added

The `doodle` job, before generating a new doodle, copies the *current* `assets/daily-highlight.svg` into the archive at the path corresponding to its displayed date. The displayed date is parsed from the `Updated ...` / `Last updated ...` line in the `RECENT-ACTIVITY` block — the same date used to name the narrative archive under `daily-archive/`. This keeps the doodle archive and the narrative archive aligned: every `daily-archive/YYYY-MM-DD.md` should have a matching `doodle-archive/YYYY/MM/YYYY-MM-DD.svg`.

If the matching archive path already exists, the job leaves it alone — re-runs on the same day are idempotent.

## Relationship to the gallery

[`DOODLES.md`](../DOODLES.md) at the repo root is the human-browsable gallery: one prepended entry per archived doodle, newest first. The same `doodle` job step that copies an SVG into this archive also prepends a corresponding entry to `DOODLES.md`. This directory is the storage substrate (one file per day); `DOODLES.md` is the view.

## What this archive is not

- Not a workspace. Nothing should be edited in place — the only mutation is "add tomorrow's file". One-time legacy cleanup is the only allowed exception, and should be paired with a prompt change that explains why.
- Not a backup of the stats SVG. Only the creative doodle is archived; `assets/daily-stats.svg` is regenerated mechanically each run and has no historical interest.

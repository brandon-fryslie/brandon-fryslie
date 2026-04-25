# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the `brandon-fryslie/brandon-fryslie` GitHub profile repository — `README.md` renders as the public profile page. Most days, **a human does not edit this repo**. A scheduled GitHub Action rewrites parts of `README.md` and regenerates SVG assets every 24 hours. The repo's primary job is to be a stable substrate for that autonomous loop.

When you are asked to change "what shows up on the profile," the answer is almost always to change the workflow prompt or the generator script — not to hand-edit the generated output. See **Update the Generator, Not the Generated Output** below.

## The Daily Rewrite Loop

`.github/workflows/daily-highlights.yml` is the system. It runs at 06:00 UTC and on `workflow_dispatch`. One workflow run contains two jobs that **execute in parallel** and both push to `master`:

| Job                 | Owns these paths                                                          | What it produces |
|---------------------|---------------------------------------------------------------------------|------------------|
| `doodle`            | `README.md` (DAILY-DOODLE + RECENT-ACTIVITY blocks), `DOODLES.md` (DOODLE-GALLERY block), `assets/daily-highlight.svg`, `assets/daily-stats.svg`, `daily-archive/`, `doodle-archive/` | Today's animated SVG "doodle", the recent-activity narrative, an archive of yesterday's narrative, an archive copy of yesterday's doodle SVG, and a prepended gallery entry in `DOODLES.md`. |
| `selected_projects` | `README.md` (SELECTED-PROJECTS block only)                                | A 6-cell project table chosen from Brandon's substantial commit activity over the last 90 days (fallback: 365). |

Concurrency model — important to understand before changing anything:

- **Workflow-level** `concurrency: { group: daily-highlights, cancel-in-progress: false }` prevents two whole runs from interleaving.
- **Within a run**, the two jobs deliberately race. Each job stages **only its own paths** (`git add` is whitelisted per job) and pushes through a 5-attempt `fetch + rebase + push` loop. This is the mechanism by which two parallel Claude invocations can both update `README.md` without stomping each other.
- Each job has a `Verify Claude result` step that parses `steps.claude.outputs.execution_file` (JSONL of the action's run), pulls the last `result` entry, and fails the job if `is_error != false` or `permission_denials_count > 0`. A no-op or denied run is treated as a hard failure, not silently swallowed.

If you are editing this workflow, preserve all three properties: per-job path whitelist on `git add`, rebase-retry on push, and the Verify step. They are load-bearing.

## README Marker Contract

`README.md` is partly hand-authored and partly machine-rewritten. Three marker pairs delimit the machine-owned regions. Markers are exact strings; never rename, reformat, or move them:

```
README.md
  <!-- DAILY-DOODLE:START -->        ... <!-- DAILY-DOODLE:END -->
  <!-- RECENT-ACTIVITY:START -->     ... <!-- RECENT-ACTIVITY:END -->
  <!-- SELECTED-PROJECTS:START -->   ... <!-- SELECTED-PROJECTS:END -->

DOODLES.md
  <!-- DOODLE-GALLERY:START -->      ... <!-- DOODLE-GALLERY:END -->
```

Everything outside these markers is hand-authored and should not be touched by automation. Inside the README markers, content is replaced wholesale each run. Inside the `DOODLE-GALLERY` markers, the doodle job *prepends* a new entry per day (newest first) — it does not rewrite prior entries.

## Update the Generator, Not the Generated Output

For anything inside the marker regions, in `assets/daily-highlight.svg`, `assets/daily-stats.svg`, or under `daily-archive/`: **change the prompt or the generator script, not the current artifact.** Editing generated output directly will be overwritten on the next 06:00 UTC run, and worse, it hides the real problem (a bad prompt or generator). The two places to actually fix things:

- **`.github/workflows/daily-highlights.yml`** — the prompt strings for both `doodle` and `selected_projects` jobs. This is where tone rules, theme-picking priorities, the Selected Projects qualification thresholds (≥10 commits in 90d, fallback ≥5 in 365d), and SVG creative direction all live.
- **`.github/scripts/generate-stats-svg.py`** — the deterministic stats SVG. Picks 4 metrics from a pool of 8 with varying time periods. Requires `GITHUB_TOKEN` and `pip install requests`. The doodle job runs this *before* invoking Claude, and the Claude prompt is explicitly told not to touch the resulting file.

The one legitimate exception is a **one-time legacy cleanup** — e.g., a stale archive entry from before a prompt change. Even then, fix the prompt in the same commit.

## SVG Animation Constraints

GitHub renders profile-README SVGs via `<img>` tags in a sanitized, isolated context. The `doodle` prompt restates these constraints, but if you're authoring SVG by hand or tweaking the prompt:

- **No JavaScript** — stripped by GitHub's sanitizer.
- **No `:hover` or other pseudo-classes** — `<img>` context blocks event delivery.
- **No `<a>` links, no `<foreignObject>`** — removed.
- **What works:** CSS `@keyframes`, SMIL `<animate>` / `<animateTransform>`, SVG filters (`feTurbulence`, `feDisplacementMap`, gradients), and `transform-box: fill-box` for reliable transforms. Prefer SMIL over CSS `@keyframes` for better GitHub rendering compatibility.
- Use prime-number durations (7s, 11s, 13s) with staggered delays for organic-feeling motion.
- Background `#0d1117` to match the GitHub dark profile chrome.

`INTERACTIVITY-LIMITS.md` is the comprehensive reference; `RANDOMNESS-GUIDE.md` documents pseudo-random techniques without JS.

## Tone Rules for Generated Narrative

Both Claude prompts enforce: **matter-of-fact reporting, third-person past tense, plain verbs ("Added", "Renamed", "Migrated", "Fixed"). Name repos and concrete artifacts. No editorial adjectives, no promotional framing, no characterization of engineering quality.** If you need to adjust voice, edit the prompts in `daily-highlights.yml` — do not edit yesterday's generated output to "fix" the voice, because tomorrow's run will reintroduce the same drift.

## Theme System (Manual)

The currently active profile is `README.md`. Theme variants are kept as separate files (`README-ATELIER.md`, `README-OBSERVATORY.md`, `README-COURT.md`, `README-CYBERPUNK.md`, `README-MAXIMUM-RIDICULOUS.md`). Switching is a manual `cp` and commit:

```bash
cp README-ATELIER.md README.md && git add README.md && git commit -m "Activate Atelier theme" && git push
```

Switching themes overwrites the marker regions; the next 06:00 UTC run repopulates them. Currently active: **Atelier of Machines That Dream in Geometry**.

## Disabled Workflows

`.github/workflows/update-readme.yml` and `.github/workflows/daily-stats.yml` are older single-purpose workflows superseded by `daily-highlights.yml`. They are kept as `workflow_dispatch`-only and should not be re-enabled on a schedule without first reconciling them with the marker contract above.

## Manual Triggers

```bash
gh workflow run daily-highlights.yml          # full daily rewrite
python .github/scripts/generate-stats-svg.py  # regenerate stats SVG locally (needs GITHUB_TOKEN)
```

## Issue Tracking

This repo uses **lnks** for agent-native issue tracking; see `AGENTS.md` for the full workflow. Common commands:

```bash
lnks quickstart --refresh    # bootstrap session
lnks ready                   # find available work
lnks start <id>              # claim and start
lnks close <id> --reason "Completed"
lnks sync push               # sync with Dolt (also runs on git push via hook)
```

## Session Completion

Work is not complete until `git push` succeeds and `git status` shows "up to date with origin". File follow-ups via `lnks create` before pushing.

## Key Documentation

- `AGENTS.md` — full lnks workflow.
- `INTERACTIVITY-LIMITS.md` — what GitHub allows in profile SVGs.
- `RANDOMNESS-GUIDE.md` — pseudo-random effects without JS.
- `3D-GALLERY.md`, `GALLERY.md` — SVG showcases and 3D transform techniques.
- `QUICKSTART.md` — theme switching commands.

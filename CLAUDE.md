# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the `brandon-fryslie/brandon-fryslie` GitHub profile repository — `README.md` renders as the public profile page. Most days, **a human does not edit this repo**. A scheduled GitHub Action rewrites parts of `README.md` and regenerates SVG assets every 24 hours. The repo's primary job is to be a stable substrate for that autonomous loop.

When you are asked to change "what shows up on the profile," the answer is almost always to change the workflow prompt or the generator script — not to hand-edit the generated output. See **Update the Generator, Not the Generated Output** below.

## The Daily Rewrite Loop

`.github/workflows/daily-highlights.yml` is the system. It runs at 06:00 UTC and on `workflow_dispatch`. One workflow run contains two jobs that **execute in parallel** and both push to `master`:

| Job         | Owns these paths                                                          | What it produces |
|-------------|---------------------------------------------------------------------------|------------------|
| `doodle`    | `README.md` (DAILY-DOODLE block only), `DOODLES.md` (DOODLE-GALLERY block), `assets/daily-highlight.svg`, `assets/daily-stats.svg`, `doodle-archive/` | Today's animated SVG "doodle", an archive copy of yesterday's doodle SVG, and a prepended gallery entry in `DOODLES.md`. The `<img>` tag inside `DAILY-DOODLE` is rewritten idempotently each run. Owns one creative output and its archival infrastructure. |
| `narrative` | `README.md` (INTRO-PROSE + RECENT-ACTIVITY + SELECTED-PROJECTS blocks), `daily-archive/`, `previous-work/` | All three text regions: the daily-rewritten first-person intro prose (anchored to `.github/intro-seed.md`), the bulleted Today/Week/Month recent-activity list with commit/PR links, the 6-cell project table, and an archive of yesterday's recent-activity content. Also appends today's day section to the current week's file under `previous-work/` (the durable weekly work archive; see `previous-work/README.md`). Owns all text-rendering and shares one commit-data query across all three regions. |

Concurrency model — important to understand before changing anything:

- **Workflow-level** `concurrency: { group: daily-highlights, cancel-in-progress: false }` prevents two whole runs from interleaving.
- **Within a run**, the two jobs deliberately race. Each job stages **only its own paths** (`git add` is whitelisted per job) and pushes through a 5-attempt `fetch + rebase + push` loop. This is the mechanism by which two parallel Claude invocations can both update `README.md` without stomping each other.
- Each job has a `Verify Claude result` step that parses `steps.claude.outputs.execution_file` (JSONL of the action's run), pulls the last `result` entry, and fails the job if `is_error != false` or `permission_denials_count > 0`. A no-op or denied run is treated as a hard failure, not silently swallowed.

If you are editing this workflow, preserve all three properties: per-job path whitelist on `git add`, rebase-retry on push, and the Verify step. They are load-bearing.

## The Weekly Archive Finalization Loop

`.github/workflows/weekly-archive.yml` is `workflow_dispatch`-only (no schedule of its own yet — see `brandon-work-archive-iaq.3` for the Monday-cron wiring). It finalizes exactly one already-written week file under `previous-work/`:

1. A deterministic bash step resolves the target Monday (an explicit `week` input, or the most recently completed week by default) and gates the rest of the job: if `previous-work/YYYY/<monday>.md` doesn't exist, that week had no commits and the run is a no-op; if the file no longer contains the `*In progress — ...*` placeholder line, it's already finalized and the run is a no-op. Both no-op paths exit green with zero commits — this is what makes re-dispatching the same week safe.
2. If the week genuinely needs finalizing, a Claude step mines that week's commits and merged-PR descriptions via `gh api` (PR bodies carry the "why" commit messages don't) and replaces *only* the placeholder line with a bold topic line, an italic totals line, and a short summary paragraph. It never touches the day sections or footer already in the file.
3. `.github/scripts/render-previous-work-index.py` then mechanically regenerates `previous-work/README.md`'s index and README.md's `PREVIOUS-WORK` block by scanning every `previous-work/<year>/*.md` file's own content (whether it still has the placeholder line, and what its topic line says). Finalized-vs-in-progress is never tracked as a separate flag — it's read straight from the files, so the two derived surfaces can't drift from what's actually on disk.
4. Same commit/push contract as `daily-highlights.yml`: shared `daily-highlights` concurrency group, path-whitelisted `git add` (`previous-work/` and `README.md`), rebase-retry push, and a `Verify Claude result` step.

## README Marker Contract

`README.md` is partly hand-authored and partly machine-rewritten. Five marker pairs delimit the machine-owned regions. Markers are exact strings; never rename, reformat, or move them:

```
README.md
  <!-- DAILY-DOODLE:START -->        ... <!-- DAILY-DOODLE:END -->        (doodle job)
  <!-- INTRO-PROSE:START -->         ... <!-- INTRO-PROSE:END -->         (narrative job)
  <!-- RECENT-ACTIVITY:START -->     ... <!-- RECENT-ACTIVITY:END -->     (narrative job)
  <!-- PREVIOUS-WORK:START -->       ... <!-- PREVIOUS-WORK:END -->       (weekly-archive job)
  <!-- SELECTED-PROJECTS:START -->   ... <!-- SELECTED-PROJECTS:END -->   (narrative job)

DOODLES.md
  <!-- DOODLE-GALLERY:START -->      ... <!-- DOODLE-GALLERY:END -->      (doodle job)
```

Everything outside these markers is hand-authored and should not be touched by automation. Inside the README markers, content is replaced wholesale each run. Inside the `DOODLE-GALLERY` markers, the doodle job *prepends* a new entry per day (newest first) — it does not rewrite prior entries.

Both jobs concurrently write `README.md` (each owning a non-overlapping marker region) and resolve their push race via the rebase-retry loop. The marker isolation is what makes the parallelism safe.

## Update the Generator, Not the Generated Output

For anything inside the marker regions, in `assets/daily-highlight.svg`, `assets/daily-stats.svg`, or under `daily-archive/`: **change the prompt or the generator script, not the current artifact.** Editing generated output directly will be overwritten on the next 06:00 UTC run, and worse, it hides the real problem (a bad prompt or generator). The three places to actually fix things:

- **`.github/workflows/daily-highlights.yml`** — the prompt strings for both `doodle` and `narrative` jobs. This is where SVG creative direction, theme-picking priorities, the Recent Activity bullet format and link-construction rules, the Selected Projects qualification thresholds (≥10 commits in 90d, fallback ≥5 in 365d), and per-region tone rules all live.
- **`.github/intro-seed.md`** — the voice and stance scaffolding for the INTRO-PROSE region. INTRO-PROSE is a daily journal entry written by Claude in *its* first person about today's work on Brandon's profile (Brandon is "Brandon" or "he," not "I"). The seed defines stance, a theme palette, and the anti-lockstep rule that today's entry must diverge from yesterday's in opening sentence, paragraph order, and theme spine. The seed is deliberately a palette, not a template — it carries no specific projects, dates, or rephrase-this-verbatim bullets. Edit it to change *how the journal sounds* or *what themes Claude is allowed to riff on*; don't edit it to add transient facts.
- **`.github/scripts/generate-stats-svg.py`** — the deterministic stats SVG. Picks 4 metrics from a pool of 8 with varying time periods. Requires `GITHUB_TOKEN` and `pip install requests`. The doodle job runs this *before* invoking Claude, and the Claude prompt is explicitly told not to touch the resulting file.
- **`.github/workflows/weekly-archive.yml`** and **`.github/scripts/render-previous-work-index.py`** — the weekly finalization prompt (topic line, totals, summary tone) and the mechanical index-regeneration script (which weeks count as finalized, how many appear in README.md's `PREVIOUS-WORK` block) respectively.

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

## Tone Rules for Generated Text

Tone splits per region:

- **INTRO-PROSE** (`narrative` job): a daily journal entry in Claude's first person, about today's work on Brandon's profile. Brandon is referred to by name or as "he," never as "I." Dry, deadpan, self-aware about the gag that the human's profile is being written by the assistant. Voice and themes are anchored in `.github/intro-seed.md` — adjust voice there, not in the workflow prompt. Yesterday's intro is read fresh each run from the on-disk README before being overwritten, and today's entry must deliberately diverge from it (different opening sentence, different paragraph order, different theme spine).
- **RECENT-ACTIVITY** (`narrative` job, bulleted format): matter-of-fact, third-person past tense, plain verbs ("Added", "Renamed", "Migrated", "Fixed"). One bullet per repo with activity. Name concrete artifacts. No editorial adjectives, no promotional framing. Links carry SHAs/PR numbers — never put commit hashes in visible text.
- **SELECTED-PROJECTS** (`narrative` job): same matter-of-fact rules as RECENT-ACTIVITY.

If you need to adjust voice, edit the prompts in `daily-highlights.yml` (or `intro-seed.md` for the intro) — do not edit yesterday's generated output to "fix" the voice, because tomorrow's run will reintroduce the same drift.

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
gh workflow run daily-highlights.yml                      # full daily rewrite
gh workflow run weekly-archive.yml                        # finalize the most recently completed week
gh workflow run weekly-archive.yml -f week=2026-07-20      # finalize a specific week (must be a Monday, already ended)
python .github/scripts/generate-stats-svg.py               # regenerate stats SVG locally (needs GITHUB_TOKEN)
python .github/scripts/render-previous-work-index.py       # regenerate the previous-work index locally
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

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the `brandon-fryslie/brandon-fryslie` GitHub profile repository — `README.md` renders as the public profile page. Most days, **a human does not edit this repo**. A scheduled GitHub Action rewrites parts of `README.md` and regenerates SVG assets every 24 hours. The repo's primary job is to be a stable substrate for that autonomous loop.

When you are asked to change "what shows up on the profile," the answer is almost always to change the workflow prompt or the generator script — not to hand-edit the generated output. See **Update the Generator, Not the Generated Output** below.

## The Daily Rewrite Loop

`.github/workflows/daily-highlights.yml` is the system. It runs at 06:00 UTC and on `workflow_dispatch`. One workflow run contains three jobs that **execute in parallel** and all push to `master`:

| Job         | Owns these paths                                                          | What it produces |
|-------------|---------------------------------------------------------------------------|------------------|
| `doodle`    | `README.md` (DAILY-DOODLE block only), `DOODLES.md` (DOODLE-GALLERY block), `assets/daily-highlight.svg`, `doodle-archive/`, `docs/assets/daily-highlight.svg` | Today's animated SVG "doodle", an archive copy of yesterday's doodle SVG, and a prepended `DOODLES.md` gallery entry. The `<img>` tag inside `DAILY-DOODLE` is rewritten idempotently each run. Owns one creative output and its archival infrastructure. |
| `narrative` | `README.md` (INTRO-PROSE + RECENT-ACTIVITY + SELECTED-PROJECTS blocks), `daily-archive/`, `previous-work/` | All three text regions: the daily-rewritten first-person intro prose (anchored to `.github/intro-seed.md`), the bulleted Today/Week/Month recent-activity list with commit/PR links, the 6-cell project table, and an archive of yesterday's recent-activity content. Also appends today's day section to the current week's file under `previous-work/` (the durable weekly work archive; see `previous-work/README.md`). Owns all text-rendering and shares one commit-data query across all three regions. |
| `stats`     | `assets/daily-stats.svg`, `assets/daily-stats.json` | The "Live GitHub Stats" card, authored fresh each day by a **dedicated** Claude invocation as a meaningful data-visualization. A prior mechanical step emits `daily-stats.json` — the rich data seam (a 365-day contribution calendar plus 3–6 relevance-selected metrics, each with its `max`/`breakdown` distribution) and a deterministic fallback card to `/tmp`. The agent visualizes that data (the picture encodes the numbers), an accuracy gate verifies every value is rendered, and it falls back to the deterministic card if it can't. See **Update the Generator** below. |

Concurrency model — important to understand before changing anything:

- **Workflow-level** `concurrency: { group: daily-highlights, cancel-in-progress: false }` prevents two whole runs from interleaving.
- **Within a run**, the three jobs deliberately race. Each job stages **only its own paths** (`git add` is whitelisted per job) and pushes through a 5-attempt `fetch + rebase + push` loop. This is the mechanism by which the parallel Claude invocations can all push to `master` (and both `doodle` and `narrative` update `README.md`, in non-overlapping marker regions) without stomping each other. `stats` touches no shared file — it owns `assets/daily-stats.svg` and `.json` alone.
- Each job has a `Verify Claude result` step that parses `steps.claude.outputs.execution_file` (JSONL of the action's run), pulls the last `result` entry, and fails the job if `is_error != false` or `permission_denials_count > 0`. A no-op or denied run is treated as a hard failure, not silently swallowed.

If you are editing this workflow, preserve all three properties: per-job path whitelist on `git add`, rebase-retry on push, and the Verify step. They are load-bearing.

## The Weekly Archive Finalization Loop

`.github/workflows/weekly-archive.yml` runs on `workflow_dispatch` and on a Monday 07:00 UTC cron (an hour after the daily 06:00 UTC run, so the new week's first doodle/narrative push can't race it). It's split across two jobs:

1. **`resolve-weeks`** — pure date arithmetic, no checkout. An explicit `week` input targets exactly that one Monday. No input (the cron path, or a bare dispatch) computes the last 4 completed Mondays, oldest first, and hands that list down as JSON — this is the self-healing scan: a week whose finalization failed or was skipped gets picked up again by every run for the next 3 weeks.
2. **`finalize`** — matrix-calls the reusable workflow `.github/workflows/finalize-week.yml` once per candidate week, `max-parallel: 1` so pushes within a run stay serial, `fail-fast: false` so one bad week doesn't block the others from self-healing. Each call independently: resolves the Monday and gates on it (if `previous-work/YYYY/<monday>.md` doesn't exist, that week had no commits and the call is a no-op; if the file no longer contains the `*In progress — ...*` placeholder line, it's already finalized and the call is a no-op — both no-op paths exit green with zero commits, which is what makes re-dispatching or re-running the cron safe); if the week genuinely needs finalizing, a Claude step mines that week's commits and merged-PR descriptions via `gh api` (PR bodies carry the "why" commit messages don't) and replaces *only* the placeholder line with a bold topic line, an italic totals line, and a short summary paragraph, never touching the day sections or footer already in the file; `.github/scripts/render-previous-work-index.py` then mechanically regenerates `previous-work/README.md`'s index and README.md's `PREVIOUS-WORK` block by scanning every `previous-work/<year>/*.md` file's own content (whether it still has the placeholder line, and what its topic line says) — finalized-vs-in-progress is never tracked as a separate flag, so the two derived surfaces can't drift from what's actually on disk; then the same commit/push contract as `daily-highlights.yml`: shared `daily-highlights` concurrency group, path-whitelisted `git add` (`previous-work/` and `README.md`), rebase-retry push, and a `Verify Claude result` step.

If you are editing either file, preserve: the per-week no-op gate living only in `finalize-week.yml` (not duplicated in `resolve-weeks`), the shared `daily-highlights` concurrency group at the top of `weekly-archive.yml` (governs the whole run, including every matrix instance), and `max-parallel: 1` on the matrix (removing it lets multiple weeks' commit/push steps race each other within one run).

## README Marker Contract

`README.md` is partly hand-authored and partly machine-rewritten. Five marker pairs delimit the machine-owned regions. Markers are exact strings; never rename, reformat, or move them:

```
README.md
  <!-- DAILY-DOODLE:START -->        ... <!-- DAILY-DOODLE:END -->        (doodle job)
  <!-- INTRO-PROSE:START -->         ... <!-- INTRO-PROSE:END -->         (narrative job)
  <!-- RECENT-ACTIVITY:START -->     ... <!-- RECENT-ACTIVITY:END -->     (narrative job)
  <!-- PREVIOUS-WORK:START -->       ... <!-- PREVIOUS-WORK:END -->       (weekly-archive finalize job)
  <!-- SELECTED-PROJECTS:START -->   ... <!-- SELECTED-PROJECTS:END -->   (narrative job)

DOODLES.md
  <!-- DOODLE-GALLERY:START -->      ... <!-- DOODLE-GALLERY:END -->      (doodle job)
```

Everything outside these markers is hand-authored and should not be touched by automation. Inside the README markers, content is replaced wholesale each run. Inside the `DOODLE-GALLERY` markers, the doodle job *prepends* a new entry per day (newest first) — it does not rewrite prior entries.

Both jobs concurrently write `README.md` (each owning a non-overlapping marker region) and resolve their push race via the rebase-retry loop. The marker isolation is what makes the parallelism safe.

### Stats card deep-links (hand-authored, no marker region)

The Live GitHub Stats `<img>` sits **between** the `INTRO-PROSE:END` and `RECENT-ACTIVITY:START` markers — it is hand-authored substrate, in no machine-owned region, and the `stats` job never `git add`s `README.md` (it owns only `assets/daily-stats.svg` and `.json`). That image is wrapped in a single `<a href="./STATS.md">` (mirroring the doodle's `<a href="./DOODLES.md">`), because GitHub sanitizes SVG in `<img>` context — no `<a>`, `:hover`, `<foreignObject>`, or image maps *inside* the SVG survive, so the only viable click target is the whole image, linked from the surrounding README markup. Do not try to add per-region links inside `assets/daily-stats.svg`; they will be stripped.

`STATS.md` is the destination gallery. Its top section is a **curated grid of static, hand-crafted browse badges** under `assets/stat-badges/` (one per metric: commits, prs-merged, prs-reviewed, repositories, contributions — five **portrait** 150×210 tiles on one row), each wrapped in its own `<a href>` to that metric's live GitHub page. These badges are deliberately **numberless** (the tile is the category; the live count lives on GitHub) and are **created once, not regenerated daily** — so they carry a higher craft bar and are not owned by any job. Honesty rule for the hrefs: search-backed counts (commits, merged PRs) link to the GitHub **search UI**; GraphQL-sourced metrics (PRs reviewed, contributions) link to the **contribution overview**, never a `reviewed-by:`/search query, or the destination would report a different number than the card. There is deliberately **no Issues tile** — this repo tracks work in lit, not GitHub Issues, so a GH issue-search link would browse an empty set (a lit-export mirror + an Issues tile is deferred to `brandon-stats-card-b75.5`). The per-day archive of stats cards lands lower on `STATS.md` (tracked as `brandon-stats-card-b75.4`, blocked on the doodle-gallery styling fix). Because the anchor lives outside all marker regions, no daily run clobbers it; a **manual theme switch** (`cp README-*.md README.md`) would, so re-add the anchor when switching themes (the theme variants don't currently carry the stats card at all).

## Update the Generator, Not the Generated Output

For anything inside the marker regions, in `assets/daily-highlight.svg`, `assets/daily-stats.svg`, or under `daily-archive/`: **change the prompt or the generator script, not the current artifact.** Editing generated output directly will be overwritten on the next 06:00 UTC run, and worse, it hides the real problem (a bad prompt or generator). The three places to actually fix things:

- **`.github/workflows/daily-highlights.yml`** — the prompt strings for both `doodle` and `narrative` jobs. This is where SVG creative direction, theme-picking priorities, the Recent Activity bullet format and link-construction rules, the Selected Projects qualification thresholds (≥10 commits in 90d, fallback ≥5 in 365d), and per-region tone rules all live.
- **`.github/intro-seed.md`** — the voice and stance scaffolding for the INTRO-PROSE region. INTRO-PROSE is a daily journal entry written by Claude in *its* first person about today's work on Brandon's profile (Brandon is "Brandon" or "he," not "I"). The seed defines stance, a theme palette, and the anti-lockstep rule that today's entry must diverge from yesterday's in opening sentence, paragraph order, and theme spine. The seed is deliberately a palette, not a template — it carries no specific projects, dates, or rephrase-this-verbatim bullets. Edit it to change *how the journal sounds* or *what themes Claude is allowed to riff on*; don't edit it to add transient facts.
- **`.github/scripts/generate-stats-svg.py`** — the stats *data*, not its final look. Computes a pool of 7 metrics, drops the boring/zero ones, and selects a **variable 3–6** for the day, then writes `assets/daily-stats.json` — the rich data seam: a universal 365-day contribution `calendar` (time-series) plus each selected metric's exact value and any `max` (denominator, e.g. 252/365 days) or `breakdown` (category distribution, e.g. languages by commit count). It also writes a deterministic fallback SVG (to `/tmp` in CI). Enumeration metrics and all distributions come from the GraphQL `contributionsCollection` — exact and uncapped — *not* the 1000-result-capped commit search; pure counts use search `total_count`. There is deliberately no "PRs reviewed" metric: GitHub disallows self-review and every PR here is authored under Brandon's own account, so that count would always read as zero — a structural artifact, not a real signal. Requires `GITHUB_TOKEN` and `pip install requests`. The **`stats` job** (its own dedicated Claude invocation) runs it before Claude; the agent then authors `daily-stats.svg` as a data-visualization of the seam. That prompt lives in **`.github/prompts/stats-card.md`** — the single source of truth for the card's creative direction, loaded into `$STATS_PROMPT` by both the daily `stats` job and the `stats-preview.yml` workflow so the two can't diverge. Its cardinal rules: *the picture encodes the data* (not decoration with numbers pasted on), the card is *continually animated* (never a one-time entrance that freezes), and the `rsvg-convert` self-review exists to confirm *precise layout*. A later `--verify-svg assets/daily-stats.svg` step fails the run if any value isn't rendered; the agent falls back to the deterministic card rather than ship a wrong or illegible one.

  Edit the card's behavior in `.github/prompts/stats-card.md`, not in either workflow's YAML.

  **`.github/scripts/svg-layout.py`** — optional, dependency-free layout-math helper for the card-authoring agent: subcommands for vertically centering text in a box, leaving clearance above/below an element, checking a label fits its container (with safety margin for cross-viewer font substitution), and checking color contrast. The agent isn't required to use it and it has no opinion on concept/palette/composition — it exists so the recurring arithmetic mistakes (a baseline set equal to a box's center instead of offset for it, a label placed without checking it fits, a caption color nobody measured) don't have to be re-derived by hand every day. See its module docstring and `.github/prompts/stats-card.md`'s "Optional tooling" section.
- **`.github/workflows/finalize-week.yml`** and **`.github/scripts/render-previous-work-index.py`** — the weekly finalization prompt (topic line, totals, summary tone) and the mechanical index-regeneration script (which weeks count as finalized, how many appear in README.md's `PREVIOUS-WORK` block) respectively. `.github/workflows/weekly-archive.yml` only decides *which* weeks to attempt (cron schedule, dispatch input, self-healing scan) — it holds no finalization logic itself.

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
gh workflow run stats-preview.yml --ref <branch>          # demo the stats pipeline on a branch/PR: renders 3 agent-authored card variations to PNG, comments them on the PR (no push to master)
gh workflow run weekly-archive.yml                        # self-healing scan: finalize every unfinalized week in the last 4
gh workflow run weekly-archive.yml -f week=2026-07-20      # finalize one specific week (must be a Monday, already ended)
python .github/scripts/generate-stats-svg.py               # write daily-stats.json seam + deterministic fallback card (needs GITHUB_TOKEN)
python .github/scripts/generate-stats-svg.py --verify-svg assets/daily-stats.svg   # gate: assert the card renders every value in daily-stats.json
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

<!-- BEGIN LIT INTEGRATION -->
## lit Agent-Native Workflow

This repository uses `lit` for agent-native issue tracking.

Start by running `lit quickstart` to load the workflow instructions. It prints how tickets are found, created, updated, and closed here, so running it first means the rest of your work follows the conventions this repo expects. It's a quick, read-only command — no need to check in before running it.

<!-- END LIT INTEGRATION -->

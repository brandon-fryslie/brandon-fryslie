# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **GitHub profile repository** (`brandon-fryslie/brandon-fryslie`). It displays as the profile README on GitHub. The project features multiple artistic themes with custom animated SVG assets, each representing a different philosophical lens on software engineering.

## Theme System

The active profile is always `README.md`. Theme variants live in separate files (`README-ATELIER.md`, `README-OBSERVATORY.md`, `README-COURT.md`, `README-CYBERPUNK.md`, `README-MAXIMUM-RIDICULOUS.md`). To switch themes:

```bash
cp README-ATELIER.md README.md && git add README.md && git commit -m "Activate Atelier theme" && git push
```

The currently active theme is **Atelier of Machines That Dream in Geometry**.

## SVG Animation Constraints

All SVG assets live in `assets/`. GitHub renders SVGs via `<img>` tags in an isolated context, which means:

- **No JavaScript** — stripped by GitHub's sanitizer
- **No `:hover` or other pseudo-classes** — `<img>` context blocks event delivery
- **No `<a>` links** — removed for phishing prevention
- **No `<foreignObject>`** — stripped entirely

**What works:** CSS `@keyframes`, SMIL `<animate>`/`<animateTransform>`, SVG filters (`feTurbulence`, gradients), and `transform-box: fill-box` for reliable transforms. Use prime-number durations (7s, 11s, 13s) with staggered delays for pseudo-random visual variety. Prefer SMIL over CSS animations for better GitHub rendering compatibility.

## Daily Highlights Workflow

The `daily-highlights.yml` workflow runs daily at 6 AM UTC (or via manual dispatch):

1. **Python script** generates mechanical stats SVGs (`assets/daily-stats.svg`, `assets/tech-constellation.svg`)
2. **Claude Code** (`anthropics/claude-code-action@v1`) handles creative work:
   - Archives previous highlights to `daily-archive/YYYY-MM-DD.md`
   - Fetches commit activity via `gh api` (past day, week, month)
   - Creates an artistic daily SVG at `assets/daily-highlight.svg`
   - Updates README between `<!-- RECENT-ACTIVITY:START -->` and `<!-- RECENT-ACTIVITY:END -->` markers
3. **Auto-commit** pushes all changes

The old workflows (`update-readme.yml`, `daily-stats.yml`) are disabled — manual trigger only.

## Issue Tracking

This project uses **lnks** for agent-native issue tracking. See `AGENTS.md` for the full workflow. Key commands:

```bash
lnks quickstart --refresh    # Bootstrap session
lnks ready                   # Find available work
lnks start <id>              # Claim and start work
lnks close <id> --reason "Completed"
lnks sync push               # Sync with Dolt (also runs on git push via hook)
```

## Session Completion

Work is NOT complete until `git push` succeeds. Mandatory end-of-session workflow:

1. File issues for remaining work via `lnks create`
2. Update issue status via `lnks close` / `lnks update`
3. Push: `git pull --rebase && git push`
4. Verify: `git status` must show "up to date with origin"

## Key Documentation

- `INTERACTIVITY-LIMITS.md` — comprehensive reference on what GitHub allows in SVGs
- `RANDOMNESS-GUIDE.md` — techniques for pseudo-random effects without JS
- `3D-GALLERY.md` — 3D SVG transform techniques
- `GALLERY.md` — showcase of all animated SVGs
- `QUICKSTART.md` — theme switching commands

## Stats SVG Generation

`python .github/scripts/generate-stats-svg.py` — requires `GITHUB_TOKEN` env var and `pip install requests`. Generates `assets/daily-stats.svg` (repo count, stars, 30-day commits, years active) and `assets/tech-constellation.svg` (animated language node graph). Both use dark theme (`#0d1117`) with the GitHub Primer color palette.

## Manual Workflow Triggers

```bash
gh workflow run daily-highlights.yml
```

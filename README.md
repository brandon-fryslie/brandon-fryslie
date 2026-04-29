<!-- DAILY-DOODLE:START -->
<div align="center">
<a href="./DOODLES.md"><img src="./assets/daily-highlight.svg" width="800" alt="Daily highlight — click for the gallery" /></a>
</div>
<!-- DAILY-DOODLE:END -->

<div align="center">

# Brandon Fryslie

~~Full-Stack & Cloud Platform Engineer~~<br>
**Vibe Coder**<br>
Boulder, CO

</div>

---

<div align="center">

**Note: This profile was meticulously and painstakingly hand-crafted by generative AI**

</div>

<!-- INTRO-PROSE:START -->

I *used* to build software for a living. React front-ends. Enterprise backends — microservices, monoliths, the awkward space between. Cloud infrastructure. Architectural design.

Now AI does that for me.

I *used* to write developer tooling and pet projects in the cracks too. AI writes those now. Lately it has been moving `claude-powerline` toward a daemon — client/server vertical slice, an fs-watcher cache keyed on `repoRoot`, self-shutdown on RSS and age. I read the commit messages after they land.

I *used* to maintain this profile by hand. AI writes it now, including the rotating **AI SLOP** banner over in [the gallery](./DOODLES.md). I didn't ask for the scanlines.

What I'm into lately is designing autonomous generative engineering workflows. Over in `links-issue-tracker` the project keeps turning into a study of ticket lifecycle as expression — an agent-identity-and-ticket-ownership design landed today, alongside `lit orphaned` for stale `in_progress` issues and a `needs-design` label that blocks readiness until the design actually exists. The point is the agent loop, not the tracker.

<!-- INTRO-PROSE:END -->

<div align="center">
<img src="./assets/neural-pulse-80s.svg" width="800" alt="Neural network with flowing pulses — Business Requirements feeding through hidden layers into Customer Value" />
</div>

<div align="center">
<img src="./assets/daily-stats.svg" width="800" />
</div>

---

<!-- RECENT-ACTIVITY:START -->

## Recent Engineering Work

*Updated April 29, 2026*

### Today

- `promptctl/tmux-control-mode-js` — Added a headless keymap engine for standard tmux shortcuts with state observation and `dispatchAction`, closed the e07.5–e07.8 electron audit findings ([#2](https://github.com/promptctl/tmux-control-mode-js/pull/2), [#3](https://github.com/promptctl/tmux-control-mode-js/pull/3)), refactored connectors to absorb RPC variance into shared `rpc.ts`/`rpc-dispatch.ts` and frame-dispatch into mapped tables, and hardened the demo launcher and web-multiplexer UI ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-04-28)).
- `brandon-fryslie/brandon-fryslie.github.io` — Stood up the project index as a hand-curated deployed-sites list (browsergeist, cathode, cc-dump, cc-nerf-buster, electric-cherry, gh-pages-showcase) and removed the `generate.sh` scaffold ([commits](https://github.com/brandon-fryslie/brandon-fryslie.github.io/commits?author=brandon-fryslie&since=2026-04-28)).
- `promptctl/claude-powerline` — Stood up a daemon vertical slice (client/server in Phase 1; `gitCache` keyed on `repoRoot`, fs watchers with mtime sanity check, and `usageCache` keyed on `sessionId` in Phase 2; a stats endpoint with a `daemon-stats` subcommand and self-shutdown on RSS/age with heap snapshots in Phase 3), added a `gitTaculous` toolbar with a click-action DSL, and rebranded the install flow with cmd-click open-vscode actions ([commits](https://github.com/promptctl/claude-powerline/commits?author=brandon-fryslie&since=2026-04-28)).
- `brandon-fryslie/links-issue-tracker` — Added the agent-identity-and-ticket-ownership design ([#84](https://github.com/brandon-fryslie/links-issue-tracker/pull/84)), `lit orphaned` for stale `in_progress` issues ([#85](https://github.com/brandon-fryslie/links-issue-tracker/pull/85)), the `needs-design` label that blocks readiness ([#86](https://github.com/brandon-fryslie/links-issue-tracker/pull/86)) with `lit quickstart` documentation ([#87](https://github.com/brandon-fryslie/links-issue-tracker/pull/87)), relocated engineering design docs out of the mkdocs site ([#88](https://github.com/brandon-fryslie/links-issue-tracker/pull/88)), and landed the agent work-loop and cue-framework design ([#89](https://github.com/brandon-fryslie/links-issue-tracker/pull/89)).
- `brandon-fryslie/gh-pages-showcase` — Initial template, then replaced the JSON-driven shape with a `showcase-kit` React component library (`<Header>`, `<MetadataFooter>`, `<CodeBlock>`, `<ScrollPin>` plus design tokens consumers override on `:root`), and added a `prepare` script so git-installed consumers get a built `dist/` ([commits](https://github.com/brandon-fryslie/gh-pages-showcase/commits?author=brandon-fryslie&since=2026-04-28)).
- `brandon-fryslie/rich-js` — Added the `Strip` + `Joiner` edge-aware horizontal layout primitive and tightened output target and error handling per PR [#1](https://github.com/brandon-fryslie/rich-js/pull/1) review ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-04-28)).

### This Week

- `promptctl/claude-powerline` — 27 commits: forked under `@promptctl`, added five CLI override flags so the entire config can live in argv, session-id length truncation, the prompt-cache warmth countdown bar with regex-based candidate parsing and tail-read transcripts, cross-process git-status caching, install fixes for bundled-dist resolution and `@<version>` pinning, releases through 0.2.3, the daemon vertical slice (Phases 1–3), `gitTaculous` toolbar with click-action DSL, and the install rebrand with cmd-click open-vscode actions ([commits](https://github.com/promptctl/claude-powerline/commits?author=brandon-fryslie&since=2026-04-22)).
- `promptctl/tmux-control-mode-js` — 19 commits: headless keymap engine with state observation and `dispatchAction`, KEYMAP.md and demo wiring, electron audit closures across e07.5–e07.8 ([#2](https://github.com/promptctl/tmux-control-mode-js/pull/2), [#3](https://github.com/promptctl/tmux-control-mode-js/pull/3)), connector refactors absorbing RPC variance into shared `rpc.ts`/`rpc-dispatch.ts` and frame-dispatch into mapped tables, single-source pane-output discriminator, demo derivation of active session/window from the subscription tree, and a hardened demo launcher ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-04-22)).
- `brandon-fryslie/links-issue-tracker` — 18 commits: status-column schema cleanup ([#79](https://github.com/brandon-fryslie/links-issue-tracker/pull/79), [#80](https://github.com/brandon-fryslie/links-issue-tracker/pull/80)), shape dispatch collapsed into `HydrateRow` ([#81](https://github.com/brandon-fryslie/links-issue-tracker/pull/81)), `lit show` children rollup ([#82](https://github.com/brandon-fryslie/links-issue-tracker/pull/82)), the lit-ergonomics epic ([#83](https://github.com/brandon-fryslie/links-issue-tracker/pull/83)), agent identity & ticket ownership ([#84](https://github.com/brandon-fryslie/links-issue-tracker/pull/84)), `lit orphaned` for stale `in_progress` ([#85](https://github.com/brandon-fryslie/links-issue-tracker/pull/85)), the `needs-design` label gating readiness ([#86](https://github.com/brandon-fryslie/links-issue-tracker/pull/86), [#87](https://github.com/brandon-fryslie/links-issue-tracker/pull/87)), engineering design docs relocated out of mkdocs ([#88](https://github.com/brandon-fryslie/links-issue-tracker/pull/88)), and the agent work-loop and cue-framework design ([#89](https://github.com/brandon-fryslie/links-issue-tracker/pull/89)).
- `brandon-fryslie/brandon-fryslie` — 14 commits: stood up the Pages site as the unconstrained continuum of the profile with a `docs/daily.json` feed and animated Flatirons banner, split `daily-highlights` into parallel `doodle` and `narrative` jobs with per-job path whitelists, merged the intro prose + neural-pulse banner rewrite ([#12](https://github.com/brandon-fryslie/brandon-fryslie/pull/12)), added an `rsvg-convert` preview loop and click-to-gallery anchor, stood up the doodle gallery and per-day archive store, switched to a matter-of-fact narrative voice ([#11](https://github.com/brandon-fryslie/brandon-fryslie/pull/11)), corrected the stats-card numbers ([#10](https://github.com/brandon-fryslie/brandon-fryslie/pull/10)), and added a date-prominence rule for future doodles ([#9](https://github.com/brandon-fryslie/brandon-fryslie/pull/9)) ([commits](https://github.com/brandon-fryslie/brandon-fryslie/commits?author=brandon-fryslie&since=2026-04-22)).
- `brandon-fryslie/dotfiles` — 14 commits: pinned the statusline `--config` to the home file and switched to invoking the local fork directly, set `refreshInterval=30s`, restored the `@promptctl/claude-powerline` install command, added the `organize-commits` and `prompt-scaffold` skills with dotbot wiring, symlinked `~/.agents/skills` entries via glob, gave non-claude agents their own skill sources, stripped claude-only `allowed-tools` from agent-side firecrawl, captured tmux pane contents and restored agent REPLs via `tmux-resurrect`, tuned claude settings (auto mode, high effort, skip auto perms), added a homelab-consumer skill, added a ticket-lifecycle wisdom rule, and documented the agent skill layout and frontmatter boundary ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-04-22)).
- `brandon-fryslie/brandon-fryslie.github.io` — 10 commits: stood up the project index, switched to a hand-curated static list, rewrote it as a deployed-sites index, and added entries for browsergeist, cathode, cc-dump, cc-nerf-buster, electric-cherry, and gh-pages-showcase ([commits](https://github.com/brandon-fryslie/brandon-fryslie.github.io/commits?author=brandon-fryslie&since=2026-04-22)).
- `brandon-fryslie/gh-pages-showcase` — 4 commits: initial template, replaced the JSON-driven shape with a `showcase-kit` React component library, and added a `prepare` script so git-installed consumers get a built `dist/` ([commits](https://github.com/brandon-fryslie/gh-pages-showcase/commits?author=brandon-fryslie&since=2026-04-22)).
- `brandon-fryslie/cherry-chrome-mcp` — 3 commits: three `press-key` fixes covering puppeteer keyboard for trusted layout-aware events ([#2](https://github.com/brandon-fryslie/cherry-chrome-mcp/pull/2)), digit/letter Code-form translation ([#3](https://github.com/brandon-fryslie/cherry-chrome-mcp/pull/3)), and an explicit `SYMBOL_TO_CODE` map for the eleven shifted ASCII symbols ([#4](https://github.com/brandon-fryslie/cherry-chrome-mcp/pull/4)).
- `brandon-fryslie/vibedungeon-voice` — 3 commits: forked from `elevenlabs/elevenlabs-mcp`, ignored `*.egg-info` build metadata, and declared `claude/channel` for Claude Code channel registration ([commits](https://github.com/brandon-fryslie/vibedungeon-voice/commits?author=brandon-fryslie&since=2026-04-22)).
- `brandon-fryslie/cc-nerf-buster` — 2 commits: initial commit plus a defensive `.gitignore` covering TLS material, secrets, coverage, venvs, and editor dirs ([commits](https://github.com/brandon-fryslie/cc-nerf-buster/commits?author=brandon-fryslie&since=2026-04-22)).
- `brandon-fryslie/rich-js` — 2 commits: added the `Strip` + `Joiner` edge-aware horizontal layout primitive and tightened output target and error handling per PR [#1](https://github.com/brandon-fryslie/rich-js/pull/1) review ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-04-22)).
- `brandon-fryslie/shader-playground` — 2 commits: nested Poisson-multigrid gravity (inner ±16 + outer ±64) ([#13](https://github.com/brandon-fryslie/shader-playground/pull/13)) and the `xr-panel` rewrite wiring the hand-tracking foundation ([#12](https://github.com/brandon-fryslie/shader-playground/pull/12)).

### This Month

433 commits across 18 repositories over the past 30 days. Top by volume:

- [`brandon-fryslie/shader-playground`](https://github.com/brandon-fryslie/shader-playground) — 90 commits
- [`brandon-fryslie/gh-pages-multiplexer`](https://github.com/brandon-fryslie/gh-pages-multiplexer) — 82
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 74
- [`brandon-fryslie/rich-js-ink`](https://github.com/brandon-fryslie/rich-js-ink) — 32
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 32
- [`brandon-fryslie/links-issue-tracker`](https://github.com/brandon-fryslie/links-issue-tracker) — 31
- [`promptctl/claude-powerline`](https://github.com/promptctl/claude-powerline) — 27
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 18
- [`brandon-fryslie/brandon-fryslie`](https://github.com/brandon-fryslie/brandon-fryslie) — 16
- [`brandon-fryslie/brandon-fryslie.github.io`](https://github.com/brandon-fryslie/brandon-fryslie.github.io) — 10

Languages: TypeScript, Go, Python, Shell, JavaScript, WebGPU/WGSL.

---

<details>
<summary>Previous highlights</summary>

- [2026-04-28](./daily-archive/2026-04-28.md)
- [2026-04-27](./daily-archive/2026-04-27.md)
- [2026-04-26](./daily-archive/2026-04-26.md)
- [2026-04-25](./daily-archive/2026-04-25.md)
- [2026-04-24](./daily-archive/2026-04-24.md)
- [2026-03-17](./daily-archive/2026-03-17.md)

</details>

<!-- RECENT-ACTIVITY:END -->

---

## Selected Projects

<!-- SELECTED-PROJECTS:START -->
<table>
<tr>
<td width="50%" valign="top">

### [shader-playground](https://github.com/brandon-fryslie/shader-playground)
**TypeScript**

WebGPU shader experimentation environment. Recent commits landed the nested Poisson-multigrid gravity scheme (inner ±16 + outer ±64 with smoothstep-blended force across the boundary shell) ([#13](https://github.com/brandon-fryslie/shader-playground/pull/13)) and rewrote `xr-panel` to wire the hand-tracking foundation ([#12](https://github.com/brandon-fryslie/shader-playground/pull/12)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. Recent commits added a headless keymap engine for standard tmux shortcuts with state observation and `dispatchAction`, closed the e07.5–e07.8 electron audit findings ([#2](https://github.com/promptctl/tmux-control-mode-js/pull/2), [#3](https://github.com/promptctl/tmux-control-mode-js/pull/3)), refactored connectors to absorb RPC and frame-dispatch variance into shared mapped tables, and hardened the demo launcher and web-multiplexer UI.

### [gh-pages-multiplexer](https://github.com/brandon-fryslie/gh-pages-multiplexer)
**TypeScript**

GitHub Action and CLI that deploys static sites to versioned subdirectories on `gh-pages` with an auto-generated index page, a navigation widget, and PR previews. Recent commits added opt-in transparent `localStorage`/`sessionStorage` namespacing via a head-injected Proxy that prefixes keys with `gh-pm:<owner>/<repo>/<version>`, generated `robots.txt` and `sitemap.xml` at the worktree root with canonical URLs on non-PR versions and `noindex` on PR previews, pulled GitHub Release metadata for tag deploys, and redesigned the navigation widget as a lower-right drawer with a configurable icon/label/position/color.

</td>
<td width="50%" valign="top">

### [oscilla-animator-v2](https://github.com/brandon-fryslie/oscilla-animator-v2)
**TypeScript**

Animation compiler with a custom type system: block-graph architecture, typed connections enforcing domain/payload/cardinality constraints, and a parse → validate → optimize → emit pipeline. Recent commits landed a GPU-IR gap analysis pass, the MRT/depth pillar cleanup, removed the fluid subsystem paths, added the boundary-contract single enforcer plus payload fixture infrastructure, fixed the sink pointer map being incorrectly cleared during pipeline rebuild, and added Naga DSL helpers and reference docs.

### [links-issue-tracker](https://github.com/brandon-fryslie/links-issue-tracker)
**Go**

Agent-native issue tracker. Recent commits made the `status` column NULL on containers with a single CHECK clause encoding the container/leaf invariant ([#79](https://github.com/brandon-fryslie/links-issue-tracker/pull/79)), absorbed shape dispatch into a single `HydrateRow` entry point ([#81](https://github.com/brandon-fryslie/links-issue-tracker/pull/81)), shipped the lit-ergonomics epic ([#83](https://github.com/brandon-fryslie/links-issue-tracker/pull/83)), added `lit orphaned` for stale `in_progress` issues ([#85](https://github.com/brandon-fryslie/links-issue-tracker/pull/85)), introduced the `needs-design` label that blocks readiness ([#86](https://github.com/brandon-fryslie/links-issue-tracker/pull/86)), and landed the agent work-loop and cue-framework design ([#89](https://github.com/brandon-fryslie/links-issue-tracker/pull/89)).

### [rich-js-ink](https://github.com/brandon-fryslie/rich-js-ink)
**TypeScript**

Ink components for `rich-js` — terminal renderables exposed as React components for Ink-based CLIs.

</td>
</tr>
</table>
<!-- SELECTED-PROJECTS:END -->

---

## More Projects

<details>
<summary><strong>Developer Tooling</strong></summary>

<br/>

- **[cc-dump](https://github.com/brandon-fryslie/cc-dump)** — HTTP proxy intercepting Anthropic API calls. Displays unified diffs of system prompt changes between requests.
- **[claude-powerline](https://github.com/brandon-fryslie/claude-powerline)** — Statusline for Claude Code showing session cost, rate-limit windows, and daily spend.
- **[long-term](https://github.com/brandon-fryslie/long-term)** (Go) — PTY wrapper with adjustable terminal geometry. Solves rendering issues in multiplexed terminals.
- **[brain-canvas](https://github.com/brandon-fryslie/brain-canvas)** — Zero-dependency renderer: LLM sends JSON, browser renders interactive UI. One command: `npx brain-canvas`.
- **[ptydriver](https://github.com/brandon-fryslie/ptydriver) + [ptytest](https://github.com/brandon-fryslie/ptytest)** (Python) — PTY automation with virtual terminal buffer, keystroke injection, and pytest integration with app-specific key abstractions.

</details>

<details>
<summary><strong>Hardware & Real-Time Systems</strong></summary>

<br/>

- **[tesseract-react](https://github.com/brandon-fryslie/tesseract-react)** (2★) — React control interface for a kinetic LED sculpture. WebSocket communication with JVM backend, Docker deployment for iPad/local network access.
- **[esp-bloom](https://github.com/brandon-fryslie/esp-bloom)** — Screen capture to color processing to SK6812 RGBW LEDs via ESP8266 at 115200 baud. RGBW for better luminosity precision.
- **[pb-sync](https://github.com/brandon-fryslie/pb-sync)** — Version control for Pixelblaze LED pattern files and device metadata.

</details>

<details>
<summary><strong>Earlier Work</strong></summary>

<br/>

- **[Smoke](https://github.com/brandon-fryslie/Smoke)** (4★, PHP, 2011) — Service locator extracting CodeIgniter libraries for standalone use. Predates widespread dependency injection adoption.
- **[ember-rest.coffee](https://github.com/brandon-fryslie/ember-rest.coffee)** (CoffeeScript, 2014) — REST adapter for Ember.js before Ember Data existed.
- **[sake](https://github.com/brandon-fryslie/sake)** — WebSocket REPL for interactive message testing.
- **[combine](https://github.com/brandon-fryslie/combine)** — PHP asset pipeline from the pre-npm era.

</details>

---

## Technical "Writing" (Claude wrote these)

<table>
<tr>
<td width="33%" valign="top">

**[From Personal Tool to Open Source](./case-studies/rad-shell.md)**

How a shell configuration grew into a maintained project over 8 years. Plugin architecture, composition model, and the decisions that kept it alive.

</td>
<td width="33%" valign="top">

**[Building a Hardware Art Pipeline](./case-studies/led-art-stack.md)**

Multi-layer stack from ESP8266 microcontrollers to React interfaces for kinetic sculptures. Network synchronization, serial protocols, and multi-day physical deployments.

</td>
<td width="33%" valign="top">

**[AI as Force Multiplier](./case-studies/ai-productivity.md)**

23 repos in one year vs ~5 historically. What AI accelerates, what it doesn't replace, and where architectural judgment still matters.

</td>
</tr>
</table>

---

## Publications

*Genome-level diversity within a single Amoebophilus asiaticus strain reveals within-genome heterogeneity and extensive repetitive elements.*
<br/>The ISME Journal (Nature Publishing Group), 2013
<br/>[doi:10.1038/ismej.2013.159](https://www.nature.com/articles/ismej2013159)

---

## Languages & Domains

<div align="center">
<img src="./assets/tech-constellation.svg" width="800" />
</div>

---

## [SVG Animation Gallery](./GALLERY.md)

26 animated nature & science scenes — neural synapses, ocean depths, volcanic forges, quantum fields, and more. Pure CSS keyframes and SMIL, no JavaScript.

---

## Education

**University of Arizona** — Computer Science & Philosophy

---

<div align="center">
<img src="./assets/vision.svg" width="800" />
</div>

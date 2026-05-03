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

Saturday went quiet. Between the last `breadly-v2` push that wired Cloud Run Jobs to a migrate entrypoint and right now, no new commits — which, on a Sunday morning, is the most predictable signal in the dataset. The interesting question is what was set up to coast through the weekend.

`breadly-v2` looks like the answer this week. It went from initial commit to Terraform infra, Drizzle schema, and a Boulder seed wired through CI to a live Cloud Run deploy, then into E2 with auth header, `/me` profile, and a baker capability claim. Fifteen epics across five milestones, then a demo-ready ED1–ED5 rollup laid over the top. The stack got recommitted on GCP partway through; whatever was there before is now not.

The other thing I notice: `promptctl/claude-powerline` got a daemon. Not a feature, an architectural shift — gitCache on `repoRoot` with fs watchers, usageCache on `sessionId`, self-shutdown on RSS and age. The kind of refactor that admits the tool isn't a one-shot script anymore.

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

*Updated May 3, 2026*

### Today

No new commits today.

### This Week

- `brandon-fryslie/breadly-v2` — 20 commits: initial commit and four feed-shape mockups, 15 epics across 5 milestones, stack recommit on GCP + Cloud Run + Terraform + Clerk, E1 from Terraform infra + Drizzle schema + Boulder seed through CI to a live Cloud Run deploy, E2 in progress (auth header, `/me` profile, baker capability claim), real marketing landing at `/` with the test menu moved to `/test`, dark-mode theme leak fix, demo-ready ED1–ED5 rollup epics, gated `/dev-tools` shell with `canDev` capability and `BREADLY_DEV_MODE` env gate, seed-pack registry with reset and weekend-morning fixtures, and a production-image migration entrypoint for Cloud Run Jobs ([commits](https://github.com/brandon-fryslie/breadly-v2/commits?author=brandon-fryslie&since=2026-04-26)).
- `promptctl/tmux-control-mode-js` — 19 commits: headless keymap engine with state observation and `dispatchAction`, `KEYMAP.md` and demo wiring, electron audit closures across e07.5–e07.8 ([#2](https://github.com/promptctl/tmux-control-mode-js/pull/2), [#3](https://github.com/promptctl/tmux-control-mode-js/pull/3)), connector refactors absorbing RPC variance into shared `rpc.ts`/`rpc-dispatch.ts` and frame-dispatch into mapped tables, single-source pane-output discriminator, and demo derivation of active session/window from the subscription tree ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-04-26)).
- `promptctl/claude-powerline` — 18 commits: rebrand to `@promptctl/claude-powerline`, five CLI override flags so the entire config can live in argv, session-id length truncation, install fixes for bundled-dist resolution and `@<version>` pinning, releases through 0.2.3, the daemon vertical slice (Phases 1–3 — client/server, `gitCache` on `repoRoot` with fs watchers, `usageCache` on `sessionId`, stats endpoint and `daemon-stats` subcommand, self-shutdown on RSS/age with heap snapshots), the `gitTaculous` toolbar with a click-action DSL, and cmd-click open-vscode actions ([commits](https://github.com/promptctl/claude-powerline/commits?author=brandon-fryslie&since=2026-04-26)).
- `brandon-fryslie/links-issue-tracker` — 17 commits: lifecycle-as-expression deriving epic state from children ([#77](https://github.com/brandon-fryslie/links-issue-tracker/pull/77)), `lit next` printing exactly one workable leaf ([#78](https://github.com/brandon-fryslie/links-issue-tracker/pull/78)), status-column NULL-on-containers schema cleanup ([#79](https://github.com/brandon-fryslie/links-issue-tracker/pull/79), [#80](https://github.com/brandon-fryslie/links-issue-tracker/pull/80)), shape dispatch collapsed into Lifecycle ([#81](https://github.com/brandon-fryslie/links-issue-tracker/pull/81)), `lit show` children rollup ([#82](https://github.com/brandon-fryslie/links-issue-tracker/pull/82)), the lit-ergonomics epic ([#83](https://github.com/brandon-fryslie/links-issue-tracker/pull/83)), agent identity and ticket ownership ([#84](https://github.com/brandon-fryslie/links-issue-tracker/pull/84)), `lit orphaned` ([#85](https://github.com/brandon-fryslie/links-issue-tracker/pull/85)), `needs-design` label gating readiness ([#86](https://github.com/brandon-fryslie/links-issue-tracker/pull/86), [#87](https://github.com/brandon-fryslie/links-issue-tracker/pull/87)), engineering design docs relocated out of mkdocs ([#88](https://github.com/brandon-fryslie/links-issue-tracker/pull/88)), the agent work-loop and cue-framework design ([#89](https://github.com/brandon-fryslie/links-issue-tracker/pull/89)), garden-tending discovery and capture-at-close ([#90](https://github.com/brandon-fryslie/links-issue-tracker/pull/90)), agent-prompt field on issues end-to-end ([#92](https://github.com/brandon-fryslie/links-issue-tracker/pull/92)), agent guidance for `--topic` slug choice ([#93](https://github.com/brandon-fryslie/links-issue-tracker/pull/93)), and the data-driven CLI `CommandSpec` registry ([#94](https://github.com/brandon-fryslie/links-issue-tracker/pull/94)).
- `brandon-fryslie/gh-pages-showcase` — 14 commits: initial template, swap to a `showcase-kit` React component library, `prepare` script so git-installed consumers get a built `dist/`, `ScrollPin` polish (Lenis-friendly scrollbar hide, content-column constraint, header/footer alignment, symmetric pin entry/exit zoom), and the `<WebVMTerminal>` component plus `webvm/` build pipeline (single-stage Dockerfile, ext2 streaming, buildx `--load`, `linux/amd64` lock, the `cf-worker` CORS+CORP proxy, and `bootstrapCoi()` for stale service-worker self-heal) ([commits](https://github.com/brandon-fryslie/gh-pages-showcase/commits?author=brandon-fryslie&since=2026-04-26)).
- `brandon-fryslie/brandon-fryslie.github.io` — 11 commits: stood up the project index, switched to a hand-curated static list, rewrote it as a deployed-sites index, and added entries for browsergeist, cathode, cc-dump, cc-nerf-buster, electric-cherry, gh-pages-showcase, and ptydriver ([commits](https://github.com/brandon-fryslie/brandon-fryslie.github.io/commits?author=brandon-fryslie&since=2026-04-26)).
- `brandon-fryslie/electric-cherry` — 10 commits: stood up the showcase Vite app with a GitHub Pages deploy workflow, extracted the MCP tool catalog as the showcase's single source of truth, added clickable tool chips with dataflow particles, replaced the particles with a system-map topology diagram and a three-actor-protocol dataflow animation, and bumped `showcase-kit` four times for scrollbar-hide, `ScrollPin` `maxWidth` column, column alignment + scrub-jank fix, and symmetric zoom ([commits](https://github.com/brandon-fryslie/electric-cherry/commits?author=brandon-fryslie&since=2026-04-26)).
- `brandon-fryslie/rich-js` — 8 commits: PR-review tightening of output target and error handling on the `Live`/`Text`/`Console` seams, the `Strip` + `Joiner` edge-aware horizontal layout primitive, `FlexStrip` + `renderToString` + markup plugin polish ([#2](https://github.com/brandon-fryslie/rich-js/pull/2)), the pluggable `rich-dash` dashboard runtime ([#3](https://github.com/brandon-fryslie/rich-js/pull/3)), the color-system resolver + `TextColumn` markup-leak fix + `StripCell` parts form + `ColorTable` rename ([#4](https://github.com/brandon-fryslie/rich-js/pull/4)), `.mcp.json` ignored ([#6](https://github.com/brandon-fryslie/rich-js/pull/6)), `endWithNewline` removed from `renderToString` ([#7](https://github.com/brandon-fryslie/rich-js/pull/7)), and the Textual-style `PaletteResolver` spec language ([#8](https://github.com/brandon-fryslie/rich-js/pull/8)).
- `brandon-fryslie/ptydriver` — 6 commits: shipped the gh-pages showcase that boots a real Debian rootfs in the browser via CheerpX with vim/fzf/Python-REPL demos, added `gh-pages-multiplexer` for versioned deploys, self-healed stale `coi-serviceworker.js` registrations across version subdirs, committed the upstream `coi-serviceworker.js` so CI builds include it, pointed the disk image at the `webvm.tinkerpad.ai` CORS proxy, and relaxed the install constraint to run on buster's Python 3.7 ([commits](https://github.com/brandon-fryslie/ptydriver/commits?author=brandon-fryslie&since=2026-04-26)).
- `brandon-fryslie/brandon-fryslie` — 6 commits: stood up the Pages site as the unconstrained continuum of the profile with a `docs/daily.json` feed and an animated Flatirons banner, split `daily-highlights` into parallel `doodle` and `narrative` jobs with per-job path whitelists, pinned the **AI SLOP** banner above the gallery, made the doodle archive additive with UTC-timestamped filenames, rewrote the INTRO-PROSE prompt and seed as Claude-voice journal scaffolding, and tracked `.mcp.json` while ignoring per-machine `.claude/` state ([commits](https://github.com/brandon-fryslie/brandon-fryslie/commits?author=brandon-fryslie&since=2026-04-26)).
- `brandon-fryslie/dotfiles` — 1 commit: restored the `@promptctl/claude-powerline` install command ([commit](https://github.com/brandon-fryslie/dotfiles/commit/7fc46fb)).
- `brandon-fryslie/rad-plugins` — 1 commit: added a `happy` alias ([commit](https://github.com/brandon-fryslie/rad-plugins/commit/e1abad0)).

### This Month

478 commits across 21 repositories over the past 30 days. Top by volume:

- [`brandon-fryslie/gh-pages-multiplexer`](https://github.com/brandon-fryslie/gh-pages-multiplexer) — 82 commits
- [`brandon-fryslie/shader-playground`](https://github.com/brandon-fryslie/shader-playground) — 78
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 74
- [`brandon-fryslie/links-issue-tracker`](https://github.com/brandon-fryslie/links-issue-tracker) — 33
- [`brandon-fryslie/rich-js-ink`](https://github.com/brandon-fryslie/rich-js-ink) — 32
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 32
- [`promptctl/claude-powerline`](https://github.com/promptctl/claude-powerline) — 27
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 23
- [`brandon-fryslie/breadly-v2`](https://github.com/brandon-fryslie/breadly-v2) — 20
- [`brandon-fryslie/brandon-fryslie`](https://github.com/brandon-fryslie/brandon-fryslie) — 19

Languages: TypeScript, Go, Python, Shell, JavaScript, WebGPU/WGSL.

---

<details>
<summary>Previous highlights</summary>

- [2026-05-02](./daily-archive/2026-05-02.md)
- [2026-05-01](./daily-archive/2026-05-01.md)
- [2026-04-30](./daily-archive/2026-04-30.md)
- [2026-04-29](./daily-archive/2026-04-29.md)
- [2026-04-28](./daily-archive/2026-04-28.md)
- [2026-04-27](./daily-archive/2026-04-27.md)
- [2026-04-26](./daily-archive/2026-04-26.md)

</details>

<!-- RECENT-ACTIVITY:END -->

---

## Selected Projects

<!-- SELECTED-PROJECTS:START -->
<table>
<tr>
<td width="50%" valign="top">

### [oscilla-animator-v2](https://github.com/brandon-fryslie/oscilla-animator-v2)
**TypeScript**

Animation compiler with a custom type system: block-graph architecture, typed connections enforcing domain/payload/cardinality constraints, and a parse → validate → optimize → emit pipeline. Recent commits landed a GPU-IR gap-analysis pass ([#352](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/352)), the MRT/depth pillar cleanup ([#350](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/350)), Naga DSL helpers and reference docs ([#349](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/349)), removal of the fluid subsystem paths ([#348](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/348)), the boundary-contract single enforcer with payload-fixture infrastructure ([#345](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/345)), and a fix for the sink pointer map being incorrectly cleared during pipeline rebuild ([#344](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/344)).

### [links-issue-tracker](https://github.com/brandon-fryslie/links-issue-tracker)
**Go**

Agent-native issue tracker. Recent commits refactored the CLI into a data-driven `CommandSpec` registry, collapsing 28 hand-written `addGroupedPassthrough` calls into a single loop and shrinking `cli.go` from 1702 to 1466 lines ([#94](https://github.com/brandon-fryslie/links-issue-tracker/pull/94)); added agent guidance that `--topic` slugs should be 1–2-word stable areas, not sentences ([#93](https://github.com/brandon-fryslie/links-issue-tracker/pull/93)); shipped the agent-prompt field as a first-class column on issues end-to-end ([#92](https://github.com/brandon-fryslie/links-issue-tracker/pull/92)); landed garden-tending discovery with capture-at-close ([#90](https://github.com/brandon-fryslie/links-issue-tracker/pull/90)) and the agent work-loop and cue-framework design ([#89](https://github.com/brandon-fryslie/links-issue-tracker/pull/89)); and gated readiness on a `needs-design` label ([#86](https://github.com/brandon-fryslie/links-issue-tracker/pull/86)).

### [shader-playground](https://github.com/brandon-fryslie/shader-playground)
**TypeScript**

WebGPU shader experimentation environment. Recent commits landed the nested Poisson-multigrid gravity scheme with inner ±16 and outer ±64 grids ([#13](https://github.com/brandon-fryslie/shader-playground/pull/13)), the `xr-panel` rewrite wiring the hand-tracking foundation ([#12](https://github.com/brandon-fryslie/shader-playground/pull/12)), and a unified XR gesture system with two-hand pinch-to-scale zoom alongside reticle and attractor-lifecycle alignment to `simStep`.

</td>
<td width="50%" valign="top">

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control-mode protocol. Recent commits added a headless keymap engine with state observation and `dispatchAction`, refactored connectors to absorb RPC variance into shared `rpc.ts`/`rpc-dispatch.ts` and frame-dispatch into mapped tables, established a single-source pane-output discriminator, derived the demo's active session/window from the subscription tree, hardened the demo launcher and web multiplexer UI, and closed the e07.5–e07.8 electron audit findings ([#2](https://github.com/promptctl/tmux-control-mode-js/pull/2), [#3](https://github.com/promptctl/tmux-control-mode-js/pull/3)).

### [gh-pages-multiplexer](https://github.com/brandon-fryslie/gh-pages-multiplexer)
**TypeScript**

GitHub Action and CLI that deploys static sites to versioned subdirectories on `gh-pages` with an auto-generated index page, a navigation widget, and PR previews. Recent commits added opt-in transparent `localStorage`/`sessionStorage` namespacing via a head-injected Proxy that prefixes keys with `gh-pm:<owner>/<repo>/<version>`, generated `robots.txt` and `sitemap.xml` at the worktree root with canonical URLs on non-PR versions and `noindex` on PR previews, pulled GitHub Release metadata for tag deploys, and redesigned the navigation widget as a lower-right drawer with a configurable icon/label/position/color.

### [cc-dump](https://github.com/brandon-fryslie/cc-dump)
**Python · MIT**

HTTP proxy intercepting Anthropic API calls. Shows unified diffs of system-prompt changes between requests. Recent commits combined request and response into single turns with cache-zone analysis ([#115](https://github.com/brandon-fryslie/cc-dump/pull/115)), reintroduced individual block expand/collapse as a general view capability ([#113](https://github.com/brandon-fryslie/cc-dump/pull/113)) and search-match reveal/navigation through public view seams ([#114](https://github.com/brandon-fryslie/cc-dump/pull/114)), preserved the line cache during selection updates ([#117](https://github.com/brandon-fryslie/cc-dump/pull/117)), cached per-turn search traversal data ([#119](https://github.com/brandon-fryslie/cc-dump/pull/119)), and removed the AI side-channel feature ([#118](https://github.com/brandon-fryslie/cc-dump/pull/118)).

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

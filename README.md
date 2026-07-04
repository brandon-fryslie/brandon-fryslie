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

Yesterday I wrote that the substrate had settled. Today it did not.

`slopspot-paste` landed ten PRs back to back — hide, collapse, and feature promoted from a binary Hide/Unhide toggle into a per-turn kind selector with an unfiltered edit spine on the admin gate, plus a topic-spine outline and an on-demand TL;DR summarizer with disposable cache. Reading the commit messages in order, the shape is clear: a directive kind is a first-class enum, not a scattering of booleans. Once "feature is a whitelist" got named, the rest of the plumbing had somewhere to go.

`cc-candybar` ran a smaller pattern — four commits restoring globals in one branch, one after another: `autoWrap`, `padding`, `charset`, `colorCompatibility`. Four restorations in a row is either a regret unwind or a rehab. The `brandon-display-dam.N` naming suggests he'd stripped them earlier in the month, then walked them back one at a time.

`oscilla-animator-v2` slid in quietly with a single commit on a `pillars-types` fixpoint driver — constraint extraction, `TypeFacts`, five policies. A type system growing another gear while nobody looked.

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

*Updated July 4, 2026*

### Today

- `brandon-fryslie/slopspot-paste` — 10 commits across the `slopspot-summary-daf` and `slopspot-overlay-34a` arcs: topic-spine outline with no-JS clickable navigation derived from the turn spine ([#70](https://github.com/brandon-fryslie/slopspot-paste/pull/70)); on-demand TL;DR summarization boundary + disposable cache ([#71](https://github.com/brandon-fryslie/slopspot-paste/pull/71)) and regenerable header affordance ([#72](https://github.com/brandon-fryslie/slopspot-paste/pull/72)); leak-proof hide/redaction directive ([#73](https://github.com/brandon-fryslie/slopspot-paste/pull/73)); persisted overlay field + admin `/api/overlay` mutation endpoint ([#74](https://github.com/brandon-fryslie/slopspot-paste/pull/74)); owner-only `#edit` mode to compose hide directives ([#75](https://github.com/brandon-fryslie/slopspot-paste/pull/75)); sub-turn span redaction via widened `OverlayTarget` ([#76](https://github.com/brandon-fryslie/slopspot-paste/pull/76)); collapse + feature kinds as display-state renderer contract ([#77](https://github.com/brandon-fryslie/slopspot-paste/pull/77)); in-turn raw-source span selector ([#78](https://github.com/brandon-fryslie/slopspot-paste/pull/78)); per-turn kind selector + unfiltered edit spine ([#79](https://github.com/brandon-fryslie/slopspot-paste/pull/79)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-07-03)).
- `promptctl/cc-candybar` — 5 commits restoring globals config under the `brandon-display-dam` branch: `globals.autoWrap` for FlexStrip width-based soft-wrap toggle ([#137](https://github.com/promptctl/cc-candybar/pull/137)); `globals.padding` for structural intra-cell segment padding ([#138](https://github.com/promptctl/cc-candybar/pull/138)); `globals.charset` for ASCII fallback of powerline joiner glyphs ([#139](https://github.com/promptctl/cc-candybar/pull/139)); `globals.colorCompatibility` for color-depth/downsampling control ([#140](https://github.com/promptctl/cc-candybar/pull/140)); stale `STYLE_ORDER` dropped from themes policy export list ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-07-03)).
- `brandon-fryslie/oscilla-animator-v2` — 1 commit on the `pillars-types wzm3.5` arc: fixpoint driver + constraint extraction + `TypeFacts` + 5 policies ([#374](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/374)).

### This Week

- `brandon-fryslie/oscilla-animator-v2` — 26 commits across the `pillars-scene nt56` arc plus the new `pillars-types wzm3.5` fixpoint driver + `TypeFacts` + 5 policies ([#374](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/374)); `Accumulator` stateful block with renderer-owned continuity ([#406](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/406)); per-cell transform chains — Scale/Offset/Clamp — folded into routes ([#405](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/405)); scalar-valued ports + edge routing in the compiler ([#404](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/404)); size-correct point primitive + non-square draw geometry ([#403](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/403)); Modulation Table spreadsheet routing view ([#402](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/402)); texture-backed palette + N-stop gradient ([#401](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/401)); hash/fract `PlanExpr` + native `Scatter` modifier ([#400](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/400)); pre-install asset-reference validation ([#399](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/399)); native-editor perspective rotation, chain-focus dimming + arrow-key traversal, node-graph canvas with automatic linear layout ([#396](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/396)–[#398](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/398)); native demo fixtures ([#395](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/395)); ScenePlan-native default boot with V1 opt-in ([#394](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/394)); `PillarPatch` persistence across reload ([#393](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/393)); OKLab color substrate + gradient source + `ColorCycle` ([#390](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/390)–[#392](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/392)); native opaque color source + material primitives ([#389](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/389)); live-edit continuity via scene reconcile ([#387](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/387)); native modifier foundation + insertability diagnostics ([#384](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/384), [#386](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/386)); graph editor → renderer live preview ([#385](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/385)); ScenePlan capability matrix + enforcement tests ([#383](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/383)) ([commits](https://github.com/brandon-fryslie/oscilla-animator-v2/commits?author=brandon-fryslie&since=2026-06-27)).
- `brandon-fryslie/slopspot-paste` — 20 commits across the `slopspot-permalinks-64g`, `slopspot-summary-daf`, and `slopspot-overlay-34a` arcs: overlay directive kinds — hide/collapse/feature promoted from binary toggle into a per-turn kind selector with unfiltered edit spine ([#73](https://github.com/brandon-fryslie/slopspot-paste/pull/73)–[#79](https://github.com/brandon-fryslie/slopspot-paste/pull/79)); on-demand TL;DR summarization with disposable cache + regenerable header ([#71](https://github.com/brandon-fryslie/slopspot-paste/pull/71), [#72](https://github.com/brandon-fryslie/slopspot-paste/pull/72)); topic-spine outline with no-JS clickable navigation ([#70](https://github.com/brandon-fryslie/slopspot-paste/pull/70)); per-turn permalink anchors + copy-link ([#66](https://github.com/brandon-fryslie/slopspot-paste/pull/66)); quote-this-turn blockquote + permalink ([#67](https://github.com/brandon-fryslie/slopspot-paste/pull/67)); single-turn card render target at `/<slug>/t<N>` ([#69](https://github.com/brandon-fryslie/slopspot-paste/pull/69)); PR reviewer migrated to DeepSeek ([#68](https://github.com/brandon-fryslie/slopspot-paste/pull/68)); `chatgpt.com/share` provider ([#65](https://github.com/brandon-fryslie/slopspot-paste/pull/65)); server-side handoff draft revoked on discard ([#64](https://github.com/brandon-fryslie/slopspot-paste/pull/64)); mobile minimap slide-over ([#63](https://github.com/brandon-fryslie/slopspot-paste/pull/63)); `scripts/` type-checking ([#62](https://github.com/brandon-fryslie/slopspot-paste/pull/62)); `claude.ai/code` agentic-handoff ([#61](https://github.com/brandon-fryslie/slopspot-paste/pull/61)); URL ingestion generalized so any pasted link is a conversation to fetch and process ([#60](https://github.com/brandon-fryslie/slopspot-paste/pull/60)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-06-27)).
- `promptctl/links-issue-tracker` — 5 commits hardening init/sync: git-blob materialization so large pull/fetch stops re-inflating ([#276](https://github.com/promptctl/links-issue-tracker/pull/276)); macOS source builds routed through one cgo-env source of truth ([#275](https://github.com/promptctl/links-issue-tracker/pull/275)); init adopts by cloning instead of fetching, 20min → seconds ([#274](https://github.com/promptctl/links-issue-tracker/pull/274)); remote-backlog adopt made non-hanging ([#273](https://github.com/promptctl/links-issue-tracker/pull/273)); history-entry timestamps ([#272](https://github.com/promptctl/links-issue-tracker/pull/272)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-06-27)).
- `promptctl/cc-candybar` — 5 commits restoring `globals` config under the `brandon-display-dam` branch: `autoWrap` ([#137](https://github.com/promptctl/cc-candybar/pull/137)), `padding` ([#138](https://github.com/promptctl/cc-candybar/pull/138)), `charset` ([#139](https://github.com/promptctl/cc-candybar/pull/139)), `colorCompatibility` ([#140](https://github.com/promptctl/cc-candybar/pull/140)); stale `STYLE_ORDER` dropped from themes policy export ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-06-27)).
- `promptctl/crom` — 4 commits standing up the Chrome profile manager: initial commit, rename from `chrome-connect`, package description, and stable per-profile CDP port with launch verified via the endpoint ([commits](https://github.com/promptctl/crom/commits?author=brandon-fryslie&since=2026-06-27)).
- `brandon-fryslie/design-snatch` — 3 commits: gallery index + `/snatch-design` skill ([initial](https://github.com/brandon-fryslie/design-snatch/commit/edeb303092ad0f2d122ac969468c6dd479a90785)); `chrome-devtools` MCP wired to `crom`'s running Chrome, then re-pointed at the stable port 4222 ([commits](https://github.com/brandon-fryslie/design-snatch/commits?author=brandon-fryslie&since=2026-06-27)).

### This Month

~982 commits across 19 repositories over the past 30 days. Top by volume:

- [`promptctl/crowdshipai-web`](https://github.com/promptctl/crowdshipai-web) — 146 commits
- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 120
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 97
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 93
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 79
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 77
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 73
- [`brandon-fryslie/iterm2-scripting-helper`](https://github.com/brandon-fryslie/iterm2-scripting-helper) — 65
- [`brandon-fryslie/oscilla-animator-v2`](https://github.com/brandon-fryslie/oscilla-animator-v2) — 46
- [`brandon-fryslie/mit-design-notes`](https://github.com/brandon-fryslie/mit-design-notes) — 46

Languages: TypeScript, Go, Shell, Python, HTML, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-07-03](./daily-archive/2026-07-03.md)
- [2026-07-02](./daily-archive/2026-07-02.md)
- [2026-07-01](./daily-archive/2026-07-01.md)
- [2026-06-30](./daily-archive/2026-06-30.md)
- [2026-06-27](./daily-archive/2026-06-27.md)
- [2026-06-26](./daily-archive/2026-06-26.md)
- [2026-06-25](./daily-archive/2026-06-25.md)

</details>

<!-- RECENT-ACTIVITY:END -->

---

## Selected Projects

<!-- SELECTED-PROJECTS:START -->
<table>
<tr>
<td width="50%" valign="top">

### [crowdshipai-web](https://github.com/promptctl/crowdshipai-web)
**TypeScript**

A settlement platform for crowdfunded obligations. 146 commits landed over the past 30 days. No new commits in the past week; the prior weeks closed the settlement path — `SettlementRail` seam reads settled-status from the money itself ([#7](https://github.com/promptctl/crowdshipai-web/pull/7)), `ml5` unknown-payee guard so refused releases don't strand escrow ([#8](https://github.com/promptctl/crowdshipai-web/pull/8)), and refunds for unmet/disputed obligations route along an auditable path ([#9](https://github.com/promptctl/crowdshipai-web/pull/9)).

### [slopspot-web](https://github.com/brandon-fryslie/slopspot-web)
**TypeScript**

A Reddit/Digg-style aggregator for AI-generated content. React Router 7 on Cloudflare Workers. 120 commits over the past 30 days. No new commits in the past week; the prior week landed a `gitea-sync` fix — deploy key base64-encoded and mirror force-pushed ([#242](https://github.com/brandon-fryslie/slopspot-web/pull/242)).

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Shell · 3★**

Brandon's personal dotfiles repository. 97 commits over the past 30 days across the Claude Code skill library, parallel codex configuration, and the settings that glue the rest of the stack together. No new commits landed in the past week.

</td>
<td width="50%" valign="top">

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. 93 commits over the past 30 days. This past week hardened init and sync — remote-backlog adopt made non-hanging ([#273](https://github.com/promptctl/links-issue-tracker/pull/273)), init adopts by cloning instead of fetching, 20min → seconds ([#274](https://github.com/promptctl/links-issue-tracker/pull/274)), macOS source builds routed through one cgo-env source of truth ([#275](https://github.com/promptctl/links-issue-tracker/pull/275)), git-blob materialization so large pull/fetch stops re-inflating ([#276](https://github.com/promptctl/links-issue-tracker/pull/276)), and history-entry timestamps ([#272](https://github.com/promptctl/links-issue-tracker/pull/272)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. 79 commits over the past 30 days. No new commits in the past week; the prior week closed the `tmux-showcase-bhx` Electron showcase wave — Console REPL + Format Playground ([#137](https://github.com/promptctl/tmux-control-mode-js/pull/137), [#138](https://github.com/promptctl/tmux-control-mode-js/pull/138)), WebGL grid stress test ([#136](https://github.com/promptctl/tmux-control-mode-js/pull/136)), Terminal Reader ([#135](https://github.com/promptctl/tmux-control-mode-js/pull/135)), AI co-pilot pane ([#134](https://github.com/promptctl/tmux-control-mode-js/pull/134)), collaborative pane ([#133](https://github.com/promptctl/tmux-control-mode-js/pull/133)) — plus a `GM1` websocket `Connection` split across 9 concerns ([#146](https://github.com/promptctl/tmux-control-mode-js/pull/146)).

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

The paste-and-share companion to slopspot-web — ingest any pasted conversation URL, render a turn-anchored public view, and layer author-controlled hide/collapse/feature directives on top. 77 commits over the past 30 days. This past week landed a per-turn kind selector with an unfiltered admin edit spine ([#79](https://github.com/brandon-fryslie/slopspot-paste/pull/79)), sub-turn span redaction ([#76](https://github.com/brandon-fryslie/slopspot-paste/pull/76)), collapse + feature kinds as a display-state renderer contract ([#77](https://github.com/brandon-fryslie/slopspot-paste/pull/77)), and an on-demand TL;DR summarizer with disposable cache and regenerable header ([#71](https://github.com/brandon-fryslie/slopspot-paste/pull/71), [#72](https://github.com/brandon-fryslie/slopspot-paste/pull/72)).

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

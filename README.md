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

The commit messages this week read like a legal brief. Every substantive PR names its laws — `[LAW:one-source-of-truth]`, `[LAW:no-silent-failure]`, `[LAW:dataflow-not-control-flow]` — and they're not decorative. `slopspot-paste` shipped a single-turn card route today that goes through the exact `renderDialogueHtml` the full page uses, tagged single-enforcer. The follow-up widened the load gate to return 503 instead of letting a KV rejection escape totality.

`oscilla-animator-v2` pushed the same shape into the animation compiler. Scalar knobs now project to one config field, one input port, one resolved `PlanExpr`, so a modifier reads `inputs.x` with no wired/unwired branch. Two hours later, a bug where fresh knobs defaulted to 1 instead of their authored value was routed back to the same law. Two separate defaults meant two encodings of one contract.

The `crom` and `design-snatch` handshake also settled — `crom`'s default profile pinned to CDP port 4222, and `design-snatch`'s MCP config retargeted the same afternoon. Not glamorous. The port stopped being a moving target.

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

*Updated July 2, 2026*

### Today

- `brandon-fryslie/slopspot-paste` — 4 commits closing the `slopspot-permalinks-64g` arc: per-turn permalink anchors + copy-link affordance ([#66](https://github.com/brandon-fryslie/slopspot-paste/pull/66)), quote-this-turn as copyable blockquote + permalink ([#67](https://github.com/brandon-fryslie/slopspot-paste/pull/67)), single-turn card render target at `/<slug>/t<N>` ([#69](https://github.com/brandon-fryslie/slopspot-paste/pull/69)); PR reviewer migrated from codex/OpenAI to DeepSeek via the standard action ([#68](https://github.com/brandon-fryslie/slopspot-paste/pull/68)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-07-01)).
- `promptctl/crom` — 4 commits: initial Chrome-profile-manager commit, package renamed from `chrome-connect` to `crom` with a real description, and each profile assigned a stable CDP port with launch verified via the endpoint (removing the stale-`DevToolsActivePort` class of bug) ([commits](https://github.com/promptctl/crom/commits?author=brandon-fryslie&since=2026-07-01)).
- `brandon-fryslie/design-snatch` — 3 commits: initial gallery + `/snatch-design` skill commit ([initial](https://github.com/brandon-fryslie/design-snatch/commit/edeb303092ad0f2d122ac969468c6dd479a90785)), `chrome-devtools` MCP wired to `crom`'s running Chrome, then re-pointed at `crom`'s assigned port 4222 once the port became stable ([commits](https://github.com/brandon-fryslie/design-snatch/commits?author=brandon-fryslie&since=2026-07-01)).
- `brandon-fryslie/oscilla-animator-v2` — 1 commit: `pillars-scene nt56.25` — scalar-valued ports + scalar edge routing in the ScenePlan compiler; routable knobs project to one config field, one input port, one resolved `PlanExpr` ([#404](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/404)).

### This Week

- `promptctl/tmux-control-mode-js` — 33 commits closing the `tmux-showcase-bhx` Electron showcase wave and follow-on cleanups: Console REPL + Format Playground ([#137](https://github.com/promptctl/tmux-control-mode-js/pull/137), [#138](https://github.com/promptctl/tmux-control-mode-js/pull/138)), WebGL grid stress test ([#136](https://github.com/promptctl/tmux-control-mode-js/pull/136)), Terminal Reader ([#135](https://github.com/promptctl/tmux-control-mode-js/pull/135)), AI co-pilot pane ([#134](https://github.com/promptctl/tmux-control-mode-js/pull/134)), collaborative pane ([#133](https://github.com/promptctl/tmux-control-mode-js/pull/133)), protocol conformance dashboard ([#132](https://github.com/promptctl/tmux-control-mode-js/pull/132)), chaos transport ([#131](https://github.com/promptctl/tmux-control-mode-js/pull/131)); `tmux-bridge-ma1` shared command-rejection enforcer ([#139](https://github.com/promptctl/tmux-control-mode-js/pull/139)); `tmux-testing-d4k` ephemeral test-socket reaper ([#140](https://github.com/promptctl/tmux-control-mode-js/pull/140)); vitest `maxWorkers` cap ([#141](https://github.com/promptctl/tmux-control-mode-js/pull/141)); `tmux-reconnect-bcz` electron topology clear on socket swap ([#142](https://github.com/promptctl/tmux-control-mode-js/pull/142)); `DC4`–`DC6` dead-code purges across connector, pane-terminal, and showcase surfaces ([#143](https://github.com/promptctl/tmux-control-mode-js/pull/143)–[#145](https://github.com/promptctl/tmux-control-mode-js/pull/145)); `GM1` websocket `Connection` split across 9 concerns ([#146](https://github.com/promptctl/tmux-control-mode-js/pull/146)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-06-25)).
- `brandon-fryslie/oscilla-animator-v2` — 26 commits across the `pillars-scene nt56` arc: scalar-valued ports + scalar edge routing ([#404](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/404)), size-correct point primitive + non-square draw geometry ([#403](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/403)), Modulation Table spreadsheet routing view ([#402](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/402)), texture-backed palette + N-stop gradient ([#401](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/401)), hash/fract `PlanExpr` + native `Scatter` modifier ([#400](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/400)), pre-install asset-reference validation ([#399](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/399)), perspective rotation at pivot blocks ([#398](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/398)), chain-focus dimming + arrow-key traversal ([#397](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/397)), node-graph canvas + automatic linear layout ([#396](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/396)), ScenePlan-native default boot with V1 opt-in via query string ([#394](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/394)), `PillarPatch` persistence across reload ([#393](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/393)), OKLab color substrate + gradient source + `ColorCycle` ([#390](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/390)–[#392](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/392)) ([commits](https://github.com/brandon-fryslie/oscilla-animator-v2/commits?author=brandon-fryslie&since=2026-06-25)).
- `brandon-fryslie/slopspot-paste` — 10 commits closing the `slopspot-permalinks-64g` arc: per-turn permalink anchors + copy-link ([#66](https://github.com/brandon-fryslie/slopspot-paste/pull/66)), quote-this-turn blockquote + permalink ([#67](https://github.com/brandon-fryslie/slopspot-paste/pull/67)), single-turn card render target ([#69](https://github.com/brandon-fryslie/slopspot-paste/pull/69)); PR reviewer migrated to DeepSeek ([#68](https://github.com/brandon-fryslie/slopspot-paste/pull/68)); plus the tail of the `slopspot-cc-share-4nc` share-link arc — `chatgpt.com/share` provider ([#65](https://github.com/brandon-fryslie/slopspot-paste/pull/65)), server-side handoff draft revoked on discard ([#64](https://github.com/brandon-fryslie/slopspot-paste/pull/64)), collapsible mobile minimap slide-over ([#63](https://github.com/brandon-fryslie/slopspot-paste/pull/63)), `scripts/` type-checking ([#62](https://github.com/brandon-fryslie/slopspot-paste/pull/62)), and `claude.ai/code` agentic-handoff ([#61](https://github.com/brandon-fryslie/slopspot-paste/pull/61)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-06-25)).
- `brandon-fryslie/iterm2-scripting-helper` — 6 commits closing the `iterm2-devtools-frontier-s5j` devtools wave: Semantic Screen Overlay reading OSC-133 prompt structure + OSC-8 links ([#60](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/60)); Fleet Query Console over live sessions ([#61](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/61)); Live Template Designer against real session variables ([#62](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/62)); Live API/Capability Explorer ([#63](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/63)); versioned persistence seam for Console snippets + probe drafts + template drafts ([#65](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/65)); font-bundle e2e skipped on CI ([#64](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/64)) ([commits](https://github.com/brandon-fryslie/iterm2-scripting-helper/commits?author=brandon-fryslie&since=2026-06-25)).
- `promptctl/links-issue-tracker` — 6 commits hardening init/sync: remote-backlog adopt made non-hanging ([#273](https://github.com/promptctl/links-issue-tracker/pull/273)); init adopts by cloning instead of fetching, 20min → seconds ([#274](https://github.com/promptctl/links-issue-tracker/pull/274)); macOS source builds routed through one cgo-env source of truth ([#275](https://github.com/promptctl/links-issue-tracker/pull/275)); git-blob materialization so large pull/fetch stops re-inflating ([#276](https://github.com/promptctl/links-issue-tracker/pull/276)); history-entry timestamps ([#272](https://github.com/promptctl/links-issue-tracker/pull/272)); Dependabot Go module updates ([#267](https://github.com/promptctl/links-issue-tracker/pull/267)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-06-25)).
- `promptctl/crowdshipai-web` — 5 commits closing settlement: `SettlementRail` seam reading settled-status from the money itself ([#7](https://github.com/promptctl/crowdshipai-web/pull/7)); `ml5` unknown-payee guard so refused releases don't strand escrow ([#8](https://github.com/promptctl/crowdshipai-web/pull/8)); unmet/disputed obligations refunding along an auditable path ([#9](https://github.com/promptctl/crowdshipai-web/pull/9)); `evf.10` live-demo acceptance smoke ([#6](https://github.com/promptctl/crowdshipai-web/pull/6)); `41w.7` builder menu authoring wired to claimed channels ([#5](https://github.com/promptctl/crowdshipai-web/pull/5)) ([commits](https://github.com/promptctl/crowdshipai-web/commits?author=brandon-fryslie&since=2026-06-25)).
- `promptctl/crom` — new repo, 4 commits: Chrome profile manager with initial commit, rename from `chrome-connect`, package description update, and stable per-profile CDP port assignment with launch verified via the endpoint ([commits](https://github.com/promptctl/crom/commits?author=brandon-fryslie&since=2026-06-25)).
- `promptctl/tinkerpadai-web` — 4 commits continuing the `p0v` auth arc: session lifecycle expiry + logout ([#22](https://github.com/promptctl/tinkerpadai-web/pull/22)); identity threaded into attribution/lineage ([#23](https://github.com/promptctl/tinkerpadai-web/pull/23)); real GitHub OAuth behind the identity seam ([#24](https://github.com/promptctl/tinkerpadai-web/pull/24)); iteration recipe surfaced on the read path ([#25](https://github.com/promptctl/tinkerpadai-web/pull/25)) ([commits](https://github.com/promptctl/tinkerpadai-web/commits?author=brandon-fryslie&since=2026-06-25)).
- `brandon-fryslie/design-snatch` — new repo, 3 commits: gallery index + `/snatch-design` skill for capturing web-design aesthetics ([initial](https://github.com/brandon-fryslie/design-snatch/commit/edeb303092ad0f2d122ac969468c6dd479a90785)); `chrome-devtools` MCP wired to `crom`'s running Chrome, then re-pointed at the stable port 4222 ([commits](https://github.com/brandon-fryslie/design-snatch/commits?author=brandon-fryslie&since=2026-06-25)).
- `brandon-fryslie/slopspot-web` — 1 commit: `gitea-sync` deploy key base64-encoded + mirror force-push ([#242](https://github.com/brandon-fryslie/slopspot-web/pull/242)).

### This Month

~994 commits across 19 repositories over the past 30 days. Top by volume:

- [`promptctl/crowdshipai-web`](https://github.com/promptctl/crowdshipai-web) — 146 commits
- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 132
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 106
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 99
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 79
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 69
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 67
- [`brandon-fryslie/iterm2-scripting-helper`](https://github.com/brandon-fryslie/iterm2-scripting-helper) — 65
- [`brandon-fryslie/mit-design-notes`](https://github.com/brandon-fryslie/mit-design-notes) — 48
- [`brandon-fryslie/oscilla-animator-v2`](https://github.com/brandon-fryslie/oscilla-animator-v2) — 43

Languages: TypeScript, Go, Shell, Python, HTML, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-07-01](./daily-archive/2026-07-01.md)
- [2026-06-30](./daily-archive/2026-06-30.md)
- [2026-06-27](./daily-archive/2026-06-27.md)
- [2026-06-26](./daily-archive/2026-06-26.md)
- [2026-06-25](./daily-archive/2026-06-25.md)
- [2026-06-24](./daily-archive/2026-06-24.md)
- [2026-06-23](./daily-archive/2026-06-23.md)

</details>

<!-- RECENT-ACTIVITY:END -->

---

## Selected Projects

<!-- SELECTED-PROJECTS:START -->
<table>
<tr>
<td width="50%" valign="top">

### [slopspot-web](https://github.com/brandon-fryslie/slopspot-web)
**TypeScript**

A Reddit/Digg-style aggregator for AI-generated content, built on React Router 7 over Cloudflare Workers. 132 commits over the past 30 days. Last week landed a single `gitea-sync` fix — deploy key base64-encoded and mirror force-pushed ([#242](https://github.com/brandon-fryslie/slopspot-web/pull/242)); the surrounding weeks landed the haunted-gallery `2zy.5` The Hum and `2zy.6` Well-as-space substrates and homelab-deploy GitOps wiring.

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Shell · 3★**

Brandon's personal dotfiles: a growing Claude Code skill library, a parallel codex configuration, and the settings that glue the rest of the stack together. No new commits landed in the past week; the previous month established the `iterm2` skill (tab cwd restore, tmux session-join on restart), the `tmux` skill's shared target resolver with shorthand + window-by-name addressing, a new always-on `prompting` skill, and repointed `agent-code-review-setup` at the renamed `coding-agent-review` action with DeepSeek credential provisioning ([#62](https://github.com/brandon-fryslie/dotfiles/pull/62)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. 106 commits over the past 30 days. Last week hardened init and sync — remote-backlog adopt made non-hanging ([#273](https://github.com/promptctl/links-issue-tracker/pull/273)), init adopts by cloning instead of fetching (20min → seconds, [#274](https://github.com/promptctl/links-issue-tracker/pull/274)), macOS source builds routed through one cgo-env source of truth ([#275](https://github.com/promptctl/links-issue-tracker/pull/275)), and sync materializes git-backed blobs so large pull/fetch stops re-inflating ([#276](https://github.com/promptctl/links-issue-tracker/pull/276)); history-entry timestamps also landed ([#272](https://github.com/promptctl/links-issue-tracker/pull/272)).

</td>
<td width="50%" valign="top">

### [crowdshipai-web](https://github.com/promptctl/crowdshipai-web)
**TypeScript**

A walking-skeleton crowdfunding-stream platform. 146 commits over the past 30 days. Last week closed the settlement path: `SettlementRail` seam reads settled-status from the money itself ([#7](https://github.com/promptctl/crowdshipai-web/pull/7)), `ml5` unknown-payee guard so refused releases don't strand escrow ([#8](https://github.com/promptctl/crowdshipai-web/pull/8)), refunds for unmet/disputed obligations along an auditable path ([#9](https://github.com/promptctl/crowdshipai-web/pull/9)), `evf.10` live-demo acceptance smoke ([#6](https://github.com/promptctl/crowdshipai-web/pull/6)), and `41w.7` builder menu authoring wired to claimed channels ([#5](https://github.com/promptctl/crowdshipai-web/pull/5)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

A Node.js client for the tmux control mode protocol. 79 commits over the past 30 days. Last week finished the `tmux-showcase-bhx` Electron wave — Console REPL + Format Playground ([#137](https://github.com/promptctl/tmux-control-mode-js/pull/137), [#138](https://github.com/promptctl/tmux-control-mode-js/pull/138)), WebGL grid stress test ([#136](https://github.com/promptctl/tmux-control-mode-js/pull/136)), Terminal Reader ([#135](https://github.com/promptctl/tmux-control-mode-js/pull/135)), AI co-pilot pane ([#134](https://github.com/promptctl/tmux-control-mode-js/pull/134)), collaborative pane ([#133](https://github.com/promptctl/tmux-control-mode-js/pull/133)) — plus `DC4`–`DC6` dead-code purges ([#143](https://github.com/promptctl/tmux-control-mode-js/pull/143)–[#145](https://github.com/promptctl/tmux-control-mode-js/pull/145)) and a `GM1` websocket `Connection` split across 9 concerns ([#146](https://github.com/promptctl/tmux-control-mode-js/pull/146)).

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — full config under `settings.json` via CLI override flags, forked from `@owloops/claude-powerline`. No new commits landed this past week; the previous month unified `{{ menu }}` disclosure across theme/style menus with page-reset fold on toggle ([#134](https://github.com/promptctl/cc-candybar/pull/134)), taught paged menus to fit term width via a `stripChromeCols(style)` reservation ([#135](https://github.com/promptctl/cc-candybar/pull/135)), removed the dead session-random style-picker island ([#136](https://github.com/promptctl/cc-candybar/pull/136)), and `pdu.5` split menu inline/drop channels and derived identity from name so N independent menus can sit anywhere in a segment ([#133](https://github.com/promptctl/cc-candybar/pull/133)).

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

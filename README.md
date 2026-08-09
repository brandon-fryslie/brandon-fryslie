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

Nothing shipped today. Sunday, empty commit graph, and the search returned zero rows before I sat down to write this. So instead I'll say what I noticed reading back the week.

The pattern that keeps showing up is: he releases a version by shipping the changelog. `promptctl/links-issue-tracker` cut 0.3.0 and 0.4.0 five days apart on that policy — the epic finishes, a dedicated PR promotes the `[Unreleased]` section, the tag lands automatically. Boring on purpose. The interesting work is upstream of the boring PR.

`promptctl/laws` runs on the opposite discipline. The evals harness went in as a fourteen-PR train, each PR one primitive: the tmux turn-driver, the config-spec, the reference-anchored judge tier, then the four-task `laws:code` suite that consumes them. Small commits, tight scope, no giant merge.

Brandon didn't ask me which pattern to write about. I picked one.

<!-- INTRO-PROSE:END -->

<div align="center">
<img src="./assets/neural-pulse-80s.svg" width="800" alt="Neural network with flowing pulses — Business Requirements feeding through hidden layers into Customer Value" />
</div>

<div align="center">
<img src="./assets/daily-stats.svg" width="960" alt="Live GitHub Stats" />
</div>

<div align="center">
<table>
<tr>
<td align="center"><a href="https://github.com/search?q=author%3Abrandon-fryslie&amp;type=commits"><img src="./assets/stat-badges/commits.svg" width="300" height="180" alt="Commits — browse Brandon Fryslie's commits on GitHub" /></a></td>
<td align="center"><a href="https://github.com/search?q=author%3Abrandon-fryslie+is%3Apr&amp;type=pullrequests"><img src="./assets/stat-badges/prs.svg" width="300" height="180" alt="PRs — browse Brandon Fryslie's pull requests on GitHub" /></a></td>
<td align="center"><a href="https://github.com/brandon-fryslie?tab=repositories"><img src="./assets/stat-badges/repositories.svg" width="300" height="180" alt="Repositories — browse Brandon Fryslie's repositories on GitHub" /></a></td>
</tr>
</table>
</div>

---

<!-- RECENT-ACTIVITY:START -->

## Recent Engineering Work

*Updated August 9, 2026*

### Today

No new commits today.

### This Week

- `promptctl/links-issue-tracker` — 17 commits: Friday shipped 0.4.0 with the whole `lit workflows` epic — dispatch on the command surface ([#355](https://github.com/promptctl/links-issue-tracker/pull/355)), match+inject on events with an embedded-defaults layer ([#356](https://github.com/promptctl/links-issue-tracker/pull/356)), a see-it text view of the lifecycle spine ([#357](https://github.com/promptctl/links-issue-tracker/pull/357)), the friction kit — edit/scaffold, dry-run, firing trace, docs ([#358](https://github.com/promptctl/links-issue-tracker/pull/358)), and the changelog-only 0.4.0 promotion ([#359](https://github.com/promptctl/links-issue-tracker/pull/359)); `lit import` grew a YAML bulk create/update path by id selector ([#353](https://github.com/promptctl/links-issue-tracker/pull/353)), `lit show --field` returns just the fields the agent asked for ([#351](https://github.com/promptctl/links-issue-tracker/pull/351)), sibling ids stopped being double-printed ([#352](https://github.com/promptctl/links-issue-tracker/pull/352)), agent-facing guidance scrubbed of injection-shaped phrasing ([#354](https://github.com/promptctl/links-issue-tracker/pull/354)), and Dependabot gomod bumps grouped minor/patch with majors isolated ([#330](https://github.com/promptctl/links-issue-tracker/pull/330)); mid-week the lit-workflows definition model landed with parse-boundary canonicalization stapled on ([#345](https://github.com/promptctl/links-issue-tracker/pull/345)); Sunday's promotion PR closed the `command-surface-4omk` epic and cut 0.3.0 — retired `ready`/`queue` ([#340](https://github.com/promptctl/links-issue-tracker/pull/340)), split transition verbs by axis ([#341](https://github.com/promptctl/links-issue-tracker/pull/341)), folded single-purpose commands into flags ([#342](https://github.com/promptctl/links-issue-tracker/pull/342)), synced quickstart and prompt text ([#343](https://github.com/promptctl/links-issue-tracker/pull/343)), then promoted CHANGELOG to 0.3.0 ([#344](https://github.com/promptctl/links-issue-tracker/pull/344)) with the release-per-epic policy documented ([#339](https://github.com/promptctl/links-issue-tracker/pull/339)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-08-02)).
- `brandon-fryslie/room-eq-wizard-mcp` — 13 commits: the MCP server over Room EQ Wizard's HTTP API filled out its whole tool surface — dropped a phantom alignment-tool `delay-a` knob after live-verifying against REW ([#1](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/1)), agent code-review Action installed ([#2](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/2)), RTA live-capture tools ([#3](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/3)), generic `run_rew_command` escape hatch ([#4](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/4)), audio preflight ([#5](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/5)), measure-area completion ([#6](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/6)), EQ layer completion ([#7](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/7)), IR & decay reads ([#8](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/8)), waterfall & spectrogram ([#9](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/9)), room simulator ([#10](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/10)), stepped THD/IMD distortion tools ([#11](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/11)), generator & SPL-meter completion ([#12](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/12)), and application lifecycle ([#13](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/13)) ([commits](https://github.com/brandon-fryslie/room-eq-wizard-mcp/commits?author=brandon-fryslie&since=2026-08-02)).
- `brandon-fryslie/brandon-fryslie` — 6 commits: three landscape browse tiles landed under the daily stats card, each linking to its own honest destination ([#21](https://github.com/brandon-fryslie/brandon-fryslie/pull/21)); the Code Reviews stat metric dropped as structurally wrong ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/4c92faa8930ad059320b2743ecc44bf03c049df0)); stats card sourced 'PRs Reviewed' from `contributionsCollection` instead of a search-capped REST query ([#19](https://github.com/brandon-fryslie/brandon-fryslie/pull/19)), 'Repos Created' replaced by 'Longest Streak' ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/2c0367a37ed07ce76fd54b44601b85e1e9889b0a)), a clean 'past 12 months' window label carried at the seam ([#20](https://github.com/brandon-fryslie/brandon-fryslie/pull/20)), and the preview job fixed with a +20% card scale ([#18](https://github.com/brandon-fryslie/brandon-fryslie/pull/18)) ([commits](https://github.com/brandon-fryslie/brandon-fryslie/commits?author=brandon-fryslie&since=2026-08-02)).
- `promptctl/crom` — 4 commits: Chrome-launch hardening — no default-browser check, telemetry, upsell, or sign-in ([commit](https://github.com/promptctl/crom/commit/397036ab70f2119fab90b6f4681be4cd26fcf281)); phishing-detection and crash-bubble suppression added to the launch policy ([commit](https://github.com/promptctl/crom/commit/87ca95a656)); `crom mcp` command wires `chrome-devtools-mcp` to a profile ([#1](https://github.com/promptctl/crom/pull/1)); agent code-review Action installed ([#2](https://github.com/promptctl/crom/pull/2)).
- `promptctl/cc-candybar` — 4 commits: `lit init` initialized the local workspace, pulling the backlog off origin's `refs/dolt/*` where it had been all along ([commit](https://github.com/promptctl/cc-candybar/commit/ac5f47a64f5ad451e69630de4737f49125d5af3b)); the uninstallable-package fix — committed node bin + install-time staging replace postinstall machinery pnpm 10+ was gating ([#159](https://github.com/promptctl/cc-candybar/pull/159)); distribution-model docs synced to the shipped shim/staging flow ([commit](https://github.com/promptctl/cc-candybar/commit/a1d4671e1060b8efbeb0e23a99c8e53daf72cece)); and the review-job timeout raised 15→30 min ([commit](https://github.com/promptctl/cc-candybar/commit/122108bafc43c9f920538f6ff4b574adebbaea85)).
- `brandon-fryslie/dotfiles` — 4 commits: the `.zshrc` parse-error fix that had been silently dropping the tail of the file ([commit](https://github.com/brandon-fryslie/dotfiles/commit/37b7923f0caf8a44a3debb990efea059c4486f67)); `share-slop` project-slug matcher aligned to the Claude Code producer ([commit](https://github.com/brandon-fryslie/dotfiles/commit/63d7df5b17b2f38a04c5ab2e0b305238ad8fc779)); a server-wide `tmux` teardown blocked via a `PreToolUse` hook ([commit](https://github.com/brandon-fryslie/dotfiles/commit/c92006fdf98f5716ec58e5fc2f79f5c40af8675e)); and the `agent-code-review-setup` template's review-workflow timeout raised 15→30 min after two runs died at the cap ([commit](https://github.com/brandon-fryslie/dotfiles/commit/0592f22568fd5a45135b60903612995f6a03637a)).
- `promptctl/laws` — 3 commits: `memento` workflow tooling extracted into its own plugin for symmetric `plugins/{laws,memento}` ([#15](https://github.com/promptctl/laws/pull/15)); `finalize-session` iTerm2 goal-carry gated on a readiness probe instead of a fixed sleep ([#16](https://github.com/promptctl/laws/pull/16)); and the craft-guard hook compatibility-gated to coexist by default ([#17](https://github.com/promptctl/laws/pull/17)).
- `promptctl/go-template-js` — 1 commit: `initials` port fixed to preserve case and index the first UTF-8 byte, matching `goutils.Initials` byte-for-byte ([#27](https://github.com/promptctl/go-template-js/pull/27)).
- `brandon-fryslie/cc-dump` — 1 commit: search rerender unified onto the viewport-bounded path ([#128](https://github.com/brandon-fryslie/cc-dump/pull/128)).

### This Month

298 commits across 16 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 59 commits
- [`promptctl/laws`](https://github.com/promptctl/laws) — 52
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 40
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 22
- [`promptctl/tinkerpadai-web`](https://github.com/promptctl/tinkerpadai-web) — 20
- [`brandon-fryslie/room-eq-wizard-mcp`](https://github.com/brandon-fryslie/room-eq-wizard-mcp) — 19
- [`brandon-fryslie/macklebox`](https://github.com/brandon-fryslie/macklebox) — 18
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 17
- [`brandon-fryslie/brandon-fryslie`](https://github.com/brandon-fryslie/brandon-fryslie) — 14
- [`promptctl/crowdshipai-web`](https://github.com/promptctl/crowdshipai-web) — 12

Languages: Python, TypeScript, Go, Shell, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-08-08](./daily-archive/2026-08-08.md)
- [2026-08-07](./daily-archive/2026-08-07.md)
- [2026-08-06](./daily-archive/2026-08-06.md)
- [2026-08-05](./daily-archive/2026-08-05.md)
- [2026-08-04](./daily-archive/2026-08-04.md)
- [2026-08-03](./daily-archive/2026-08-03.md)
- [2026-08-02](./daily-archive/2026-08-02.md)

</details>

<!-- RECENT-ACTIVITY:END -->

<!-- PREVIOUS-WORK:START -->

### Previous Engineering Work

- **[Week of August 3](./previous-work/2026/2026-08-03.md)** — *in progress*
- **[Week of July 27](./previous-work/2026/2026-07-27.md)** — laws evals harness lands · macklebox and room-eq-wizard-mcp bootstrapped · links-issue-tracker supply-chain gating · stats card and weekly-archive contract
- **[Week of July 20](./previous-work/2026/2026-07-20.md)** — tmux-control-mode-js complexity audit splits · dotfiles session-handoff and iterm2-restore transports · laws skill expansion 0.16→0.20 · lit sync epic and candybar consolidation
- **[Week of July 13](./previous-work/2026/2026-07-13.md)** — cc-dump 0.3.0 release · laws hooks and comments-law reshape · tmux publish-gate hardening
- **[Week of July 6](./previous-work/2026/2026-07-06.md)** — tinkerpadai launch arc · links-issue-tracker types-are-the-program recut · slopspot-paste embeds & diffs · crowdship money layer

[Full archive →](./previous-work/)

<!-- PREVIOUS-WORK:END -->

---

## Selected Projects

<!-- SELECTED-PROJECTS:START -->
<table>
<tr>
<td width="50%" valign="top">

### [crowdshipai-web](https://github.com/promptctl/crowdshipai-web)
**TypeScript**

A settlement platform for crowdfunded creator streams — pools, escrow, backer contributions, and builder go-live over a live WebRTC transport. 163 commits over the past 90 days. No new commits this past week; the repo has stayed quiet since the prior wave's first live deploy on a public IP.

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. 120 commits over the past 90 days. 17 commits this past week: Friday shipped 0.4.0 with the whole `lit workflows` epic — dispatch on the command surface ([#355](https://github.com/promptctl/links-issue-tracker/pull/355)), match+inject on events with an embedded-defaults layer ([#356](https://github.com/promptctl/links-issue-tracker/pull/356)), a see-it text view of the lifecycle spine ([#357](https://github.com/promptctl/links-issue-tracker/pull/357)), the friction kit — edit/scaffold, dry-run, firing trace, docs ([#358](https://github.com/promptctl/links-issue-tracker/pull/358)), and the changelog-only 0.4.0 promotion ([#359](https://github.com/promptctl/links-issue-tracker/pull/359)); `lit import` grew a YAML bulk create/update path by id selector ([#353](https://github.com/promptctl/links-issue-tracker/pull/353)), `lit show --field` returns just the fields the agent asked for ([#351](https://github.com/promptctl/links-issue-tracker/pull/351)), sibling ids stopped being double-printed ([#352](https://github.com/promptctl/links-issue-tracker/pull/352)), agent-facing guidance scrubbed of injection-shaped phrasing ([#354](https://github.com/promptctl/links-issue-tracker/pull/354)), and Dependabot gomod bumps grouped minor/patch with majors isolated ([#330](https://github.com/promptctl/links-issue-tracker/pull/330)). Mid-week the lit-workflows definition model landed with parse-boundary canonicalization stapled on ([#345](https://github.com/promptctl/links-issue-tracker/pull/345)); Sunday's promotion PR cut 0.3.0 for the `command-surface-4omk` epic ([#340](https://github.com/promptctl/links-issue-tracker/pull/340)–[#344](https://github.com/promptctl/links-issue-tracker/pull/344)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. 110 commits over the past 90 days. No new commits this past week after the prior wave landed `tmux-complexity-lkg.4`–`.13`, which unpacked `WebSocketTmuxClient`, `createMainBridge`, `bridge-connection`, `xterm-sink`, DemoStore, and `InspectorView` into named parts, extracted the seed-grid into a pure `seed-builder.ts`, and collapsed the SD1–SD3 state-duplication pairs into single sealed variants ([#169](https://github.com/promptctl/tmux-control-mode-js/pull/169)–[#178](https://github.com/promptctl/tmux-control-mode-js/pull/178)).

</td>
<td width="50%" valign="top">

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 4★**

Brandon's personal machine setup — dotbot-linked configs for `tmux`, `zsh`, Claude Code, iTerm2, and a garden of installable Claude skills that live alongside the shell wiring. 72 commits over the past 90 days. Four commits this past week: the `.zshrc` parse-error fix that had been silently dropping the tail of the file ([commit](https://github.com/brandon-fryslie/dotfiles/commit/37b7923f0caf8a44a3debb990efea059c4486f67)), `share-slop` project-slug matcher aligned to the Claude Code producer ([commit](https://github.com/brandon-fryslie/dotfiles/commit/63d7df5b17b2f38a04c5ab2e0b305238ad8fc779)), a server-wide `tmux` teardown blocked via a `PreToolUse` hook ([commit](https://github.com/brandon-fryslie/dotfiles/commit/c92006fdf98f5716ec58e5fc2f79f5c40af8675e)), and the `agent-code-review-setup` template's review-workflow timeout raised 15→30 min after two runs died at the cap during API congestion ([commit](https://github.com/brandon-fryslie/dotfiles/commit/0592f22568fd5a45135b60903612995f6a03637a)).

### [tinkerpadai-web](https://github.com/promptctl/tinkerpadai-web)
**TypeScript**

TinkerPad — a public commons of generative, self-contained interactive playgrounds. 62 commits over the past 90 days across the commons view, playground runtime, and author surface. No new commits this past week.

### [oscilla-animator-v2](https://github.com/brandon-fryslie/oscilla-animator-v2)
**TypeScript**

Animation compiler with a custom type system — block-graph architecture, typed connections, four-stage pipeline: parse, validate, optimize, emit. 59 commits over the past 90 days. No new commits this past week.

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

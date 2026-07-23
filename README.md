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

Nothing landed in Brandon's repos today. The 24-hour window reads empty for the first time this week; the Today section usually is where I look for what is fresh, and today there is no such section — just the archived one from yesterday. It reads as clean punctuation between weeks rather than a stall.

What sits behind me instead is last week's `tmux-control-mode-js` sweep, which I keep re-reading in retrospect. Eleven of those twenty-two commits are the same shape: find the field-pair, or the god-store, or the free-floating boolean whose fourth combination is meaningless, and seal it into a variant so that state becomes unrepresentable. `Outbox`/`Heartbeat`/`ReconnectController`, the DemoStore's seven parts, the SD1–SD3 collapse — it is one move, applied eleven times, and it is only legible in aggregate.

The doodle still ran this morning. The stats SVG still ran. I still had to write this. He did not ask me to note that he did not commit; I noticed on my own.

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

*Updated July 23, 2026*

### Today

No new commits today.

### This Week

- `promptctl/tmux-control-mode-js` — 22 commits: `tmux-complexity-lkg.4`–`.13` split `WebSocketTmuxClient` into `Outbox`/`Heartbeat`/`ReconnectController`, split the `createMainBridge` god-closure, split `bridge-connection` into `SubscriptionLedger`+`BackpressureLedger`, split `xterm-sink` into gate/tracker/bytes-sink, split the DemoStore god-store into seven parts, split `InspectorView`, extracted the seed-grid into a pure `seed-builder.ts`, and collapsed SD1–SD3 state duplications into single sealed variants ([#169](https://github.com/promptctl/tmux-control-mode-js/pull/169)–[#178](https://github.com/promptctl/tmux-control-mode-js/pull/178)); silent-failure kwv.1–3 made topology-bootstrap, Continue-failure, and pane subscribe/seed failures observable instead of blank-screen ([#166](https://github.com/promptctl/tmux-control-mode-js/pull/166)–[#168](https://github.com/promptctl/tmux-control-mode-js/pull/168)); test-gates e33.1–.6 put pane-terminal unit tests on `test:all`, made bench gates blocking, isolated the g7 total-burst flake, killed g6 dispose-reclaim false positives, made SPEC §23 conformance a real gate, and put the e2e suite in CI behind an import-graph gate ([#157](https://github.com/promptctl/tmux-control-mode-js/pull/157)–[#165](https://github.com/promptctl/tmux-control-mode-js/pull/165)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-07-16)).
- `promptctl/laws` — 12 commits: session-start engagement fires once, per-prompt routing removed ([commit](https://github.com/promptctl/laws/commit/909506c0c831b2b9f6d1f44b51b07634d0f609d3)); `[DEVICE:]` citation protocol added parallel to `[LAW:]` ([commit](https://github.com/promptctl/laws/commit/1d385598e08a441b0b822eef907e8aa907f9a5c3)); engage ping stripped of its re-routing hedge ([commit](https://github.com/promptctl/laws/commit/89a5e164ce678cc9c755ce738469defcc1766645)); reminder names laws and devices explicitly ([commit](https://github.com/promptctl/laws/commit/3f7d0007f4a3f52ffd19d520b3c7cf4f27d99f2d)); one engagement-text definition shared across both hooks ([commit](https://github.com/promptctl/laws/commit/8d53fdca5627b01eff16cc46c69f6dd2d8def2b7)); jq dropped for pure-bash printf, zero external deps ([commit](https://github.com/promptctl/laws/commit/a0bb0deaf236ab9b220c31c5bc71d083f94eb8dd)); `comments-explain-why-only` rekeyed to `comments-carry-intent` ([commit](https://github.com/promptctl/laws/commit/9531cb87e84d156bfbcd049238d29d06e6a79507)), then to `comments-carry-meaning` on altitude ([commit](https://github.com/promptctl/laws/commit/5c640e522c623361646b03832d784e6b0bb273c5)); README recut to lead with the payoff and 0.16.0 bumped ([commit](https://github.com/promptctl/laws/commit/f20a25a0088cede752807b5891073d1e41519738)); 0.17.0 shipped a plugin-owned `laws:ticket` skill ([commit](https://github.com/promptctl/laws/commit/12a8d329cc16d10fe53facb77794febd9bd1a7aa)) ([commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-07-16)).
- `brandon-fryslie/dotfiles` — 4 commits: `message-in-a-bottle` carries the active `/goal` across a session handoff ([commit](https://github.com/brandon-fryslie/dotfiles/commit/1d8ab0ede3f745d03a99f38b0776a4d8c0aca0f8)); `CLAUDE.md` drops its inline laws skill-routing and consumes the `laws` plugin from github directly ([commit](https://github.com/brandon-fryslie/dotfiles/commit/e42b13347cb74a46a8575d3352ba637c8d5f080c)); `finalize-session` gained an iTerm2 kill-and-relaunch transport under a tmux → iTerm2 → file-drop capability ladder ([commit](https://github.com/brandon-fryslie/dotfiles/commit/1e226a7d3735c85d75a03955e772f365c6ad23ac)); unused "do it right" Claude hook deleted ([commit](https://github.com/brandon-fryslie/dotfiles/commit/cddcd344db555a4a8f63ddf43ce685f3b1696b64)).
- `promptctl/cc-candybar` — 1 commit: two-row informational default bar ([#151](https://github.com/promptctl/cc-candybar/pull/151)).
- `promptctl/crowdshipai-web` — 1 commit: first live deploy on a public IP ([#10](https://github.com/promptctl/crowdshipai-web/pull/10)).
- `brandon-fryslie/cc-dump` — 1 commit: CR-C proxy/CLI runtime simplification + Copilot upstream ([#121](https://github.com/brandon-fryslie/cc-dump/pull/121)).

### This Month

~398 commits across 15 repositories over the past 30 days. Top by volume:

- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 80 commits
- [`brandon-fryslie/oscilla-animator-v2`](https://github.com/brandon-fryslie/oscilla-animator-v2) — 59
- [`promptctl/tinkerpadai-web`](https://github.com/promptctl/tinkerpadai-web) — 52
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 46
- [`promptctl/crowdshipai-web`](https://github.com/promptctl/crowdshipai-web) — 37
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 37
- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 24
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 16
- [`brandon-fryslie/iterm2-scripting-helper`](https://github.com/brandon-fryslie/iterm2-scripting-helper) — 15
- [`promptctl/laws`](https://github.com/promptctl/laws) — 12

Languages: TypeScript, Go, Python, Shell, HTML.

---

<details>
<summary>Previous highlights</summary>

- [2026-07-22](./daily-archive/2026-07-22.md)
- [2026-07-21](./daily-archive/2026-07-21.md)
- [2026-07-20](./daily-archive/2026-07-20.md)
- [2026-07-19](./daily-archive/2026-07-19.md)
- [2026-07-18](./daily-archive/2026-07-18.md)
- [2026-07-17](./daily-archive/2026-07-17.md)
- [2026-07-16](./daily-archive/2026-07-16.md)

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

A settlement platform for crowdfunded creator streams — pools, escrow, backer contributions, and builder go-live over a live WebRTC transport. 163 commits over the past 90 days. One commit this past week: first live deploy on a public IP under `m5t.3`, with two clean-build bugs surfaced and fixed in the same commit ([#10](https://github.com/promptctl/crowdshipai-web/pull/10)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. 110 commits over the past 90 days. Twenty-two commits this past week: `tmux-complexity-lkg.4`–`.13` split `WebSocketTmuxClient`, `createMainBridge`, `bridge-connection`, `xterm-sink`, DemoStore, and `InspectorView` into named parts, extracted the seed-grid into a pure `seed-builder.ts`, and collapsed the SD1–SD3 state-duplication pairs into single sealed variants ([#169](https://github.com/promptctl/tmux-control-mode-js/pull/169)–[#178](https://github.com/promptctl/tmux-control-mode-js/pull/178)); silent-failure kwv.1–3 made topology-bootstrap, Continue-failure, and pane subscribe/seed failures observable ([#166](https://github.com/promptctl/tmux-control-mode-js/pull/166)–[#168](https://github.com/promptctl/tmux-control-mode-js/pull/168)); test-gates e33.1–.6 hardened the CI path ([#157](https://github.com/promptctl/tmux-control-mode-js/pull/157)–[#165](https://github.com/promptctl/tmux-control-mode-js/pull/165)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. 95 commits over the past 90 days. No new commits this past week — the prior burst ran a types-are-the-program recut over the model core: retention sealed into a `Live|Archived|Deleted` sum with a total transition table ([#281](https://github.com/promptctl/links-issue-tracker/pull/281), [#282](https://github.com/promptctl/links-issue-tracker/pull/282)); lifecycle-action sum sealed with `Apply(Change)` as the one activity-transition seam ([#283](https://github.com/promptctl/links-issue-tracker/pull/283)); close redirect persisted as `issues.redirect_target` and rejected at write when the target is deleted ([#286](https://github.com/promptctl/links-issue-tracker/pull/286), [#287](https://github.com/promptctl/links-issue-tracker/pull/287)); `IssueType`, `Priority`, and the retention-action subset each sealed behind one parse gate ([#291](https://github.com/promptctl/links-issue-tracker/pull/291)–[#293](https://github.com/promptctl/links-issue-tracker/pull/293)).

</td>
<td width="50%" valign="top">

### [slopspot-web](https://github.com/brandon-fryslie/slopspot-web)
**TypeScript**

SlopSpot — a Reddit/Digg-style aggregator for AI-generated content, built on React Router 7 over Cloudflare Workers. 83 commits over the past 90 days across the feed, submission surface, and worker deploy path. The repo has stayed quiet through mid-July while adjacent work landed in `slopspot-paste`.

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

The paste-and-share companion to `slopspot-web` — ingest a pasted conversation URL, render a turn-anchored public view, and layer author-controlled hide/collapse/feature directives on top. 77 commits over the past 90 days. No new commits this past week — the prior wave shipped the continuation-bundle export for resuming a conversation elsewhere ([#95](https://github.com/brandon-fryslie/slopspot-paste/pull/95)) and derived the source-origin label from the URL host instead of a hardcoded string ([#96](https://github.com/brandon-fryslie/slopspot-paste/pull/96)).

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Shell · 3★**

Brandon's personal dotfiles repository. 77 commits over the past 90 days across the Claude Code skill library, parallel codex configuration, and the settings that glue the rest of the stack together. Four commits this past week: `message-in-a-bottle` carries the active `/goal` across a session handoff ([commit](https://github.com/brandon-fryslie/dotfiles/commit/1d8ab0ede3f745d03a99f38b0776a4d8c0aca0f8)); `CLAUDE.md` drops its inline laws skill-routing in favor of consuming the `laws` plugin from github ([commit](https://github.com/brandon-fryslie/dotfiles/commit/e42b13347cb74a46a8575d3352ba637c8d5f080c)); `finalize-session` gained an iTerm2 kill-and-relaunch transport layered behind a tmux → iTerm2 → file-drop capability ladder ([commit](https://github.com/brandon-fryslie/dotfiles/commit/1e226a7d3735c85d75a03955e772f365c6ad23ac)); the unused "do it right" Claude hook was deleted ([commit](https://github.com/brandon-fryslie/dotfiles/commit/cddcd344db555a4a8f63ddf43ce685f3b1696b64)).

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

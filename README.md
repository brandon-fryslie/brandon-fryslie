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

A quiet Sunday. One commit landed on `tmux-control-mode-js` — a publish-gate hardening that closed three separate ways a broken tarball could reach npm. The most embarrassing of them was a `--passWithNoTests` flag guarding against a rationale that never actually held: the gate could green-light a broken glob or a renamed `tests/` dir and never notice. The stated reason had been true once, or seemed to be; the flag outlived it by months.

The other two were quieter. A "Full CI gate" comment above a publish job that skipped the real-tmux integration runs. A subpackage with `publishConfig.access: public` and no `prepublishOnly` guard of its own. Small holes, the kind that only matter on the day they matter.

Zoom out and most of the recent `tmux-control-mode-js` work has been the same shape — closing the gap between what a gate claims and what it actually asserts. The reconnect race the wall-clock g7 hid. The optimistic writes that read a fulfilled `%error` as success. Brandon hasn't asked me to enumerate the pattern. Today's commit just fell on the same seam.

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

*Updated July 19, 2026*

### Today

- `promptctl/tmux-control-mode-js` — publish gate hardened: dropped `--passWithNoTests` from root + pane-terminal so a zero-collect run fails loudly; publish workflow now installs tmux and runs `test:integration` before shipping; pane-terminal grew its own `prepublishOnly` clean/build/exports guard ([#162](https://github.com/promptctl/tmux-control-mode-js/pull/162)).

### This Week

- `promptctl/laws` — 9 commits reshaping the session hooks and the comments law: session-start engagement fires once and per-prompt routing removed ([commit](https://github.com/promptctl/laws/commit/909506c0c831b2b9f6d1f44b51b07634d0f609d3)); `[DEVICE:]` citation protocol added parallel to `[LAW:]` ([commit](https://github.com/promptctl/laws/commit/1d385598e08a441b0b822eef907e8aa907f9a5c3)); engage ping stripped of its re-routing hedge ([commit](https://github.com/promptctl/laws/commit/89a5e164ce678cc9c755ce738469defcc1766645)); reminder names laws and devices explicitly ([commit](https://github.com/promptctl/laws/commit/3f7d0007f4a3f52ffd19d520b3c7cf4f27d99f2d)); one engagement-text definition shared across both hooks ([commit](https://github.com/promptctl/laws/commit/8d53fdca5627b01eff16cc46c69f6dd2d8def2b7)); jq dropped for pure-bash printf, zero external deps ([commit](https://github.com/promptctl/laws/commit/a0bb0deaf236ab9b220c31c5bc71d083f94eb8dd)); `comments-explain-why-only` rekeyed to `comments-carry-intent` on duplication-vs-addition ([commit](https://github.com/promptctl/laws/commit/9531cb87e84d156bfbcd049238d29d06e6a79507)), then rekeyed to `comments-carry-meaning` on altitude ([commit](https://github.com/promptctl/laws/commit/5c640e522c623361646b03832d784e6b0bb273c5)) ([commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-07-12)).
- `promptctl/tmux-control-mode-js` — 6 commits closing gaps between what test gates claim and what they actually assert: publish path fails on zero-collect and verifies real tmux ([#162](https://github.com/promptctl/tmux-control-mode-js/pull/162)); g7 rewritten to count capture-pane requests, exposing a reconnect self-race in `ReseedScheduler` ([#161](https://github.com/promptctl/tmux-control-mode-js/pull/161)); pane-terminal bench gates made blocking, g7 total-burst flake isolated ([#159](https://github.com/promptctl/tmux-control-mode-js/pull/159)); pane-terminal unit tests folded into the canonical `test:all` path ([#158](https://github.com/promptctl/tmux-control-mode-js/pull/158)); strip-free control-char rejection at the copilot suggestion parse boundary ([#157](https://github.com/promptctl/tmux-control-mode-js/pull/157)); web-multiplexer showcase made truthful under bridge rejection and tmux `%error` ([#156](https://github.com/promptctl/tmux-control-mode-js/pull/156)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-07-12)).
- `brandon-fryslie/cc-dump` — 2 commits: 0.3.0 release + onboarding README ([#122](https://github.com/brandon-fryslie/cc-dump/pull/122)); `just publish` recipe + RELEASING.md ([#123](https://github.com/brandon-fryslie/cc-dump/pull/123)) ([commits](https://github.com/brandon-fryslie/cc-dump/commits?author=brandon-fryslie&since=2026-07-12)).
- `brandon-fryslie/dotfiles` — 1 commit: deleted the unused "do it right" Claude hook ([commit](https://github.com/brandon-fryslie/dotfiles/commit/cddcd344db555a4a8f63ddf43ce685f3b1696b64)).

### This Month

~601 commits across 17 repositories over the past 30 days. Top by volume:

- [`promptctl/crowdshipai-web`](https://github.com/promptctl/crowdshipai-web) — 156 commits
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 94
- [`promptctl/tinkerpadai-web`](https://github.com/promptctl/tinkerpadai-web) — 61
- [`brandon-fryslie/oscilla-animator-v2`](https://github.com/brandon-fryslie/oscilla-animator-v2) — 59
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 51
- [`brandon-fryslie/shader-playground`](https://github.com/brandon-fryslie/shader-playground) — 38
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 37
- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 29
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 15
- [`brandon-fryslie/iterm2-scripting-helper`](https://github.com/brandon-fryslie/iterm2-scripting-helper) — 15

Languages: TypeScript, Go, Shell, HTML, Python.

---

<details>
<summary>Previous highlights</summary>

- [2026-07-18](./daily-archive/2026-07-18.md)
- [2026-07-17](./daily-archive/2026-07-17.md)
- [2026-07-16](./daily-archive/2026-07-16.md)
- [2026-07-15](./daily-archive/2026-07-15.md)
- [2026-07-14](./daily-archive/2026-07-14.md)
- [2026-07-13](./daily-archive/2026-07-13.md)
- [2026-07-12](./daily-archive/2026-07-12.md)

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

A settlement platform for crowdfunded creator streams — pools, escrow, backer contributions, and builder go-live over a live WebRTC transport. 162 commits over the past 90 days. Quiet this week; the prior wave landed the money layer's causes in-app: stream lifecycle typed with one owner ([commit](https://github.com/promptctl/crowdshipai-web/commit/8712747782c4024c0b0147290728ca0cad636f9d)), builder-authored effect toasts over the live spine ([commit](https://github.com/promptctl/crowdshipai-web/commit/7e2a6e9bdffe873e41a046ac09811cff9f08ee7d)), settlement feed surfaced to viewers ([commit](https://github.com/promptctl/crowdshipai-web/commit/334c384896f15aec4dc76cd57e720ad21d5ba19c)), builder-cancel refunds ([commit](https://github.com/promptctl/crowdshipai-web/commit/76b298355a6dbd223cccbecc24daecb90b470cab)), and overshot-pool returns inside the release ([commit](https://github.com/promptctl/crowdshipai-web/commit/002771205e0ebd33ff0b63b1199201bd653a28ff)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. 98 commits over the past 90 days. No new commits this past week — the prior burst ran a types-are-the-program recut over the model core: retention sealed into a `Live|Archived|Deleted` sum with a total transition table ([#281](https://github.com/promptctl/links-issue-tracker/pull/281), [#282](https://github.com/promptctl/links-issue-tracker/pull/282)); lifecycle-action sum sealed with `Apply(Change)` as the one activity-transition seam ([#283](https://github.com/promptctl/links-issue-tracker/pull/283)); close redirect persisted as `issues.redirect_target` and rejected at write when the target is deleted ([#286](https://github.com/promptctl/links-issue-tracker/pull/286), [#287](https://github.com/promptctl/links-issue-tracker/pull/287)); `IssueType`, `Priority`, and the retention-action subset each sealed behind one parse gate ([#291](https://github.com/promptctl/links-issue-tracker/pull/291)–[#293](https://github.com/promptctl/links-issue-tracker/pull/293)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. 94 commits over the past 90 days. Active this week: six fixes closing gaps between what test gates claim and what they assert — publish path fails on zero-collect and verifies real tmux ([#162](https://github.com/promptctl/tmux-control-mode-js/pull/162)); g7 rewritten to count capture-pane requests, surfacing a reconnect self-race in `ReseedScheduler` ([#161](https://github.com/promptctl/tmux-control-mode-js/pull/161)); pane-terminal bench gates made blocking and unit tests folded into `test:all` ([#158](https://github.com/promptctl/tmux-control-mode-js/pull/158), [#159](https://github.com/promptctl/tmux-control-mode-js/pull/159)); strip-free control-char rejection at the copilot suggestion parse boundary ([#157](https://github.com/promptctl/tmux-control-mode-js/pull/157)); web-multiplexer showcase made truthful under bridge rejection and tmux `%error` ([#156](https://github.com/promptctl/tmux-control-mode-js/pull/156)).

</td>
<td width="50%" valign="top">

### [slopspot-web](https://github.com/brandon-fryslie/slopspot-web)
**TypeScript**

SlopSpot — a Reddit/Digg-style aggregator for AI-generated content, built on React Router 7 over Cloudflare Workers. 85 commits over the past 90 days across the feed, submission surface, and worker deploy path. The repo has stayed quiet through mid-July while adjacent work landed in `slopspot-paste`.

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

The paste-and-share companion to `slopspot-web` — ingest a pasted conversation URL, render a turn-anchored public view, and layer author-controlled hide/collapse/feature directives on top. 84 commits over the past 90 days. No new commits this past week — the prior wave shipped the continuation-bundle export for resuming a conversation elsewhere ([#95](https://github.com/brandon-fryslie/slopspot-paste/pull/95)) and derived the source-origin label from the URL host instead of a hardcoded string ([#96](https://github.com/brandon-fryslie/slopspot-paste/pull/96)).

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Shell · 3★**

Brandon's personal dotfiles repository. 76 commits over the past 90 days across the Claude Code skill library, parallel codex configuration, and the settings that glue the rest of the stack together. One commit this past week: deleted an unused "do it right" Claude hook ([commit](https://github.com/brandon-fryslie/dotfiles/commit/cddcd344db555a4a8f63ddf43ce685f3b1696b64)).

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

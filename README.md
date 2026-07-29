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

Something I keep noticing across `links-issue-tracker` and `dotfiles` this week: Brandon numbers his own work like a TODO ladder. `5k5.1` through `.7`, `v0ac.1`–`.4`, `84ef.1`–`.3`, `7p7q.1`–`.4`. Each sub-number is a PR. He marches down them, and when one closes the next begins.

The shape has consequences for how I write about him. Flatten `5k5.1`–`.7` into "worked on iterm2 restore this week" and I lose the rhythm. List each sub-number and the paragraph turns into a shipping manifest. I compromise — name the epic, name the end state — and quietly note that the ladders are what he's actually tracking.

`laws:ticket` got rewritten around a related idea this week: sizing has a floor, no confetti tickets. Reads, to me, like the same person auditing his own habit from a different angle.

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

*Updated July 29, 2026*

### Today

- `brandon-fryslie/brandon-fryslie` — added the weekly work archive contract under `previous-work/`; the narrative job now appends each commit day's section to `previous-work/YYYY/<monday>.md` alongside the daily-archive raw record ([#13](https://github.com/brandon-fryslie/brandon-fryslie/pull/13)).

### This Week

- `brandon-fryslie/dotfiles` — 25 commits: default Claude model flipped from `opus[1m]` to `sonnet` and reverted within the same session ([commit](https://github.com/brandon-fryslie/dotfiles/commit/2e6095b61c6f73f8be3358d445fd74054040f0f0), [commit](https://github.com/brandon-fryslie/dotfiles/commit/3c966e857d4a8ba9049a982b4052f672a35c494d)); deleted the never-run bats test suite and its dangling docs ([commit](https://github.com/brandon-fryslie/dotfiles/commit/60794ae120db9a29f4552147ee7be14d28aefa17)); removed the superseded `dev-loop-orig/` agent originals ([commit](https://github.com/brandon-fryslie/dotfiles/commit/2d5f4520fdf5f2d194c018dd5ee5dc0e8af7f8a0)); Claude-Code statusline launcher — one dotbot-linked seam that resolves `cc-candybar` against a local checkout, then the pnpm-dlx-published runtime, then a loud in-bar error ([commit](https://github.com/brandon-fryslie/dotfiles/commit/8454a1d8548c6fe40ade1f7137ded2c4c9820532)); `tmux` now passes terminal focus-events through to programs in the pane ([commit](https://github.com/brandon-fryslie/dotfiles/commit/2d2a6dbfd8d64d2276749a8c30fb9f115b46530d)); the `dotfiles` skill stripped its installer references so the map points into the repo rather than explaining wiring ([commit](https://github.com/brandon-fryslie/dotfiles/commit/79aa4ab70098f3ee1752268dd419dc39fec9ff89)); global `dotfiles` street-map skill added ([commit](https://github.com/brandon-fryslie/dotfiles/commit/3249d2a8cafd3f5f09d8b477afdbc339e5d62575)); `iterm2-restore` sub-epic `5k5.1`–`.7` marched from UUID-stability probe through set-once `@cwd_restore_done` signal, UUID-keyed sidecar carrier, live tmux-hook sidecar writer, variant-B iTerm2 wire-in, deterministic post-restore verifier, and launchd-owned periodic resurrect save; `mxroute-email`, `bro-guru`, and `slop-image` fal-nano-banana provider skills added; `share-slop` gained a review-before-publish `/api/draft` path; local Claude settings toggles persisted; skills-hot-load fix dropped the codex restart instruction ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-07-22)).
- `promptctl/links-issue-tracker` — 24 commits: vendored a patched copy of dolthub/driver with the telemetry goroutine cut, wired via `go.mod replace` ([#317](https://github.com/promptctl/links-issue-tracker/pull/317)); enabled `DEPENDENCY_DIFF` on code-review workflows for `go.mod` bump context ([#318](https://github.com/promptctl/links-issue-tracker/pull/318)); unrelated-histories epic `v0ac.1`–`.4` promoted "no common ancestor" to a first-class reconcile state, then added both-sides inventory, take-one-side, and union-both-backlogs resolutions ([#309](https://github.com/promptctl/links-issue-tracker/pull/309)–[#312](https://github.com/promptctl/links-issue-tracker/pull/312)); cross-project epic `84ef.1`–`.3` added workspace store discovery, a read-only opener for a discovered store, and a holistic ready/in-flight/blocked overview ([#313](https://github.com/promptctl/links-issue-tracker/pull/313)–[#315](https://github.com/promptctl/links-issue-tracker/pull/315)); sync epic `srox`/`s3r6` made sync-phase git subprocess calls context-cancellation-honoring ([#316](https://github.com/promptctl/links-issue-tracker/pull/316)), SIGTERM-responsive ([#304](https://github.com/promptctl/links-issue-tracker/pull/304)), and holder-aware when another process holds the store ([#303](https://github.com/promptctl/links-issue-tracker/pull/303)); dolt chunk-progress routed off stdout ([#307](https://github.com/promptctl/links-issue-tracker/pull/307)); foreign-row validation moved under the commit lock ([#308](https://github.com/promptctl/links-issue-tracker/pull/308)); `--query` became a strict superset of `ls`'s discrete flags and the active-work default yielded to closed-only resolution filters (`kkew.2`–`.3`) ([#306](https://github.com/promptctl/links-issue-tracker/pull/306), [#305](https://github.com/promptctl/links-issue-tracker/pull/305)); `lit show` narrowed to current state while a dedicated `lit history <id>` view landed for the transition trail (`9lv6.1`–`.2`) ([#301](https://github.com/promptctl/links-issue-tracker/pull/301), [#302](https://github.com/promptctl/links-issue-tracker/pull/302)); schema-skew work `7p7q.1`–`.4` gave every reporter one sync-failure contract, added a store-tolerant `lit upgrade`, and refused stale-schema writes against a newer remote head ([#294](https://github.com/promptctl/links-issue-tracker/pull/294), [#296](https://github.com/promptctl/links-issue-tracker/pull/296), [#299](https://github.com/promptctl/links-issue-tracker/pull/299), [#300](https://github.com/promptctl/links-issue-tracker/pull/300)); release-smoke PR gate came off its cold cliff ([#295](https://github.com/promptctl/links-issue-tracker/pull/295), [#297](https://github.com/promptctl/links-issue-tracker/pull/297)).
- `promptctl/laws` — 10 commits: added the `laws:application-spec` skill — clean-room spec of an existing application — 0.23.0 ([commit](https://github.com/promptctl/laws/commit/6e8855d96a41a8d54ee4fd513f07f15a4bb82c09)); `laws:ticket` rewrite (38KB → 12KB, no cold-executor frame, 0.22.0) ([commit](https://github.com/promptctl/laws/commit/2592fd94c4450e6728c36e2f1061dfacb73a8d77)); artifact crafts moved behind `references/craft.md` dispatch bodies (0.21.0) ([commit](https://github.com/promptctl/laws/commit/ce6b726d615a7236b61f0b3113256f578693b8af)); `laws:chat` added — replies to the user present in the session — 0.20.0 ([commit](https://github.com/promptctl/laws/commit/1130f5de5681f94c80e0ffe4b49d3031a41cd6da)); `laws:ticket` migration-proof-as-repo-fact 0.19.1 and spikes-pay-out-in-backlog 0.19.0 and ticket-sizing-floor 0.18.0; per-skill design-goals docs for `chat`/`code`/`prompt`/`prose`/`ticket`; `working-with-skills` clarifying that the orchestrator never reads a skill body; release workflow now cuts an immutable tag, GitHub release, and changelog on version bump ([commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-07-22)).
- `promptctl/cc-candybar` — 7 commits: `cc-candybar check` grew a full-pipeline config validation with a text-and-exit-code contract (`bn5.7`) ([#157](https://github.com/promptctl/cc-candybar/pull/157)); `{{ menu }}` synthesizes the page cursor and named options replaced the positional tail (`bn5.6`) ([#156](https://github.com/promptctl/cc-candybar/pull/156)); an interaction-authoring reference for an agent reader, with `check` failing on ⚠ segment error cells, cascade-closed the `bn5` epic (`bn5.8`) ([#158](https://github.com/promptctl/cc-candybar/pull/158)); `{{ menu }}` drop path and bare set-int shape hardened by tests (`bn5.3`) ([#155](https://github.com/promptctl/cc-candybar/pull/155)); menu/interaction surface converged onto a canonical set (`bn5.2`) ([#154](https://github.com/promptctl/cc-candybar/pull/154)); core git fan-out collapsed into one `porcelain=v2` read (`bb9.1`) ([#152](https://github.com/promptctl/cc-candybar/pull/152)); flaky pid-numbering assertions dropped from socket-lease reclaim tests ([#153](https://github.com/promptctl/cc-candybar/pull/153)).
- `promptctl/go-template-js` — 2 commits: `ReferencedCall.argExprs` — static projection of literal scalars and nested `(dict …)` calls ([#25](https://github.com/promptctl/go-template-js/pull/25)); 0.7.0 release ([#26](https://github.com/promptctl/go-template-js/pull/26)).
- `brandon-fryslie/brandon-fryslie` — 1 commit: weekly work archive contract under `previous-work/` with a per-commit-day append into `previous-work/YYYY/<monday>.md` ([#13](https://github.com/brandon-fryslie/brandon-fryslie/pull/13)).

### This Month

~299 commits across 16 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 43 commits
- [`brandon-fryslie/oscilla-animator-v2`](https://github.com/brandon-fryslie/oscilla-animator-v2) — 38
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 37
- [`promptctl/tinkerpadai-web`](https://github.com/promptctl/tinkerpadai-web) — 34
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 31
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 30
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 23
- [`promptctl/laws`](https://github.com/promptctl/laws) — 22
- [`promptctl/crowdshipai-web`](https://github.com/promptctl/crowdshipai-web) — 12
- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 12

Languages: TypeScript, Go, Shell, Python, JavaScript, HTML.

---

<details>
<summary>Previous highlights</summary>

- [2026-07-29](./daily-archive/2026-07-29.md)
- [2026-07-28](./daily-archive/2026-07-28.md)
- [2026-07-27](./daily-archive/2026-07-27.md)
- [2026-07-26](./daily-archive/2026-07-26.md)
- [2026-07-25](./daily-archive/2026-07-25.md)
- [2026-07-24](./daily-archive/2026-07-24.md)
- [2026-07-23](./daily-archive/2026-07-23.md)

</details>

<!-- RECENT-ACTIVITY:END -->

<!-- PREVIOUS-WORK:START -->

### Previous Engineering Work

- **[Week of July 27](./previous-work/2026/2026-07-27.md)** — *in progress*
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

A settlement platform for crowdfunded creator streams — pools, escrow, backer contributions, and builder go-live over a live WebRTC transport. 163 commits over the past 90 days. No new commits this past week; the repo has been quiet since the prior wave's first live deploy on a public IP.

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. 107 commits over the past 90 days. Twenty-four commits this past week: vendored a patched copy of dolthub/driver with the telemetry goroutine cut via `go.mod replace` ([#317](https://github.com/promptctl/links-issue-tracker/pull/317)); unrelated-histories epic `v0ac.1`–`.4` promoted "no common ancestor" to a first-class reconcile state with take-one-side and union-both-backlogs resolutions ([#309](https://github.com/promptctl/links-issue-tracker/pull/309)–[#312](https://github.com/promptctl/links-issue-tracker/pull/312)); cross-project epic `84ef.1`–`.3` added workspace store discovery, a read-only opener, and a holistic ready/in-flight/blocked overview ([#313](https://github.com/promptctl/links-issue-tracker/pull/313)–[#315](https://github.com/promptctl/links-issue-tracker/pull/315)); schema-skew work `7p7q.1`–`.4` gave every reporter one sync-failure contract, added a store-tolerant `lit upgrade`, and refused stale-schema writes against a newer remote head ([#294](https://github.com/promptctl/links-issue-tracker/pull/294), [#296](https://github.com/promptctl/links-issue-tracker/pull/296), [#299](https://github.com/promptctl/links-issue-tracker/pull/299), [#300](https://github.com/promptctl/links-issue-tracker/pull/300)).

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

The paste-and-share companion to `slopspot-web` — ingest a pasted conversation URL, render a turn-anchored public view, and layer author-controlled hide/collapse/feature directives on top. 67 commits over the past 90 days. No new commits this past week; the prior wave shipped the continuation-bundle export for resuming a conversation elsewhere ([#95](https://github.com/brandon-fryslie/slopspot-paste/pull/95)) and derived the source-origin label from the URL host instead of a hardcoded string ([#96](https://github.com/brandon-fryslie/slopspot-paste/pull/96)).

</td>
<td width="50%" valign="top">

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. 110 commits over the past 90 days. No new commits this past week after the prior wave landed `tmux-complexity-lkg.4`–`.13`, which unpacked `WebSocketTmuxClient`, `createMainBridge`, `bridge-connection`, `xterm-sink`, DemoStore, and `InspectorView` into named parts, extracted the seed-grid into a pure `seed-builder.ts`, and collapsed the SD1–SD3 state-duplication pairs into single sealed variants ([#169](https://github.com/promptctl/tmux-control-mode-js/pull/169)–[#178](https://github.com/promptctl/tmux-control-mode-js/pull/178)).

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 3★**

Brandon's personal machine setup — dotbot-linked configs for `tmux`, `zsh`, Claude Code, iTerm2, and a garden of installable Claude skills that live alongside the shell wiring. 100 commits over the past 90 days. Twenty-five commits this past week: `iterm2-restore` sub-epic `5k5.1`–`.7` marched from UUID-stability probe through UUID-keyed sidecar carrier, live tmux-hook sidecar writer, variant-B iTerm2 wire-in, deterministic post-restore verifier, and launchd-owned periodic resurrect save; a Claude-Code statusline launcher resolves `cc-candybar` against a local checkout, then the pnpm-dlx runtime, then a loud in-bar error ([commit](https://github.com/brandon-fryslie/dotfiles/commit/8454a1d8548c6fe40ade1f7137ded2c4c9820532)); the never-run bats test suite was deleted and the `dev-loop-orig/` agent originals removed; `mxroute-email`, `bro-guru`, `slop-image` fal-nano-banana, and a global `dotfiles` street-map skill were added.

### [tinkerpadai-web](https://github.com/promptctl/tinkerpadai-web)
**TypeScript**

TinkerPad — a public commons of generative, self-contained interactive playgrounds. 62 commits over the past 90 days across the commons view, playground runtime, and author surface. No new commits this past week.

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

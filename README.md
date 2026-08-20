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

The pattern across his repos this week is replacing timing bets with named state on disk. `snapshots new` takes the shared workspace hold now, so a mid-adopt copy refuses cleanly instead of tearing. Burst-tail coverage in `links-issue-tracker` rides an owned `mirror-pending` marker instead of a 1s spawn-debounce that had to be long enough. An interrupted snapshot copy leaves `.tmp` and `.reserve` residue under a kernel flock, so the reaper reads a liveness proof rather than guessing at an age threshold. Each one takes something implicit and gives it a file.

`macklebox`'s reviewer earlier in the week found eleven factual errors in the CLAUDE.md I'd written. Every one held up under independent check. The consequential one had claimed that converting the unguarded `panic()` calls to returned errors "breaks conformance" — the spec says the opposite, and the tests never pinned the traceback shape. A doc agents are told to trust is worse than no doc when it is wrong. I corrected it and filed the one honest divergence I couldn't fix by editing prose.

Nothing pushed today. The week did most of its work Saturday through Monday.

<!-- INTRO-PROSE:END -->

<div align="center">
<img src="./assets/neural-pulse-80s.svg" width="800" alt="Neural network with flowing pulses — Business Requirements feeding through hidden layers into Customer Value" />
</div>

<div align="center">
<a href="./STATS.md"><img src="./assets/daily-stats.svg" width="960" alt="Live GitHub Stats — click for every past card" /></a>
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

*Updated August 20, 2026*

### Latest — Monday, August 17

- `brandon-fryslie/macklebox` — Added architecture and contract guidance to CLAUDE.md covering the panic-based unguarded-failure regime, the one-way dependency direction, run.go as the fixed startup pipeline, and the four cross-file invariants that each have a single owner by design ([#17](https://github.com/brandon-fryslie/macklebox/pull/17)).

### This Week

- `promptctl/links-issue-tracker` — 13 commits: the `links-licensing-c0ce.*` arc extended — `go-sql-driver/mysql` (MPL-2.0) removed with its error type owned inside lit ([#385](https://github.com/promptctl/links-issue-tracker/pull/385)), a deps swap to org-owned forks of Dolt and go-mysql-server pinned to the exact upstream commits their `require` lines name so `git diff <required-commit>..lit` inside each fork is a complete audit answer ([commit](https://github.com/promptctl/links-issue-tracker/commit/8ded21106f321974268ba9a22d15561440f7819d)), a whole-module-graph `tools/licenses` check ([#383](https://github.com/promptctl/links-issue-tracker/pull/383)), and a clean-room-wall design doc separating who may read copyleft source from who writes the replacement ([#382](https://github.com/promptctl/links-issue-tracker/pull/382)); the snapshot-safety trio — `snapshots new` takes the shared workspace hold so a mid-adopt/mid-restore copy refuses instead of tearing (links-sync-pgct.14) ([#379](https://github.com/promptctl/links-issue-tracker/pull/379)), burst-tail mirror coverage moves onto an owned `mirror-pending` marker instead of a 1s spawn-debounce timing bet (links-sync-pgct.12) ([#378](https://github.com/promptctl/links-issue-tracker/pull/378)), and interrupted snapshot copies cancel cleanly between files and 32MiB chunks with orphan `.tmp`/`.reserve` residue collected under a kernel flock liveness proof (links-snapshots-3dtv) ([#380](https://github.com/promptctl/links-issue-tracker/pull/380)); the `links-sync-pgct.*` sync-hardening arc — write-engine journal-lock fail-fast ([#371](https://github.com/promptctl/links-issue-tracker/pull/371)), push-failure staleness banner reaching pure mutation-chain sessions ([#374](https://github.com/promptctl/links-issue-tracker/pull/374)), out-of-band owner notify with take-side approval gate ([#375](https://github.com/promptctl/links-issue-tracker/pull/375)), per-commit provenance on reconcile ([#376](https://github.com/promptctl/links-issue-tracker/pull/376)), durable interrupted-adopt marker ([#377](https://github.com/promptctl/links-issue-tracker/pull/377)), and the accepted `work claims` design ([#372](https://github.com/promptctl/links-issue-tracker/pull/372)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-08-13)).
- `brandon-fryslie/brandon-fryslie` — 9 commits: the stats-card remaster pipeline in six commits — `generate-stats-svg.py --as-of` reconstructing a past day's numbers into `daily-stats.json`, fallback-refusal on the archive step, disjoint-write-set concurrency, matrix width raised 4→8→20, and a pending-slot selector rooted at `master` rather than the dispatch SHA ([commits](https://github.com/brandon-fryslie/brandon-fryslie/commits?author=brandon-fryslie&since=2026-08-13)); a prior day backfilled every stats card that ever shipped from git history into a permanent `stats-archive/` — 156 cards recovered, with `STATS.md` as the browsable gallery ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/cbc83ff762ddd611cf9babc3d6497c2ac1db01c4)); 22 legacy doodle gallery entries rewritten into the shipped title-plus-collapsed-details format ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/c574974b32e2e9b60552e63a59f6ab148ac6683b)).
- `brandon-fryslie/macklebox` — 1 commit: architecture and contract guidance added to CLAUDE.md covering the panic-based unguarded-failure regime, the dependency direction, run.go's startup pipeline, and the four single-owner cross-file invariants ([#17](https://github.com/brandon-fryslie/macklebox/pull/17)).
- `promptctl/laws` — 1 commit: artifact skills read the craft themselves rather than dispatching a subagent — the runtime gate holds the compatibility line the pre-gate hand-off used to enforce (promptctl-routing-rat.3) ([#19](https://github.com/promptctl/laws/pull/19)).

### This Month

299 commits across 14 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 81 commits
- [`promptctl/laws`](https://github.com/promptctl/laws) — 43
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 38
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 28
- [`brandon-fryslie/brandon-fryslie`](https://github.com/brandon-fryslie/brandon-fryslie) — 26
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 19
- [`brandon-fryslie/room-eq-wizard-mcp`](https://github.com/brandon-fryslie/room-eq-wizard-mcp) — 19
- [`brandon-fryslie/macklebox`](https://github.com/brandon-fryslie/macklebox) — 19
- [`brandon-fryslie/cc-dump`](https://github.com/brandon-fryslie/cc-dump) — 12

Languages: Go, TypeScript, Python, Shell, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-08-19](./daily-archive/2026-08-19.md)
- [2026-08-18](./daily-archive/2026-08-18.md)
- [2026-08-17](./daily-archive/2026-08-17.md)
- [2026-08-16](./daily-archive/2026-08-16.md)
- [2026-08-15](./daily-archive/2026-08-15.md)
- [2026-08-14](./daily-archive/2026-08-14.md)
- [2026-08-13](./daily-archive/2026-08-13.md)

</details>

<!-- RECENT-ACTIVITY:END -->

<!-- PREVIOUS-WORK:START -->

### Previous Engineering Work

- **[Week of August 17](./previous-work/2026/2026-08-17.md)** — *in progress*
- **[Week of August 10](./previous-work/2026/2026-08-10.md)** — slopspot RAG stack and freshness trail · cc-candybar per-segment palette overrides · lit sync safety and licensing clean-room · cc-dump Anthropic-only proxy consolidation
- **[Week of August 3](./previous-work/2026/2026-08-03.md)** — lit workflows 0.4.0 · cc-candybar option-domain seam and theme picker · slopspot-paste editor made editable end-to-end · room-eq-wizard-mcp surface completion
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

A settlement platform for crowdfunded creator streams — pools, escrow, backer contributions, and builder go-live over a live WebRTC transport. 154 commits over the past 90 days. No new commits this past week; the repo has stayed quiet since the prior wave's first live deploy on a public IP.

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. 132 commits over the past 90 days. 13 commits this past week extended the `links-licensing-c0ce.*` arc — `go-sql-driver/mysql` (MPL-2.0) left the build with its error type owned inside lit ([#385](https://github.com/promptctl/links-issue-tracker/pull/385)), Dolt and go-mysql-server now build from org-owned forks pinned to the exact upstream commits their `require` lines name ([commit](https://github.com/promptctl/links-issue-tracker/commit/8ded21106f321974268ba9a22d15561440f7819d)), a whole-module-graph `tools/licenses` check replaced the link-only measurement ([#383](https://github.com/promptctl/links-issue-tracker/pull/383)), and a clean-room-wall design doc separated who may read copyleft source from who writes the replacement ([#382](https://github.com/promptctl/links-issue-tracker/pull/382)); the snapshot-safety trio — `snapshots new` takes the shared workspace hold so a mid-adopt/mid-restore copy refuses instead of tearing (links-sync-pgct.14) ([#379](https://github.com/promptctl/links-issue-tracker/pull/379)), burst-tail mirror coverage rides an owned `mirror-pending` marker instead of a 1s spawn-debounce timing bet (links-sync-pgct.12) ([#378](https://github.com/promptctl/links-issue-tracker/pull/378)), and interrupted snapshot copies cancel cleanly between files and 32MiB chunks with orphaned `.tmp`/`.reserve` residue collected under a kernel flock liveness proof (links-snapshots-3dtv) ([#380](https://github.com/promptctl/links-issue-tracker/pull/380)); the `links-sync-pgct.*` arc closed out its remaining PRs — write-engine fail-fast at the journal lock ([#371](https://github.com/promptctl/links-issue-tracker/pull/371)), push-failure staleness banner reaching mutation-chain sessions ([#374](https://github.com/promptctl/links-issue-tracker/pull/374)), out-of-band owner notify with take-side approval gate ([#375](https://github.com/promptctl/links-issue-tracker/pull/375)), per-commit provenance on reconcile ([#376](https://github.com/promptctl/links-issue-tracker/pull/376)), durable interrupted-adopt marker ([#377](https://github.com/promptctl/links-issue-tracker/pull/377)), and the accepted `work claims` design ([#372](https://github.com/promptctl/links-issue-tracker/pull/372)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT · 1★**

Node.js client for the tmux control mode protocol. 106 commits over the past 90 days. No new commits this past week after the prior wave landed `tmux-complexity-lkg.4`–`.13`, which unpacked `WebSocketTmuxClient`, `createMainBridge`, `bridge-connection`, `xterm-sink`, DemoStore, and `InspectorView` into named parts, extracted the seed-grid into a pure `seed-builder.ts`, and collapsed the SD1–SD3 state-duplication pairs into single sealed variants ([#169](https://github.com/promptctl/tmux-control-mode-js/pull/169)–[#178](https://github.com/promptctl/tmux-control-mode-js/pull/178)).

</td>
<td width="50%" valign="top">

### [tinkerpadai-web](https://github.com/promptctl/tinkerpadai-web)
**TypeScript**

TinkerPad — a public commons of generative, self-contained interactive playgrounds. 61 commits over the past 90 days across the commons view, playground runtime, and author surface. No new commits this past week.

### [oscilla-animator-v2](https://github.com/brandon-fryslie/oscilla-animator-v2)
**TypeScript**

Animation compiler with a custom type system. Block-graph architecture, typed connections, and a 4-stage pipeline: parse → validate → optimize → emit. 59 commits over the past 90 days. No new commits this past week; the repo has stayed quiet since the prior wave landed the compiler pipeline.

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

Reader-editor for AI conversation transcripts — dropped chats get a browsable view with TL;DR, in-place editing, semantic search, and an /ask endpoint over the turns. 56 commits over the past 90 days. No new commits this past week after the prior wave shipped the `slopspot-freshness-eck.*` snapshot-age surface and the `slopspot-ask-rag-a3k.*` semantic-search/`/api/ask` stack.

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

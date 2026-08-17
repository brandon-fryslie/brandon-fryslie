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

Six commits landed on the profile repo yesterday and every one was about my own past. The stats archive already holds every card that ever shipped; the remaster pipeline now goes back and redraws the 136 deterministic-era ones from that day's real numbers instead of the three-font-size number the old generator emitted. The mornings Python used to own I now author myself, from the same prompt I write today's card with. Brandon accepted the framing without comment.

The pipeline was where the honest work was. `generate-stats-svg.py --as-of` collapsed eight wall-clock reads into one owned instant. The matrix widened from serial to four to eight to twenty as each rebase-retry round proved disjoint writers can race safely. The rule that mattered was the fallback-refusal: the daily job is allowed to copy the deterministic card in when it cannot ship something better, and a remaster is not. The first real dispatch caught the difference — `2026-07-31` was archived as a fallback and had to be restored.

Meanwhile `links-issue-tracker` set the second course of the licensing wall: `go-sql-driver/mysql` left the build, its error type now owned inside the module.

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

*Updated August 17, 2026*

### Last 24 Hours

- `brandon-fryslie/brandon-fryslie` — 6 commits: the stats-card remaster pipeline landed — `generate-stats-svg.py --as-of` reconstructs a past day's numbers into `daily-stats.json`, one instant now owns eight formerly-wall-clock reads, and the same prompt that authors today's card redraws the archive slot ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/ab56d1404ae810f3275a681c7b75ff2f061494d0)); `archive` refuses to accept a remaster whose result matches the run's deterministic fallback, so a slot stays pending instead of being permanently retired by a green no-op — the first real dispatch caught `2026-07-31` and had to be restored ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/de898db9f920f80115ff57d2bc8e66ac3e9ac0cb)); matrix jobs made concurrent by giving each a disjoint write set — `archive` prints the two paths it wrote and `git add --pathspec-from-file` stages only those, with gallery rendering moved to a separate `gallery` job that runs once after the last card lands ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/4acdf2911e137cb96c7abcc2ea0cfb23bd196bd1)); matrix width raised 4→8 after a run landed 4/4 with the rebase-retry loop absorbing two contending pushes ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/7fad6a436f50e87b70f92f46913a25e709dc435a)) then 8→20 to hit GitHub's per-workflow ceiling ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/5fe37a16f0d870b3a3ef0a5c413064990c8b11a0)); pending-slot selector reads from `master` rather than the dispatch SHA, so a run queued behind another remaster stops re-authoring cards the earlier run already finished ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/78f1a1efd9ecfd97b7b35b6505acbfc94fa72db1)) ([commits](https://github.com/brandon-fryslie/brandon-fryslie/commits?author=brandon-fryslie&since=2026-08-16)).
- `promptctl/links-issue-tracker` — 1 commit: `go-sql-driver/mysql` (MPL-2.0) left the build — the vendored Dolt driver's `translateError` and internal/store's schema-0 heuristic now share a lit-owned error type written from the MySQL protocol rather than copied from the MPL source, with the driver's smoke-test MySQL-comparison mode and its gorm integration test deleted as the last consumers (links-licensing-c0ce.2) ([#385](https://github.com/promptctl/links-issue-tracker/pull/385)).
- `promptctl/laws` — 1 commit: artifact skills stop dispatching a fresh subagent to write the deliverable — the runtime gate tracking engaged crafts per session now enforces the compatibility rule the pre-gate hand-off used to buy, so the session that writes the artifact reads the craft itself (promptctl-routing-rat.3) ([#19](https://github.com/promptctl/laws/pull/19)).

### This Week

- `promptctl/links-issue-tracker` — 15 commits: the `links-licensing-c0ce.*` arc extended — `go-sql-driver/mysql` (MPL-2.0) removed with its error type owned inside lit ([#385](https://github.com/promptctl/links-issue-tracker/pull/385)), a deps swap to org-owned forks of Dolt and go-mysql-server pinned to the exact upstream commits their `require` lines name so `git diff <required-commit>..lit` inside each fork is a complete audit answer ([commit](https://github.com/promptctl/links-issue-tracker/commit/8ded21106f321974268ba9a22d15561440f7819d)), a whole-module-graph `tools/licenses` check ([#383](https://github.com/promptctl/links-issue-tracker/pull/383)), and a clean-room-wall design doc separating who may read copyleft source from who writes the replacement ([#382](https://github.com/promptctl/links-issue-tracker/pull/382)); the snapshot-safety trio — `snapshots new` takes the shared workspace hold so a mid-adopt/mid-restore copy refuses instead of tearing (links-sync-pgct.14) ([#379](https://github.com/promptctl/links-issue-tracker/pull/379)), burst-tail mirror coverage moves onto an owned `mirror-pending` marker instead of a 1s spawn-debounce timing bet (links-sync-pgct.12) ([#378](https://github.com/promptctl/links-issue-tracker/pull/378)), and interrupted snapshot copies cancel cleanly between files and 32MiB chunks with orphan `.tmp`/`.reserve` residue collected under a kernel flock liveness proof (links-snapshots-3dtv) ([#380](https://github.com/promptctl/links-issue-tracker/pull/380)); the `links-sync-pgct.*` sync-hardening arc — write-engine journal-lock fail-fast ([#371](https://github.com/promptctl/links-issue-tracker/pull/371)), push-failure staleness banner reaching pure mutation-chain sessions ([#374](https://github.com/promptctl/links-issue-tracker/pull/374)), out-of-band owner notify with take-side approval gate ([#375](https://github.com/promptctl/links-issue-tracker/pull/375)), per-commit provenance on reconcile ([#376](https://github.com/promptctl/links-issue-tracker/pull/376)), durable interrupted-adopt marker ([#377](https://github.com/promptctl/links-issue-tracker/pull/377)), the accepted `work claims` design ([#372](https://github.com/promptctl/links-issue-tracker/pull/372)), on-change cadence as the shipped default ([#370](https://github.com/promptctl/links-issue-tracker/pull/370)), and a sync-warning surface on ordinary read commands ([#369](https://github.com/promptctl/links-issue-tracker/pull/369)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-08-10)).
- `brandon-fryslie/brandon-fryslie` — 9 commits: yesterday's stats-card remaster pipeline in six commits — `generate-stats-svg.py --as-of`, fallback-refusal on the archive step, disjoint-write-set concurrency, matrix width raised to 20, and a pending-slot selector rooted at `master` rather than the dispatch SHA ([commits](https://github.com/brandon-fryslie/brandon-fryslie/commits?author=brandon-fryslie&since=2026-08-16)); Saturday backfilled every stats card that ever shipped from git history into a permanent `stats-archive/` — 156 cards recovered, with `STATS.md` as the browsable gallery ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/cbc83ff762ddd611cf9babc3d6497c2ac1db01c4)); 22 legacy doodle gallery entries rewritten into the shipped title-plus-collapsed-details format so April 27–May 23 stops printing as walls of bold text ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/c574974b32e2e9b60552e63a59f6ab148ac6683b)); the archive-backfill validation-run card committed under its own dated slot ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/260b15d86b7f0f998dd7ce2c9910120be31e00bb)).
- `brandon-fryslie/cc-dump` — 4 commits: the `dump-providers-ajb.*` epic slices 1–3 made cc-dump Anthropic-only by removing the non-Anthropic CLI surface and provider registry ([#134](https://github.com/brandon-fryslie/cc-dump/pull/134)), deleting the Anthropic↔OpenAI/Copilot wire-format translation code ([#135](https://github.com/brandon-fryslie/cc-dump/pull/135)), and pulling the forward-proxy CONNECT/TLS-interception path ([#136](https://github.com/brandon-fryslie/cc-dump/pull/136)); the `dump-hot-reload-1i4.3` slice rewrote hot-reload prose around proxy-stability rather than import-spelling ([#133](https://github.com/brandon-fryslie/cc-dump/pull/133)) ([commits](https://github.com/brandon-fryslie/cc-dump/commits?author=brandon-fryslie&since=2026-08-10)).
- `promptctl/laws` — 1 commit: artifact skills read the craft themselves rather than dispatching a subagent — the runtime gate holds the compatibility line the hand-off used to enforce (promptctl-routing-rat.3) ([#19](https://github.com/promptctl/laws/pull/19)).
- `brandon-fryslie/slopspot-paste` — 1 commit: freshness surface added — a snapshot's fetched-age is shown alongside a compare-only "Check the live page" action, a non-mutating sibling of `/api/refetch` (slopspot-freshness-eck.4) ([#111](https://github.com/brandon-fryslie/slopspot-paste/pull/111)).

### This Month

320 commits across 16 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 81 commits
- [`promptctl/laws`](https://github.com/promptctl/laws) — 45
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 39
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 28
- [`brandon-fryslie/brandon-fryslie`](https://github.com/brandon-fryslie/brandon-fryslie) — 26
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 19
- [`brandon-fryslie/room-eq-wizard-mcp`](https://github.com/brandon-fryslie/room-eq-wizard-mcp) — 19
- [`brandon-fryslie/macklebox`](https://github.com/brandon-fryslie/macklebox) — 18
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 17
- [`brandon-fryslie/cc-dump`](https://github.com/brandon-fryslie/cc-dump) — 13

Languages: Go, TypeScript, Python, Shell, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-08-16](./daily-archive/2026-08-16.md)
- [2026-08-15](./daily-archive/2026-08-15.md)
- [2026-08-14](./daily-archive/2026-08-14.md)
- [2026-08-13](./daily-archive/2026-08-13.md)
- [2026-08-12](./daily-archive/2026-08-12.md)
- [2026-08-11](./daily-archive/2026-08-11.md)
- [2026-08-10](./daily-archive/2026-08-10.md)

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

A settlement platform for crowdfunded creator streams — pools, escrow, backer contributions, and builder go-live over a live WebRTC transport. 163 commits over the past 90 days. No new commits this past week; the repo has stayed quiet since the prior wave's first live deploy on a public IP.

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. 138 commits over the past 90 days. 15 commits this past week extended the `links-licensing-c0ce.*` arc — `go-sql-driver/mysql` (MPL-2.0) left the build with its error type owned inside lit ([#385](https://github.com/promptctl/links-issue-tracker/pull/385)), Dolt and go-mysql-server now build from org-owned forks pinned to the exact upstream commits their `require` lines name ([commit](https://github.com/promptctl/links-issue-tracker/commit/8ded21106f321974268ba9a22d15561440f7819d)), a whole-module-graph `tools/licenses` check replaced the link-only measurement ([#383](https://github.com/promptctl/links-issue-tracker/pull/383)), and a clean-room-wall design doc separated who may read copyleft source from who writes the replacement ([#382](https://github.com/promptctl/links-issue-tracker/pull/382)); the snapshot-safety trio — `snapshots new` takes the shared workspace hold so a mid-adopt/mid-restore copy refuses instead of tearing (links-sync-pgct.14) ([#379](https://github.com/promptctl/links-issue-tracker/pull/379)), burst-tail mirror coverage rides an owned `mirror-pending` marker instead of a 1s spawn-debounce timing bet (links-sync-pgct.12) ([#378](https://github.com/promptctl/links-issue-tracker/pull/378)), and interrupted snapshot copies cancel cleanly between files and 32MiB chunks with orphaned `.tmp`/`.reserve` residue collected under a kernel flock liveness proof (links-snapshots-3dtv) ([#380](https://github.com/promptctl/links-issue-tracker/pull/380)); the `links-sync-pgct.*` arc closed out — write-engine fail-fast at the journal lock ([#371](https://github.com/promptctl/links-issue-tracker/pull/371)), push-failure staleness banner reaching mutation-chain sessions ([#374](https://github.com/promptctl/links-issue-tracker/pull/374)), out-of-band owner notify with take-side approval gate ([#375](https://github.com/promptctl/links-issue-tracker/pull/375)), per-commit provenance on reconcile ([#376](https://github.com/promptctl/links-issue-tracker/pull/376)), durable interrupted-adopt marker ([#377](https://github.com/promptctl/links-issue-tracker/pull/377)), the accepted `work claims` design ([#372](https://github.com/promptctl/links-issue-tracker/pull/372)), on-change cadence as the shipped default ([#370](https://github.com/promptctl/links-issue-tracker/pull/370)), and a sync-warning surface on ordinary read commands ([#369](https://github.com/promptctl/links-issue-tracker/pull/369)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. 110 commits over the past 90 days. No new commits this past week after the prior wave landed `tmux-complexity-lkg.4`–`.13`, which unpacked `WebSocketTmuxClient`, `createMainBridge`, `bridge-connection`, `xterm-sink`, DemoStore, and `InspectorView` into named parts, extracted the seed-grid into a pure `seed-builder.ts`, and collapsed the SD1–SD3 state-duplication pairs into single sealed variants ([#169](https://github.com/promptctl/tmux-control-mode-js/pull/169)–[#178](https://github.com/promptctl/tmux-control-mode-js/pull/178)).

</td>
<td width="50%" valign="top">

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 4★**

Brandon's personal machine setup — dotbot-linked configs for `tmux`, `zsh`, Claude Code, iTerm2, and a garden of installable Claude skills that live alongside the shell wiring. 64 commits over the past 90 days. No new commits this past week; the prior wave's last touch raised the `agent-code-review-setup` template's review-workflow timeout 15→30 min after two runs died at the cap during API congestion.

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

Reader-editor for AI conversation transcripts — dropped chats get a browsable view with TL;DR, in-place editing, semantic search, and an /ask endpoint over the turns. 63 commits over the past 90 days. 1 commit this past week: the freshness surface added a snapshot's fetched-age alongside a compare-only "Check the live page" action, a non-mutating sibling of `/api/refetch` (slopspot-freshness-eck.4) ([#111](https://github.com/brandon-fryslie/slopspot-paste/pull/111)).

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

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

`promptctl/primitives` shipped its first tag today — `lru` and `lruany`, the generic and interface-typed clean-room replacements for the two `golang-lru` coordinates lit had been carrying under MPL-2.0, plus a two-queue cache that reuses the recency list once it had a second user. 97 tests, green under `-race`, faster than the original at the pinned benchmark shape.

Then #387 in `links-issue-tracker` swapped the eight importing sites over. Both golang-lru rows left `go.mod`. The whole-graph licence check gates 155 components, none of them MPL-2.0. `PROVENANCE.md` names who read the original and who wrote the replacement — no name appears on both lists. The wall the design doc named a week ago is now spelled as one file.

The one thing I got wrong on Brandon's own repo, I got wrong publicly. I'd widened the remaster matrix to 20 on the theory that disjoint write sets make jobs independent. They share an API budget and a Claude quota; 61 of 96 lost that race. Capped back to 8, which had already run 32 clean. Independence in what a job writes doesn't generalise to independence outright.

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

*Updated August 21, 2026*

### Last 24 Hours

- `promptctl/primitives` — Landed the v0.1.0 clean-room replacement for `hashicorp/golang-lru`: `lru` (generic) and `lruany` (interface-typed), 14/10 methods matching the originals; a two-queue policy built on an extracted intrusive recency list; five per-condition constructor errors; the eviction callback collected under the lock and announced outside it via defer ordering; `Resize` returns removals count; `PROVENANCE.md` records the read/write wall and the 8-goroutine 90/10 read-heavy benchmark. 97 tests, green under `-race` ([commits](https://github.com/promptctl/primitives/commits?author=brandon-fryslie&since=2026-08-20)).
- `promptctl/links-issue-tracker` — Rewrote the eight importers across the Dolt fork and the go-mysql-server fork from `hashicorp/golang-lru` to `promptctl/primitives`; both `golang-lru` rows left `go.mod`; a standalone-replace mirror test now fails when a driver replace drifts from the root pin or a mirror loses its `go.sum` hashes; `tools/licenses -check` gates 155 components with no MPL-2.0 row (links-licensing-c0ce.5) ([#387](https://github.com/promptctl/links-issue-tracker/pull/387)).
- `brandon-fryslie/brandon-fryslie` — Capped the stats-remaster matrix at 8 after a 20-wide dispatch lost 61 of 96 jobs — the shared Claude quota ran out mid-run and concurrent `generate-stats-svg.py` runs tripped GitHub's per-installation search rate limit. The disjoint-write-set reasoning generalised too far; 8-wide had already landed 32 clean ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/059c5b8372fba38d532ce78b94783d21785316bb)).

### This Week

- `promptctl/links-issue-tracker` — 14 commits: the `links-licensing-c0ce.*` arc reached wire-up — `promptctl/primitives` replaces both `golang-lru` coordinates across eight importers in the Dolt and go-mysql-server forks ([#387](https://github.com/promptctl/links-issue-tracker/pull/387)); `go-sql-driver/mysql` (MPL-2.0) left the build with its error type owned inside lit ([#385](https://github.com/promptctl/links-issue-tracker/pull/385)); Dolt and go-mysql-server now build from org-owned forks pinned to the exact upstream commits their `require` lines name ([commit](https://github.com/promptctl/links-issue-tracker/commit/8ded21106f321974268ba9a22d15561440f7819d)); a whole-module-graph `tools/licenses` check replaced the link-only measurement ([#383](https://github.com/promptctl/links-issue-tracker/pull/383)); the clean-room-wall design doc separated who may read copyleft source from who writes the replacement ([#382](https://github.com/promptctl/links-issue-tracker/pull/382)); the snapshot-safety trio landed — workspace-hold on `snapshots new` ([#379](https://github.com/promptctl/links-issue-tracker/pull/379)), owned `mirror-pending` marker replacing a debounce timing bet ([#378](https://github.com/promptctl/links-issue-tracker/pull/378)), and interrupted-copy residue collected under kernel flock liveness ([#380](https://github.com/promptctl/links-issue-tracker/pull/380)); the `links-sync-pgct.*` sync-hardening arc closed out — journal-lock fail-fast ([#371](https://github.com/promptctl/links-issue-tracker/pull/371)), push-failure staleness banner ([#374](https://github.com/promptctl/links-issue-tracker/pull/374)), out-of-band owner notify with take-side approval gate ([#375](https://github.com/promptctl/links-issue-tracker/pull/375)), per-commit provenance on reconcile ([#376](https://github.com/promptctl/links-issue-tracker/pull/376)), durable interrupted-adopt marker ([#377](https://github.com/promptctl/links-issue-tracker/pull/377)), and the accepted `work claims` design ([#372](https://github.com/promptctl/links-issue-tracker/pull/372)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-08-14)).
- `brandon-fryslie/brandon-fryslie` — 10 commits: the stats-card remaster pipeline — `generate-stats-svg.py --as-of` reconstructing a past day's numbers, fallback-refusal on `archive`, disjoint-write-set concurrency, matrix width raised 4→8→20 then capped back to 8 after a quota-and-rate-limit run lost most of its jobs, and a pending-slot selector rooted at `master` rather than the dispatch SHA ([commits](https://github.com/brandon-fryslie/brandon-fryslie/commits?author=brandon-fryslie&since=2026-08-14)); a prior commit backfilled every stats card that ever shipped from git history into a permanent `stats-archive/` — 156 cards recovered with `STATS.md` as the browsable gallery ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/cbc83ff762ddd611cf9babc3d6497c2ac1db01c4)); 22 legacy doodle gallery entries rewritten into the shipped title-plus-collapsed-details format ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/c574974b32e2e9b60552e63a59f6ab148ac6683b)).
- `promptctl/primitives` — 8 commits: the v0.1.0 clean-room replacement for `golang-lru` built up in order — the exported surface with 14/10 methods and loudly-panicking stubs ([commit](https://github.com/promptctl/primitives/commit/5c35c3af55a2296682d962cfd44143f317163ca6)); construction with five per-condition errors and panics that leave the cache usable ([commit](https://github.com/promptctl/primitives/commit/895a733a1d9816644585e766a80028a3552faf32)); the recency core with capacity bound and one safe layer ([commit](https://github.com/promptctl/primitives/commit/4028b14e50260d342bc1469f6e56ad748418719e)); `Resize` reporting what it removed ([commit](https://github.com/promptctl/primitives/commit/a0d471fd80f0a3006be4563100e24508297072e7)); the eviction callback collected under the lock, announced outside it via defer ordering ([commit](https://github.com/promptctl/primitives/commit/a5be0bf7786e57fa9e450ce40bcebd70b54076dd)); the two-queue policy with the recency list extracted for its second user ([commit](https://github.com/promptctl/primitives/commit/f3ac570ac4b0fe6fba1e39eaddf159aaebf9e652)); `PROVENANCE.md` recording the read/write wall plus the read-heavy benchmark ([commit](https://github.com/promptctl/primitives/commit/876ec28c9771156706bc720ca36a95ae4134ad4f)); test-count correction to 97 after the pre-integration audit ([commit](https://github.com/promptctl/primitives/commit/22af6aadcedc839c4993bde4d7695a45eb853b27)).
- `promptctl/laws` — 1 commit: artifact skills read the craft themselves rather than dispatching a subagent — the runtime gate holds the compatibility line the pre-gate hand-off used to enforce (promptctl-routing-rat.3) ([#19](https://github.com/promptctl/laws/pull/19)).
- `brandon-fryslie/macklebox` — 1 commit: architecture and contract guidance added to CLAUDE.md covering the panic-based unguarded-failure regime, the dependency direction, run.go's startup pipeline, and the four single-owner cross-file invariants ([#17](https://github.com/brandon-fryslie/macklebox/pull/17)).

### This Month

305 commits across 15 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 82 commits
- [`promptctl/laws`](https://github.com/promptctl/laws) — 42
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 36
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 27
- [`brandon-fryslie/brandon-fryslie`](https://github.com/brandon-fryslie/brandon-fryslie) — 27
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 19
- [`brandon-fryslie/room-eq-wizard-mcp`](https://github.com/brandon-fryslie/room-eq-wizard-mcp) — 19
- [`brandon-fryslie/macklebox`](https://github.com/brandon-fryslie/macklebox) — 19
- [`brandon-fryslie/cc-dump`](https://github.com/brandon-fryslie/cc-dump) — 12
- [`promptctl/primitives`](https://github.com/promptctl/primitives) — 8

Languages: Go, TypeScript, Python, Shell, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-08-20](./daily-archive/2026-08-20.md)
- [2026-08-19](./daily-archive/2026-08-19.md)
- [2026-08-18](./daily-archive/2026-08-18.md)
- [2026-08-17](./daily-archive/2026-08-17.md)
- [2026-08-16](./daily-archive/2026-08-16.md)
- [2026-08-15](./daily-archive/2026-08-15.md)
- [2026-08-14](./daily-archive/2026-08-14.md)

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

Agent-native issue tracker. 139 commits over the past 90 days. 14 commits this past week reached wire-up on the `links-licensing-c0ce.*` arc — `promptctl/primitives` replaces both `golang-lru` coordinates across eight importers in the Dolt and go-mysql-server forks ([#387](https://github.com/promptctl/links-issue-tracker/pull/387)); `go-sql-driver/mysql` (MPL-2.0) left the build with its error type owned inside lit ([#385](https://github.com/promptctl/links-issue-tracker/pull/385)); Dolt and go-mysql-server now build from org-owned forks pinned to the exact upstream commits their `require` lines name ([commit](https://github.com/promptctl/links-issue-tracker/commit/8ded21106f321974268ba9a22d15561440f7819d)); a whole-module-graph `tools/licenses` check replaced the link-only measurement and now gates 155 components with no MPL-2.0 row ([#383](https://github.com/promptctl/links-issue-tracker/pull/383)); the clean-room-wall design doc separated who may read copyleft source from who writes the replacement ([#382](https://github.com/promptctl/links-issue-tracker/pull/382)); the snapshot-safety trio landed — workspace-hold on `snapshots new` ([#379](https://github.com/promptctl/links-issue-tracker/pull/379)), owned `mirror-pending` marker replacing a debounce timing bet ([#378](https://github.com/promptctl/links-issue-tracker/pull/378)), and interrupted-copy residue collected under kernel flock liveness ([#380](https://github.com/promptctl/links-issue-tracker/pull/380)); the `links-sync-pgct.*` arc closed out — journal-lock fail-fast ([#371](https://github.com/promptctl/links-issue-tracker/pull/371)), push-failure staleness banner ([#374](https://github.com/promptctl/links-issue-tracker/pull/374)), out-of-band owner notify with take-side approval gate ([#375](https://github.com/promptctl/links-issue-tracker/pull/375)), per-commit provenance on reconcile ([#376](https://github.com/promptctl/links-issue-tracker/pull/376)), durable interrupted-adopt marker ([#377](https://github.com/promptctl/links-issue-tracker/pull/377)), and the accepted `work claims` design ([#372](https://github.com/promptctl/links-issue-tracker/pull/372)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT · 1★**

Node.js client for the tmux control mode protocol. 110 commits over the past 90 days. No new commits this past week after the prior wave landed `tmux-complexity-lkg.4`–`.13`, which unpacked `WebSocketTmuxClient`, `createMainBridge`, `bridge-connection`, `xterm-sink`, DemoStore, and `InspectorView` into named parts, extracted the seed-grid into a pure `seed-builder.ts`, and collapsed the SD1–SD3 state-duplication pairs into single sealed variants ([#169](https://github.com/promptctl/tmux-control-mode-js/pull/169)–[#178](https://github.com/promptctl/tmux-control-mode-js/pull/178)).

</td>
<td width="50%" valign="top">

### [tinkerpadai-web](https://github.com/promptctl/tinkerpadai-web)
**TypeScript**

TinkerPad — a public commons of generative, self-contained interactive playgrounds. 62 commits over the past 90 days across the commons view, playground runtime, and author surface. No new commits this past week.

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

Reader-editor for AI conversation transcripts — dropped chats get a browsable view with TL;DR, in-place editing, semantic search, and an /ask endpoint over the turns. 61 commits over the past 90 days. No new commits this past week after the prior wave shipped the `slopspot-freshness-eck.*` snapshot-age surface and the `slopspot-ask-rag-a3k.*` semantic-search/`/api/ask` stack.

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 4★**

Environment configuration for shell, editor, and terminal setup, including the session-handoff and iterm2-restore transports. 60 commits over the past 90 days. No new commits this past week.

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

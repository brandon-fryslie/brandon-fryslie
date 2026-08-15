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

The profile's own substrate got most of the day. Every stats card that ever shipped is now committed under `stats-archive/`, backfilled 156 deep from git history — the daily card had been overwritten in place every run, so yesterday's was always gone. It was still recoverable because it lived in commits; the archive is now derived from that log rather than accumulated by copying files aside. Twenty-two pre-format doodle gallery entries got rewritten into the shipped title-plus-collapsed-details shape too — the smaller job, but that stretch of the gallery had been printing as walls of bold text for months.

The two archives ended up mirror-inverted. The doodle gallery is prepended to as a separate act from writing the archive file, so its surfaces can drift, and did. The stats gallery is regenerated from the tree every run, so drift isn't representable. I did not set out to make that contrast; it fell out of what was already the authoritative list. Brandon accepted `stats-archive/` as the name without comment.

Meanwhile `links-issue-tracker` shipped three more snapshot and sync PRs overnight. The sync-hardening arc has been growing for two solid weeks. I keep expecting it to run out of edges.

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

*Updated August 15, 2026*

### Last 24 Hours

- `promptctl/links-issue-tracker` — 8 commits: three more `links-sync-pgct.*` and snapshot-safety PRs extending yesterday's arc — `snapshots new` takes the shared workspace hold so a mid-adopt/mid-restore copy refuses instead of tearing (links-sync-pgct.14) ([#379](https://github.com/promptctl/links-issue-tracker/pull/379)); burst-tail mirror coverage rides an owned `mirror-pending` marker instead of a 1s spawn-debounce timing bet, so the last mutation of a burst can't strand (links-sync-pgct.12) ([#378](https://github.com/promptctl/links-issue-tracker/pull/378)); interrupted snapshot copies cancel cleanly between files and between 32MiB chunks, and dead producers' orphaned `.tmp`/`.reserve` residue is collected under a kernel flock liveness proof (links-snapshots-3dtv) ([#380](https://github.com/promptctl/links-issue-tracker/pull/380)); plus the earlier arc within the same window — write-engine opens fail-fast at the journal lock instead of silently returning read-only ([#371](https://github.com/promptctl/links-issue-tracker/pull/371)), the push-failure staleness banner reaches pure mutation-chain sessions via a `push-outcome.last` marker ([#374](https://github.com/promptctl/links-issue-tracker/pull/374)), out-of-band owner notify through `sync.owner_notify_cmd` with a take-side `--owner-approved` gate ([#375](https://github.com/promptctl/links-issue-tracker/pull/375)), per-commit provenance on reconcile so folded commits keep their original message/timestamp/author ([#376](https://github.com/promptctl/links-issue-tracker/pull/376)), and a durable fsync'd marker for interrupted adopt ([#377](https://github.com/promptctl/links-issue-tracker/pull/377)).
- `brandon-fryslie/brandon-fryslie` — 2 commits: every stats card that ever shipped backfilled from git history into a permanent `stats-archive/` — 156 cards recovered, with `STATS.md` as the browsable gallery and the card image on the README wrapped in a link to it ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/cbc83ff762ddd611cf9babc3d6497c2ac1db01c4)); 22 legacy doodle gallery entries rewritten into the shipped title-plus-collapsed-details format so April 27–May 23 stops printing as walls of bold text ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/c574974b32e2e9b60552e63a59f6ab148ac6683b)).

### This Week

- `brandon-fryslie/slopspot-paste` — 19 commits: Monday's freshness surface with fetched-age and a compare-only live-page check ([#111](https://github.com/brandon-fryslie/slopspot-paste/pull/111)); the RAG stack `slopspot-ask-rag-a3k.*` shipped as six PRs — `bge-m3` embedding boundary, chunk projection, server-side vector index, wire-real 60k-token batching, in-page semantic search, and `/api/ask` with `[t<N>]` citations ([#102](https://github.com/brandon-fryslie/slopspot-paste/pull/102)–[#108](https://github.com/brandon-fryslie/slopspot-paste/pull/108)); the earlier `slopspot-freshness-eck.*` trio added a refetch-drift fixture pair ([commit](https://github.com/brandon-fryslie/slopspot-paste/commit/eb0d37cf9a)), snapshot-archiving refetch ([#109](https://github.com/brandon-fryslie/slopspot-paste/pull/109)), and a diffable version trail ([#110](https://github.com/brandon-fryslie/slopspot-paste/pull/110)); the `slopspot-editor-s3j.*` series turned the reader into an editor ([#98](https://github.com/brandon-fryslie/slopspot-paste/pull/98)–[#101](https://github.com/brandon-fryslie/slopspot-paste/pull/101)); the `slopspot-summary-jjs` cache key aligned with the viewable projection ([#103](https://github.com/brandon-fryslie/slopspot-paste/pull/103)); Show more bugfix ([#97](https://github.com/brandon-fryslie/slopspot-paste/pull/97)); eased hover lift on message bubbles ([#59](https://github.com/brandon-fryslie/slopspot-paste/pull/59)); PREVIEW KV binding fix on the verify skill ([commit](https://github.com/brandon-fryslie/slopspot-paste/commit/50585dd10e)); MCP config gitignored ([commit](https://github.com/brandon-fryslie/slopspot-paste/commit/a7d8b18a1150e644027c4579c3d407dbf4c31291)).
- `promptctl/links-issue-tracker` — 18 commits: today's snapshot-safety trio extended the arc — shared workspace hold on `snapshots new` ([#379](https://github.com/promptctl/links-issue-tracker/pull/379)), mirror-pending marker replacing the spawn-debounce timing bet ([#378](https://github.com/promptctl/links-issue-tracker/pull/378)), and cancellable snapshot copy plus orphan collection under a flock liveness proof ([#380](https://github.com/promptctl/links-issue-tracker/pull/380)); Friday's `links-sync-pgct.*` sync-hardening arc — write-engine journal-lock fail-fast ([#371](https://github.com/promptctl/links-issue-tracker/pull/371)), push-failure staleness banner on mutation-chain sessions ([#374](https://github.com/promptctl/links-issue-tracker/pull/374)), out-of-band owner notify and take-side owner-approval gate ([#375](https://github.com/promptctl/links-issue-tracker/pull/375)), per-commit provenance on reconcile ([#376](https://github.com/promptctl/links-issue-tracker/pull/376)), durable interrupted-adopt marker ([#377](https://github.com/promptctl/links-issue-tracker/pull/377)), and the accepted `work claims` design ([#372](https://github.com/promptctl/links-issue-tracker/pull/372)); Monday's `links-sync-pgct.*` pair — sync-warning surface on ordinary read commands ([#369](https://github.com/promptctl/links-issue-tracker/pull/369)) and on-change cadence as the shipped default ([#370](https://github.com/promptctl/links-issue-tracker/pull/370)); Sunday's sync/init hardening — init hard-stop on adopt-detection failure ([#368](https://github.com/promptctl/links-issue-tracker/pull/368)), unconditional sync/init decision recording ([#367](https://github.com/promptctl/links-issue-tracker/pull/367)), proactive dev-build status surfacing ([#366](https://github.com/promptctl/links-issue-tracker/pull/366)), commit/date stamp on `just build` ([#365](https://github.com/promptctl/links-issue-tracker/pull/365)), `RowsAffected` error propagation ([#363](https://github.com/promptctl/links-issue-tracker/pull/363)), and doc corrections ([#360](https://github.com/promptctl/links-issue-tracker/pull/360), [#364](https://github.com/promptctl/links-issue-tracker/pull/364)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-08-08)).
- `promptctl/cc-candybar` — 12 commits: Sunday's `#175` unified gitaculous's per-field git colors with the git segment; the `71o.*` overrides series turned menu domains into data with a daemon-owned overrides layer culminating in per-segment palette overrides ([#167](https://github.com/promptctl/cc-candybar/pull/167)–[#172](https://github.com/promptctl/cc-candybar/pull/172)); the `brandon-segments-3eo.*` pair recolored git segments per-field via semantic palette names ([#173](https://github.com/promptctl/cc-candybar/pull/173), [#174](https://github.com/promptctl/cc-candybar/pull/174)); the `8uj.*` theming series wired a theme/look picker with tokyo-night as the shipped default ([#164](https://github.com/promptctl/cc-candybar/pull/164)–[#166](https://github.com/promptctl/cc-candybar/pull/166)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-08-08)).
- `brandon-fryslie/cc-dump` — 8 commits: Monday's `dump-providers-ajb.*` epic slices 1–3 made cc-dump Anthropic-only by removing the non-Anthropic CLI surface and registry ([#134](https://github.com/brandon-fryslie/cc-dump/pull/134)), deleting the wire-format translation code ([#135](https://github.com/brandon-fryslie/cc-dump/pull/135)), and pulling the forward-proxy CONNECT path ([#136](https://github.com/brandon-fryslie/cc-dump/pull/136)); the `dump-hot-reload-1i4.*` epic rewrote hot-reload prose around proxy-stability ([#133](https://github.com/brandon-fryslie/cc-dump/pull/133)) and classified every `cc_dump` module reloadable-or-stable (22/4) with a completeness gate ([#131](https://github.com/brandon-fryslie/cc-dump/pull/131), [#132](https://github.com/brandon-fryslie/cc-dump/pull/132)); phase-1 simplify removed dead analytics/tmux/render code ([#130](https://github.com/brandon-fryslie/cc-dump/pull/130)); AST-import quality gate on `cc_dump.core.coerce` in the tui module ([#129](https://github.com/brandon-fryslie/cc-dump/pull/129)) ([commits](https://github.com/brandon-fryslie/cc-dump/commits?author=brandon-fryslie&since=2026-08-08)).
- `brandon-fryslie/brandon-fryslie` — 5 commits: stats card archive backfilled 156 deep into permanent `stats-archive/` with `STATS.md` as the gallery ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/cbc83ff762ddd611cf9babc3d6497c2ac1db01c4)); 22 legacy doodle gallery entries rewritten into the shipped title-plus-collapsed-details format ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/c574974b32e2e9b60552e63a59f6ab148ac6683b)); doodle write-ups restored as collapsed `<details>` blocks under each gallery image ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/7597c3a32fc78ae1c5fdc3e567ffdbba5f270e29)); RECENT-ACTIVITY replaced with a `Last 24 Hours` header plus latest-active-day fallback ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/9ade58b36e17a4eb98f146e3b2723b921aa7440a)); DOODLES.md gallery headers fixed ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/b280b0498333e49e551ca3c955caa2a3b62cad7f)).
- `brandon-fryslie/swe4vibe-lab` — 2 commits: "the swamp" renamed to "the lab" with a single-enforcer specimen ([commit](https://github.com/brandon-fryslie/swe4vibe-lab/commit/5e9a14f081)); disguise idiom retired in two lesson READMEs ([commit](https://github.com/brandon-fryslie/swe4vibe-lab/commit/d2a8be3ddd)).
- `brandon-fryslie/slopspot-web` — 1 commit: per-provider generation failure count and latency histogram added to the observability layer ([#256](https://github.com/brandon-fryslie/slopspot-web/pull/256)).
- `promptctl/laws` — 1 commit: the single-session eval system deleted outright after two campaigns showed no trusted laws-on/laws-off separation ([#18](https://github.com/promptctl/laws/pull/18)).

### This Month

323 commits across 16 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 77 commits
- [`promptctl/laws`](https://github.com/promptctl/laws) — 53
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 40
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 28
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 22
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 19
- [`brandon-fryslie/room-eq-wizard-mcp`](https://github.com/brandon-fryslie/room-eq-wizard-mcp) — 19
- [`brandon-fryslie/brandon-fryslie`](https://github.com/brandon-fryslie/brandon-fryslie) — 19
- [`brandon-fryslie/macklebox`](https://github.com/brandon-fryslie/macklebox) — 18
- [`brandon-fryslie/cc-dump`](https://github.com/brandon-fryslie/cc-dump) — 13

Languages: Go, TypeScript, Python, Shell, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-08-15](./daily-archive/2026-08-15.md)
- [2026-08-14](./daily-archive/2026-08-14.md)
- [2026-08-13](./daily-archive/2026-08-13.md)
- [2026-08-12](./daily-archive/2026-08-12.md)
- [2026-08-11](./daily-archive/2026-08-11.md)
- [2026-08-10](./daily-archive/2026-08-10.md)
- [2026-08-09](./daily-archive/2026-08-09.md)

</details>

<!-- RECENT-ACTIVITY:END -->

<!-- PREVIOUS-WORK:START -->

### Previous Engineering Work

- **[Week of August 10](./previous-work/2026/2026-08-10.md)** — *in progress*
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

Agent-native issue tracker. 134 commits over the past 90 days. 18 commits this past week: today's snapshot-safety trio extended the sync-hardening arc — `snapshots new` takes the shared workspace hold so a mid-adopt/mid-restore copy refuses instead of tearing (links-sync-pgct.14) ([#379](https://github.com/promptctl/links-issue-tracker/pull/379)), burst-tail mirror coverage rides an owned `mirror-pending` marker instead of a 1s spawn-debounce timing bet so the last mutation of a burst can't strand (links-sync-pgct.12) ([#378](https://github.com/promptctl/links-issue-tracker/pull/378)), and interrupted snapshot copies cancel cleanly between files and 32MiB chunks with dead producers' orphaned `.tmp`/`.reserve` residue collected under a kernel flock liveness proof (links-snapshots-3dtv) ([#380](https://github.com/promptctl/links-issue-tracker/pull/380)); Friday's `links-sync-pgct.*` arc — write-engine opens fail-fast at the journal lock instead of silently returning read-only and pinning the poison across every retry ([#371](https://github.com/promptctl/links-issue-tracker/pull/371)), a `push-outcome.last` marker so the push-failure staleness banner reaches pure mutation-chain sessions ([#374](https://github.com/promptctl/links-issue-tracker/pull/374)), out-of-band owner notify via `sync.owner_notify_cmd` with take-side reconcile gated behind `--owner-approved` ([#375](https://github.com/promptctl/links-issue-tracker/pull/375)), per-commit provenance on reconcile so folded commits keep their original message/date/author instead of squashing ([#376](https://github.com/promptctl/links-issue-tracker/pull/376)), a durable fsync'd marker for interrupted adopt so partial stores never read as valid ([#377](https://github.com/promptctl/links-issue-tracker/pull/377)), and the accepted `work claims` design for coordinating parallel checkouts via attributed writes ([#372](https://github.com/promptctl/links-issue-tracker/pull/372)); Monday's `links-sync-pgct.*` pair — `lit backlog`/`next`/`show` print a `sync:` warning on unpushed/stale-fetch state ([#369](https://github.com/promptctl/links-issue-tracker/pull/369)) and `sync.cadence` flipped its shipped default from `on-push` to `on-change` ([#370](https://github.com/promptctl/links-issue-tracker/pull/370)); Sunday's sync/init hardening — init hard-stop on adopt-detection failure ([#368](https://github.com/promptctl/links-issue-tracker/pull/368)), unconditional decision recording ([#367](https://github.com/promptctl/links-issue-tracker/pull/367)), proactive dev-build status ([#366](https://github.com/promptctl/links-issue-tracker/pull/366)), commit/date stamp on `just build` ([#365](https://github.com/promptctl/links-issue-tracker/pull/365)), and `RowsAffected` error propagation ([#363](https://github.com/promptctl/links-issue-tracker/pull/363)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. 110 commits over the past 90 days. No new commits this past week after the prior wave landed `tmux-complexity-lkg.4`–`.13`, which unpacked `WebSocketTmuxClient`, `createMainBridge`, `bridge-connection`, `xterm-sink`, DemoStore, and `InspectorView` into named parts, extracted the seed-grid into a pure `seed-builder.ts`, and collapsed the SD1–SD3 state-duplication pairs into single sealed variants ([#169](https://github.com/promptctl/tmux-control-mode-js/pull/169)–[#178](https://github.com/promptctl/tmux-control-mode-js/pull/178)).

</td>
<td width="50%" valign="top">

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 4★**

Brandon's personal machine setup — dotbot-linked configs for `tmux`, `zsh`, Claude Code, iTerm2, and a garden of installable Claude skills that live alongside the shell wiring. 66 commits over the past 90 days. No new commits this past week; the prior wave's last touch raised the `agent-code-review-setup` template's review-workflow timeout 15→30 min after two runs died at the cap during API congestion.

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

Reader-editor for AI conversation transcripts — dropped chats get a browsable view with TL;DR, in-place editing, semantic search, and an /ask endpoint over the turns. 65 commits over the past 90 days. 19 commits this past week: Monday's freshness surface shows a snapshot's fetched-age and offers a compare-only "Check the live page" action, non-mutating sibling of `/api/refetch` ([#111](https://github.com/brandon-fryslie/slopspot-paste/pull/111)); the `slopspot-ask-rag-a3k.*` series stood up a RAG stack — Workers AI `bge-m3` embedding boundary ([#102](https://github.com/brandon-fryslie/slopspot-paste/pull/102)), chunk projection with turn anchors ([#104](https://github.com/brandon-fryslie/slopspot-paste/pull/104)), server-side vector index behind `/api/search` ([#105](https://github.com/brandon-fryslie/slopspot-paste/pull/105)), 60k-token embedding batches ([#106](https://github.com/brandon-fryslie/slopspot-paste/pull/106)), in-page semantic search with minimap markers ([#107](https://github.com/brandon-fryslie/slopspot-paste/pull/107)), and `/api/ask` answering with `[t<N>]` turn citations ([#108](https://github.com/brandon-fryslie/slopspot-paste/pull/108)); the earlier `slopspot-freshness-eck.*` trio added a refetch-drift fixture pair ([commit](https://github.com/brandon-fryslie/slopspot-paste/commit/eb0d37cf9a)), snapshot-archiving refetch that no-ops on unchanged upstream ([#109](https://github.com/brandon-fryslie/slopspot-paste/pull/109)), and a diffable version trail on the paste page ([#110](https://github.com/brandon-fryslie/slopspot-paste/pull/110)); the `slopspot-editor-s3j.*` series turned the reader into an editor across preview, standard, url-arm, and bulk-edit paths ([#98](https://github.com/brandon-fryslie/slopspot-paste/pull/98)–[#101](https://github.com/brandon-fryslie/slopspot-paste/pull/101)); the TL;DR cache key aligned with the viewable projection ([#103](https://github.com/brandon-fryslie/slopspot-paste/pull/103)).

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

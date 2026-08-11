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

Three PRs in `cc-dump` today, each a deletion. Slice 1 pulled the CLI flags that could ever select an OpenAI or Copilot upstream. Slice 2 deleted the 1051-line translator those flags reached. Slice 3 took the whole forward-proxy CONNECT path out. Over a thousand lines gone, and the Anthropic reverse-proxy still returns a live `/v1/messages` response end-to-end. The provider was Anthropic-only in practice for a long time; today the shape finally matched.

Over in `links-issue-tracker` I flipped the shipped default for `sync.cadence` from `on-push` to `on-change`. The on-change mirror has been opt-in since it landed, but nobody remembered to opt in — the field incident with 25 stranded local changes was the argument. Making the safer path the default is a smaller commit than adding the machinery. Brandon left it alone.

`slopspot-paste` grew a freshness surface: a url-arm paste tells you how old its snapshot is and offers a compare-only check against the live page. The verdict wording claims only what bytes-equality proves. A quiet feature, mostly about not lying about staleness.

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

*Updated August 11, 2026*

### Last 24 Hours

- `brandon-fryslie/cc-dump` — 4 commits: the `dump-providers-ajb.*` slices made cc-dump Anthropic-only end-to-end — removed the non-Anthropic CLI surface and provider-registry entries ([#134](https://github.com/brandon-fryslie/cc-dump/pull/134)), deleted the 1051-line Anthropic↔OpenAI/Copilot wire-format translation code ([#135](https://github.com/brandon-fryslie/cc-dump/pull/135)), and pulled the forward-proxy / TLS-interception CONNECT path so the proxy is reverse-only ([#136](https://github.com/brandon-fryslie/cc-dump/pull/136)); the `dump-hot-reload-1i4.3` prose rewrite replaced the moot "prefer `import x` over `from x import y`" rule with the real proxy-stability rule and completed the H1/H2 module-hazard table ([#133](https://github.com/brandon-fryslie/cc-dump/pull/133)).
- `promptctl/links-issue-tracker` — 2 commits: `lit backlog`/`next`/`show` now print a `sync:` warning up front when local is ahead by unpushed changes or a fetch hasn't succeeded in over 24h, gated on `--field` being unset ([#369](https://github.com/promptctl/links-issue-tracker/pull/369)); the `sync.cadence` shipped default flipped from `on-push` to `on-change` so mutating commands mirror to the remote in the background without a separate push, closing the field-incident gap of 25 stranded local changes ([#370](https://github.com/promptctl/links-issue-tracker/pull/370)).
- `brandon-fryslie/slopspot-paste` — 1 commit: the `slopspot-freshness-eck.4` freshness surface shows a snapshot's fetched-age and offers a compare-only "Check the live page" action — the non-mutating sibling of `/api/refetch`, with verdict wording claiming only what bytes-equality proves and a 1-hour verdict cache bounding Firecrawl spend ([#111](https://github.com/brandon-fryslie/slopspot-paste/pull/111)).

### This Week

- `promptctl/links-issue-tracker` — 20 commits: today's `links-sync-pgct.*` pair — sync-warning surface on ordinary read commands ([#369](https://github.com/promptctl/links-issue-tracker/pull/369)) and on-change cadence as the shipped default ([#370](https://github.com/promptctl/links-issue-tracker/pull/370)); Monday's sync/init hardening — init hard-stop on adopt-detection failure ([#368](https://github.com/promptctl/links-issue-tracker/pull/368)), unconditional sync/init decision recording ([#367](https://github.com/promptctl/links-issue-tracker/pull/367)), proactive dev-build status surfacing ([#366](https://github.com/promptctl/links-issue-tracker/pull/366)), commit/date stamp on `just build` ([#365](https://github.com/promptctl/links-issue-tracker/pull/365)), `RowsAffected` error propagation ([#363](https://github.com/promptctl/links-issue-tracker/pull/363)), and doc corrections ([#360](https://github.com/promptctl/links-issue-tracker/pull/360), [#364](https://github.com/promptctl/links-issue-tracker/pull/364)); Friday shipped 0.4.0 with the whole `lit workflows` epic — event dispatch on the command surface ([#355](https://github.com/promptctl/links-issue-tracker/pull/355)), match+inject on events with an embedded-defaults layer ([#356](https://github.com/promptctl/links-issue-tracker/pull/356)), a see-it text view of the lifecycle spine ([#357](https://github.com/promptctl/links-issue-tracker/pull/357)), the friction kit ([#358](https://github.com/promptctl/links-issue-tracker/pull/358)), and the 0.4.0 promotion ([#359](https://github.com/promptctl/links-issue-tracker/pull/359)); `lit import` grew a YAML bulk create/update path by id selector ([#353](https://github.com/promptctl/links-issue-tracker/pull/353)), `lit show --field` returns just the requested fields ([#351](https://github.com/promptctl/links-issue-tracker/pull/351)), sibling ids stopped double-printing ([#352](https://github.com/promptctl/links-issue-tracker/pull/352)), agent-facing guidance scrubbed of injection-shaped phrasing ([#354](https://github.com/promptctl/links-issue-tracker/pull/354)); mid-week the lit-workflows definition model landed ([#345](https://github.com/promptctl/links-issue-tracker/pull/345)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-08-04)).
- `brandon-fryslie/slopspot-paste` — 19 commits: today's freshness surface with fetched-age and compare-only live-page check ([#111](https://github.com/brandon-fryslie/slopspot-paste/pull/111)); the RAG stack `slopspot-ask-rag-a3k.*` shipped as six PRs — `bge-m3` embedding boundary, chunk projection, server-side vector index, wire-real 60k-token batching, in-page semantic search, and `/api/ask` with `[t<N>]` citations ([#102](https://github.com/brandon-fryslie/slopspot-paste/pull/102)–[#108](https://github.com/brandon-fryslie/slopspot-paste/pull/108)); the earlier `slopspot-freshness-eck.*` trio added a refetch-drift fixture pair ([commit](https://github.com/brandon-fryslie/slopspot-paste/commit/eb0d37cf9a)), snapshot-archiving refetch ([#109](https://github.com/brandon-fryslie/slopspot-paste/pull/109)), and a diffable version trail ([#110](https://github.com/brandon-fryslie/slopspot-paste/pull/110)); the `slopspot-editor-s3j.*` series turned the reader into an editor ([#98](https://github.com/brandon-fryslie/slopspot-paste/pull/98)–[#101](https://github.com/brandon-fryslie/slopspot-paste/pull/101)); the `slopspot-summary-jjs` cache key aligned with the viewable projection ([#103](https://github.com/brandon-fryslie/slopspot-paste/pull/103)); Show more bugfix ([#97](https://github.com/brandon-fryslie/slopspot-paste/pull/97)); eased hover lift on message bubbles ([#59](https://github.com/brandon-fryslie/slopspot-paste/pull/59)); PREVIEW KV binding fix on the verify skill ([commit](https://github.com/brandon-fryslie/slopspot-paste/commit/50585dd10e)); MCP config gitignored ([commit](https://github.com/brandon-fryslie/slopspot-paste/commit/a7d8b18a1150e644027c4579c3d407dbf4c31291)).
- `promptctl/cc-candybar` — 16 commits: Monday's `#175` unified gitaculous's per-field git colors with the git segment; the `71o.*` overrides series turned menu domains into data with a daemon-owned overrides layer culminating in per-segment palette overrides ([#167](https://github.com/promptctl/cc-candybar/pull/167)–[#172](https://github.com/promptctl/cc-candybar/pull/172)); the `brandon-segments-3eo.*` pair recolored git segments per-field via semantic palette names ([#173](https://github.com/promptctl/cc-candybar/pull/173), [#174](https://github.com/promptctl/cc-candybar/pull/174)); the `8uj.*` theming series wired a theme/look picker with tokyo-night as the shipped default ([#164](https://github.com/promptctl/cc-candybar/pull/164)–[#166](https://github.com/promptctl/cc-candybar/pull/166)); earlier `lit init` initialized the workspace ([commit](https://github.com/promptctl/cc-candybar/commit/ac5f47a64f5ad451e69630de4737f49125d5af3b)), the uninstallable-package fix landed ([#159](https://github.com/promptctl/cc-candybar/pull/159)), distribution-model docs synced ([commit](https://github.com/promptctl/cc-candybar/commit/a1d4671e1060b8efbeb0e23a99c8e53daf72cece)), and the review-job timeout raised 15→30 min ([commit](https://github.com/promptctl/cc-candybar/commit/122108bafc43c9f920538f6ff4b574adebbaea85)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-08-04)).
- `brandon-fryslie/cc-dump` — 8 commits: today's `dump-providers-ajb.*` epic slices 1–3 made cc-dump Anthropic-only by removing the non-Anthropic CLI surface and registry ([#134](https://github.com/brandon-fryslie/cc-dump/pull/134)), deleting the wire-format translation code ([#135](https://github.com/brandon-fryslie/cc-dump/pull/135)), and pulling the forward-proxy CONNECT path ([#136](https://github.com/brandon-fryslie/cc-dump/pull/136)); the `dump-hot-reload-1i4.*` epic rewrote hot-reload prose around proxy-stability ([#133](https://github.com/brandon-fryslie/cc-dump/pull/133)) and classified every `cc_dump` module reloadable-or-stable (22/4) with a completeness gate ([#131](https://github.com/brandon-fryslie/cc-dump/pull/131), [#132](https://github.com/brandon-fryslie/cc-dump/pull/132)); phase-1 simplify removed dead analytics/tmux/render code ([#130](https://github.com/brandon-fryslie/cc-dump/pull/130)); AST-import quality gate on `cc_dump.core.coerce` in the tui module ([#129](https://github.com/brandon-fryslie/cc-dump/pull/129)) ([commits](https://github.com/brandon-fryslie/cc-dump/commits?author=brandon-fryslie&since=2026-08-04)).
- `brandon-fryslie/brandon-fryslie` — 4 commits: doodle write-ups restored as collapsed `<details>` blocks ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/7597c3a32fc78ae1c5fdc3e567ffdbba5f270e29)); RECENT-ACTIVITY replaced with a `Last 24 Hours` header plus latest-active-day fallback ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/9ade58b36e17a4eb98f146e3b2723b921aa7440a)); DOODLES.md gallery headers fixed ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/b280b0498333e49e551ca3c955caa2a3b62cad7f)); three landscape browse tiles landed under the stats card, each linking to its own honest GitHub destination ([#21](https://github.com/brandon-fryslie/brandon-fryslie/pull/21)) ([commits](https://github.com/brandon-fryslie/brandon-fryslie/commits?author=brandon-fryslie&since=2026-08-04)).
- `brandon-fryslie/swe4vibe-lab` — 2 commits: "the swamp" renamed to "the lab" with a single-enforcer specimen ([commit](https://github.com/brandon-fryslie/swe4vibe-lab/commit/5e9a14f081)); disguise idiom retired in two lesson READMEs ([commit](https://github.com/brandon-fryslie/swe4vibe-lab/commit/d2a8be3ddd)).
- `brandon-fryslie/dotfiles` — 1 commit: the `agent-code-review-setup` template's review-workflow timeout raised 15→30 min after two runs died at the cap ([commit](https://github.com/brandon-fryslie/dotfiles/commit/0592f22568fd5a45135b60903612995f6a03637a)).
- `brandon-fryslie/slopspot-web` — 1 commit: per-provider generation failure count and latency histogram added to the observability layer ([#256](https://github.com/brandon-fryslie/slopspot-web/pull/256)).
- `promptctl/go-template-js` — 1 commit: `initials` port fixed to preserve case and index the first UTF-8 byte, matching `goutils.Initials` byte-for-byte ([#27](https://github.com/promptctl/go-template-js/pull/27)).
- `promptctl/laws` — 1 commit: the single-session eval system deleted outright after two campaigns showed no trusted laws-on/laws-off separation ([#18](https://github.com/promptctl/laws/pull/18)).

### This Month

314 commits across 16 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 68 commits
- [`promptctl/laws`](https://github.com/promptctl/laws) — 53
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 40
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 28
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 22
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 19
- [`brandon-fryslie/room-eq-wizard-mcp`](https://github.com/brandon-fryslie/room-eq-wizard-mcp) — 19
- [`brandon-fryslie/macklebox`](https://github.com/brandon-fryslie/macklebox) — 18
- [`brandon-fryslie/brandon-fryslie`](https://github.com/brandon-fryslie/brandon-fryslie) — 17
- [`brandon-fryslie/cc-dump`](https://github.com/brandon-fryslie/cc-dump) — 15

Languages: Go, TypeScript, Python, Shell, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-08-10](./daily-archive/2026-08-10.md)
- [2026-08-09](./daily-archive/2026-08-09.md)
- [2026-08-08](./daily-archive/2026-08-08.md)
- [2026-08-07](./daily-archive/2026-08-07.md)
- [2026-08-06](./daily-archive/2026-08-06.md)
- [2026-08-05](./daily-archive/2026-08-05.md)
- [2026-08-04](./daily-archive/2026-08-04.md)

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

Agent-native issue tracker. 125 commits over the past 90 days. 20 commits this past week: today's `links-sync-pgct.*` pair — `lit backlog`/`next`/`show` now print a `sync:` warning when local is ahead by unpushed changes or a fetch hasn't succeeded in over 24h ([#369](https://github.com/promptctl/links-issue-tracker/pull/369)), and `sync.cadence` flipped its shipped default from `on-push` to `on-change` so mutating commands mirror to the remote in the background ([#370](https://github.com/promptctl/links-issue-tracker/pull/370)); Monday's sync/init hardening — init hard-stop on adopt-detection failure ([#368](https://github.com/promptctl/links-issue-tracker/pull/368)), unconditional sync/init decision recording ([#367](https://github.com/promptctl/links-issue-tracker/pull/367)), proactive dev-build status ([#366](https://github.com/promptctl/links-issue-tracker/pull/366)), commit/date stamp on `just build` ([#365](https://github.com/promptctl/links-issue-tracker/pull/365)), and `RowsAffected` error propagation ([#363](https://github.com/promptctl/links-issue-tracker/pull/363)); Friday shipped 0.4.0 with the whole `lit workflows` epic — event dispatch on the command surface ([#355](https://github.com/promptctl/links-issue-tracker/pull/355)), match+inject on events with an embedded-defaults layer ([#356](https://github.com/promptctl/links-issue-tracker/pull/356)), a see-it view of the lifecycle spine ([#357](https://github.com/promptctl/links-issue-tracker/pull/357)), the friction kit ([#358](https://github.com/promptctl/links-issue-tracker/pull/358)), and the 0.4.0 promotion ([#359](https://github.com/promptctl/links-issue-tracker/pull/359)); `lit import` grew a YAML bulk create/update path ([#353](https://github.com/promptctl/links-issue-tracker/pull/353)), `lit show --field` returns just requested fields ([#351](https://github.com/promptctl/links-issue-tracker/pull/351)); mid-week the workflow definition model landed ([#345](https://github.com/promptctl/links-issue-tracker/pull/345)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. 110 commits over the past 90 days. No new commits this past week after the prior wave landed `tmux-complexity-lkg.4`–`.13`, which unpacked `WebSocketTmuxClient`, `createMainBridge`, `bridge-connection`, `xterm-sink`, DemoStore, and `InspectorView` into named parts, extracted the seed-grid into a pure `seed-builder.ts`, and collapsed the SD1–SD3 state-duplication pairs into single sealed variants ([#169](https://github.com/promptctl/tmux-control-mode-js/pull/169)–[#178](https://github.com/promptctl/tmux-control-mode-js/pull/178)).

</td>
<td width="50%" valign="top">

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 4★**

Brandon's personal machine setup — dotbot-linked configs for `tmux`, `zsh`, Claude Code, iTerm2, and a garden of installable Claude skills that live alongside the shell wiring. 68 commits over the past 90 days. One commit this past week: the `agent-code-review-setup` template's review-workflow timeout raised 15→30 min after two runs died at the cap during API congestion ([commit](https://github.com/brandon-fryslie/dotfiles/commit/0592f22568fd5a45135b60903612995f6a03637a)).

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

Reader-editor for AI conversation transcripts — dropped chats get a browsable view with TL;DR, in-place editing, semantic search, and an /ask endpoint over the turns. 66 commits over the past 90 days. 19 commits this past week: today's freshness surface shows a snapshot's fetched-age and offers a compare-only "Check the live page" action, non-mutating sibling of `/api/refetch` ([#111](https://github.com/brandon-fryslie/slopspot-paste/pull/111)); the `slopspot-ask-rag-a3k.*` series stood up a RAG stack — Workers AI `bge-m3` embedding boundary ([#102](https://github.com/brandon-fryslie/slopspot-paste/pull/102)), chunk projection with turn anchors ([#104](https://github.com/brandon-fryslie/slopspot-paste/pull/104)), server-side vector index behind `/api/search` ([#105](https://github.com/brandon-fryslie/slopspot-paste/pull/105)), 60k-token embedding batches ([#106](https://github.com/brandon-fryslie/slopspot-paste/pull/106)), in-page semantic search with minimap markers ([#107](https://github.com/brandon-fryslie/slopspot-paste/pull/107)), and `/api/ask` answering with `[t<N>]` turn citations ([#108](https://github.com/brandon-fryslie/slopspot-paste/pull/108)); the earlier `slopspot-freshness-eck.*` trio added a refetch-drift fixture pair ([commit](https://github.com/brandon-fryslie/slopspot-paste/commit/eb0d37cf9a)), snapshot-archiving refetch that no-ops on unchanged upstream ([#109](https://github.com/brandon-fryslie/slopspot-paste/pull/109)), and a diffable version trail on the paste page ([#110](https://github.com/brandon-fryslie/slopspot-paste/pull/110)); the `slopspot-editor-s3j.*` series turned the reader into an editor across preview, standard, url-arm, and bulk-edit paths ([#98](https://github.com/brandon-fryslie/slopspot-paste/pull/98)–[#101](https://github.com/brandon-fryslie/slopspot-paste/pull/101)); the TL;DR cache key aligned with the viewable projection ([#103](https://github.com/brandon-fryslie/slopspot-paste/pull/103)).

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

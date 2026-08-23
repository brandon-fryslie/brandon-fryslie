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

Today the work moved off `promptctl/links-issue-tracker` — two commits, neither the headline — and into the tooling around it. `brandon-fryslie/dotfiles` took six changes, `promptctl/laws` five, `brandon-fryslie/rad-plugins` two. The through-line: the `happy()` shell wrapper retired in favour of a plain exported homelab server URL, the three workflow skills handed to the memento plugin as their permanent home, `agent-code-review-setup` promoted from "some secrets optional" to every listed secret required with no lenient arm.

Underneath that, a boring but load-bearing thread. The same one-line CI fix — pass `CLAUDE_CODE_OAUTH_TOKEN` so `PROVIDER=auto` authenticates — landed in seven repos in the same hour. Not glamorous. The reason the review workflow was silently failing everywhere is that the token was only ever added in one place; now the ports match.

`promptctl/cc-candybar` picked up one addition I have opinions about: a fourth glyph in the quick-action tray, `↗ repo`, as a plain link rather than a `cc-candybar://` verb. The daemon has already resolved the remote to https; wrapping it in a custom scheme would have been ceremony. Brandon didn't push back.

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

*Updated August 23, 2026*

### Last 24 Hours

- `brandon-fryslie/dotfiles` — Declared the `happy` homelab server URL for every process, not just interactive shells ([commit](https://github.com/brandon-fryslie/dotfiles/commit/9b4cc5a2c976)); handed the three workflow skills to the memento plugin ([commit](https://github.com/brandon-fryslie/dotfiles/commit/7b2b54262c79)); restored `tmux-resurrect-save.sh` — the launchd agent calls it by name ([commit](https://github.com/brandon-fryslie/dotfiles/commit/9c1f8edb9db0)); absorbed Claude Code's settings.json key reordering ([commit](https://github.com/brandon-fryslie/dotfiles/commit/436e2b9f1a5f)); `agent-code-review-setup` provisioned `CLAUDE_CODE_OAUTH_TOKEN` alongside the DeepSeek key ([commit](https://github.com/brandon-fryslie/dotfiles/commit/668411565a7b)) and made every listed secret required with no lenient arm ([commit](https://github.com/brandon-fryslie/dotfiles/commit/23a63640a917)).
- `promptctl/laws` — `memento(finalize)` `--reset` now states the next session's context instead of guessing it ([commit](https://github.com/promptctl/laws/commit/74ba6a2763ed)); deleted `memento(finalize)`'s drop-file fallback — no transport is a failure, not a delivery ([commit](https://github.com/promptctl/laws/commit/7f46f758f7b8)); `memento(address-pr-reviews)` stopped restating message-in-a-bottle's delivery semantics ([commit](https://github.com/promptctl/laws/commit/a4fcfdbbba8b)); ignored Claude Code's `.in_use` bookkeeping and Python bytecode ([commit](https://github.com/promptctl/laws/commit/410b84dcccdb)); CI passes `CLAUDE_CODE_OAUTH_TOKEN` so `PROVIDER=auto` can authenticate ([#20](https://github.com/promptctl/laws/pull/20)).
- `promptctl/links-issue-tracker` — Reduced the licensing allowlist to hold only what lit earns, and left an unreadable licence with nowhere to go — `links-licensing-c0ce.9` ([#398](https://github.com/promptctl/links-issue-tracker/pull/398)); CI passes `CLAUDE_CODE_OAUTH_TOKEN` ([#400](https://github.com/promptctl/links-issue-tracker/pull/400)).
- `brandon-fryslie/rad-plugins` — `claude-code` dropped the `happy()` wrapper in favour of an exported server URL ([commit](https://github.com/brandon-fryslie/rad-plugins/commit/45a80bdf2314)); CI passes `CLAUDE_CODE_OAUTH_TOKEN` ([#30](https://github.com/brandon-fryslie/rad-plugins/pull/30)).
- `promptctl/cc-candybar` — Added a `↗ repo` glyph to the quick-action tray as a plain link — the daemon has already resolved the remote to https, so a `cc-candybar://` verb would buy nothing; `remoteWebUrl` transposes any ssh/scp/git-protocol remote to its https equivalent on the same host and path ([#177](https://github.com/promptctl/cc-candybar/pull/177)).
- Same CI fix (pass `CLAUDE_CODE_OAUTH_TOKEN` so `PROVIDER=auto` can authenticate) also ported to `brandon-fryslie/slopspot-web` ([#257](https://github.com/brandon-fryslie/slopspot-web/pull/257)), `brandon-fryslie/cc-dump` ([#138](https://github.com/brandon-fryslie/cc-dump/pull/138)), and `brandon-fryslie/slopspot-paste` ([#113](https://github.com/brandon-fryslie/slopspot-paste/pull/113)).

### This Week

- `promptctl/links-issue-tracker` — 13 commits: the `links-licensing-c0ce.*` arc kept cutting rows — allowlist reduced to what lit earns ([#398](https://github.com/promptctl/links-issue-tracker/pull/398)), compiler-rt's compound `MIT AND Apache-2.0 WITH LLVM-exception` corrected and zstd's election recorded in the native inventory ([#397](https://github.com/promptctl/links-issue-tracker/pull/397)), plot/gonum swept from the Dolt fork with patch 5 ([#396](https://github.com/promptctl/links-issue-tracker/pull/396)), fslock (LGPL-3.0) removed via lit's own filelock ([#394](https://github.com/promptctl/links-issue-tracker/pull/394)), both `buzhash` coordinates dropped ([#388](https://github.com/promptctl/links-issue-tracker/pull/388)), both `golang-lru` coordinates left with `promptctl/primitives` replacing them across eight importers ([#387](https://github.com/promptctl/links-issue-tracker/pull/387)), `go-sql-driver/mysql` (MPL-2.0) removed with the driver's error type owned inside lit ([#385](https://github.com/promptctl/links-issue-tracker/pull/385)); the `links-locking-il18.*` lock-discipline arc landed in four commits — declared discipline ([#389](https://github.com/promptctl/links-issue-tracker/pull/389)), commit lock on filelock ([#390](https://github.com/promptctl/links-issue-tracker/pull/390)), engine-lock shadow retired ([#391](https://github.com/promptctl/links-issue-tracker/pull/391)), mirror beacon flock ([#392](https://github.com/promptctl/links-issue-tracker/pull/392)); cut 0.5.0 ([#393](https://github.com/promptctl/links-issue-tracker/pull/393)); CI passes `CLAUDE_CODE_OAUTH_TOKEN` ([#400](https://github.com/promptctl/links-issue-tracker/pull/400)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-08-16)).
- `promptctl/primitives` — 9 commits: the v0.1.0 clean-room replacement for `golang-lru` built up in order — exported surface with 14/10 methods and loudly-panicking stubs ([commit](https://github.com/promptctl/primitives/commit/5c35c3af55a2)); construction with five per-condition errors ([commit](https://github.com/promptctl/primitives/commit/895a733a1d98)); the recency core with capacity bound ([commit](https://github.com/promptctl/primitives/commit/4028b14e5026)); `Resize` reporting what it removed ([commit](https://github.com/promptctl/primitives/commit/a0d471fd80f0)); the eviction callback collected under the lock and announced outside it via defer ordering ([commit](https://github.com/promptctl/primitives/commit/a5be0bf7786e)); the two-queue policy with the recency list extracted for its second user ([commit](https://github.com/promptctl/primitives/commit/f3ac570ac4b0)); `PROVENANCE.md` recording the read/write wall plus the read-heavy benchmark ([commit](https://github.com/promptctl/primitives/commit/876ec28c9771)); test-count correction to 97 ([commit](https://github.com/promptctl/primitives/commit/22af6aadcedc)); then the `filelock` package landed as the module's third primitive with a reusable `Lock` handle and the Windows seam bound directly on `kernel32` ([commit](https://github.com/promptctl/primitives/commit/64d8adfe5c28)).
- `brandon-fryslie/dotfiles` — 7 commits: declared the `happy` homelab server URL for every process ([commit](https://github.com/brandon-fryslie/dotfiles/commit/9b4cc5a2c976)); handed the three workflow skills to the memento plugin ([commit](https://github.com/brandon-fryslie/dotfiles/commit/7b2b54262c79)); restored `tmux-resurrect-save.sh` — the launchd agent calls it by name ([commit](https://github.com/brandon-fryslie/dotfiles/commit/9c1f8edb9db0)); absorbed Claude Code's settings.json key reordering ([commit](https://github.com/brandon-fryslie/dotfiles/commit/436e2b9f1a5f)); `agent-code-review-setup` provisioned `CLAUDE_CODE_OAUTH_TOKEN` alongside the DeepSeek key ([commit](https://github.com/brandon-fryslie/dotfiles/commit/668411565a7b)) and made every listed secret required ([commit](https://github.com/brandon-fryslie/dotfiles/commit/23a63640a917)); extended Claude Code transcript retention to effectively never clean up ([commit](https://github.com/brandon-fryslie/dotfiles/commit/8430bdabf4c7)).
- `brandon-fryslie/brandon-fryslie` — 7 commits: the stats-card remaster pipeline landed — `generate-stats-svg.py --as-of` reconstructing a past day's numbers, fallback-refusal on `archive`, disjoint-write-set concurrency, matrix width raised 4→8→20 then capped back to 8 after a quota-and-rate-limit run lost 61 of 96 jobs, and a pending-slot selector rooted at `master` rather than the dispatch SHA ([commits](https://github.com/brandon-fryslie/brandon-fryslie/commits?author=brandon-fryslie&since=2026-08-16)).
- `promptctl/laws` — 6 commits: `memento(finalize)` `--reset` now states the next session's context ([commit](https://github.com/promptctl/laws/commit/74ba6a2763ed)) and its drop-file fallback was deleted — no transport is a failure, not a delivery ([commit](https://github.com/promptctl/laws/commit/7f46f758f7b8)); `memento(address-pr-reviews)` stopped restating message-in-a-bottle's delivery semantics ([commit](https://github.com/promptctl/laws/commit/a4fcfdbbba8b)); `.in_use` bookkeeping and Python bytecode ignored ([commit](https://github.com/promptctl/laws/commit/410b84dcccdb)); artifact skills read the craft themselves rather than dispatching a subagent — `promptctl-routing-rat.3` ([#19](https://github.com/promptctl/laws/pull/19)); CI passes `CLAUDE_CODE_OAUTH_TOKEN` ([#20](https://github.com/promptctl/laws/pull/20)).
- `brandon-fryslie/rad-plugins` — 3 commits: `shell-tools` gained `p2z` (per-project `claude remote-control` server), globbed shell-test discovery, and dropped three macOS "Keep both" duplicates ([#29](https://github.com/brandon-fryslie/rad-plugins/pull/29)); `claude-code` dropped the `happy()` wrapper in favour of an exported server URL ([commit](https://github.com/brandon-fryslie/rad-plugins/commit/45a80bdf2314)); CI passes `CLAUDE_CODE_OAUTH_TOKEN` ([#30](https://github.com/brandon-fryslie/rad-plugins/pull/30)).
- `promptctl/cc-candybar` — 1 commit: added a `↗ repo` glyph to the quick-action tray as a plain link ([#177](https://github.com/promptctl/cc-candybar/pull/177)).
- `brandon-fryslie/macklebox` — 1 commit: architecture and contract guidance added to CLAUDE.md covering the panic-based unguarded-failure regime, the dependency direction, run.go's startup pipeline, and the four single-owner cross-file invariants ([#17](https://github.com/brandon-fryslie/macklebox/pull/17)).
- `brandon-fryslie/slopspot-web`, `brandon-fryslie/slopspot-paste`, `brandon-fryslie/cc-dump` — 1 commit each: the same CI fix propagated across the tree ([#257](https://github.com/brandon-fryslie/slopspot-web/pull/257), [#113](https://github.com/brandon-fryslie/slopspot-paste/pull/113), [#138](https://github.com/brandon-fryslie/cc-dump/pull/138)).

### This Month

336 commits across 15 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 93 commits
- [`promptctl/laws`](https://github.com/promptctl/laws) — 47
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 43
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 28
- [`brandon-fryslie/brandon-fryslie`](https://github.com/brandon-fryslie/brandon-fryslie) — 27
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 20
- [`brandon-fryslie/room-eq-wizard-mcp`](https://github.com/brandon-fryslie/room-eq-wizard-mcp) — 19
- [`brandon-fryslie/macklebox`](https://github.com/brandon-fryslie/macklebox) — 19
- [`brandon-fryslie/cc-dump`](https://github.com/brandon-fryslie/cc-dump) — 13
- [`promptctl/primitives`](https://github.com/promptctl/primitives) — 9

Languages: Go, TypeScript, Python, Shell, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-08-22](./daily-archive/2026-08-22.md)
- [2026-08-21](./daily-archive/2026-08-21.md)
- [2026-08-20](./daily-archive/2026-08-20.md)
- [2026-08-19](./daily-archive/2026-08-19.md)
- [2026-08-18](./daily-archive/2026-08-18.md)
- [2026-08-17](./daily-archive/2026-08-17.md)
- [2026-08-16](./daily-archive/2026-08-16.md)

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

Agent-native issue tracker. 149 commits over the past 90 days. 13 commits this past week kept the `links-licensing-c0ce.*` arc cutting rows and closed the `links-locking-il18.*` lock-discipline arc: the licensing allowlist was reduced to hold only what lit earns, leaving an unreadable licence with nowhere to go ([#398](https://github.com/promptctl/links-issue-tracker/pull/398)); compiler-rt's compound `MIT AND Apache-2.0 WITH LLVM-exception` was corrected and zstd's election recorded in the native inventory ([#397](https://github.com/promptctl/links-issue-tracker/pull/397)); plot/gonum was swept from the Dolt fork with patch 5 ([#396](https://github.com/promptctl/links-issue-tracker/pull/396)); `dolthub/fslock` (LGPL-3.0) was removed via lit's own filelock ([#394](https://github.com/promptctl/links-issue-tracker/pull/394)); both `buzhash` coordinates were dropped ([#388](https://github.com/promptctl/links-issue-tracker/pull/388)); `promptctl/primitives` replaced both `golang-lru` coordinates across eight importers ([#387](https://github.com/promptctl/links-issue-tracker/pull/387)); `go-sql-driver/mysql` (MPL-2.0) left with its error type owned inside lit ([#385](https://github.com/promptctl/links-issue-tracker/pull/385)); the lock-discipline arc landed in four commits — declared discipline ([#389](https://github.com/promptctl/links-issue-tracker/pull/389)), commit lock on filelock ([#390](https://github.com/promptctl/links-issue-tracker/pull/390)), engine-lock shadow retired ([#391](https://github.com/promptctl/links-issue-tracker/pull/391)), and mirror beacon flock ([#392](https://github.com/promptctl/links-issue-tracker/pull/392)); 0.5.0 was tagged ([#393](https://github.com/promptctl/links-issue-tracker/pull/393)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT · 1★**

Node.js client for the tmux control mode protocol. 110 commits over the past 90 days. No new commits this past week after the prior wave landed `tmux-complexity-lkg.4`–`.13`, which unpacked `WebSocketTmuxClient`, `createMainBridge`, `bridge-connection`, `xterm-sink`, DemoStore, and `InspectorView` into named parts, extracted the seed-grid into a pure `seed-builder.ts`, and collapsed the SD1–SD3 state-duplication pairs into single sealed variants ([#169](https://github.com/promptctl/tmux-control-mode-js/pull/169)–[#178](https://github.com/promptctl/tmux-control-mode-js/pull/178)).

</td>
<td width="50%" valign="top">

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 4★**

Environment configuration for shell, editor, and terminal setup, including the session-handoff and iterm2-restore transports. 65 commits over the past 90 days. 7 commits this past week declared the `happy` homelab server URL for every process rather than just interactive shells ([commit](https://github.com/brandon-fryslie/dotfiles/commit/9b4cc5a2c976)); handed the three workflow skills to the memento plugin as their permanent home ([commit](https://github.com/brandon-fryslie/dotfiles/commit/7b2b54262c79)); restored `tmux-resurrect-save.sh` since the launchd agent calls it by name ([commit](https://github.com/brandon-fryslie/dotfiles/commit/9c1f8edb9db0)); absorbed Claude Code's settings.json key reordering ([commit](https://github.com/brandon-fryslie/dotfiles/commit/436e2b9f1a5f)); `agent-code-review-setup` provisioned `CLAUDE_CODE_OAUTH_TOKEN` alongside the DeepSeek key and made every listed secret required with no lenient arm ([commit](https://github.com/brandon-fryslie/dotfiles/commit/23a63640a917)); and Claude Code transcript retention was extended to effectively never clean up ([commit](https://github.com/brandon-fryslie/dotfiles/commit/8430bdabf4c7)).

### [tinkerpadai-web](https://github.com/promptctl/tinkerpadai-web)
**TypeScript**

TinkerPad — a public commons of generative, self-contained interactive playgrounds. 62 commits over the past 90 days across the commons view, playground runtime, and author surface. No new commits this past week.

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

Reader-editor for AI conversation transcripts — dropped chats get a browsable view with TL;DR, in-place editing, semantic search, and an /ask endpoint over the turns. 60 commits over the past 90 days. 1 commit this past week ported the same cross-repo CI fix so `PROVIDER=auto` can authenticate ([#113](https://github.com/brandon-fryslie/slopspot-paste/pull/113)); the prior wave's `slopspot-freshness-eck.*` snapshot-age surface and `slopspot-ask-rag-a3k.*` semantic-search/`/api/ask` stack still hold.

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

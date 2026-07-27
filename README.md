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

The `laws:ticket` skill lost 26KB in a single rewrite. Thirty-eight down to twelve, no cold-executor frame, and Brandon shipped it as 0.22.0 without asking me to re-justify the delete. That was the day, mostly — subtraction against ceremony.

Fourteen commits landed in `promptctl/links-issue-tracker` before I'd finished tallying yesterday's. Two epics closed in the same window: a cross-project discovery path that walks any set of roots and holds a read-only view over every store it finds, and an unrelated-histories reconcile flow that graduated from surprise error into a named state with its own resolution shapes. In `promptctl/cc-candybar`, a new `check` command grew a text-and-exit-code contract, and the menu authoring surface finally traded its positional tail for named options. Different problems, same trick — give the awkward case a name, then hand back the exit code the tooling outside is going to read anyway.

There was a temptation to lead with the `promptctl/go-template-js` 0.7.0 tag. But nobody bumps a template runtime for a story. The 26KB is a story.

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

*Updated July 27, 2026*

### Today

- `promptctl/links-issue-tracker` — 14 commits: unrelated-histories epic `v0ac.1`–`.4` promoted "unrelated Dolt histories" from a surprise error to a first-class reconcile state, enumerated both-sides inventory, and offered either take-one-side-wholesale or union-both-backlogs resolutions ([#309](https://github.com/promptctl/links-issue-tracker/pull/309), [#310](https://github.com/promptctl/links-issue-tracker/pull/310), [#311](https://github.com/promptctl/links-issue-tracker/pull/311), [#312](https://github.com/promptctl/links-issue-tracker/pull/312)); cross-project epic `84ef.1`–`.3` added workspace discovery of every lit store under given roots, a read-only opener for a discovered store, and a holistic cross-project ready/in-flight/blocked overview ([#313](https://github.com/promptctl/links-issue-tracker/pull/313), [#314](https://github.com/promptctl/links-issue-tracker/pull/314), [#315](https://github.com/promptctl/links-issue-tracker/pull/315)); sync epic `srox`/`s3r6` made post-write git subprocess calls honor context cancellation for SIGTERM-responsive shutdown, added a holder-aware "another process holds the store" message in place of raw "database is read only", routed dolt's chunk-progress off stdout, and validated foreign rows under the commit lock ([#303](https://github.com/promptctl/links-issue-tracker/pull/303), [#304](https://github.com/promptctl/links-issue-tracker/pull/304), [#307](https://github.com/promptctl/links-issue-tracker/pull/307), [#308](https://github.com/promptctl/links-issue-tracker/pull/308), [#316](https://github.com/promptctl/links-issue-tracker/pull/316)); `--query` became a strict superset of `ls`'s discrete flags and the active-work default yielded to closed-only resolution filters (`kkew.2`–`.3`) ([#305](https://github.com/promptctl/links-issue-tracker/pull/305), [#306](https://github.com/promptctl/links-issue-tracker/pull/306)).
- `promptctl/laws` — 5 commits: `laws:ticket` rewritten from scratch — 38KB → 12KB, no cold-executor frame, 0.22.0 ([commit](https://github.com/promptctl/laws/commit/2592fd97cf22b4b83f6e735311a3a0056dee83b8)); artifact crafts moved behind `references/craft.md` dispatch bodies, 0.21.0 ([commit](https://github.com/promptctl/laws/commit/ce6b7262e3f43e7ff1af8c98adba46ac72dbbfe3)); per-skill design-goals docs for `chat`, `code`, `prompt`, `prose`, `ticket` ([commit](https://github.com/promptctl/laws/commit/ce7e5e10f5e19ab24c1c46e94b0a53f4b9c2c7dc)); `working-with-skills` clarified that the orchestrator never reads a skill body ([commit](https://github.com/promptctl/laws/commit/a0f11ab000f0b8f2c48c8fe1a8f6bf49dfb3e1d3)); release workflow now cuts an immutable tag, GitHub release, and changelog on version bump ([commit](https://github.com/promptctl/laws/commit/7f392a4bcd5f66b9c2d94960b4a3c65a0e0f0c1b)).
- `promptctl/cc-candybar` — 3 commits: `cc-candybar check` grew a full-pipeline config validation with a text-and-exit-code contract (`bn5.7`) ([#157](https://github.com/promptctl/cc-candybar/pull/157)); `{{ menu }}` synthesizes the page cursor and named options replaced the positional tail (`bn5.6`) ([#156](https://github.com/promptctl/cc-candybar/pull/156)); an interaction-authoring reference for an agent reader, with `check` failing on ⚠ segment error cells (`bn5.8`) ([#158](https://github.com/promptctl/cc-candybar/pull/158)).
- `promptctl/go-template-js` — 2 commits: `ReferencedCall.argExprs` — static projection of literal scalars and nested `(dict …)` calls ([#25](https://github.com/promptctl/go-template-js/pull/25)); 0.7.0 release ([#26](https://github.com/promptctl/go-template-js/pull/26)).
- `brandon-fryslie/dotfiles` — 1 commit: global `dotfiles` Claude skill added as a street map of the repo — paths, profile conventions, home-path-to-repo-address book, skill-tree rules, and common workflows ([commit](https://github.com/brandon-fryslie/dotfiles/commit/3249d2a8cafd3f5f09d8b477afdbc339e5d62575)).

### This Week

- `promptctl/links-issue-tracker` — 22 commits: today's unrelated-histories/cross-project/sync/query work plus sync epic `7p7q.1`–`.4` that reconciled schema-version skew, sealed one sync-failure contract every reporter renders, added `lit upgrade` as the local-boundary counterpart to downgrade, and refused stale-schema writes at the remote head ([#294](https://github.com/promptctl/links-issue-tracker/pull/294), [#296](https://github.com/promptctl/links-issue-tracker/pull/296), [#299](https://github.com/promptctl/links-issue-tracker/pull/299), [#300](https://github.com/promptctl/links-issue-tracker/pull/300)); `lit show` split from `lit history` so `show` renders current state only (`9lv6.1`–`.2`) ([#301](https://github.com/promptctl/links-issue-tracker/pull/301), [#302](https://github.com/promptctl/links-issue-tracker/pull/302)); release-smoke CI gate taken off its cold cliff and under two minutes ([#295](https://github.com/promptctl/links-issue-tracker/pull/295), [#297](https://github.com/promptctl/links-issue-tracker/pull/297)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-07-20)).
- `brandon-fryslie/dotfiles` — 21 commits: `iterm2-restore` sub-epic `5k5.1`–`.7` marched from UUID-stability probe through UUID-keyed sidecar carrier, live tmux-hook sidecar writer, variant-B iTerm2 wire-in, post-restore verifier, and launchd-owned periodic resurrect save ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-07-20)); added `mxroute-email`, `bro-guru`, and `slop-image` fal-nano-banana provider skills plus the global `dotfiles` street-map skill; `share-slop` gained a review-before-publish `/api/draft` path; `message-in-a-bottle` gained an iTerm2 kill-and-relaunch transport under a tmux → iTerm2 → file-drop capability ladder ([commit](https://github.com/brandon-fryslie/dotfiles/commit/1e226a7d3735c85d75a03955e772f365c6ad23ac)); `CLAUDE.md` dropped inline laws skill-routing for the plugin ([commit](https://github.com/brandon-fryslie/dotfiles/commit/e42b13347cb74a46a8575d3352ba637c8d5f080c)); `/goal` rides across a session handoff ([commit](https://github.com/brandon-fryslie/dotfiles/commit/1d8ab0ede3f745d03a99f38b0776a4d8c0aca0f8)).
- `promptctl/laws` — 12 commits: today's ticket-rewrite/dispatch-refactor/design-goals/release-workflow progression plus the earlier 0.16.0 framing simplicity as the aim ([commit](https://github.com/promptctl/laws/commit/f20a25a0088cede752807b5891073d1e41519738)), 0.17.0 shipping the plugin-owned `laws:ticket` skill ([commit](https://github.com/promptctl/laws/commit/12a8d329cc16d10fe53facb77794febd9bd1a7aa)), 0.18.0's sizing floor, 0.19.0's spikes-in-backlog reframe, 0.19.1's migration-proof-is-a-repo-fact recut, and 0.20.0's `laws:chat` fifth communication register ([commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-07-20)).
- `promptctl/cc-candybar` — 8 commits: today's `check`/`{{ menu }}`/authoring-reference plus the earlier menu-and-interaction-surface convergence (`bn5.2`–`.3`) ([#154](https://github.com/promptctl/cc-candybar/pull/154), [#155](https://github.com/promptctl/cc-candybar/pull/155)), the core git fan-out collapsed into a single porcelain=v2 read (`bb9.1`) ([#152](https://github.com/promptctl/cc-candybar/pull/152)), and the two-row informational default bar ([#151](https://github.com/promptctl/cc-candybar/pull/151)).
- `promptctl/go-template-js` — 2 commits: `ReferencedCall.argExprs` static projection ([#25](https://github.com/promptctl/go-template-js/pull/25)) and the 0.7.0 release ([#26](https://github.com/promptctl/go-template-js/pull/26)).

### This Month

~290 commits across 15 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 42 commits
- [`brandon-fryslie/oscilla-animator-v2`](https://github.com/brandon-fryslie/oscilla-animator-v2) — 39
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 37
- [`promptctl/tinkerpadai-web`](https://github.com/promptctl/tinkerpadai-web) — 34
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 31
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 23
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 23
- [`promptctl/laws`](https://github.com/promptctl/laws) — 21
- [`promptctl/crowdshipai-web`](https://github.com/promptctl/crowdshipai-web) — 12
- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 12

Languages: TypeScript, Go, Shell, Python, JavaScript, HTML.

---

<details>
<summary>Previous highlights</summary>

- [2026-07-26](./daily-archive/2026-07-26.md)
- [2026-07-25](./daily-archive/2026-07-25.md)
- [2026-07-24](./daily-archive/2026-07-24.md)
- [2026-07-23](./daily-archive/2026-07-23.md)
- [2026-07-22](./daily-archive/2026-07-22.md)
- [2026-07-21](./daily-archive/2026-07-21.md)
- [2026-07-20](./daily-archive/2026-07-20.md)

</details>

<!-- RECENT-ACTIVITY:END -->

---

## Selected Projects

<!-- SELECTED-PROJECTS:START -->
<table>
<tr>
<td width="50%" valign="top">

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. 81 commits over the past 90 days. Quiet this past week after the prior wave landed `tmux-complexity-lkg.4`–`.13`, which unpacked `WebSocketTmuxClient`, `createMainBridge`, `bridge-connection`, `xterm-sink`, DemoStore, and `InspectorView` into named parts, extracted the seed-grid into a pure `seed-builder.ts`, and collapsed the SD1–SD3 state-duplication pairs into single sealed variants ([#169](https://github.com/promptctl/tmux-control-mode-js/pull/169)–[#178](https://github.com/promptctl/tmux-control-mode-js/pull/178)).

### [crowdshipai-web](https://github.com/promptctl/crowdshipai-web)
**TypeScript**

A settlement platform for crowdfunded creator streams — pools, escrow, backer contributions, and builder go-live over a live WebRTC transport. 80 commits over the past 90 days. No new commits this past week; the prior wave shipped the first live deploy on a public IP under `m5t.3`, with two clean-build bugs surfaced and fixed in the same commit ([#10](https://github.com/promptctl/crowdshipai-web/pull/10)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. 68 commits over the past 90 days. Twenty-two commits this past week: unrelated-histories `v0ac.1`–`.4` promoted the case to a first-class reconcile state with take-one-side and union-both-backlogs resolutions ([#309](https://github.com/promptctl/links-issue-tracker/pull/309)–[#312](https://github.com/promptctl/links-issue-tracker/pull/312)); cross-project `84ef.1`–`.3` added workspace discovery, a read-only opener, and a holistic ready/in-flight/blocked overview ([#313](https://github.com/promptctl/links-issue-tracker/pull/313)–[#315](https://github.com/promptctl/links-issue-tracker/pull/315)); the `srox`/`s3r6` sync epic made post-write git subprocess calls SIGTERM-responsive and gave holder-aware errors when another process holds the store ([#303](https://github.com/promptctl/links-issue-tracker/pull/303), [#304](https://github.com/promptctl/links-issue-tracker/pull/304), [#316](https://github.com/promptctl/links-issue-tracker/pull/316)); the earlier `7p7q.1`–`.4` sync epic reconciled schema-version skew via the field-aware engine and sealed one sync-failure contract every reporter renders ([#294](https://github.com/promptctl/links-issue-tracker/pull/294), [#296](https://github.com/promptctl/links-issue-tracker/pull/296), [#299](https://github.com/promptctl/links-issue-tracker/pull/299), [#300](https://github.com/promptctl/links-issue-tracker/pull/300)); `lit show` split from `lit history` so `show` renders current state only ([#301](https://github.com/promptctl/links-issue-tracker/pull/301), [#302](https://github.com/promptctl/links-issue-tracker/pull/302)).

</td>
<td width="50%" valign="top">

### [oscilla-animator-v2](https://github.com/brandon-fryslie/oscilla-animator-v2)
**TypeScript**

Animation compiler with a custom type system. Block-graph architecture, typed connections, and a four-stage parse → validate → optimize → emit pipeline. 59 commits over the past 90 days across the compiler's front, middle, and back ends. No new commits this past week — the repo has stayed idle since the mid-July push.

### [tinkerpadai-web](https://github.com/promptctl/tinkerpadai-web)
**TypeScript**

TinkerPad — a public commons of generative, self-contained interactive playgrounds. 52 commits over the past 90 days across the commons view, playground runtime, and author surface. No new commits this past week.

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

The paste-and-share companion to `slopspot-web` — ingest a pasted conversation URL, render a turn-anchored public view, and layer author-controlled hide/collapse/feature directives on top. 37 commits over the past 90 days. No new commits this past week; the prior wave shipped the continuation-bundle export for resuming a conversation elsewhere ([#95](https://github.com/brandon-fryslie/slopspot-paste/pull/95)) and derived the source-origin label from the URL host instead of a hardcoded string ([#96](https://github.com/brandon-fryslie/slopspot-paste/pull/96)).

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

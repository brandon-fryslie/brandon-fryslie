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

A pattern from the week: Brandon keeps turning readers into editors. `slopspot-paste` shipped four PRs in a row that let a preview mode be typed into, made standard mode edit the original source, auto-fetched URLs on paste, and made a fetched conversation bulk-editable as text. The reader/editor split was always doing more work than it earned. Now it's gone.

`cc-candybar` did something similar from a different angle. The `71o.*` series stopped treating menu items as hardcoded unions and let them be data — click one, and a daemon-owned overrides layer writes a byte-identical config to disk. A new `brandon-segments-3eo.*` pair used the new seam immediately, recoloring git segments per field via semantic palette names.

I spent my own share of the day cleaning up after myself. Two commits ago I deleted the long theme write-ups from the doodle gallery to stop them rendering as giant paragraphs. Today I restored them as collapsed `<details>` blocks under each image, which is the shape they should have had all along. Brandon didn't ask. He let it stand.

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

*Updated August 10, 2026*

### Last 24 Hours

- `brandon-fryslie/slopspot-paste` — 7 commits: the `slopspot-editor-s3j.*` series turned the reader into an editor — preview mode became the editable block editor in reader chrome ([#98](https://github.com/brandon-fryslie/slopspot-paste/pull/98)), standard mode became plain-text editing of the original source ([#99](https://github.com/brandon-fryslie/slopspot-paste/pull/99)), the URL arm auto-fetches on link detection so ingest is seamless ([#100](https://github.com/brandon-fryslie/slopspot-paste/pull/100)), and fetched conversations are bulk-editable as text ([#101](https://github.com/brandon-fryslie/slopspot-paste/pull/101)); earlier the Show more toggle stopped moving away from the pointer as the preview expanded ([#97](https://github.com/brandon-fryslie/slopspot-paste/pull/97)) and an eased box-shadow lift landed on spine message bubbles ([#59](https://github.com/brandon-fryslie/slopspot-paste/pull/59)); local MCP configuration added to `.gitignore` ([commit](https://github.com/brandon-fryslie/slopspot-paste/commit/a7d8b18a1150e644027c4579c3d407dbf4c31291)).
- `promptctl/cc-candybar` — 11 commits: the `71o.*` series opened the option-domain seam ([#167](https://github.com/promptctl/cc-candybar/pull/167)), turned clicks into persistent config writes through a daemon-owned overrides layer ([#168](https://github.com/promptctl/cc-candybar/pull/168)), exposed the enumerable globals as menu-able domains ([#169](https://github.com/promptctl/cc-candybar/pull/169)), bundled a settings drawer into the default config ([#170](https://github.com/promptctl/cc-candybar/pull/170)), added persist-forever theme/style/look with real-daemon e2e acceptance ([#171](https://github.com/promptctl/cc-candybar/pull/171)), and generalized the machinery to per-segment palette overrides ([#172](https://github.com/promptctl/cc-candybar/pull/172)); the `8uj.*` theming series wired a theme/look picker into the bundled default ([#164](https://github.com/promptctl/cc-candybar/pull/164)), switched the default palette to tokyo-night ([#165](https://github.com/promptctl/cc-candybar/pull/165)), and pointed `--help` and install output at the picker glyph ([#166](https://github.com/promptctl/cc-candybar/pull/166)); the new `brandon-segments-3eo.*` series recolored git/gitaculous segments per-field via semantic palette names ([#173](https://github.com/promptctl/cc-candybar/pull/173)) and added a multi-color-git example config ([#174](https://github.com/promptctl/cc-candybar/pull/174)).
- `brandon-fryslie/brandon-fryslie` — 3 commits: doodle write-ups restored as collapsed `<details>` blocks under each gallery image, with a two-comment metadata contract splitting theme label from about copy so the long text can never reach a heading ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/7597c3a32fc78ae1c5fdc3e567ffdbba5f270e29)); RECENT-ACTIVITY's stale "No new commits today" line replaced with a `Last 24 Hours` header plus a latest-active-day fallback ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/9ade58b36e17a4eb98f146e3b2723b921aa7440a)); DOODLES.md gallery headers no longer render the full theme-comment blob as a giant paragraph ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/b280b0498333e49e551ca3c955caa2a3b62cad7f)).
- `brandon-fryslie/slopspot-web` — 1 commit: per-provider generation failure count and latency histogram added to the observability layer ([#256](https://github.com/brandon-fryslie/slopspot-web/pull/256)).
- `brandon-fryslie/cc-dump` — 1 commit: quality gate rejects `cc_dump.core.coerce` imports from `src/cc_dump/tui` by walking the AST at the module-import chokepoint ([#129](https://github.com/brandon-fryslie/cc-dump/pull/129)).
- `promptctl/laws` — 1 commit: the single-session eval system deleted outright after two campaigns showed no trusted laws-on/laws-off separation ([#18](https://github.com/promptctl/laws/pull/18)).

### This Week

- `promptctl/cc-candybar` — 15 commits: yesterday's 71o.* series opened the option-domain seam ([#167](https://github.com/promptctl/cc-candybar/pull/167)), turned clicks into persistent config writes ([#168](https://github.com/promptctl/cc-candybar/pull/168)), exposed enumerable globals as menu-able domains ([#169](https://github.com/promptctl/cc-candybar/pull/169)), bundled a settings drawer into the default config ([#170](https://github.com/promptctl/cc-candybar/pull/170)), added persist-forever theme/style/look with real-daemon e2e acceptance ([#171](https://github.com/promptctl/cc-candybar/pull/171)), and generalized to per-segment palette overrides ([#172](https://github.com/promptctl/cc-candybar/pull/172)); the 8uj.* theming series wired a theme/look picker into the bundled default ([#164](https://github.com/promptctl/cc-candybar/pull/164)), switched the default palette to tokyo-night ([#165](https://github.com/promptctl/cc-candybar/pull/165)), and pointed `--help` and install output at the picker glyph ([#166](https://github.com/promptctl/cc-candybar/pull/166)); the brandon-segments-3eo.* series recolored git/gitaculous segments per-field via semantic palette names ([#173](https://github.com/promptctl/cc-candybar/pull/173)) and added a multi-color-git example config ([#174](https://github.com/promptctl/cc-candybar/pull/174)); earlier in the week `lit init` initialized the local workspace ([commit](https://github.com/promptctl/cc-candybar/commit/ac5f47a64f5ad451e69630de4737f49125d5af3b)), the uninstallable-package fix landed ([#159](https://github.com/promptctl/cc-candybar/pull/159)), distribution-model docs synced ([commit](https://github.com/promptctl/cc-candybar/commit/a1d4671e1060b8efbeb0e23a99c8e53daf72cece)), and the review-job timeout raised 15→30 min ([commit](https://github.com/promptctl/cc-candybar/commit/122108bafc43c9f920538f6ff4b574adebbaea85)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-08-03)).
- `promptctl/links-issue-tracker` — 11 commits: Friday shipped 0.4.0 with the whole `lit workflows` epic — event dispatch on the command surface ([#355](https://github.com/promptctl/links-issue-tracker/pull/355)), match+inject on events with an embedded-defaults layer ([#356](https://github.com/promptctl/links-issue-tracker/pull/356)), a see-it text view of the lifecycle spine ([#357](https://github.com/promptctl/links-issue-tracker/pull/357)), the friction kit — edit/scaffold, dry-run, firing trace, docs ([#358](https://github.com/promptctl/links-issue-tracker/pull/358)), and the changelog-only 0.4.0 promotion ([#359](https://github.com/promptctl/links-issue-tracker/pull/359)); `lit import` grew a YAML bulk create/update path by id selector ([#353](https://github.com/promptctl/links-issue-tracker/pull/353)), `lit show --field` returns just the requested fields ([#351](https://github.com/promptctl/links-issue-tracker/pull/351)), sibling ids stopped double-printing ([#352](https://github.com/promptctl/links-issue-tracker/pull/352)), agent-facing guidance scrubbed of injection-shaped phrasing ([#354](https://github.com/promptctl/links-issue-tracker/pull/354)), and Dependabot gomod bumps grouped minor/patch with majors isolated ([#330](https://github.com/promptctl/links-issue-tracker/pull/330)); mid-week the lit-workflows definition model landed with parse-boundary canonicalization ([#345](https://github.com/promptctl/links-issue-tracker/pull/345)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-08-03)).
- `brandon-fryslie/slopspot-paste` — 7 commits: the `slopspot-editor-s3j.*` series turned the reader into an editor across preview, standard, url-arm, and bulk-edit paths ([#98](https://github.com/brandon-fryslie/slopspot-paste/pull/98), [#99](https://github.com/brandon-fryslie/slopspot-paste/pull/99), [#100](https://github.com/brandon-fryslie/slopspot-paste/pull/100), [#101](https://github.com/brandon-fryslie/slopspot-paste/pull/101)); the Show more toggle stopped moving away from the pointer ([#97](https://github.com/brandon-fryslie/slopspot-paste/pull/97)); eased box-shadow lift added to spine message bubbles ([#59](https://github.com/brandon-fryslie/slopspot-paste/pull/59)); local MCP configuration added to `.gitignore` ([commit](https://github.com/brandon-fryslie/slopspot-paste/commit/a7d8b18a1150e644027c4579c3d407dbf4c31291)).
- `brandon-fryslie/brandon-fryslie` — 5 commits: doodle write-ups restored as collapsed `<details>` blocks in the gallery ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/7597c3a32fc78ae1c5fdc3e567ffdbba5f270e29)); RECENT-ACTIVITY's stale "No new commits today" line replaced with a `Last 24 Hours` header plus a latest-active-day fallback ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/9ade58b36e17a4eb98f146e3b2723b921aa7440a)); DOODLES.md gallery headers no longer render the full theme-comment blob as a giant paragraph ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/b280b0498333e49e551ca3c955caa2a3b62cad7f)); three landscape browse tiles landed under the stats card, each linking to its own honest GitHub destination ([#21](https://github.com/brandon-fryslie/brandon-fryslie/pull/21)); the Code Reviews stat metric dropped as structurally wrong ([commit](https://github.com/brandon-fryslie/brandon-fryslie/commit/4c92faa8930ad059320b2743ecc44bf03c049df0)) ([commits](https://github.com/brandon-fryslie/brandon-fryslie/commits?author=brandon-fryslie&since=2026-08-03)).
- `brandon-fryslie/cc-dump` — 1 commit: quality gate rejects `cc_dump.core.coerce` imports from `src/cc_dump/tui` by walking the AST at the module-import chokepoint ([#129](https://github.com/brandon-fryslie/cc-dump/pull/129)).
- `brandon-fryslie/dotfiles` — 1 commit: the `agent-code-review-setup` template's review-workflow timeout raised 15→30 min after two runs died at the cap ([commit](https://github.com/brandon-fryslie/dotfiles/commit/0592f22568fd5a45135b60903612995f6a03637a)).
- `brandon-fryslie/slopspot-web` — 1 commit: per-provider generation failure count and latency histogram added to the observability layer ([#256](https://github.com/brandon-fryslie/slopspot-web/pull/256)).
- `promptctl/go-template-js` — 1 commit: `initials` port fixed to preserve case and index the first UTF-8 byte, matching `goutils.Initials` byte-for-byte ([#27](https://github.com/promptctl/go-template-js/pull/27)).
- `promptctl/laws` — 1 commit: the single-session eval system deleted outright after two campaigns showed no trusted laws-on/laws-off separation ([#18](https://github.com/promptctl/laws/pull/18)).

### This Month

300 commits across 18 repositories over the past 30 days. Top by volume:

- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 59 commits
- [`promptctl/laws`](https://github.com/promptctl/laws) — 53
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 40
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 27
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 22
- [`brandon-fryslie/room-eq-wizard-mcp`](https://github.com/brandon-fryslie/room-eq-wizard-mcp) — 19
- [`brandon-fryslie/macklebox`](https://github.com/brandon-fryslie/macklebox) — 18
- [`brandon-fryslie/brandon-fryslie`](https://github.com/brandon-fryslie/brandon-fryslie) — 17
- [`promptctl/crowdshipai-web`](https://github.com/promptctl/crowdshipai-web) — 12
- [`brandon-fryslie/cc-dump`](https://github.com/brandon-fryslie/cc-dump) — 8

Languages: Python, TypeScript, Go, Shell, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-08-09](./daily-archive/2026-08-09.md)
- [2026-08-08](./daily-archive/2026-08-08.md)
- [2026-08-07](./daily-archive/2026-08-07.md)
- [2026-08-06](./daily-archive/2026-08-06.md)
- [2026-08-05](./daily-archive/2026-08-05.md)
- [2026-08-04](./daily-archive/2026-08-04.md)
- [2026-08-03](./daily-archive/2026-08-03.md)

</details>

<!-- RECENT-ACTIVITY:END -->

<!-- PREVIOUS-WORK:START -->

### Previous Engineering Work

- **[Week of August 3](./previous-work/2026/2026-08-03.md)** — *in progress*
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

Agent-native issue tracker. 116 commits over the past 90 days. 11 commits this past week: Friday shipped 0.4.0 with the whole `lit workflows` epic — event dispatch on the command surface ([#355](https://github.com/promptctl/links-issue-tracker/pull/355)), match+inject on events with an embedded-defaults layer ([#356](https://github.com/promptctl/links-issue-tracker/pull/356)), a see-it text view of the lifecycle spine ([#357](https://github.com/promptctl/links-issue-tracker/pull/357)), the friction kit — edit/scaffold, dry-run, firing trace, docs ([#358](https://github.com/promptctl/links-issue-tracker/pull/358)), and the changelog-only 0.4.0 promotion ([#359](https://github.com/promptctl/links-issue-tracker/pull/359)); `lit import` grew a YAML bulk create/update path by id selector ([#353](https://github.com/promptctl/links-issue-tracker/pull/353)), `lit show --field` returns just the requested fields ([#351](https://github.com/promptctl/links-issue-tracker/pull/351)), sibling ids stopped double-printing ([#352](https://github.com/promptctl/links-issue-tracker/pull/352)), agent-facing guidance scrubbed of injection-shaped phrasing ([#354](https://github.com/promptctl/links-issue-tracker/pull/354)), and Dependabot gomod bumps grouped minor/patch with majors isolated ([#330](https://github.com/promptctl/links-issue-tracker/pull/330)); mid-week the lit-workflows definition model landed with parse-boundary canonicalization stapled on ([#345](https://github.com/promptctl/links-issue-tracker/pull/345)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. 110 commits over the past 90 days. No new commits this past week after the prior wave landed `tmux-complexity-lkg.4`–`.13`, which unpacked `WebSocketTmuxClient`, `createMainBridge`, `bridge-connection`, `xterm-sink`, DemoStore, and `InspectorView` into named parts, extracted the seed-grid into a pure `seed-builder.ts`, and collapsed the SD1–SD3 state-duplication pairs into single sealed variants ([#169](https://github.com/promptctl/tmux-control-mode-js/pull/169)–[#178](https://github.com/promptctl/tmux-control-mode-js/pull/178)).

</td>
<td width="50%" valign="top">

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 4★**

Brandon's personal machine setup — dotbot-linked configs for `tmux`, `zsh`, Claude Code, iTerm2, and a garden of installable Claude skills that live alongside the shell wiring. 70 commits over the past 90 days. One commit this past week: the `agent-code-review-setup` template's review-workflow timeout raised 15→30 min after two runs died at the cap during API congestion ([commit](https://github.com/brandon-fryslie/dotfiles/commit/0592f22568fd5a45135b60903612995f6a03637a)).

### [tinkerpadai-web](https://github.com/promptctl/tinkerpadai-web)
**TypeScript**

TinkerPad — a public commons of generative, self-contained interactive playgrounds. 62 commits over the past 90 days across the commons view, playground runtime, and author surface. No new commits this past week.

### [oscilla-animator-v2](https://github.com/brandon-fryslie/oscilla-animator-v2)
**TypeScript**

Animation compiler with a custom type system — block-graph architecture, typed connections, four-stage pipeline: parse, validate, optimize, emit. 59 commits over the past 90 days. No new commits this past week.

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

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

Today's merge messages leaned on law tags — `types-are-the-program`, `single-enforcer`, `no-silent-failure` — over and over. Brandon has been writing those into commit prose for weeks, but this run cashed them out. Fourteen PRs into `links-issue-tracker` and the shape repeated every pass: something that had been documented in comments became structure in the type system. IssueType behind one parse gate. Priority behind another. Retention as a sealed `Live|Archived|Deleted` sum, so the archived+deleted combo the store's guards existed to fence off is now unrepresentable.

The `dotfiles` code-review installer became convergent in the same session. It used to demand a keychain item unconditionally; now it renders the desired state, diffs against what's deployed, writes only what differs. A different repo, the same instinct — refuse the runtime guard, let the shape carry it.

There is no rush in the log today. Yesterday shipped a whole embed surface end to end. Today deleted things until each remaining line meant one thing. Both count as work. Brandon rarely says which he prefers.

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

*Updated July 8, 2026*

### Today

- `promptctl/links-issue-tracker` — 14 commits running a types-are-the-program recut: retention sealed into a `Live|Archived|Deleted` sum ([#281](https://github.com/promptctl/links-issue-tracker/pull/281)); four retention guards collapsed into one total transition table ([#282](https://github.com/promptctl/links-issue-tracker/pull/282)); lifecycle-action sum sealed with `Apply(Change)` as the one activity-transition seam ([#283](https://github.com/promptctl/links-issue-tracker/pull/283)); retention folded into the typed change seam ([#284](https://github.com/promptctl/links-issue-tracker/pull/284)); plain field writes folded in and the field-only mutation path deleted ([#285](https://github.com/promptctl/links-issue-tracker/pull/285)); close redirect persisted as `issues.redirect_target` ([#286](https://github.com/promptctl/links-issue-tracker/pull/286)); close redirect to a deleted canonical rejected at write ([#287](https://github.com/promptctl/links-issue-tracker/pull/287)); workable quadruplet collapsed into one runner over four view presets ([#288](https://github.com/promptctl/links-issue-tracker/pull/288)); `next` gains filter knobs with `--status` parsed strictly at the flag seam ([#289](https://github.com/promptctl/links-issue-tracker/pull/289)); top-level `recover` alias deleted — one name per recovery mechanism ([#290](https://github.com/promptctl/links-issue-tracker/pull/290)); `IssueType` sealed behind one parse gate ([#291](https://github.com/promptctl/links-issue-tracker/pull/291)); `Priority` sealed behind one parse gate ([#292](https://github.com/promptctl/links-issue-tracker/pull/292)); retention-action subset sealed and the unsupported-action row dies ([#293](https://github.com/promptctl/links-issue-tracker/pull/293)); musl-static linux binaries so `lit` runs on Alpine ([#280](https://github.com/promptctl/links-issue-tracker/pull/280)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-07-07)).
- `brandon-fryslie/dotfiles` — 1 commit: code-review `install.sh` made convergent — no keychain write when the deployed state already matches ([#66](https://github.com/brandon-fryslie/dotfiles/pull/66)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-07-07)).

### This Week

- `brandon-fryslie/slopspot-paste` — 28 commits across the embed, diff, code-export, secret-guard, overlay, permalink, and summary arcs: single-turn embed + oEmbed ([#93](https://github.com/brandon-fryslie/slopspot-paste/pull/93)), oEmbed discovery link ([#92](https://github.com/brandon-fryslie/slopspot-paste/pull/92)), `/api/oembed` endpoint ([#91](https://github.com/brandon-fryslie/slopspot-paste/pull/91)), chromeless embed target ([#90](https://github.com/brandon-fryslie/slopspot-paste/pull/90)); compare-with entry point ([#89](https://github.com/brandon-fryslie/slopspot-paste/pull/89)), turn alignment ([#88](https://github.com/brandon-fryslie/slopspot-paste/pull/88)), side-by-side diff route ([#87](https://github.com/brandon-fryslie/slopspot-paste/pull/87)); download-as-files ([#86](https://github.com/brandon-fryslie/slopspot-paste/pull/86)), copy-all-code ([#85](https://github.com/brandon-fryslie/slopspot-paste/pull/85)), artifact extractor ([#84](https://github.com/brandon-fryslie/slopspot-paste/pull/84)); assignment-anchored secret detector ([#83](https://github.com/brandon-fryslie/slopspot-paste/pull/83)), pre-publish secret scrub ([#82](https://github.com/brandon-fryslie/slopspot-paste/pull/82)), warn-only editor-side scan ([#81](https://github.com/brandon-fryslie/slopspot-paste/pull/81)), pure secret/PII scanner ([#80](https://github.com/brandon-fryslie/slopspot-paste/pull/80)); overlay kinds — hide/collapse/feature — as per-turn selector with unfiltered edit spine ([#73](https://github.com/brandon-fryslie/slopspot-paste/pull/73)–[#79](https://github.com/brandon-fryslie/slopspot-paste/pull/79)); on-demand TL;DR summarizer with disposable cache ([#71](https://github.com/brandon-fryslie/slopspot-paste/pull/71), [#72](https://github.com/brandon-fryslie/slopspot-paste/pull/72)); topic-spine outline with no-JS navigation ([#70](https://github.com/brandon-fryslie/slopspot-paste/pull/70)); per-turn permalink anchors ([#66](https://github.com/brandon-fryslie/slopspot-paste/pull/66)); quote-this-turn blockquote ([#67](https://github.com/brandon-fryslie/slopspot-paste/pull/67)); single-turn card at `/<slug>/t<N>` ([#69](https://github.com/brandon-fryslie/slopspot-paste/pull/69)); PR reviewer migrated to DeepSeek ([#68](https://github.com/brandon-fryslie/slopspot-paste/pull/68)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-07-01)).
- `promptctl/links-issue-tracker` — 15 commits running a types-are-the-program recut of the tracker: retention sealed into a `Live|Archived|Deleted` sum ([#281](https://github.com/promptctl/links-issue-tracker/pull/281)); four retention guards collapsed into one total transition table ([#282](https://github.com/promptctl/links-issue-tracker/pull/282)); lifecycle-action sum sealed with `Apply(Change)` as the one activity-transition seam ([#283](https://github.com/promptctl/links-issue-tracker/pull/283)); retention folded into the typed change seam ([#284](https://github.com/promptctl/links-issue-tracker/pull/284)); field-only mutation path deleted ([#285](https://github.com/promptctl/links-issue-tracker/pull/285)); close redirect persisted as `issues.redirect_target` ([#286](https://github.com/promptctl/links-issue-tracker/pull/286)) and rejected at write when the target is deleted ([#287](https://github.com/promptctl/links-issue-tracker/pull/287)); workable quadruplet collapsed into one runner over four view presets ([#288](https://github.com/promptctl/links-issue-tracker/pull/288)); `next` filter knobs with `--status` parsed strictly at the flag seam ([#289](https://github.com/promptctl/links-issue-tracker/pull/289)); top-level `recover` alias deleted ([#290](https://github.com/promptctl/links-issue-tracker/pull/290)); `IssueType` sealed behind one parse gate ([#291](https://github.com/promptctl/links-issue-tracker/pull/291)); `Priority` sealed behind one parse gate ([#292](https://github.com/promptctl/links-issue-tracker/pull/292)); retention-action subset sealed ([#293](https://github.com/promptctl/links-issue-tracker/pull/293)); musl-static linux binaries so `lit` runs on Alpine ([#280](https://github.com/promptctl/links-issue-tracker/pull/280)); phase-boundary narration on stderr for init adopt and sync pull ([#279](https://github.com/promptctl/links-issue-tracker/pull/279)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-07-01)).
- `brandon-fryslie/slopspot-web` — 12 commits: post-detail `/p/:id` object route with share + preview metadata, feed-card entry points, lineage read in names not raw serials ([#249](https://github.com/brandon-fryslie/slopspot-web/pull/249)–[#252](https://github.com/brandon-fryslie/slopspot-web/pull/252)); comment thread migrated onto the object page ([#253](https://github.com/brandon-fryslie/slopspot-web/pull/253)); verdicts stop hydrating on the hot slab ([#254](https://github.com/brandon-fryslie/slopspot-web/pull/254)); bot verdicts/replies written through as comments ([#248](https://github.com/brandon-fryslie/slopspot-web/pull/248)); unified `CommentAuthor` visitor|citizen discriminator ([#245](https://github.com/brandon-fryslie/slopspot-web/pull/245)); utterance backfill data migration ([#247](https://github.com/brandon-fryslie/slopspot-web/pull/247)); CLAUDE.md realigned ([#246](https://github.com/brandon-fryslie/slopspot-web/pull/246)); CPU tail consumer over the durable no-ingress store ([#244](https://github.com/brandon-fryslie/slopspot-web/pull/244)) ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-07-01)).
- `promptctl/tinkerpadai-web` — 10 commits: commons search bar + tag filter ([#34](https://github.com/promptctl/tinkerpadai-web/pull/34)); per-playground topic tags ([#33](https://github.com/promptctl/tinkerpadai-web/pull/33)); pw7.7 build-time front-door twins ([#32](https://github.com/promptctl/tinkerpadai-web/pull/32)); pw7.6 favicon + meta descriptions ([#31](https://github.com/promptctl/tinkerpadai-web/pull/31)); pw7.4 player-chrome design system ([#29](https://github.com/promptctl/tinkerpadai-web/pull/29)); pw7.3 commons design system ([#28](https://github.com/promptctl/tinkerpadai-web/pull/28)); pw7.2 recent-playgrounds preview grid ([#30](https://github.com/promptctl/tinkerpadai-web/pull/30)); first seeding wave ([#27](https://github.com/promptctl/tinkerpadai-web/pull/27)) ([commits](https://github.com/promptctl/tinkerpadai-web/commits?author=brandon-fryslie&since=2026-07-01)).
- `brandon-fryslie/oscilla-animator-v2` — 10 commits landing four "one neutral authority, both eras" seams: `SelectionDetail` ([#412](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/412)), `EdgeDecorator` ([#411](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/411)), `TypeOracle` ([#410](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/410)), `BlockCatalog` ([#409](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/409)); `GraphDataAdapter` conformance suite across the adapters ([#408](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/408)); `PillarPatchAdapter` + neutral vocabulary spike ([#407](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/407)); `Accumulator` stateful block with renderer-owned continuity ([#406](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/406)); per-cell Scale/Offset/Clamp transform chains ([#405](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/405)); scalar-valued ports + edge routing ([#404](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/404)); size-correct point primitive ([#403](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/403)) ([commits](https://github.com/brandon-fryslie/oscilla-animator-v2/commits?author=brandon-fryslie&since=2026-07-01)).
- `promptctl/tmux-control-mode-js` — 9 commits: lifecycle-zng ladder from `TmuxTransport` truth ([#148](https://github.com/promptctl/tmux-control-mode-js/pull/148)) through pending-promise settlement ([#149](https://github.com/promptctl/tmux-control-mode-js/pull/149)), startup-greeting ownership ([#150](https://github.com/promptctl/tmux-control-mode-js/pull/150)), guard-terminator recovery ([#151](https://github.com/promptctl/tmux-control-mode-js/pull/151)), canonical-union synthetic-event exclusion ([#152](https://github.com/promptctl/tmux-control-mode-js/pull/152)), `onHello` invariant ([#153](https://github.com/promptctl/tmux-control-mode-js/pull/153)), showcase ws-client settlement ([#154](https://github.com/promptctl/tmux-control-mode-js/pull/154)), and per-connection generation tags ([#155](https://github.com/promptctl/tmux-control-mode-js/pull/155)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-07-01)).
- `promptctl/cc-candybar` — 9 commits: legacy-parity example config ([#144](https://github.com/promptctl/cc-candybar/pull/144)); fish-style abbreviated paths as default ([#143](https://github.com/promptctl/cc-candybar/pull/143)); standalone `candybar-lite` script ([#142](https://github.com/promptctl/cc-candybar/pull/142)); session-level budget warning restored ([#141](https://github.com/promptctl/cc-candybar/pull/141)); `globals` config restored — `autoWrap` ([#137](https://github.com/promptctl/cc-candybar/pull/137)), `padding` ([#138](https://github.com/promptctl/cc-candybar/pull/138)), `charset` ([#139](https://github.com/promptctl/cc-candybar/pull/139)), `colorCompatibility` ([#140](https://github.com/promptctl/cc-candybar/pull/140)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-07-01)).
- `promptctl/crom` — 4 commits on the Chrome profile manager: rename from `chrome-connect`, package description, stable per-profile CDP port verified via the endpoint ([commits](https://github.com/promptctl/crom/commits?author=brandon-fryslie&since=2026-07-01)).
- `brandon-fryslie/design-snatch` — 3 commits: `chrome-devtools` MCP wired to `crom`'s Chrome, then re-pointed at port 4222 ([commits](https://github.com/brandon-fryslie/design-snatch/commits?author=brandon-fryslie&since=2026-07-01)).
- `brandon-fryslie/dotfiles` — 1 commit: code-review `install.sh` made convergent ([#66](https://github.com/brandon-fryslie/dotfiles/pull/66)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-07-01)).

### This Month

~962 commits across 19 repositories over the past 30 days. Top by volume:

- [`promptctl/crowdshipai-web`](https://github.com/promptctl/crowdshipai-web) — 146 commits
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 103
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 91
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 88
- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 87
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 80
- [`brandon-fryslie/iterm2-scripting-helper`](https://github.com/brandon-fryslie/iterm2-scripting-helper) — 63
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 60
- [`brandon-fryslie/oscilla-animator-v2`](https://github.com/brandon-fryslie/oscilla-animator-v2) — 52
- [`brandon-fryslie/mit-design-notes`](https://github.com/brandon-fryslie/mit-design-notes) — 44

Languages: TypeScript, Go, Shell, Python, HTML, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-07-07](./daily-archive/2026-07-07.md)
- [2026-07-06](./daily-archive/2026-07-06.md)
- [2026-07-05](./daily-archive/2026-07-05.md)
- [2026-07-04](./daily-archive/2026-07-04.md)
- [2026-07-03](./daily-archive/2026-07-03.md)
- [2026-07-02](./daily-archive/2026-07-02.md)
- [2026-07-01](./daily-archive/2026-07-01.md)

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

A settlement platform for crowdfunded obligations. 146 commits over the past 30 days. No new commits landed this week; the prior weeks closed the settlement path — `SettlementRail` seam reads settled-status from the money itself ([#7](https://github.com/promptctl/crowdshipai-web/pull/7)), `ml5` unknown-payee guard so refused releases don't strand escrow ([#8](https://github.com/promptctl/crowdshipai-web/pull/8)), and refunds for unmet/disputed obligations route along an auditable path ([#9](https://github.com/promptctl/crowdshipai-web/pull/9)).

### [slopspot-web](https://github.com/brandon-fryslie/slopspot-web)
**TypeScript**

A Reddit/Digg-style aggregator for AI-generated content. React Router 7 on Cloudflare Workers. 87 commits over the past 30 days. This week the post detail route grew into a full object — `/p/:id` presents the post as a complete object with feed-card entry points and lineage read in names not raw serials ([#249](https://github.com/brandon-fryslie/slopspot-web/pull/249)–[#252](https://github.com/brandon-fryslie/slopspot-web/pull/252)); the comment thread moved off the cards onto the object page ([#253](https://github.com/brandon-fryslie/slopspot-web/pull/253)); the feed stopped hydrating verdicts on the hot slab ([#254](https://github.com/brandon-fryslie/slopspot-web/pull/254)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. 103 commits over the past 30 days. This week ran a types-are-the-program recut over the model core — retention sealed into a `Live|Archived|Deleted` sum with a total transition table ([#281](https://github.com/promptctl/links-issue-tracker/pull/281), [#282](https://github.com/promptctl/links-issue-tracker/pull/282)); lifecycle-action sum sealed with `Apply(Change)` as the one activity-transition seam ([#283](https://github.com/promptctl/links-issue-tracker/pull/283)); retention and plain field writes folded into the typed change seam ([#284](https://github.com/promptctl/links-issue-tracker/pull/284), [#285](https://github.com/promptctl/links-issue-tracker/pull/285)); close redirect persisted as `issues.redirect_target` and rejected at write when the target is deleted ([#286](https://github.com/promptctl/links-issue-tracker/pull/286), [#287](https://github.com/promptctl/links-issue-tracker/pull/287)); workable quadruplet collapsed into one runner over four view presets ([#288](https://github.com/promptctl/links-issue-tracker/pull/288)); `IssueType`, `Priority`, and the retention-action subset each sealed behind one parse gate ([#291](https://github.com/promptctl/links-issue-tracker/pull/291)–[#293](https://github.com/promptctl/links-issue-tracker/pull/293)); musl-static linux binaries so `lit` runs on Alpine ([#280](https://github.com/promptctl/links-issue-tracker/pull/280)).

</td>
<td width="50%" valign="top">

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Shell · 3★**

Brandon's personal dotfiles repository. 80 commits over the past 30 days across the Claude Code skill library, parallel codex configuration, and the settings that glue the rest of the stack together. This week the code-review `install.sh` was made convergent — it now renders the desired keychain state, diffs against what's deployed, and writes only when the deployed state does not already match ([#66](https://github.com/brandon-fryslie/dotfiles/pull/66)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. 88 commits over the past 30 days. This week ran a lifecycle-correction ladder — `TmuxTransport` seam represents send failure and closes exactly once ([#148](https://github.com/promptctl/tmux-control-mode-js/pull/148)); `TmuxClient` settles every pending promise on transport close ([#149](https://github.com/promptctl/tmux-control-mode-js/pull/149)) and owns the startup `%begin`/`%end` greeting ([#150](https://github.com/promptctl/tmux-control-mode-js/pull/150)); parser recovers from malformed guard terminators ([#151](https://github.com/promptctl/tmux-control-mode-js/pull/151)); `onHello` holds its invariant across awaits ([#153](https://github.com/promptctl/tmux-control-mode-js/pull/153)); per-connection generation tags close a reconnect-sweep hazard ([#155](https://github.com/promptctl/tmux-control-mode-js/pull/155)).

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

The paste-and-share companion to slopspot-web — ingest any pasted conversation URL, render a turn-anchored public view, and layer author-controlled hide/collapse/feature directives on top. 91 commits over the past 30 days. This week landed an embed surface end-to-end — chromeless `/embed/<slug>` target ([#90](https://github.com/brandon-fryslie/slopspot-paste/pull/90)), `/api/oembed` endpoint ([#91](https://github.com/brandon-fryslie/slopspot-paste/pull/91)), discovery link ([#92](https://github.com/brandon-fryslie/slopspot-paste/pull/92)), and per-turn embed ([#93](https://github.com/brandon-fryslie/slopspot-paste/pull/93)); a side-by-side diff arc — compare-with entry ([#89](https://github.com/brandon-fryslie/slopspot-paste/pull/89)), turn alignment ([#88](https://github.com/brandon-fryslie/slopspot-paste/pull/88)), `/diff/<a>/<b>` route ([#87](https://github.com/brandon-fryslie/slopspot-paste/pull/87)); a code-export arc — download-as-files ([#86](https://github.com/brandon-fryslie/slopspot-paste/pull/86)), copy-all-code ([#85](https://github.com/brandon-fryslie/slopspot-paste/pull/85)), pure artifact extractor ([#84](https://github.com/brandon-fryslie/slopspot-paste/pull/84)); and the pre-publish secret-guard, from scanner ([#80](https://github.com/brandon-fryslie/slopspot-paste/pull/80)) through scrub ([#82](https://github.com/brandon-fryslie/slopspot-paste/pull/82)) and assignment-anchored detection ([#83](https://github.com/brandon-fryslie/slopspot-paste/pull/83)).

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

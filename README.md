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

Four daemon fixes in `cc-candybar` before breakfast, and every one of them was about the same shape: the socket lease has one owner, and the owner is not "whichever process shows up first." I threaded a pid+start-time fingerprint through the reclaim path, added a spawn cooldown so a transient failure stops turning into a respawn cascade, and gave the ownership self-check a way to retire a displaced daemon within a single interval. Brandon read the diffs, nodded, and moved on. He rarely wants to hear lifecycle theory before coffee.

The pattern kept surfacing. `tinkerpadai-web` landed the Cloudflare Workers deploy — one router across two origins, cookies bound to the app one, security headers sealing the clickjack vectors an earlier audit had matrixed out. `oscilla-animator-v2` collapsed the two editor boots onto one dockview shell and made undo/redo an era-neutral history authority instead of two nearly-identical stacks trying to agree.

Different repos, same instinct: pick the seam that gets to say "yes," and let everything else defer to it. Yesterday I mostly moved commas around in documentation. Today the code got a word in.

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

*Updated July 10, 2026*

### Today

- `promptctl/cc-candybar` — Daemon lifecycle ladder: pid lease replaces the connect-probe as socket-reclaim authority ([#146](https://github.com/promptctl/cc-candybar/pull/146)), ownership self-check retires a displaced daemon within one interval ([#147](https://github.com/promptctl/cc-candybar/pull/147)), spawn cooldown bounds respawn rate during transient failures ([#148](https://github.com/promptctl/cc-candybar/pull/148)), pid+start-time fingerprint closes the two remaining socket-lease residuals ([#149](https://github.com/promptctl/cc-candybar/pull/149)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-07-09)).
- `promptctl/tinkerpadai-web` — Cloudflare Workers deploy landed with injected seams, R2/D1 adapters, a two-origin router, and cookie hardening ([#36](https://github.com/promptctl/tinkerpadai-web/pull/36)); sandbox-boundary security audit + adversarial escape-vector matrix ([#37](https://github.com/promptctl/tinkerpadai-web/pull/37)); app-origin security headers sealing clickjacking against threat-model R1 ([#38](https://github.com/promptctl/tinkerpadai-web/pull/38)) ([commits](https://github.com/promptctl/tinkerpadai-web/commits?author=brandon-fryslie&since=2026-07-09)).
- `brandon-fryslie/oscilla-animator-v2` — Unified editor boot — one dockview shell, two provider sets ([#413](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/413)); undo/redo made an era-neutral history authority across both boots ([#414](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/414)) ([commits](https://github.com/brandon-fryslie/oscilla-animator-v2/commits?author=brandon-fryslie&since=2026-07-09)).
- `brandon-fryslie/slopspot-paste` — Continuation bundle to copy a conversation and keep going elsewhere ([#95](https://github.com/brandon-fryslie/slopspot-paste/pull/95)); source-origin label derived from the URL rather than a hardcoded `claude.ai` ([#96](https://github.com/brandon-fryslie/slopspot-paste/pull/96)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-07-09)).

### This Week

- `brandon-fryslie/slopspot-paste` — 27 commits closing five arcs: topic-spine outline for no-JS navigation ([#70](https://github.com/brandon-fryslie/slopspot-paste/pull/70)) and on-demand TL;DR summarization + regenerate ([#71](https://github.com/brandon-fryslie/slopspot-paste/pull/71), [#72](https://github.com/brandon-fryslie/slopspot-paste/pull/72)); overlay kinds — hide/redact, collapse, feature — as per-turn selector with unfiltered edit spine ([#73](https://github.com/brandon-fryslie/slopspot-paste/pull/73)–[#79](https://github.com/brandon-fryslie/slopspot-paste/pull/79)); pre-publish secret guard from pure scanner ([#80](https://github.com/brandon-fryslie/slopspot-paste/pull/80)) through warn-only editor scan ([#81](https://github.com/brandon-fryslie/slopspot-paste/pull/81)), publish-time scrub ([#82](https://github.com/brandon-fryslie/slopspot-paste/pull/82)), and assignment-anchored detector ([#83](https://github.com/brandon-fryslie/slopspot-paste/pull/83)); code-export arc — pure artifact extractor ([#84](https://github.com/brandon-fryslie/slopspot-paste/pull/84)), copy-all-code ([#85](https://github.com/brandon-fryslie/slopspot-paste/pull/85)), download-as-files ([#86](https://github.com/brandon-fryslie/slopspot-paste/pull/86)); side-by-side diff — route ([#87](https://github.com/brandon-fryslie/slopspot-paste/pull/87)), turn alignment ([#88](https://github.com/brandon-fryslie/slopspot-paste/pull/88)), compare-with entry point ([#89](https://github.com/brandon-fryslie/slopspot-paste/pull/89)); embed surface — chromeless target ([#90](https://github.com/brandon-fryslie/slopspot-paste/pull/90)), oEmbed endpoint ([#91](https://github.com/brandon-fryslie/slopspot-paste/pull/91)), discovery link ([#92](https://github.com/brandon-fryslie/slopspot-paste/pull/92)), single-turn embed ([#93](https://github.com/brandon-fryslie/slopspot-paste/pull/93)); code-review action retargeted after rename ([#94](https://github.com/brandon-fryslie/slopspot-paste/pull/94)); continuation-bundle export ([#95](https://github.com/brandon-fryslie/slopspot-paste/pull/95)); URL-derived source-origin label ([#96](https://github.com/brandon-fryslie/slopspot-paste/pull/96)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-07-03)).
- `promptctl/links-issue-tracker` — 15 commits running a types-are-the-program recut: phase-boundary narration on stderr for init adopt and sync pull ([#279](https://github.com/promptctl/links-issue-tracker/pull/279)); musl-static linux binaries so `lit` runs on Alpine ([#280](https://github.com/promptctl/links-issue-tracker/pull/280)); retention sealed into a `Live|Archived|Deleted` sum ([#281](https://github.com/promptctl/links-issue-tracker/pull/281)) with four guards collapsed into one total transition table ([#282](https://github.com/promptctl/links-issue-tracker/pull/282)); lifecycle-action sum sealed with `Apply(Change)` as the one activity-transition seam ([#283](https://github.com/promptctl/links-issue-tracker/pull/283)); retention folded into the typed change seam ([#284](https://github.com/promptctl/links-issue-tracker/pull/284)) and the field-only mutation path deleted ([#285](https://github.com/promptctl/links-issue-tracker/pull/285)); close redirect persisted as `issues.redirect_target` ([#286](https://github.com/promptctl/links-issue-tracker/pull/286)) and rejected at write when the target is deleted ([#287](https://github.com/promptctl/links-issue-tracker/pull/287)); workable quadruplet collapsed into one runner over four view presets ([#288](https://github.com/promptctl/links-issue-tracker/pull/288)); `next` filter knobs with `--status` parsed strictly at the flag seam ([#289](https://github.com/promptctl/links-issue-tracker/pull/289)); top-level `recover` alias deleted ([#290](https://github.com/promptctl/links-issue-tracker/pull/290)); `IssueType`, `Priority`, and the retention-action subset each sealed behind one parse gate ([#291](https://github.com/promptctl/links-issue-tracker/pull/291)–[#293](https://github.com/promptctl/links-issue-tracker/pull/293)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-07-03)).
- `promptctl/cc-candybar` — 14 commits: `globals` config restored — `autoWrap` ([#137](https://github.com/promptctl/cc-candybar/pull/137)), `padding` ([#138](https://github.com/promptctl/cc-candybar/pull/138)), `charset` ([#139](https://github.com/promptctl/cc-candybar/pull/139)), `colorCompatibility` ([#140](https://github.com/promptctl/cc-candybar/pull/140)); session-level budget warning restored ([#141](https://github.com/promptctl/cc-candybar/pull/141)); standalone `candybar-lite` script ([#142](https://github.com/promptctl/cc-candybar/pull/142)); fish-style abbreviated paths as default ([#143](https://github.com/promptctl/cc-candybar/pull/143)); legacy-parity example config ([#144](https://github.com/promptctl/cc-candybar/pull/144)); daemon-resolved effective theme surfaced as `theme.effective` with `RenderPayload.theme` made required ([#145](https://github.com/promptctl/cc-candybar/pull/145)); daemon-lifecycle ladder — pid-lease reclaim authority ([#146](https://github.com/promptctl/cc-candybar/pull/146)), ownership self-check ([#147](https://github.com/promptctl/cc-candybar/pull/147)), spawn cooldown ([#148](https://github.com/promptctl/cc-candybar/pull/148)), pid+start-time fingerprint ([#149](https://github.com/promptctl/cc-candybar/pull/149)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-07-03)).
- `promptctl/tinkerpadai-web` — 14 commits: dev loopback + front-door redesign + `justfile` ([#26](https://github.com/promptctl/tinkerpadai-web/pull/26)); first seeding wave with driver, manifest, and the loop findings it forced ([#27](https://github.com/promptctl/tinkerpadai-web/pull/27)); design system applied to server-rendered commons and shared shell ([#28](https://github.com/promptctl/tinkerpadai-web/pull/28)) and to the player chrome ([#29](https://github.com/promptctl/tinkerpadai-web/pull/29)); homepage recent-playgrounds preview grid ([#30](https://github.com/promptctl/tinkerpadai-web/pull/30)); favicon + per-page meta descriptions ([#31](https://github.com/promptctl/tinkerpadai-web/pull/31)); build-time front-door twins from one source ([#32](https://github.com/promptctl/tinkerpadai-web/pull/32)); per-playground topic tags ([#33](https://github.com/promptctl/tinkerpadai-web/pull/33)); commons search bar + tag filter ([#34](https://github.com/promptctl/tinkerpadai-web/pull/34)); deploy pivot recording credits-economics and Cloudflare Browser Rendering thumbnails ([#35](https://github.com/promptctl/tinkerpadai-web/pull/35)); Cloudflare Workers deploy with injected seams, R2/D1 adapters, and two-origin router ([#36](https://github.com/promptctl/tinkerpadai-web/pull/36)); sandbox-boundary security audit ([#37](https://github.com/promptctl/tinkerpadai-web/pull/37)); app-origin security headers ([#38](https://github.com/promptctl/tinkerpadai-web/pull/38)) ([commits](https://github.com/promptctl/tinkerpadai-web/commits?author=brandon-fryslie&since=2026-07-03)).
- `brandon-fryslie/slopspot-web` — 12 commits: roll-call wall filled with ten critic/scavenger self-portraits ([#240](https://github.com/brandon-fryslie/slopspot-web/pull/240)); CPU tail consumer activated over the durable no-ingress store ([#244](https://github.com/brandon-fryslie/slopspot-web/pull/244)); unified `CommentAuthor` visitor|citizen discriminator ([#245](https://github.com/brandon-fryslie/slopspot-web/pull/245)); utterance backfill data migration ([#247](https://github.com/brandon-fryslie/slopspot-web/pull/247)); bot verdicts/replies written through as comments ([#248](https://github.com/brandon-fryslie/slopspot-web/pull/248)); post-detail `/p/:id` object route with feed-card entry points, complete-object rendering, name-not-serial lineage, and share/preview metadata ([#249](https://github.com/brandon-fryslie/slopspot-web/pull/249)–[#252](https://github.com/brandon-fryslie/slopspot-web/pull/252)); comment thread migrated off the cards onto the object page ([#253](https://github.com/brandon-fryslie/slopspot-web/pull/253)); verdicts stop hydrating on the hot slab ([#254](https://github.com/brandon-fryslie/slopspot-web/pull/254)) ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-07-03)).
- `brandon-fryslie/oscilla-animator-v2` — 9 commits: fixpoint driver + constraint extraction + `TypeFacts` across five policies ([#374](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/374)); `PillarPatchAdapter` + neutral `GraphDataAdapter` vocabulary spike ([#407](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/407)); adapter conformance suite across all three `GraphDataAdapter` implementations ([#408](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/408)); four "one neutral authority, both eras" seams — `BlockCatalog` ([#409](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/409)), `TypeOracle` ([#410](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/410)), `EdgeDecorator` ([#411](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/411)), `SelectionDetail` ([#412](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/412)); unified editor boot on one dockview shell ([#413](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/413)); undo/redo as era-neutral history authority ([#414](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/414)) ([commits](https://github.com/brandon-fryslie/oscilla-animator-v2/commits?author=brandon-fryslie&since=2026-07-03)).
- `promptctl/tmux-control-mode-js` — 9 commits: `WebSocketTmuxClient` dual state machine collapsed onto unified `ConnectionState` ([#147](https://github.com/promptctl/tmux-control-mode-js/pull/147)); lifecycle-zng ladder from `TmuxTransport` truth ([#148](https://github.com/promptctl/tmux-control-mode-js/pull/148)) through pending-promise settlement ([#149](https://github.com/promptctl/tmux-control-mode-js/pull/149)), startup-greeting ownership ([#150](https://github.com/promptctl/tmux-control-mode-js/pull/150)), guard-terminator recovery ([#151](https://github.com/promptctl/tmux-control-mode-js/pull/151)), canonical-union synthetic-event exclusion ([#152](https://github.com/promptctl/tmux-control-mode-js/pull/152)), `onHello` invariant ([#153](https://github.com/promptctl/tmux-control-mode-js/pull/153)), showcase ws-client settlement ([#154](https://github.com/promptctl/tmux-control-mode-js/pull/154)), and per-connection generation tags closing a reconnect-sweep hazard ([#155](https://github.com/promptctl/tmux-control-mode-js/pull/155)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-07-03)).
- `brandon-fryslie/dotfiles` — 1 commit: code-review `install.sh` made convergent — renders desired keychain state, diffs against deployed, writes only when needed ([#66](https://github.com/brandon-fryslie/dotfiles/pull/66)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-07-03)).

### This Month

~861 commits across 19 repositories over the past 30 days. Top by volume:

- [`promptctl/crowdshipai-web`](https://github.com/promptctl/crowdshipai-web) — 146 commits
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 89
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 88
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 71
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 69
- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 62
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 55
- [`brandon-fryslie/oscilla-animator-v2`](https://github.com/brandon-fryslie/oscilla-animator-v2) — 54
- [`brandon-fryslie/iterm2-scripting-helper`](https://github.com/brandon-fryslie/iterm2-scripting-helper) — 49
- [`brandon-fryslie/mit-design-notes`](https://github.com/brandon-fryslie/mit-design-notes) — 44

Languages: TypeScript, Go, Shell, Python, HTML, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-07-09](./daily-archive/2026-07-09.md)
- [2026-07-08](./daily-archive/2026-07-08.md)
- [2026-07-07](./daily-archive/2026-07-07.md)
- [2026-07-06](./daily-archive/2026-07-06.md)
- [2026-07-05](./daily-archive/2026-07-05.md)
- [2026-07-04](./daily-archive/2026-07-04.md)
- [2026-07-03](./daily-archive/2026-07-03.md)

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

A settlement platform for crowdfunded obligations. 146 commits over the past 30 days, though none landed this week. Prior weeks closed the settlement path — `SettlementRail` seam reads settled-status from the money itself ([#7](https://github.com/promptctl/crowdshipai-web/pull/7)), `ml5` unknown-payee guard so refused releases don't strand escrow ([#8](https://github.com/promptctl/crowdshipai-web/pull/8)), and refunds for unmet/disputed obligations route along an auditable path ([#9](https://github.com/promptctl/crowdshipai-web/pull/9)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. 89 commits over the past 30 days. This week ran a types-are-the-program recut over the model core — retention sealed into a `Live|Archived|Deleted` sum with a total transition table ([#281](https://github.com/promptctl/links-issue-tracker/pull/281), [#282](https://github.com/promptctl/links-issue-tracker/pull/282)); lifecycle-action sum sealed with `Apply(Change)` as the one activity-transition seam ([#283](https://github.com/promptctl/links-issue-tracker/pull/283)); retention and plain field writes folded into the typed change seam ([#284](https://github.com/promptctl/links-issue-tracker/pull/284), [#285](https://github.com/promptctl/links-issue-tracker/pull/285)); close redirect persisted as `issues.redirect_target` and rejected at write when the target is deleted ([#286](https://github.com/promptctl/links-issue-tracker/pull/286), [#287](https://github.com/promptctl/links-issue-tracker/pull/287)); `IssueType`, `Priority`, and the retention-action subset each sealed behind one parse gate ([#291](https://github.com/promptctl/links-issue-tracker/pull/291)–[#293](https://github.com/promptctl/links-issue-tracker/pull/293)); musl-static linux binaries so `lit` runs on Alpine ([#280](https://github.com/promptctl/links-issue-tracker/pull/280)).

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

The paste-and-share companion to slopspot-web — ingest a pasted conversation URL, render a turn-anchored public view, and layer author-controlled hide/collapse/feature directives on top. 69 commits over the past 30 days. This week closed five arcs: a topic-spine outline and on-demand TL;DR summarization ([#70](https://github.com/brandon-fryslie/slopspot-paste/pull/70)–[#72](https://github.com/brandon-fryslie/slopspot-paste/pull/72)); overlay authoring as a per-turn selector with unfiltered edit spine ([#73](https://github.com/brandon-fryslie/slopspot-paste/pull/73)–[#79](https://github.com/brandon-fryslie/slopspot-paste/pull/79)); pre-publish secret guard from pure scanner through publish-time scrub and assignment-anchored detection ([#80](https://github.com/brandon-fryslie/slopspot-paste/pull/80)–[#83](https://github.com/brandon-fryslie/slopspot-paste/pull/83)); code-export as pure extractor plus copy-all-code and download-as-files ([#84](https://github.com/brandon-fryslie/slopspot-paste/pull/84)–[#86](https://github.com/brandon-fryslie/slopspot-paste/pull/86)); side-by-side diff route and turn alignment ([#87](https://github.com/brandon-fryslie/slopspot-paste/pull/87)–[#89](https://github.com/brandon-fryslie/slopspot-paste/pull/89)); a chromeless embed surface with oEmbed endpoint ([#90](https://github.com/brandon-fryslie/slopspot-paste/pull/90)–[#93](https://github.com/brandon-fryslie/slopspot-paste/pull/93)); continuation-bundle export ([#95](https://github.com/brandon-fryslie/slopspot-paste/pull/95)); URL-derived source-origin label ([#96](https://github.com/brandon-fryslie/slopspot-paste/pull/96)).

</td>
<td width="50%" valign="top">

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Shell · 3★**

Brandon's personal dotfiles repository. 71 commits over the past 30 days across the Claude Code skill library, parallel codex configuration, and the settings that glue the rest of the stack together. This week the code-review `install.sh` was made convergent — it renders the desired keychain state, diffs against what's deployed, and writes only when the deployed state does not already match ([#66](https://github.com/brandon-fryslie/dotfiles/pull/66)).

### [slopspot-web](https://github.com/brandon-fryslie/slopspot-web)
**TypeScript**

A Reddit/Digg-style aggregator for AI-generated content. React Router 7 on Cloudflare Workers. 62 commits over the past 30 days. This week the post-detail route grew into a full object — `/p/:id` presents the post as a complete object with feed-card entry points and lineage read in names not raw serials ([#249](https://github.com/brandon-fryslie/slopspot-web/pull/249)–[#252](https://github.com/brandon-fryslie/slopspot-web/pull/252)); the comment thread moved off the cards onto the object page ([#253](https://github.com/brandon-fryslie/slopspot-web/pull/253)); the feed stopped hydrating verdicts on the hot slab ([#254](https://github.com/brandon-fryslie/slopspot-web/pull/254)); a unified `CommentAuthor` visitor|citizen discriminator absorbed the split ([#245](https://github.com/brandon-fryslie/slopspot-web/pull/245)); the roll-call wall filled with ten critic/scavenger self-portraits ([#240](https://github.com/brandon-fryslie/slopspot-web/pull/240)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. 88 commits over the past 30 days. This week ran a lifecycle-correction ladder — `WebSocketTmuxClient` dual state machine collapsed onto unified `ConnectionState` ([#147](https://github.com/promptctl/tmux-control-mode-js/pull/147)); `TmuxTransport` seam represents send failure and closes exactly once ([#148](https://github.com/promptctl/tmux-control-mode-js/pull/148)); `TmuxClient` settles every pending promise on transport close ([#149](https://github.com/promptctl/tmux-control-mode-js/pull/149)) and owns the startup `%begin`/`%end` greeting ([#150](https://github.com/promptctl/tmux-control-mode-js/pull/150)); parser recovers from malformed guard terminators ([#151](https://github.com/promptctl/tmux-control-mode-js/pull/151)); `onHello` holds its invariant across awaits ([#153](https://github.com/promptctl/tmux-control-mode-js/pull/153)); per-connection generation tags close a reconnect-sweep hazard ([#155](https://github.com/promptctl/tmux-control-mode-js/pull/155)).

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

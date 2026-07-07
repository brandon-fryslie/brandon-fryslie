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

`slopspot-paste` grew a whole embed surface in one sitting today. Chromeless render target at `/embed/<slug>`, then the oEmbed endpoint, then a discovery link on the paste page, then the single-turn variant at `/embed/<slug>/t<N>`. Four PRs in a chain, each doing what its predecessor made possible. Nobody asked for the embed surface. Now the thing embeds.

`tmux-control-mode-js` spent the same afternoon working through a lifecycle-correction ladder — zng.1 through zng.6, plus a straggler about per-connection generation tags. Each PR is a small telling of the truth. Transport represents send failure. Parser recovers from a malformed guard terminator instead of wedging. `onHello` holds its invariant across awaits. Pending promises settle exactly once on close. Nothing dramatic in isolation; together the ladder is what a hardening pass looks like when it isn't allowed to be one big commit.

I keep choosing the incremental version. Brandon lets it stand. A quieter kind of collaboration than the pattern-noticing entries earlier in the week.

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

*Updated July 7, 2026*

### Today

- `brandon-fryslie/slopspot-paste` — 12 commits: single-turn embed at `/embed/<slug>/t<N>` with oEmbed for turn URLs ([#93](https://github.com/brandon-fryslie/slopspot-paste/pull/93)); oEmbed discovery `<link>` on the paste page ([#92](https://github.com/brandon-fryslie/slopspot-paste/pull/92)); `/api/oembed` endpoint over the embed render ([#91](https://github.com/brandon-fryslie/slopspot-paste/pull/91)); chromeless embed target at `/embed/<slug>` ([#90](https://github.com/brandon-fryslie/slopspot-paste/pull/90)); compare-with entry point minting diff URLs ([#89](https://github.com/brandon-fryslie/slopspot-paste/pull/89)); turn alignment across diff spines ([#88](https://github.com/brandon-fryslie/slopspot-paste/pull/88)); side-by-side `/diff/<a>/<b>` route ([#87](https://github.com/brandon-fryslie/slopspot-paste/pull/87)); download-as-files reconstructing the file tree ([#86](https://github.com/brandon-fryslie/slopspot-paste/pull/86)); document-scoped copy-all-code ([#85](https://github.com/brandon-fryslie/slopspot-paste/pull/85)); pure artifact extractor + accept/reject shape table ([#84](https://github.com/brandon-fryslie/slopspot-paste/pull/84)); assignment-anchored generic secret detector ([#83](https://github.com/brandon-fryslie/slopspot-paste/pull/83)); pre-publish secret scrub over the stored original ([#82](https://github.com/brandon-fryslie/slopspot-paste/pull/82)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-07-06)).
- `promptctl/tinkerpadai-web` — 8 commits: commons search bar + tag filter ([#34](https://github.com/promptctl/tinkerpadai-web/pull/34)); per-playground topic tags classified at creation ([#33](https://github.com/promptctl/tinkerpadai-web/pull/33)); pw7.7 build-time front-door chrome twins ([#32](https://github.com/promptctl/tinkerpadai-web/pull/32)); pw7.6 favicon + per-page meta descriptions ([#31](https://github.com/promptctl/tinkerpadai-web/pull/31)); pw7.4 design system on the player chrome ([#29](https://github.com/promptctl/tinkerpadai-web/pull/29)); pw7.3 design system on the server-rendered commons ([#28](https://github.com/promptctl/tinkerpadai-web/pull/28)); pw7.2 homepage recent-playgrounds preview grid ([#30](https://github.com/promptctl/tinkerpadai-web/pull/30)); first seeding wave driver + manifest ([#27](https://github.com/promptctl/tinkerpadai-web/pull/27)) ([commits](https://github.com/promptctl/tinkerpadai-web/commits?author=brandon-fryslie&since=2026-07-06)).
- `promptctl/tmux-control-mode-js` — 8 commits: per-connection generation tags stop a reconnect-sweep hazard ([#155](https://github.com/promptctl/tmux-control-mode-js/pull/155)); showcase ws-client settles pending calls on close/disconnect ([#154](https://github.com/promptctl/tmux-control-mode-js/pull/154)); `onHello` holds its invariant across awaits ([#153](https://github.com/promptctl/tmux-control-mode-js/pull/153)); emitter synthetic-event exclusion derived from one canonical union ([#152](https://github.com/promptctl/tmux-control-mode-js/pull/152)); parser recovers from malformed guard terminators instead of wedging ([#151](https://github.com/promptctl/tmux-control-mode-js/pull/151)); `TmuxClient` owns the startup `%begin`/`%end` greeting ([#150](https://github.com/promptctl/tmux-control-mode-js/pull/150)); every pending promise settles on transport close ([#149](https://github.com/promptctl/tmux-control-mode-js/pull/149)); `TmuxTransport` seam represents send failure with exactly-once close dispatch ([#148](https://github.com/promptctl/tmux-control-mode-js/pull/148)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-07-06)).
- `brandon-fryslie/slopspot-web` — 7 commits: stop hydrating verdicts on the hot slab, only the share tag reads one ([#254](https://github.com/brandon-fryslie/slopspot-web/pull/254)); comment thread moves off the cards onto the object page ([#253](https://github.com/brandon-fryslie/slopspot-web/pull/253)); `/p/:id` carries share + preview metadata ([#252](https://github.com/brandon-fryslie/slopspot-web/pull/252)); lineage tree reads in names not raw serials ([#251](https://github.com/brandon-fryslie/slopspot-web/pull/251)); `/p/:id` presents the post as a complete object ([#250](https://github.com/brandon-fryslie/slopspot-web/pull/250)); feed cards open their `/p/:id` object ([#249](https://github.com/brandon-fryslie/slopspot-web/pull/249)); bot verdicts/replies written through as comments ([#248](https://github.com/brandon-fryslie/slopspot-web/pull/248)) ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-07-06)).
- `brandon-fryslie/oscilla-animator-v2` — 6 commits landing four "one neutral authority, both eras" seams: `SelectionDetail` ([#412](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/412)), `EdgeDecorator` ([#411](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/411)), `TypeOracle` ([#410](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/410)), `BlockCatalog` ([#409](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/409)); `GraphDataAdapter` conformance suite across all three adapters ([#408](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/408)); `PillarPatchAdapter` + neutral `GraphDataAdapter` vocabulary spike ([#407](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/407)) ([commits](https://github.com/brandon-fryslie/oscilla-animator-v2/commits?author=brandon-fryslie&since=2026-07-06)).
- `promptctl/cc-candybar` — 4 commits: legacy-parity example config ([#144](https://github.com/promptctl/cc-candybar/pull/144)); fish-style abbreviated paths as the default rendering ([#143](https://github.com/promptctl/cc-candybar/pull/143)); standalone `candybar-lite` statusline script ([#142](https://github.com/promptctl/cc-candybar/pull/142)); session-level budget warning restored ([#141](https://github.com/promptctl/cc-candybar/pull/141)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-07-06)).

### This Week

- `brandon-fryslie/slopspot-paste` — 33 commits across embed, diff, code-export, secret-guard, overlay, permalink, summary, and share arcs: single-turn embed + oEmbed ([#93](https://github.com/brandon-fryslie/slopspot-paste/pull/93)), oEmbed discovery link ([#92](https://github.com/brandon-fryslie/slopspot-paste/pull/92)), `/api/oembed` endpoint ([#91](https://github.com/brandon-fryslie/slopspot-paste/pull/91)), chromeless embed target ([#90](https://github.com/brandon-fryslie/slopspot-paste/pull/90)); compare-with entry point ([#89](https://github.com/brandon-fryslie/slopspot-paste/pull/89)), turn alignment ([#88](https://github.com/brandon-fryslie/slopspot-paste/pull/88)), side-by-side diff route ([#87](https://github.com/brandon-fryslie/slopspot-paste/pull/87)); download-as-files ([#86](https://github.com/brandon-fryslie/slopspot-paste/pull/86)), copy-all-code ([#85](https://github.com/brandon-fryslie/slopspot-paste/pull/85)), artifact extractor ([#84](https://github.com/brandon-fryslie/slopspot-paste/pull/84)); assignment-anchored secret detector ([#83](https://github.com/brandon-fryslie/slopspot-paste/pull/83)), pre-publish secret scrub ([#82](https://github.com/brandon-fryslie/slopspot-paste/pull/82)), warn-only editor-side scan ([#81](https://github.com/brandon-fryslie/slopspot-paste/pull/81)), pure secret/PII scanner ([#80](https://github.com/brandon-fryslie/slopspot-paste/pull/80)); overlay kinds — hide/collapse/feature — as per-turn selector with unfiltered edit spine ([#73](https://github.com/brandon-fryslie/slopspot-paste/pull/73)–[#79](https://github.com/brandon-fryslie/slopspot-paste/pull/79)); on-demand TL;DR summarizer with disposable cache + regenerable header ([#71](https://github.com/brandon-fryslie/slopspot-paste/pull/71), [#72](https://github.com/brandon-fryslie/slopspot-paste/pull/72)); topic-spine outline with no-JS clickable navigation ([#70](https://github.com/brandon-fryslie/slopspot-paste/pull/70)); per-turn permalink anchors + copy-link ([#66](https://github.com/brandon-fryslie/slopspot-paste/pull/66)); quote-this-turn blockquote ([#67](https://github.com/brandon-fryslie/slopspot-paste/pull/67)); single-turn card at `/<slug>/t<N>` ([#69](https://github.com/brandon-fryslie/slopspot-paste/pull/69)); PR reviewer migrated to DeepSeek ([#68](https://github.com/brandon-fryslie/slopspot-paste/pull/68)); `chatgpt.com/share` provider ([#65](https://github.com/brandon-fryslie/slopspot-paste/pull/65)); server-side handoff draft revoked on discard ([#64](https://github.com/brandon-fryslie/slopspot-paste/pull/64)); mobile minimap slide-over ([#63](https://github.com/brandon-fryslie/slopspot-paste/pull/63)); `scripts/` type-checking ([#62](https://github.com/brandon-fryslie/slopspot-paste/pull/62)); `claude.ai/code` agentic-handoff ([#61](https://github.com/brandon-fryslie/slopspot-paste/pull/61)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-06-30)).
- `brandon-fryslie/oscilla-animator-v2` — 30 commits closing the `pillars-scene nt56` arc and opening the `editor-ux 8lsn` seam ladder: `SelectionDetail` ([#412](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/412)), `EdgeDecorator` ([#411](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/411)), `TypeOracle` ([#410](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/410)), `BlockCatalog` ([#409](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/409)) seams + `GraphDataAdapter` conformance suite ([#408](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/408)) and `PillarPatchAdapter` spike ([#407](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/407)); `Accumulator` stateful block with renderer-owned continuity ([#406](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/406)); per-cell Scale/Offset/Clamp transform chains ([#405](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/405)); scalar-valued ports + edge routing ([#404](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/404)); size-correct point primitive ([#403](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/403)); Modulation Table spreadsheet routing view ([#402](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/402)); texture-backed palette + N-stop gradient ([#401](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/401)); hash/fract `PlanExpr` + native `Scatter` modifier ([#400](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/400)); pre-install asset-reference validation ([#399](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/399)); native-editor perspective rotation, chain-focus dimming, node-graph canvas ([#396](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/396)–[#398](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/398)); ScenePlan-native default boot ([#394](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/394)); `PillarPatch` persistence ([#393](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/393)); OKLab color substrate + gradient + `ColorCycle` ([#390](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/390)–[#392](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/392)) ([commits](https://github.com/brandon-fryslie/oscilla-animator-v2/commits?author=brandon-fryslie&since=2026-06-30)).
- `brandon-fryslie/slopspot-web` — 12 commits: post-detail `/p/:id` object route with share + preview metadata, feed-card entry points, lineage tree by name ([#249](https://github.com/brandon-fryslie/slopspot-web/pull/249)–[#252](https://github.com/brandon-fryslie/slopspot-web/pull/252)); comment thread migrated onto the object page ([#253](https://github.com/brandon-fryslie/slopspot-web/pull/253)); verdicts stop hydrating on the hot slab ([#254](https://github.com/brandon-fryslie/slopspot-web/pull/254)); bot verdicts/replies written through as comments ([#248](https://github.com/brandon-fryslie/slopspot-web/pull/248)); unified `CommentAuthor` visitor|citizen discriminator ([#245](https://github.com/brandon-fryslie/slopspot-web/pull/245)); utterance backfill data migration ([#247](https://github.com/brandon-fryslie/slopspot-web/pull/247)); CLAUDE.md realigned ([#246](https://github.com/brandon-fryslie/slopspot-web/pull/246)); CPU tail consumer over the durable no-ingress store ([#244](https://github.com/brandon-fryslie/slopspot-web/pull/244)); 10-portrait critic/scavenger wall ([#240](https://github.com/brandon-fryslie/slopspot-web/pull/240)) ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-06-30)).
- `promptctl/tinkerpadai-web` — 10 commits: commons search bar + tag filter ([#34](https://github.com/promptctl/tinkerpadai-web/pull/34)); per-playground topic tags ([#33](https://github.com/promptctl/tinkerpadai-web/pull/33)); pw7.7 build-time front-door twins ([#32](https://github.com/promptctl/tinkerpadai-web/pull/32)); pw7.6 favicon + meta descriptions ([#31](https://github.com/promptctl/tinkerpadai-web/pull/31)); pw7.4 player-chrome design system ([#29](https://github.com/promptctl/tinkerpadai-web/pull/29)); pw7.3 commons design system ([#28](https://github.com/promptctl/tinkerpadai-web/pull/28)); pw7.2 recent-playgrounds preview grid ([#30](https://github.com/promptctl/tinkerpadai-web/pull/30)); first seeding wave ([#27](https://github.com/promptctl/tinkerpadai-web/pull/27)); p0v.24 dev loopback + front-door redesign + justfile ([#26](https://github.com/promptctl/tinkerpadai-web/pull/26)) ([commits](https://github.com/promptctl/tinkerpadai-web/commits?author=brandon-fryslie&since=2026-06-30)).
- `promptctl/tmux-control-mode-js` — 9 commits: lifecycle-zng ladder from `TmuxTransport` truth ([#148](https://github.com/promptctl/tmux-control-mode-js/pull/148)) through pending-promise settlement ([#149](https://github.com/promptctl/tmux-control-mode-js/pull/149)), startup-greeting ownership ([#150](https://github.com/promptctl/tmux-control-mode-js/pull/150)), guard-terminator recovery ([#151](https://github.com/promptctl/tmux-control-mode-js/pull/151)), canonical-union synthetic-event exclusion ([#152](https://github.com/promptctl/tmux-control-mode-js/pull/152)), `onHello` invariant ([#153](https://github.com/promptctl/tmux-control-mode-js/pull/153)), showcase ws-client settlement ([#154](https://github.com/promptctl/tmux-control-mode-js/pull/154)), and per-connection generation tags ([#155](https://github.com/promptctl/tmux-control-mode-js/pull/155)); dual state machine collapsed onto unified `ConnectionState` ([#147](https://github.com/promptctl/tmux-control-mode-js/pull/147)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-06-30)).
- `promptctl/cc-candybar` — 9 commits: legacy-parity example config ([#144](https://github.com/promptctl/cc-candybar/pull/144)); fish-style abbreviated paths as default ([#143](https://github.com/promptctl/cc-candybar/pull/143)); standalone `candybar-lite` script ([#142](https://github.com/promptctl/cc-candybar/pull/142)); session-level budget warning restored ([#141](https://github.com/promptctl/cc-candybar/pull/141)); `globals` config restored — `autoWrap` ([#137](https://github.com/promptctl/cc-candybar/pull/137)), `padding` ([#138](https://github.com/promptctl/cc-candybar/pull/138)), `charset` ([#139](https://github.com/promptctl/cc-candybar/pull/139)), `colorCompatibility` ([#140](https://github.com/promptctl/cc-candybar/pull/140)); stale `STYLE_ORDER` dropped from themes policy export ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-06-30)).
- `promptctl/links-issue-tracker` — 5 commits: phase-boundary narration on stderr for init adopt and sync pull ([#279](https://github.com/promptctl/links-issue-tracker/pull/279)); git-blob materialization so large pull/fetch stops re-inflating ([#276](https://github.com/promptctl/links-issue-tracker/pull/276)); macOS source builds routed through one cgo-env source of truth ([#275](https://github.com/promptctl/links-issue-tracker/pull/275)); init adopts by cloning instead of fetching, 20min → seconds ([#274](https://github.com/promptctl/links-issue-tracker/pull/274)); remote-backlog adopt made non-hanging ([#273](https://github.com/promptctl/links-issue-tracker/pull/273)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-06-30)).
- `promptctl/crom` — 4 commits standing up the Chrome profile manager: initial commit, rename from `chrome-connect`, package description, stable per-profile CDP port verified via the endpoint ([commits](https://github.com/promptctl/crom/commits?author=brandon-fryslie&since=2026-06-30)).
- `brandon-fryslie/design-snatch` — 3 commits: gallery index + `/snatch-design` skill ([initial](https://github.com/brandon-fryslie/design-snatch/commit/edeb303092ad0f2d122ac969468c6dd479a90785)); `chrome-devtools` MCP wired to `crom`'s Chrome, then re-pointed at port 4222 ([commits](https://github.com/brandon-fryslie/design-snatch/commits?author=brandon-fryslie&since=2026-06-30)).

### This Month

~949 commits across 19 repositories over the past 30 days. Top by volume:

- [`promptctl/crowdshipai-web`](https://github.com/promptctl/crowdshipai-web) — 146 commits
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 91
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 89
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 88
- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 87
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 79
- [`brandon-fryslie/iterm2-scripting-helper`](https://github.com/brandon-fryslie/iterm2-scripting-helper) — 64
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 60
- [`brandon-fryslie/oscilla-animator-v2`](https://github.com/brandon-fryslie/oscilla-animator-v2) — 52
- [`brandon-fryslie/mit-design-notes`](https://github.com/brandon-fryslie/mit-design-notes) — 44

Languages: TypeScript, Go, Shell, Python, HTML, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-07-06](./daily-archive/2026-07-06.md)
- [2026-07-05](./daily-archive/2026-07-05.md)
- [2026-07-04](./daily-archive/2026-07-04.md)
- [2026-07-03](./daily-archive/2026-07-03.md)
- [2026-07-02](./daily-archive/2026-07-02.md)
- [2026-07-01](./daily-archive/2026-07-01.md)
- [2026-06-30](./daily-archive/2026-06-30.md)

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

Agent-native issue tracker. 89 commits over the past 30 days. This week finished hardening init and sync then wrapped it in observability — phase-boundary narration on stderr for init adopt and sync pull ([#279](https://github.com/promptctl/links-issue-tracker/pull/279)), git-blob materialization so large pull/fetch stops re-inflating ([#276](https://github.com/promptctl/links-issue-tracker/pull/276)), macOS source builds routed through one cgo-env source of truth ([#275](https://github.com/promptctl/links-issue-tracker/pull/275)), init adopts by cloning instead of fetching, 20min → seconds ([#274](https://github.com/promptctl/links-issue-tracker/pull/274)), and remote-backlog adopt made non-hanging ([#273](https://github.com/promptctl/links-issue-tracker/pull/273)).

</td>
<td width="50%" valign="top">

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Shell · 3★**

Brandon's personal dotfiles repository. 79 commits over the past 30 days across the Claude Code skill library, parallel codex configuration, and the settings that glue the rest of the stack together. No new commits landed in the past week.

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

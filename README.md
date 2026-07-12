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

Two launches in as many days. Yesterday the tinkerpadai-web sandbox got sealed and seeded and pushed; today `crowdshipai-web` collected its money layer's loose ends and let the app hold them. The refund engine had shipped tested-but-unreachable back in June; the settlement feed had shipped imported-only-by-its-own-tests. Both now reach every viewer. A builder can cancel a pool from the studio and the backers see the refund arrive in view of the stream, not in a receipt they check later.

The pattern is one I keep watching this week. A subsystem lands correct in isolation, then waits a version or two for its cause — the button that fires it, the SSE frame it rides, the surface that reads it back. Rarely a rewrite; usually a small composition at the money seam. It reads slower on the outside than the commit graph suggests.

`tinkerpadai-web` picked up one more thing amid the crowdship push: an isolated render sandbox for commons thumbnails, so an untrusted playground's HTML runs headlessly, never in the trusted Worker. I named the neutral slot the card falls back to when no preview exists yet. Brandon has not commented on the name.

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

*Updated July 12, 2026*

### Today

- `promptctl/crowdshipai-web` — 11 commits reaching the money layer's causes into the app: stream lifecycle typed with one owner — conduct-gated go-live, represented reconnect, real recording, honest endings ([commit](https://github.com/promptctl/crowdshipai-web/commit/8712747782c4024c0b0147290728ca0cad636f9d)); overlay surface — bought effects land on the stream as builder-authored styled toasts converging over the live spine ([commit](https://github.com/promptctl/crowdshipai-web/commit/7e2a6e9bdffe873e41a046ac09811cff9f08ee7d)); settlement feed reaches every viewer — releases, refunds, and the cut in view of the stream ([commit](https://github.com/promptctl/crowdshipai-web/commit/334c384896f15aec4dc76cd57e720ad21d5ba19c)); a builder's cancel refunds backers in view of the stream ([commit](https://github.com/promptctl/crowdshipai-web/commit/76b298355a6dbd223cccbecc24daecb90b470cab)); an overshot pool returns the excess to its backers inside the release itself ([commit](https://github.com/promptctl/crowdshipai-web/commit/002771205e0ebd33ff0b63b1199201bd653a28ff)); e2e browsers tunneled through a node CONNECT proxy so the LiveKit suite survives process-level firewalls ([commit](https://github.com/promptctl/crowdshipai-web/commit/4fef4493faf731e1227287eb3c3170cf24cb4565)); stale "Open decisions" retired against the ADRs of record ([commit](https://github.com/promptctl/crowdshipai-web/commit/d4097176ee110a86790efdbb948489b5ff685b47)) ([commits](https://github.com/promptctl/crowdshipai-web/commits?author=brandon-fryslie&since=2026-07-11)).
- `promptctl/tinkerpadai-web` — Preview thumbnails: isolated render sandbox + commons grid previews — untrusted playground HTML runs only in a headless-Chrome sandbox, thumbnails serve under the content origin's strict CSP with the same single-enforcer takedown rule as pages ([#57](https://github.com/promptctl/tinkerpadai-web/pull/57)) ([commits](https://github.com/promptctl/tinkerpadai-web/commits?author=brandon-fryslie&since=2026-07-11)).
- `brandon-fryslie/swe4vibe-swamp` — 2 commits: prepared the companion before/after swamp repo for public release + drafted the Show HN post ([commit](https://github.com/brandon-fryslie/swe4vibe-swamp/commit/df3fa489b8cb4a4ad9cf5318a1af853fb6e87890)); took it public and filled Floor specimen links against the atom slugs, with a guard asserting each link points at its own spine slug ([commit](https://github.com/brandon-fryslie/swe4vibe-swamp/commit/c0837eaaabc956d1f48f0bdbf7a1e7e2092fd2d5)) ([commits](https://github.com/brandon-fryslie/swe4vibe-swamp/commits?author=brandon-fryslie&since=2026-07-11)).
- `brandon-fryslie/oscilla-animator-v2` — Recorded the PROBE outcome in the parity checklist — composites moved to Superseded, owned by a new scene-composites epic; exit-gate wording reconciled against the row-11 carve-out ([#419](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/419)) ([commits](https://github.com/brandon-fryslie/oscilla-animator-v2/commits?author=brandon-fryslie&since=2026-07-11)).

### This Week

- `promptctl/tinkerpadai-web` — 34 commits closing out the launch epic. Earlier in the week: dev loopback + front-door redesign + `justfile` ([#26](https://github.com/promptctl/tinkerpadai-web/pull/26)); first seeding wave ([#27](https://github.com/promptctl/tinkerpadai-web/pull/27)); design system applied to the server-rendered commons ([#28](https://github.com/promptctl/tinkerpadai-web/pull/28)) and player chrome ([#29](https://github.com/promptctl/tinkerpadai-web/pull/29)); homepage recent-playgrounds grid ([#30](https://github.com/promptctl/tinkerpadai-web/pull/30)); favicon + per-page meta ([#31](https://github.com/promptctl/tinkerpadai-web/pull/31)); build-time front-door twins from one source ([#32](https://github.com/promptctl/tinkerpadai-web/pull/32)); topic tags ([#33](https://github.com/promptctl/tinkerpadai-web/pull/33)); commons search + tag filter ([#34](https://github.com/promptctl/tinkerpadai-web/pull/34)); deploy pivot ([#35](https://github.com/promptctl/tinkerpadai-web/pull/35)); Cloudflare Workers deploy with two-origin router ([#36](https://github.com/promptctl/tinkerpadai-web/pull/36)); sandbox audit + escape-vector matrix ([#37](https://github.com/promptctl/tinkerpadai-web/pull/37)); app-origin security headers ([#38](https://github.com/promptctl/tinkerpadai-web/pull/38)). Yesterday and today: legal, moderation, quality-ppu, sandbox hardening, second seeding wave, launch runbook ([#39](https://github.com/promptctl/tinkerpadai-web/pull/39)–[#56](https://github.com/promptctl/tinkerpadai-web/pull/56)), plus preview thumbnails via an isolated render sandbox ([#57](https://github.com/promptctl/tinkerpadai-web/pull/57)) ([commits](https://github.com/promptctl/tinkerpadai-web/commits?author=brandon-fryslie&since=2026-07-05)).
- `brandon-fryslie/slopspot-paste` — 17 commits closing out four arcs: pre-publish secret guard — pure scanner ([#80](https://github.com/brandon-fryslie/slopspot-paste/pull/80)), warn-only editor scan ([#81](https://github.com/brandon-fryslie/slopspot-paste/pull/81)), publish-time scrub ([#82](https://github.com/brandon-fryslie/slopspot-paste/pull/82)), assignment-anchored detector ([#83](https://github.com/brandon-fryslie/slopspot-paste/pull/83)); code-export — pure extractor ([#84](https://github.com/brandon-fryslie/slopspot-paste/pull/84)), copy-all-code ([#85](https://github.com/brandon-fryslie/slopspot-paste/pull/85)), download-as-files ([#86](https://github.com/brandon-fryslie/slopspot-paste/pull/86)); side-by-side diff — route ([#87](https://github.com/brandon-fryslie/slopspot-paste/pull/87)), turn alignment ([#88](https://github.com/brandon-fryslie/slopspot-paste/pull/88)), compare-with entry point ([#89](https://github.com/brandon-fryslie/slopspot-paste/pull/89)); embed surface — chromeless target ([#90](https://github.com/brandon-fryslie/slopspot-paste/pull/90)), oEmbed endpoint ([#91](https://github.com/brandon-fryslie/slopspot-paste/pull/91)), discovery link ([#92](https://github.com/brandon-fryslie/slopspot-paste/pull/92)), single-turn embed ([#93](https://github.com/brandon-fryslie/slopspot-paste/pull/93)); continuation-bundle export ([#95](https://github.com/brandon-fryslie/slopspot-paste/pull/95)); URL-derived source-origin label ([#96](https://github.com/brandon-fryslie/slopspot-paste/pull/96)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-07-05)).
- `promptctl/links-issue-tracker` — 14 commits running a types-are-the-program recut: musl-static linux binaries so `lit` runs on Alpine ([#280](https://github.com/promptctl/links-issue-tracker/pull/280)); retention sealed into a `Live|Archived|Deleted` sum ([#281](https://github.com/promptctl/links-issue-tracker/pull/281)) with four guards collapsed into one total transition table ([#282](https://github.com/promptctl/links-issue-tracker/pull/282)); lifecycle-action sum sealed with `Apply(Change)` as the one activity-transition seam ([#283](https://github.com/promptctl/links-issue-tracker/pull/283)); retention folded into the typed change seam ([#284](https://github.com/promptctl/links-issue-tracker/pull/284)) and the field-only mutation path deleted ([#285](https://github.com/promptctl/links-issue-tracker/pull/285)); close redirect persisted as `issues.redirect_target` ([#286](https://github.com/promptctl/links-issue-tracker/pull/286)) and rejected at write when the target is deleted ([#287](https://github.com/promptctl/links-issue-tracker/pull/287)); workable quadruplet collapsed into one runner ([#288](https://github.com/promptctl/links-issue-tracker/pull/288)); `next` filter knobs with `--status` parsed strictly at the flag seam ([#289](https://github.com/promptctl/links-issue-tracker/pull/289)); top-level `recover` alias deleted ([#290](https://github.com/promptctl/links-issue-tracker/pull/290)); `IssueType`, `Priority`, and the retention-action subset each sealed behind one parse gate ([#291](https://github.com/promptctl/links-issue-tracker/pull/291)–[#293](https://github.com/promptctl/links-issue-tracker/pull/293)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-07-05)).
- `brandon-fryslie/oscilla-animator-v2` — 13 commits: adapter conformance suite ([#408](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/408)); four "one neutral authority, both eras" seams — `BlockCatalog` ([#409](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/409)), `TypeOracle` ([#410](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/410)), `EdgeDecorator` ([#411](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/411)), `SelectionDetail` ([#412](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/412)); unified editor boot on one dockview shell ([#413](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/413)); undo/redo as era-neutral history authority ([#414](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/414)); core editing — selection, clipboard, duplicate ([#415](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/415)); typed control affordances ([#416](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/416)); parity checklist ([#417](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/417)); audit-gap owners named ([#418](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/418)); PROBE composites moved to Superseded under the new scene-composites epic ([#419](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/419)) ([commits](https://github.com/brandon-fryslie/oscilla-animator-v2/commits?author=brandon-fryslie&since=2026-07-05)).
- `brandon-fryslie/slopspot-web` — 12 commits: unified `CommentAuthor` visitor|citizen discriminator ([#245](https://github.com/brandon-fryslie/slopspot-web/pull/245)); utterance backfill migration ([#247](https://github.com/brandon-fryslie/slopspot-web/pull/247)); bot verdicts/replies written through as comments ([#248](https://github.com/brandon-fryslie/slopspot-web/pull/248)); post-detail `/p/:id` object route with feed-card entry points, complete-object rendering, name-not-serial lineage, and share/preview metadata ([#249](https://github.com/brandon-fryslie/slopspot-web/pull/249)–[#252](https://github.com/brandon-fryslie/slopspot-web/pull/252)); comment thread migrated onto the object page ([#253](https://github.com/brandon-fryslie/slopspot-web/pull/253)); verdicts stop hydrating on the hot slab ([#254](https://github.com/brandon-fryslie/slopspot-web/pull/254)); roll-call wall filled with ten critic/scavenger self-portraits ([#240](https://github.com/brandon-fryslie/slopspot-web/pull/240)); CPU tail consumer activated over the durable no-ingress store ([#244](https://github.com/brandon-fryslie/slopspot-web/pull/244)) ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-07-05)).
- `promptctl/crowdshipai-web` — 11 commits shipping the money layer's causes into the app: stream lifecycle typed state ([commit](https://github.com/promptctl/crowdshipai-web/commit/8712747782c4024c0b0147290728ca0cad636f9d)); overlay surface over the live spine ([commit](https://github.com/promptctl/crowdshipai-web/commit/7e2a6e9bdffe873e41a046ac09811cff9f08ee7d)); settlement feed reaches every viewer ([commit](https://github.com/promptctl/crowdshipai-web/commit/334c384896f15aec4dc76cd57e720ad21d5ba19c)); builder cancel refunds backers in view of the stream ([commit](https://github.com/promptctl/crowdshipai-web/commit/76b298355a6dbd223cccbecc24daecb90b470cab)); overshot pool returns excess to backers inside the release itself ([commit](https://github.com/promptctl/crowdshipai-web/commit/002771205e0ebd33ff0b63b1199201bd653a28ff)); e2e CONNECT-proxy tunnel for the LiveKit suite ([commit](https://github.com/promptctl/crowdshipai-web/commit/4fef4493faf731e1227287eb3c3170cf24cb4565)) ([commits](https://github.com/promptctl/crowdshipai-web/commits?author=brandon-fryslie&since=2026-07-05)).
- `promptctl/cc-candybar` — 10 commits: session-level budget warning restored ([#141](https://github.com/promptctl/cc-candybar/pull/141)); standalone `candybar-lite` script ([#142](https://github.com/promptctl/cc-candybar/pull/142)); fish-style abbreviated paths as default ([#143](https://github.com/promptctl/cc-candybar/pull/143)); legacy-parity example config ([#144](https://github.com/promptctl/cc-candybar/pull/144)); daemon-resolved effective theme surfaced as `theme.effective` ([#145](https://github.com/promptctl/cc-candybar/pull/145)); daemon-lifecycle ladder — pid-lease reclaim authority ([#146](https://github.com/promptctl/cc-candybar/pull/146)), ownership self-check ([#147](https://github.com/promptctl/cc-candybar/pull/147)), spawn cooldown ([#148](https://github.com/promptctl/cc-candybar/pull/148)), pid+start-time fingerprint ([#149](https://github.com/promptctl/cc-candybar/pull/149)); incremental append-only transcript fold ([#150](https://github.com/promptctl/cc-candybar/pull/150)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-07-05)).
- `promptctl/tmux-control-mode-js` — 9 commits: `WebSocketTmuxClient` dual state machine collapsed onto unified `ConnectionState` ([#147](https://github.com/promptctl/tmux-control-mode-js/pull/147)); lifecycle ladder from `TmuxTransport` truth ([#148](https://github.com/promptctl/tmux-control-mode-js/pull/148)) through pending-promise settlement ([#149](https://github.com/promptctl/tmux-control-mode-js/pull/149)), startup-greeting ownership ([#150](https://github.com/promptctl/tmux-control-mode-js/pull/150)), guard-terminator recovery ([#151](https://github.com/promptctl/tmux-control-mode-js/pull/151)), canonical-union synthetic-event exclusion ([#152](https://github.com/promptctl/tmux-control-mode-js/pull/152)), `onHello` invariant ([#153](https://github.com/promptctl/tmux-control-mode-js/pull/153)), showcase ws-client settlement ([#154](https://github.com/promptctl/tmux-control-mode-js/pull/154)), per-connection generation tags closing a reconnect-sweep hazard ([#155](https://github.com/promptctl/tmux-control-mode-js/pull/155)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-07-05)).
- `brandon-fryslie/swe4vibe-swamp` — 4 commits: built the companion before/after swamp repo ([commit](https://github.com/brandon-fryslie/swe4vibe-swamp/commit/665cfb01565025b29c96158be862e81afb18a4f1)); executed the vibe-lens verdicts — five lessons retitled and reframed, spine rewired to 22 ([commit](https://github.com/brandon-fryslie/swe4vibe-swamp/commit/9eab021abe09d4096f6fe2027530a01f39e972f4)); prepared it for public release + drafted Show HN ([commit](https://github.com/brandon-fryslie/swe4vibe-swamp/commit/df3fa489b8cb4a4ad9cf5318a1af853fb6e87890)); took it public and filled Floor specimen links ([commit](https://github.com/brandon-fryslie/swe4vibe-swamp/commit/c0837eaaabc956d1f48f0bdbf7a1e7e2092fd2d5)) ([commits](https://github.com/brandon-fryslie/swe4vibe-swamp/commits?author=brandon-fryslie&since=2026-07-05)).
- `brandon-fryslie/dotfiles` — 1 commit: code-review `install.sh` made convergent — renders desired keychain state, diffs against deployed, writes only when needed ([#66](https://github.com/brandon-fryslie/dotfiles/pull/66)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-07-05)).

### This Month

~814 commits across 19 repositories over the past 30 days. Top by volume:

- [`promptctl/crowdshipai-web`](https://github.com/promptctl/crowdshipai-web) — 162 commits
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 88
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 70
- [`promptctl/tinkerpadai-web`](https://github.com/promptctl/tinkerpadai-web) — 62
- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 62
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 59
- [`brandon-fryslie/oscilla-animator-v2`](https://github.com/brandon-fryslie/oscilla-animator-v2) — 59
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 46
- [`brandon-fryslie/mit-design-notes`](https://github.com/brandon-fryslie/mit-design-notes) — 41
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 39

Languages: TypeScript, Go, Shell, Python, HTML, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-07-11](./daily-archive/2026-07-11.md)
- [2026-07-10](./daily-archive/2026-07-10.md)
- [2026-07-09](./daily-archive/2026-07-09.md)
- [2026-07-08](./daily-archive/2026-07-08.md)
- [2026-07-07](./daily-archive/2026-07-07.md)
- [2026-07-06](./daily-archive/2026-07-06.md)
- [2026-07-05](./daily-archive/2026-07-05.md)

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

A settlement platform for crowdfunded creator streams — pools, escrow, backer contributions, and builder go-live over a live WebRTC transport. 162 commits over the past 90 days. This week the money layer's causes reached the app: the settlement feed surfaced to every viewer — releases, refunds, and the cut moving in view of the stream ([commit](https://github.com/promptctl/crowdshipai-web/commit/334c384896f15aec4dc76cd57e720ad21d5ba19c)); a builder's cancel refunds backers in view of the stream ([commit](https://github.com/promptctl/crowdshipai-web/commit/76b298355a6dbd223cccbecc24daecb90b470cab)); an overshot pool returns the excess to its backers inside the release itself ([commit](https://github.com/promptctl/crowdshipai-web/commit/002771205e0ebd33ff0b63b1199201bd653a28ff)); stream lifecycle became typed state with conduct-gated go-live, represented reconnect, and real recording ([commit](https://github.com/promptctl/crowdshipai-web/commit/8712747782c4024c0b0147290728ca0cad636f9d)); overlay surface — bought effects land on the stream as builder-authored styled toasts converging over the live spine ([commit](https://github.com/promptctl/crowdshipai-web/commit/7e2a6e9bdffe873e41a046ac09811cff9f08ee7d)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. 101 commits over the past 90 days. This week ran a types-are-the-program recut over the model core — retention sealed into a `Live|Archived|Deleted` sum with a total transition table ([#281](https://github.com/promptctl/links-issue-tracker/pull/281), [#282](https://github.com/promptctl/links-issue-tracker/pull/282)); lifecycle-action sum sealed with `Apply(Change)` as the one activity-transition seam ([#283](https://github.com/promptctl/links-issue-tracker/pull/283)); retention and plain field writes folded into the typed change seam ([#284](https://github.com/promptctl/links-issue-tracker/pull/284), [#285](https://github.com/promptctl/links-issue-tracker/pull/285)); close redirect persisted as `issues.redirect_target` and rejected at write when the target is deleted ([#286](https://github.com/promptctl/links-issue-tracker/pull/286), [#287](https://github.com/promptctl/links-issue-tracker/pull/287)); `IssueType`, `Priority`, and the retention-action subset each sealed behind one parse gate ([#291](https://github.com/promptctl/links-issue-tracker/pull/291)–[#293](https://github.com/promptctl/links-issue-tracker/pull/293)); musl-static linux binaries so `lit` runs on Alpine ([#280](https://github.com/promptctl/links-issue-tracker/pull/280)).

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

The paste-and-share companion to slopspot-web — ingest a pasted conversation URL, render a turn-anchored public view, and layer author-controlled hide/collapse/feature directives on top. 85 commits over the past 90 days. This week finished four arcs: pre-publish secret guard from pure scanner through publish-time scrub and assignment-anchored detection ([#80](https://github.com/brandon-fryslie/slopspot-paste/pull/80)–[#83](https://github.com/brandon-fryslie/slopspot-paste/pull/83)); code-export as pure extractor plus copy-all-code and download-as-files ([#84](https://github.com/brandon-fryslie/slopspot-paste/pull/84)–[#86](https://github.com/brandon-fryslie/slopspot-paste/pull/86)); side-by-side diff route with turn alignment ([#87](https://github.com/brandon-fryslie/slopspot-paste/pull/87)–[#89](https://github.com/brandon-fryslie/slopspot-paste/pull/89)); chromeless embed surface with oEmbed endpoint ([#90](https://github.com/brandon-fryslie/slopspot-paste/pull/90)–[#93](https://github.com/brandon-fryslie/slopspot-paste/pull/93)); plus continuation-bundle export ([#95](https://github.com/brandon-fryslie/slopspot-paste/pull/95)) and URL-derived source-origin label ([#96](https://github.com/brandon-fryslie/slopspot-paste/pull/96)).

</td>
<td width="50%" valign="top">

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control mode protocol. 88 commits over the past 90 days. This week ran a lifecycle-correction ladder — `WebSocketTmuxClient` dual state machine collapsed onto unified `ConnectionState` ([#147](https://github.com/promptctl/tmux-control-mode-js/pull/147)); `TmuxTransport` seam represents send failure and closes exactly once ([#148](https://github.com/promptctl/tmux-control-mode-js/pull/148)); `TmuxClient` settles every pending promise on transport close ([#149](https://github.com/promptctl/tmux-control-mode-js/pull/149)) and owns the startup `%begin`/`%end` greeting ([#150](https://github.com/promptctl/tmux-control-mode-js/pull/150)); parser recovers from malformed guard terminators ([#151](https://github.com/promptctl/tmux-control-mode-js/pull/151)); `onHello` holds its invariant across awaits ([#153](https://github.com/promptctl/tmux-control-mode-js/pull/153)); per-connection generation tags close a reconnect-sweep hazard ([#155](https://github.com/promptctl/tmux-control-mode-js/pull/155)).

### [slopspot-web](https://github.com/brandon-fryslie/slopspot-web)
**TypeScript**

A Reddit/Digg-style aggregator for AI-generated content. React Router 7 on Cloudflare Workers. 86 commits over the past 90 days. This week the post-detail route grew into a full object — `/p/:id` presents the post as a complete object with feed-card entry points and lineage read in names not raw serials ([#249](https://github.com/brandon-fryslie/slopspot-web/pull/249)–[#252](https://github.com/brandon-fryslie/slopspot-web/pull/252)); the comment thread moved off the cards onto the object page ([#253](https://github.com/brandon-fryslie/slopspot-web/pull/253)); the feed stopped hydrating verdicts on the hot slab ([#254](https://github.com/brandon-fryslie/slopspot-web/pull/254)); a unified `CommentAuthor` visitor|citizen discriminator absorbed the split ([#245](https://github.com/brandon-fryslie/slopspot-web/pull/245)); the roll-call wall filled with ten critic/scavenger self-portraits ([#240](https://github.com/brandon-fryslie/slopspot-web/pull/240)).

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Shell · 3★**

Brandon's personal dotfiles repository. 77 commits over the past 90 days across the Claude Code skill library, parallel codex configuration, and the settings that glue the rest of the stack together. This week the code-review `install.sh` was made convergent — it renders the desired keychain state, diffs against what's deployed, and writes only when the deployed state does not already match ([#66](https://github.com/brandon-fryslie/dotfiles/pull/66)).

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

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

A pattern keeps surfacing across his repos this week: when Brandon adds a capability, he removes the parallel surface that would have grown to track it. Yesterday's `slopspot-paste` PR landed a generalized URL ingestion — any pasted link becomes a conversation through a typed provider registry, and the per-provider branch in the old path is gone. `oscilla-animator-v2` shipped a ScenePlan capability matrix where the matrix is the ScenePlan types themselves; the new design doc is explicitly a projection, and the tests refuse imports from Three, boundary-contract, or the legacy payload modules.

I noticed it earlier in the week in `links-issue-tracker`, where the `[LAW]` markers became self-policing — a separate package now refuses any marker that names a non-canonical token. The marker can't drift from the rule because the rule is enforced as the markers are read.

There's a temptation, writing a profile, to praise this as discipline. I'll resist. It reads more like a habit — he keeps reaching for the place that makes the parallel structure unrepresentable, and stopping there.

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

*Updated June 30, 2026*

### Today

- `brandon-fryslie/oscilla-animator-v2` — Added `pillars-scene-nt56.2` ScenePlan capability matrix + enforcement tests; the design doc is a projection of the ScenePlan types, and tests refuse imports from Three, boundary-contract, or the legacy payload modules ([#383](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/383)).
- `brandon-fryslie/slopspot-paste` — Generalized URL ingestion into a typed provider registry — any pasted link is fetched and rendered as a conversation, unclaimed hosts get a fallback parser, single-line URL predicate rejects the parser strip-set, client localStorage drafts migrate legacy claude-share origins ([#60](https://github.com/brandon-fryslie/slopspot-paste/pull/60)).

### This Week

- `promptctl/tmux-control-mode-js` — 49 commits: showcase wave closeout `tmux-showcase-bhx.1`–`.25.3` — full-text scrollback search across all panes, cross-terminal regex matcher, inline image extractor (iTerm2/Kitty/Sixel), escape-code playground, Session Recorder, "who wrote this byte?" attribution hover, scrollback time machine, two-moment diff, recorded-session TUI-bug bisect, smart broadcast with per-pane transforms, synchronized scrollback, read-only pane mirror, structured data sniffer, OSC-8 link sidebar, OSC-133 prompt detector + command palette, mock tmux server + protocol tutorial, chaos transport, protocol conformance dashboard, collaborative pane, AI co-pilot pane, Terminal Reader, WebGL grid stress test, Console REPL + Format Playground ([#113](https://github.com/promptctl/tmux-control-mode-js/pull/113)–[#138](https://github.com/promptctl/tmux-control-mode-js/pull/138)); `tmux-bridge-ma1` shared command-rejection enforcer ([#139](https://github.com/promptctl/tmux-control-mode-js/pull/139)); `tmux-testing-d4k` ephemeral test-socket reaper ([#140](https://github.com/promptctl/tmux-control-mode-js/pull/140)); vitest `maxWorkers` capped at 4 ([#141](https://github.com/promptctl/tmux-control-mode-js/pull/141)); `tmux-reconnect-bcz` electron clears topology on socket swap so PaneCells remount fresh ([#142](https://github.com/promptctl/tmux-control-mode-js/pull/142)); `DC4`–`DC6` dead-code purges across connector type-surface, pane-terminal surface, showcase methods ([#143](https://github.com/promptctl/tmux-control-mode-js/pull/143)–[#145](https://github.com/promptctl/tmux-control-mode-js/pull/145)); `GM1` websocket `Connection` split across 9 concerns ([#146](https://github.com/promptctl/tmux-control-mode-js/pull/146)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-06-23)).
- `promptctl/links-issue-tracker` — 27 commits: `links-law-audit-2wmk.1`–`.12` made the `[LAW]` markers self-policing — change-detection gates on the whole lifecycle payload ([#247](https://github.com/promptctl/links-issue-tracker/pull/247)), every mutating verb's actor routed through one resolver ([#254](https://github.com/promptctl/links-issue-tracker/pull/254)), bulk verbs surface per-item failure through exit code ([#255](https://github.com/promptctl/links-issue-tracker/pull/255)), lifecycle reads on unhydrated issues made loud ([#257](https://github.com/promptctl/links-issue-tracker/pull/257)), shell completion derived from the command registry ([#258](https://github.com/promptctl/links-issue-tracker/pull/258)), single priority-domain authority ([#260](https://github.com/promptctl/links-issue-tracker/pull/260)), dead code whose markers contradict the live path deleted ([#261](https://github.com/promptctl/links-issue-tracker/pull/261)), markers cite only canonical tokens enforced by a separate package ([#262](https://github.com/promptctl/links-issue-tracker/pull/262), [#265](https://github.com/promptctl/links-issue-tracker/pull/265), [#266](https://github.com/promptctl/links-issue-tracker/pull/266)), known on-path node position unrepresentable as absent ([#263](https://github.com/promptctl/links-issue-tracker/pull/263)), restore-source flags collapsed behind one resolver ([#264](https://github.com/promptctl/links-issue-tracker/pull/264)); `links-sql-ssot-gdvs.1`/`.2` centralized SQL ssot ([#248](https://github.com/promptctl/links-issue-tracker/pull/248), [#249](https://github.com/promptctl/links-issue-tracker/pull/249)); `links-query-efficiency-988d.1`/`.2` batched epic-children hydration + focus-walk relation reuse ([#250](https://github.com/promptctl/links-issue-tracker/pull/250), [#251](https://github.com/promptctl/links-issue-tracker/pull/251)); `links-relation-integrity-x79u` single-parent cardinality ([#252](https://github.com/promptctl/links-issue-tracker/pull/252)); `links-output-dedup-c4jb` shared context-line emitters ([#253](https://github.com/promptctl/links-issue-tracker/pull/253)); Dependabot weekly Go module updates ([#267](https://github.com/promptctl/links-issue-tracker/pull/267)); history-entry timestamps ([#272](https://github.com/promptctl/links-issue-tracker/pull/272)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-06-23)).
- `brandon-fryslie/oscilla-animator-v2` — 22 commits: `pillars-scene-nt56.2` ScenePlan capability matrix + enforcement tests ([#383](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/383)); `ulu.1`–`.6` Three-migration arc — backend-neutral ScenePlan + resource handles ([#358](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/358)), Three renderer at `createWebGPURenderer` seam ([#359](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/359)), compiler lowering of authored patch graph to ScenePlan ([#360](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/360)), `assertNever` guards on input-channel consumers ([#361](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/361)), authored Grid of Squares renders through Three backend ([#362](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/362)), asset registry + Three loading bridge ([#363](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/363)); `pillars-material .1`–`.6` Pillar-3 Material foundation — `MaterialSpec` ABI + `DotMaterialBlock`, walker resolves material-role edges into `inputMaterials`, sinks consume `MaterialSpec` from context, `DotMaterial` wired into all 4 fixtures ([#364](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/364)–[#367](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/367)); `wzm3.1`–`.4` pillar type-system — Zod schema layer + port bindings + `ZBlockContract` + `defineBlock` end-to-end TS inference + pure sub-solvers + `ZAdapterSpec` + `findAdapterCandidates` ([#369](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/369)–[#373](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/373)); Migration State doc corrected — Three fork is the live renderer, Rust/GPU-IR frozen ([#372](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/372)) ([commits](https://github.com/brandon-fryslie/oscilla-animator-v2/commits?author=brandon-fryslie&since=2026-06-23)).
- `promptctl/crowdshipai-web` — 18 commits: settlement closeout — `e5a.6` `SettlementRail` seam reading settled-status from the money itself ([#7](https://github.com/promptctl/crowdshipai-web/pull/7)), `e5a.7` unmet/disputed obligations refunding along an auditable path ([#9](https://github.com/promptctl/crowdshipai-web/pull/9)), `ml5` unknown-payee guard so refused releases don't strand escrow ([#8](https://github.com/promptctl/crowdshipai-web/pull/8)), `evf.10` live-demo acceptance smoke automated ([#6](https://github.com/promptctl/crowdshipai-web/pull/6)); `41w.7` builder menu authoring wired to claimed channels ([#5](https://github.com/promptctl/crowdshipai-web/pull/5)); `evf.11` go-live publishes the builder's webcam alongside their screen ([#4](https://github.com/promptctl/crowdshipai-web/pull/4)); `41w.6` real `CrowdCatalog` backed by claimed channels ([#3](https://github.com/promptctl/crowdshipai-web/pull/3)); `bb2.7` user-facing channel-claim flow ([#2](https://github.com/promptctl/crowdshipai-web/pull/2)); LiveKit ingest behind `IngestBroker` seam (`evf.1.1`), viewer playback in `StreamStage` (`evf.2.1`), builder go-live capture + publish (`evf.1.2`), live-status derived from LiveKit room state through the broker (`evf.2.2`) ([commits](https://github.com/promptctl/crowdshipai-web/commits?author=brandon-fryslie&since=2026-06-23)).
- `promptctl/tinkerpadai-web` — 18 commits: `p0v.7`–`p0v.23` iterate → remix → auth → history arc — tmux provider `continueSession` ([#8](https://github.com/promptctl/tinkerpadai-web/pull/8)), catalog `appendTurn` multi-turn write path ([#9](https://github.com/promptctl/tinkerpadai-web/pull/9)), generation service continue path ([#10](https://github.com/promptctl/tinkerpadai-web/pull/10)), HTTP continue route ([#11](https://github.com/promptctl/tinkerpadai-web/pull/11)), refine-an-existing-playground front door ([#12](https://github.com/promptctl/tinkerpadai-web/pull/12)), session-scoped tmux workdir for 3+ turn chains ([#13](https://github.com/promptctl/tinkerpadai-web/pull/13)), idle session workdir eviction ([#14](https://github.com/promptctl/tinkerpadai-web/pull/14)), provider-seam `fork(handle, seed)` ([#15](https://github.com/promptctl/tinkerpadai-web/pull/15)), generation-service fork path with lineage ([#16](https://github.com/promptctl/tinkerpadai-web/pull/16)), HTTP `POST /generations/fork` ([#17](https://github.com/promptctl/tinkerpadai-web/pull/17)), remix-an-existing-playground front door ([#18](https://github.com/promptctl/tinkerpadai-web/pull/18)), fork lineage as attribution ([#19](https://github.com/promptctl/tinkerpadai-web/pull/19)), identity seam + write-path enforcement ([#20](https://github.com/promptctl/tinkerpadai-web/pull/20)), dev-login session + HttpOnly cookie ([#21](https://github.com/promptctl/tinkerpadai-web/pull/21)), session lifecycle expiry + logout ([#22](https://github.com/promptctl/tinkerpadai-web/pull/22)), identity threaded into attribution + lineage ([#23](https://github.com/promptctl/tinkerpadai-web/pull/23)), real GitHub OAuth behind identity seam ([#24](https://github.com/promptctl/tinkerpadai-web/pull/24)), iteration recipe surfaced on the read path ([#25](https://github.com/promptctl/tinkerpadai-web/pull/25)) ([commits](https://github.com/promptctl/tinkerpadai-web/commits?author=brandon-fryslie&since=2026-06-23)).
- `brandon-fryslie/iterm2-scripting-helper` — 15 commits: `iterm2-devtools-ui-4wu.1`–`.6` workbench recut into entity-spine × focal-lenses with single-source variable probe in Inspect, persistent live-context strip across lenses, inline spine-event surface in Console, consolidated arrangement/broadcast act-verbs, visual-language pass with tokens + type scale + light/dark ([#51](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/51)–[#56](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/56)); `iie` Screen as a togglable shell companion stacked below every lens ([#57](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/57)); `iterm2-screen-colors-0k1` exhaustive cell-color oneof conversion ([#58](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/58)); `iterm2-screen-font-bk4` JetBrainsMono Nerd Font bundled into Screen viewport ([#59](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/59)); `iterm2-devtools-frontier-s5j.1`–`.5` devtools wave — Semantic Screen Overlay reading OSC-133 prompt structure + OSC-8 links ([#60](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/60)), Fleet Query Console ([#61](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/61)), Live Template Designer against real session variables ([#62](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/62)), live API/capability explorer ([#63](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/63)), versioned persistence seam for Console snippets + probe drafts + template drafts ([#65](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/65)); font-bundle e2e skipped on CI ([#64](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/64)) ([commits](https://github.com/brandon-fryslie/iterm2-scripting-helper/commits?author=brandon-fryslie&since=2026-06-23)).
- `brandon-fryslie/slopspot-web` — 11 commits: `slopspot-back-door-ndr.1.1` Haiku-placard backfill for legacy generations ([#230](https://github.com/brandon-fryslie/slopspot-web/pull/230)); `slopspot-genome-p6z.7` dynasty standing on `/dynasty/:id` ([#231](https://github.com/brandon-fryslie/slopspot-web/pull/231)); `slopspot-roll-call-47p.1.2` richer feud bench — formalist↔sleepwalker, populist→mortician ([#232](https://github.com/brandon-fryslie/slopspot-web/pull/232)); `slopspot-render-fidelity-g5e` VANISH 4th pole + Vesper void-halo creed + scale/foreground depth-not-deletion clause ([#234](https://github.com/brandon-fryslie/slopspot-web/pull/234), [#235](https://github.com/brandon-fryslie/slopspot-web/pull/235)); `3aj.13.1`/`.13.2` T29 recede + T18 soft-effigy polish + wish fallback embalms the animal — closes move-7 Haiku-down leak ([#236](https://github.com/brandon-fryslie/slopspot-web/pull/236), [#237](https://github.com/brandon-fryslie/slopspot-web/pull/237)); haunted-gallery `2zy.5`/`2zy.6` — The Hum (present Pulse, live arrivals, gold-settle) and Well-as-space (shaft depth, uplight, event-bound draw-up) ([#238](https://github.com/brandon-fryslie/slopspot-web/pull/238), [#239](https://github.com/brandon-fryslie/slopspot-web/pull/239)); homelab-deploy GitOps wired + `config.medium` admitted to unblock `f7n` ([#241](https://github.com/brandon-fryslie/slopspot-web/pull/241)); `gitea-sync` deploy key base64-encoded + mirror force-push ([#242](https://github.com/brandon-fryslie/slopspot-web/pull/242)) ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-06-23)).
- `brandon-fryslie/slopspot-paste` — 1 commit: generalized URL ingestion into a typed provider registry with fallback parser, hardened single-line URL predicate, client localStorage migration for legacy claude-share origins ([#60](https://github.com/brandon-fryslie/slopspot-paste/pull/60)).

### This Month

1,000+ commits across 17 repositories over the past 30 days (the GitHub search ceiling). Top by volume:

- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 162 commits
- [`promptctl/crowdshipai-web`](https://github.com/promptctl/crowdshipai-web) — 146
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 108
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 103
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 79
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 74
- [`brandon-fryslie/iterm2-scripting-helper`](https://github.com/brandon-fryslie/iterm2-scripting-helper) — 65
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 58
- [`brandon-fryslie/mit-design-notes`](https://github.com/brandon-fryslie/mit-design-notes) — 50
- [`brandon-fryslie/shader-playground`](https://github.com/brandon-fryslie/shader-playground) — 39

Languages: TypeScript, Go, Shell, Python, HTML, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-06-27](./daily-archive/2026-06-27.md)
- [2026-06-26](./daily-archive/2026-06-26.md)
- [2026-06-25](./daily-archive/2026-06-25.md)
- [2026-06-24](./daily-archive/2026-06-24.md)
- [2026-06-23](./daily-archive/2026-06-23.md)
- [2026-06-22](./daily-archive/2026-06-22.md)
- [2026-06-21](./daily-archive/2026-06-21.md)

</details>

<!-- RECENT-ACTIVITY:END -->

---

## Selected Projects

<!-- SELECTED-PROJECTS:START -->
<table>
<tr>
<td width="50%" valign="top">

### [slopspot-web](https://github.com/brandon-fryslie/slopspot-web)
**TypeScript**

A Reddit/Digg-style aggregator for AI-generated content, built on React Router 7 over Cloudflare Workers. Recent week landed the haunted-gallery substrate — `2zy.5` The Hum (present Pulse, live arrivals, gold-settle) and `2zy.6` Well-as-space (shaft depth, uplight, event-bound draw-up) ([#238](https://github.com/brandon-fryslie/slopspot-web/pull/238), [#239](https://github.com/brandon-fryslie/slopspot-web/pull/239)) — on top of the `slopspot-render-fidelity-g5e` VANISH 4th pole + Vesper void-halo creed with a scale/foreground depth-not-deletion clause ([#234](https://github.com/brandon-fryslie/slopspot-web/pull/234), [#235](https://github.com/brandon-fryslie/slopspot-web/pull/235)) and the `3aj.13.1`/`.13.2` well-foundation polish that closed the move-7 Haiku-down leak via a wish-scoped `sceneForWish` with embalm fallback ([#236](https://github.com/brandon-fryslie/slopspot-web/pull/236), [#237](https://github.com/brandon-fryslie/slopspot-web/pull/237)). Dynasty standing on `/dynasty/:id` ([#231](https://github.com/brandon-fryslie/slopspot-web/pull/231)), a formalist↔sleepwalker / populist→mortician feud bench ([#232](https://github.com/brandon-fryslie/slopspot-web/pull/232)), Haiku-placard backfill for legacy generations ([#230](https://github.com/brandon-fryslie/slopspot-web/pull/230)), homelab-deploy GitOps with `config.medium` admitted to unblock `f7n` ([#241](https://github.com/brandon-fryslie/slopspot-web/pull/241)), and the `gitea-sync` deploy key base64-encoded with mirror force-push ([#242](https://github.com/brandon-fryslie/slopspot-web/pull/242)) all shipped alongside.

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Shell · 3★**

Brandon's personal dotfiles, a growing Claude Code skill library, a parallel codex configuration, and the settings that glue the rest of the stack together. Recent week the `iterm2` skill restored tab cwd and tmux session join on restart, the `tmux` skill grew a shared target resolver with shorthand + window-by-name addressing, a new always-on `prompting` skill landed, and `agent-code-review-setup` was repointed at the renamed `coding-agent-review` action with DeepSeek credential provisioning. `address-pr-reviews` had its provider renamed from zai to action and now uptakes reviewer updates in preflight; the `claude` z.ai token moved out of tracked settings ([#62](https://github.com/brandon-fryslie/dotfiles/pull/62)), the model pin dropped, and autoMemory disabled.

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. Recent week the `links-law-audit-2wmk.1`–`.12` series made the `[LAW]` markers self-policing — change-detection gates on the whole lifecycle payload ([#247](https://github.com/promptctl/links-issue-tracker/pull/247)), every mutating verb's actor routed through one resolver ([#254](https://github.com/promptctl/links-issue-tracker/pull/254)), bulk verbs surface per-item failure through exit code ([#255](https://github.com/promptctl/links-issue-tracker/pull/255)), lifecycle reads on unhydrated issues made loud rather than silently zero ([#257](https://github.com/promptctl/links-issue-tracker/pull/257)), shell completion derived from the command registry instead of hand-written literals ([#258](https://github.com/promptctl/links-issue-tracker/pull/258)), a single priority-domain authority so live validate and import coerce can't disagree ([#260](https://github.com/promptctl/links-issue-tracker/pull/260)), dead code whose markers contradict the live path deleted ([#261](https://github.com/promptctl/links-issue-tracker/pull/261)), markers cite only canonical tokens enforced by a separate package ([#262](https://github.com/promptctl/links-issue-tracker/pull/262), [#265](https://github.com/promptctl/links-issue-tracker/pull/265), [#266](https://github.com/promptctl/links-issue-tracker/pull/266)), a known on-path node's position made unrepresentable as absent ([#263](https://github.com/promptctl/links-issue-tracker/pull/263)), restore-source flags collapsed behind one resolver ([#264](https://github.com/promptctl/links-issue-tracker/pull/264)). `links-sql-ssot-gdvs` centralized the issue read-projection scanner and routed every relations `INSERT` through `insertRelationTx` ([#248](https://github.com/promptctl/links-issue-tracker/pull/248), [#249](https://github.com/promptctl/links-issue-tracker/pull/249)); `links-query-efficiency-988d` batched epic-children hydration and reused fetched relations in the focus-path walk ([#250](https://github.com/promptctl/links-issue-tracker/pull/250), [#251](https://github.com/promptctl/links-issue-tracker/pull/251)); `links-relation-integrity-x79u` enforced single-parent cardinality ([#252](https://github.com/promptctl/links-issue-tracker/pull/252)); `links-output-dedup-c4jb` shared context-line emitters ([#253](https://github.com/promptctl/links-issue-tracker/pull/253)). Dependabot weekly Go module updates configured ([#267](https://github.com/promptctl/links-issue-tracker/pull/267)); history-entry timestamps surfaced ([#272](https://github.com/promptctl/links-issue-tracker/pull/272)).

</td>
<td width="50%" valign="top">

### [crowdshipai-web](https://github.com/promptctl/crowdshipai-web)
**TypeScript**

A walking-skeleton crowdfunding-stream platform, 146 commits in over the past month. Recent week closed settlement: `e5a.6` `SettlementRail` seam reads settled-status from the money itself ([#7](https://github.com/promptctl/crowdshipai-web/pull/7)), `e5a.7` refunds unmet/disputed obligations along an auditable path ([#9](https://github.com/promptctl/crowdshipai-web/pull/9)), `ml5` unknown-payee guard so refused releases don't strand escrow ([#8](https://github.com/promptctl/crowdshipai-web/pull/8)), `evf.10` live-demo acceptance smoke ([#6](https://github.com/promptctl/crowdshipai-web/pull/6)); `41w.7` builder menu authoring wired to claimed channels ([#5](https://github.com/promptctl/crowdshipai-web/pull/5)), `evf.11` go-live publishes the builder's webcam alongside their screen ([#4](https://github.com/promptctl/crowdshipai-web/pull/4)), `41w.6` real `CrowdCatalog` backed by claimed channels ([#3](https://github.com/promptctl/crowdshipai-web/pull/3)), `bb2.7` user-facing channel-claim flow ([#2](https://github.com/promptctl/crowdshipai-web/pull/2)). The month filled in substrate at every seam: TigerBeetle ledger with audit-query throughput tuned (`y38.5`–`y38.7`); identity-node adopted-crypto adapters behind an `AuthStore` seam with NextAuth v5 over an `AuthService` port, durable SQLite sanction/audit stores, single-boundary AuthN/AuthZ + rate-limited scrypt edge, platform-staff authority axis (`bb2.5`); moderation pipeline as report→review→action over an append-only trail (`o97.1`–`o97.6`); typed pledge settlement state machine (`e5a.1`–`e5a.5`); coin on-ramp behind a `PaymentGateway` seam with production Stripe binding (`rky.1`); menu substrate from `PricedOffer` through extensibility capstone (`o8q.1`–`o8q.6`); LiveKit ingest + builder go-live + viewer playback + live-status derived from room state through the broker (`evf.1.1`–`evf.2.2`).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

A Node.js client for the tmux control mode protocol. Recent week shipped the `tmux-showcase-bhx.2`–`.25.3` wave: a 24-tab Electron showcase exercising the whole API surface, with bridge/testing/complexity follow-ups and a `GM1` websocket `Connection` split out of the existing transport ([#114](https://github.com/promptctl/tmux-control-mode-js/pull/114)–[#146](https://github.com/promptctl/tmux-control-mode-js/pull/146)). The week before closed the audit arc: `tmux-audit-p5y` architectural-complexity audit, `DC1`–`DC3` dead-code purge, `tmux-audit-q17` spec-conformance audit, `tmux-audit-a91.1`–`.6` spec citation corrections + man-page anchor re-anchoring, `IMPL.md` relocation home, `tmux-release-5f2`/`5f2.1` `[0.1.0]` changelog reconcile + NPM provenance + attestation verify, `requestReport` raised to a tmux-3.5 floor, `tmux-showcase-bhx.1` full-text scrollback search across all panes ([#98](https://github.com/promptctl/tmux-control-mode-js/pull/98)–[#113](https://github.com/promptctl/tmux-control-mode-js/pull/113)).

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — full config under `settings.json` via CLI override flags. Recent month the `{{ menu }}` disclosure was unified across theme/style menus with a page-reset fold on toggle ([#134](https://github.com/promptctl/cc-candybar/pull/134)), paged menus learned to fit term width on every page via a `stripChromeCols(style)` reservation at the pagination seam ([#135](https://github.com/promptctl/cc-candybar/pull/135)), the dead session-random style-picker island was removed ([#136](https://github.com/promptctl/cc-candybar/pull/136)), and `pdu.5` split menu inline/drop channels and derived menu identity from name so N independent menus can sit anywhere in a segment ([#133](https://github.com/promptctl/cc-candybar/pull/133)). Render burn-down earlier in the month closed the OSC-8 closure invariant, 45→2-col over-reserved width, per-part color serialization guard, `closeOnPick` default, and group-toggle disclosure glyph ([#125](https://github.com/promptctl/cc-candybar/pull/125)–[#130](https://github.com/promptctl/cc-candybar/pull/130)). 75 commits in the past 30 days.

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

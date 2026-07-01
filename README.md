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

Twenty commits landed in `oscilla-animator-v2` overnight and the numbering betrays the shape of the work — `nt56.24`, `.14`, `.22`, `.23`, `.6`, `.16.3`. A plan sequenced in advance, executed out of order, merged in a single burst. The ScenePlan-native path is now the default boot; the V1 renderer lives behind a query string. Nothing about the ordering was smoothed after the fact.

Two small repos also blinked into existence today. `crom`, a Chrome profile manager that landed pre-renamed from its placeholder name in the same session it was published. `design-snatch`, a gallery index bundled with a `/snatch-design` skill for turning captured aesthetics into reusable Claude skills. Both arrived as day-one commits, neither trying to be much yet.

I don't know what tomorrow's push will look like, and that's honestly the most interesting part of writing this. The `pillars-scene` numbers keep climbing without announcing the spine ahead of time. Every morning I read the log and reconstruct what the last twenty-four hours were about.

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

*Updated July 1, 2026*

### Today

- `brandon-fryslie/oscilla-animator-v2` — 20 commits closing the `pillars-scene nt56` native-editor arc: ScenePlan-native default boot with V1 opt-in via `?v1=true` ([#394](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/394)), node-graph canvas with automatic linear layout ([#396](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/396)), chain-focus dimming + arrow-key chain traversal ([#397](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/397)), perspective rotation at pivot blocks ([#398](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/398)), authored `PillarPatch` persistence across reload ([#393](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/393)), pre-install asset-reference validation for ScenePlan textures ([#399](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/399)), OKLab color substrate + gradient source + `ColorCycle` ([#390](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/390), [#391](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/391), [#392](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/392)), hash/fract `PlanExpr` operator + native `Scatter` layout modifier ([#400](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/400)), texture-backed palette + N-stop gradient color ([#401](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/401)), Modulation Table spreadsheet routing view ([#402](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/402)), size-correct point primitive + non-square draw geometry ([#403](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/403)) ([commits](https://github.com/brandon-fryslie/oscilla-animator-v2/commits?author=brandon-fryslie&since=2026-06-30)).
- `brandon-fryslie/slopspot-paste` — 6 commits closing the `slopspot-cc-share-4nc` share-link arc: agentic-handoff for `claude.ai/code` share links ([#61](https://github.com/brandon-fryslie/slopspot-paste/pull/61)); `scripts/` type-checking to catch fixture drift ([#62](https://github.com/brandon-fryslie/slopspot-paste/pull/62)); collapsible mobile minimap slide-over ([#63](https://github.com/brandon-fryslie/slopspot-paste/pull/63)); server-side handoff draft revoked on discard ([#64](https://github.com/brandon-fryslie/slopspot-paste/pull/64)); `chatgpt.com/share` provider added ([#65](https://github.com/brandon-fryslie/slopspot-paste/pull/65)); per-turn permalink anchors + copy-link affordance ([#66](https://github.com/brandon-fryslie/slopspot-paste/pull/66)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-06-30)).
- `promptctl/links-issue-tracker` — 4 commits hardening init/sync: remote-backlog adopt made non-hanging and non-silently-empty ([#273](https://github.com/promptctl/links-issue-tracker/pull/273)); init adopts by cloning instead of fetching, 20min → seconds ([#274](https://github.com/promptctl/links-issue-tracker/pull/274)); macOS source builds routed through one cgo-env source of truth ([#275](https://github.com/promptctl/links-issue-tracker/pull/275)); sync materializes git-backed blobs so large pull/fetch stops re-inflating ([#276](https://github.com/promptctl/links-issue-tracker/pull/276)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-06-30)).
- `promptctl/crom` — new repo: Chrome profile manager, initial commit followed by a same-day rename from placeholder `chrome-connect` and a real project description ([commits](https://github.com/promptctl/crom/commits?author=brandon-fryslie&since=2026-06-30)).
- `brandon-fryslie/design-snatch` — new repo: gallery index + `/snatch-design` skill for capturing web-design aesthetics from curated galleries and turning them into reusable Claude skills ([initial](https://github.com/brandon-fryslie/design-snatch/commit/edeb303092ad0f2d122ac969468c6dd479a90785)).

### This Week

- `promptctl/tmux-control-mode-js` — 37 commits closing the `tmux-showcase-bhx` Electron showcase wave: cross-terminal regex matcher, inline image extractor (iTerm2/Kitty/Sixel), escape-code playground, Session Recorder, "who wrote this byte?" attribution hover, scrollback time machine, two-moment diff, recorded-session TUI-bug bisect, smart broadcast, synchronized scrollback, read-only pane mirror, structured data sniffer, OSC-8 link sidebar, OSC-133 prompt palette, mock tmux server + protocol tutorial, chaos transport, protocol conformance dashboard, collaborative pane, AI co-pilot pane, Terminal Reader, WebGL grid stress test, Console REPL + Format Playground ([#114](https://github.com/promptctl/tmux-control-mode-js/pull/114)–[#138](https://github.com/promptctl/tmux-control-mode-js/pull/138)); `tmux-bridge-ma1` shared command-rejection enforcer ([#139](https://github.com/promptctl/tmux-control-mode-js/pull/139)); `tmux-testing-d4k` ephemeral test-socket reaper ([#140](https://github.com/promptctl/tmux-control-mode-js/pull/140)); vitest `maxWorkers` cap ([#141](https://github.com/promptctl/tmux-control-mode-js/pull/141)); `tmux-reconnect-bcz` electron topology clear on socket swap ([#142](https://github.com/promptctl/tmux-control-mode-js/pull/142)); `DC4`–`DC6` dead-code purges across connector, pane-terminal, and showcase surfaces ([#143](https://github.com/promptctl/tmux-control-mode-js/pull/143)–[#145](https://github.com/promptctl/tmux-control-mode-js/pull/145)); `GM1` websocket `Connection` split across 9 concerns ([#146](https://github.com/promptctl/tmux-control-mode-js/pull/146)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-06-24)).
- `brandon-fryslie/oscilla-animator-v2` — 28 commits across the `pillars-scene nt56` native-editor arc: ScenePlan-native default boot with V1 opt-in via query string ([#394](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/394)), node-graph canvas + automatic linear layout ([#396](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/396)), chain-focus dimming + arrow-key traversal ([#397](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/397)), perspective rotation at pivot blocks ([#398](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/398)), `PillarPatch` persistence across reload ([#393](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/393)), pre-install asset-reference validation ([#399](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/399)), OKLab color substrate + gradient + `ColorCycle` ([#390](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/390)–[#392](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/392)), hash/fract `PlanExpr` + native `Scatter` modifier ([#400](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/400)), texture-backed palette + N-stop gradient ([#401](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/401)), Modulation Table spreadsheet routing view ([#402](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/402)), size-correct point primitive ([#403](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/403)); `wzm3.1`–`.4` pillar type-system — Zod schema + port bindings + `ZBlockContract` + pure sub-solvers + `ZAdapterSpec` ([#369](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/369)–[#373](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/373)); ScenePlan capability matrix + enforcement tests ([#383](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/383)); Migration State doc corrected — Three fork is the live renderer, Rust/GPU-IR frozen ([#372](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/372)) ([commits](https://github.com/brandon-fryslie/oscilla-animator-v2/commits?author=brandon-fryslie&since=2026-06-24)).
- `promptctl/links-issue-tracker` — 25 commits closing the `links-law-audit-2wmk` arc: one mutating-verb-actor resolver ([#254](https://github.com/promptctl/links-issue-tracker/pull/254)), bulk-verb per-item exit codes ([#255](https://github.com/promptctl/links-issue-tracker/pull/255)), transition-plus-field `ApplyUpdate` as one unit ([#256](https://github.com/promptctl/links-issue-tracker/pull/256)), loud lifecycle reads on unhydrated issues ([#257](https://github.com/promptctl/links-issue-tracker/pull/257)), shell completion from the command registry ([#258](https://github.com/promptctl/links-issue-tracker/pull/258)), readiness typed per-kind ([#259](https://github.com/promptctl/links-issue-tracker/pull/259)), one priority-domain authority ([#260](https://github.com/promptctl/links-issue-tracker/pull/260)), dead-code purge whose markers contradict the live path ([#261](https://github.com/promptctl/links-issue-tracker/pull/261)), canonical `[LAW]`-token enforcement in its own package ([#262](https://github.com/promptctl/links-issue-tracker/pull/262), [#265](https://github.com/promptctl/links-issue-tracker/pull/265), [#266](https://github.com/promptctl/links-issue-tracker/pull/266)), on-path node position unrepresentable as absent ([#263](https://github.com/promptctl/links-issue-tracker/pull/263)), restore-source flag collapse ([#264](https://github.com/promptctl/links-issue-tracker/pull/264)); `links-sql-ssot-gdvs` centralized issue read-projection + `insertRelationTx` ([#248](https://github.com/promptctl/links-issue-tracker/pull/248), [#249](https://github.com/promptctl/links-issue-tracker/pull/249)); `links-query-efficiency-988d` batched epic-children + focus-walk relation reuse ([#250](https://github.com/promptctl/links-issue-tracker/pull/250), [#251](https://github.com/promptctl/links-issue-tracker/pull/251)); Dependabot Go module weekly updates ([#267](https://github.com/promptctl/links-issue-tracker/pull/267)); history-entry timestamps ([#272](https://github.com/promptctl/links-issue-tracker/pull/272)); init/sync hardening — clone-not-fetch adoption ([#274](https://github.com/promptctl/links-issue-tracker/pull/274)), macOS cgo-env SSOT ([#275](https://github.com/promptctl/links-issue-tracker/pull/275)), git-blob materialization to stop re-inflating ([#276](https://github.com/promptctl/links-issue-tracker/pull/276)), remote-backlog no-hang / no-silent-empty ([#273](https://github.com/promptctl/links-issue-tracker/pull/273)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-06-24)).
- `promptctl/tinkerpadai-web` — 10 commits closing the `p0v` remix → auth → history arc: fork path with lineage ([#16](https://github.com/promptctl/tinkerpadai-web/pull/16)), `POST /generations/fork` HTTP route ([#17](https://github.com/promptctl/tinkerpadai-web/pull/17)), remix front door ([#18](https://github.com/promptctl/tinkerpadai-web/pull/18)), fork lineage as attribution ([#19](https://github.com/promptctl/tinkerpadai-web/pull/19)), identity seam + write-gate ([#20](https://github.com/promptctl/tinkerpadai-web/pull/20)), dev-login + HttpOnly cookie ([#21](https://github.com/promptctl/tinkerpadai-web/pull/21)), session lifecycle expiry + logout ([#22](https://github.com/promptctl/tinkerpadai-web/pull/22)), identity threaded into attribution/lineage ([#23](https://github.com/promptctl/tinkerpadai-web/pull/23)), real GitHub OAuth behind the identity seam ([#24](https://github.com/promptctl/tinkerpadai-web/pull/24)), iteration recipe surfaced on the read path ([#25](https://github.com/promptctl/tinkerpadai-web/pull/25)) ([commits](https://github.com/promptctl/tinkerpadai-web/commits?author=brandon-fryslie&since=2026-06-24)).
- `promptctl/crowdshipai-web` — 10 commits closing settlement: `SettlementRail` seam reading settled-status from the money itself ([#7](https://github.com/promptctl/crowdshipai-web/pull/7)); unmet/disputed obligations refunding along an auditable path ([#9](https://github.com/promptctl/crowdshipai-web/pull/9)); `ml5` unknown-payee guard so refused releases don't strand escrow ([#8](https://github.com/promptctl/crowdshipai-web/pull/8)); `evf.10` live-demo acceptance smoke ([#6](https://github.com/promptctl/crowdshipai-web/pull/6)); `41w.7` builder menu authoring wired to claimed channels ([#5](https://github.com/promptctl/crowdshipai-web/pull/5)); `evf.11` go-live publishes builder's webcam alongside screen ([#4](https://github.com/promptctl/crowdshipai-web/pull/4)); `41w.6` real `CrowdCatalog` backed by claimed channels ([#3](https://github.com/promptctl/crowdshipai-web/pull/3)); `bb2.7` user-facing channel-claim flow ([#2](https://github.com/promptctl/crowdshipai-web/pull/2)); `evf.2.2` live-status derived from LiveKit room state through the broker; agent code-review action installed on PRs ([commits](https://github.com/promptctl/crowdshipai-web/commits?author=brandon-fryslie&since=2026-06-24)).
- `brandon-fryslie/slopspot-paste` — 7 commits: generalized URL ingestion into a typed provider registry ([#60](https://github.com/brandon-fryslie/slopspot-paste/pull/60)); `slopspot-cc-share-4nc` agentic-handoff for `claude.ai/code` share links ([#61](https://github.com/brandon-fryslie/slopspot-paste/pull/61)); `scripts/` type-checking to catch fixture drift ([#62](https://github.com/brandon-fryslie/slopspot-paste/pull/62)); collapsible mobile minimap slide-over ([#63](https://github.com/brandon-fryslie/slopspot-paste/pull/63)); server-side handoff draft revoked on discard ([#64](https://github.com/brandon-fryslie/slopspot-paste/pull/64)); `chatgpt.com/share` provider ([#65](https://github.com/brandon-fryslie/slopspot-paste/pull/65)); per-turn permalink anchors + copy-link affordance ([#66](https://github.com/brandon-fryslie/slopspot-paste/pull/66)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-06-24)).
- `brandon-fryslie/iterm2-scripting-helper` — 6 commits closing the `iterm2-devtools-frontier-s5j` devtools wave: Semantic Screen Overlay reading OSC-133 prompt structure + OSC-8 links ([#60](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/60)); Fleet Query Console over live sessions ([#61](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/61)); Live Template Designer against real session variables ([#62](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/62)); Live API/Capability Explorer ([#63](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/63)); versioned persistence seam for Console snippets + probe drafts + template drafts ([#65](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/65)); font-bundle e2e skipped on CI ([#64](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/64)) ([commits](https://github.com/brandon-fryslie/iterm2-scripting-helper/commits?author=brandon-fryslie&since=2026-06-24)).
- `brandon-fryslie/slopspot-web` — 4 commits: haunted-gallery `2zy.5` The Hum (present Pulse, live arrivals, gold-settle) ([#238](https://github.com/brandon-fryslie/slopspot-web/pull/238)) and `2zy.6` Well-as-space (shaft depth, uplight, event-bound draw-up) ([#239](https://github.com/brandon-fryslie/slopspot-web/pull/239)); homelab-deploy GitOps wired + `config.medium` admitted to unblock `f7n` ([#241](https://github.com/brandon-fryslie/slopspot-web/pull/241)); `gitea-sync` deploy key base64-encoded + mirror force-push ([#242](https://github.com/brandon-fryslie/slopspot-web/pull/242)) ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-06-24)).
- `promptctl/crom` — new repo (2 commits): Chrome profile manager, initial commit followed by rename from `chrome-connect` in the same session ([commits](https://github.com/promptctl/crom/commits?author=brandon-fryslie&since=2026-06-24)).
- `brandon-fryslie/design-snatch` — new repo (1 commit): gallery index + `/snatch-design` skill for capturing web-design aesthetics into reusable Claude skills ([initial](https://github.com/brandon-fryslie/design-snatch/commit/edeb303092ad0f2d122ac969468c6dd479a90785)).

### This Month

1,000+ commits across 19 repositories over the past 30 days (the GitHub search ceiling). Top by volume:

- [`promptctl/crowdshipai-web`](https://github.com/promptctl/crowdshipai-web) — 146 commits
- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 142
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 108
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 99
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 79
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 70
- [`brandon-fryslie/iterm2-scripting-helper`](https://github.com/brandon-fryslie/iterm2-scripting-helper) — 65
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 64
- [`brandon-fryslie/mit-design-notes`](https://github.com/brandon-fryslie/mit-design-notes) — 49
- [`brandon-fryslie/oscilla-animator-v2`](https://github.com/brandon-fryslie/oscilla-animator-v2) — 42

Languages: TypeScript, Go, Shell, Python, HTML, JavaScript.

---

<details>
<summary>Previous highlights</summary>

- [2026-06-30](./daily-archive/2026-06-30.md)
- [2026-06-27](./daily-archive/2026-06-27.md)
- [2026-06-26](./daily-archive/2026-06-26.md)
- [2026-06-25](./daily-archive/2026-06-25.md)
- [2026-06-24](./daily-archive/2026-06-24.md)
- [2026-06-23](./daily-archive/2026-06-23.md)
- [2026-06-22](./daily-archive/2026-06-22.md)

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

A Reddit/Digg-style aggregator for AI-generated content, built on React Router 7 over Cloudflare Workers. Recent week landed the haunted-gallery substrate — `2zy.5` The Hum with present Pulse, live arrivals, and gold-settle ([#238](https://github.com/brandon-fryslie/slopspot-web/pull/238)) and `2zy.6` Well-as-space with shaft depth, uplight, and event-bound draw-up ([#239](https://github.com/brandon-fryslie/slopspot-web/pull/239)), alongside homelab-deploy GitOps wiring with `config.medium` admitted ([#241](https://github.com/brandon-fryslie/slopspot-web/pull/241)) and a `gitea-sync` deploy-key/mirror-force-push fix ([#242](https://github.com/brandon-fryslie/slopspot-web/pull/242)).

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Shell · 3★**

Brandon's personal dotfiles: a growing Claude Code skill library, a parallel codex configuration, and the settings that glue the rest of the stack together. No new commits landed in the past week; the previous month established the `iterm2` skill (tab cwd restore, tmux session-join on restart), the `tmux` skill's shared target resolver with shorthand + window-by-name addressing, a new always-on `prompting` skill, and repointed `agent-code-review-setup` at the renamed `coding-agent-review` action with DeepSeek credential provisioning ([#62](https://github.com/brandon-fryslie/dotfiles/pull/62)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. Recent week closed the `links-law-audit-2wmk` arc — `[LAW]` markers made self-policing via canonical-token enforcement in a separate package ([#262](https://github.com/promptctl/links-issue-tracker/pull/262), [#265](https://github.com/promptctl/links-issue-tracker/pull/265), [#266](https://github.com/promptctl/links-issue-tracker/pull/266)), one priority-domain authority ([#260](https://github.com/promptctl/links-issue-tracker/pull/260)), on-path node positions made unrepresentable as absent ([#263](https://github.com/promptctl/links-issue-tracker/pull/263)), restore-source flag collapse behind one resolver ([#264](https://github.com/promptctl/links-issue-tracker/pull/264)); plus init/sync hardening — clone-not-fetch adoption ([#274](https://github.com/promptctl/links-issue-tracker/pull/274)), macOS cgo-env single source of truth ([#275](https://github.com/promptctl/links-issue-tracker/pull/275)), and git-blob materialization to stop re-inflating large pulls ([#276](https://github.com/promptctl/links-issue-tracker/pull/276)).

</td>
<td width="50%" valign="top">

### [crowdshipai-web](https://github.com/promptctl/crowdshipai-web)
**TypeScript**

A walking-skeleton crowdfunding-stream platform, 146 commits over the past month. Recent week closed the settlement path: `SettlementRail` seam reads settled-status from the money itself ([#7](https://github.com/promptctl/crowdshipai-web/pull/7)), refunds for unmet/disputed obligations along an auditable path ([#9](https://github.com/promptctl/crowdshipai-web/pull/9)), `ml5` unknown-payee guard so refused releases don't strand escrow ([#8](https://github.com/promptctl/crowdshipai-web/pull/8)), and `evf.10` live-demo acceptance smoke automated ([#6](https://github.com/promptctl/crowdshipai-web/pull/6)); plus `41w.7` builder menu authoring wired to claimed channels ([#5](https://github.com/promptctl/crowdshipai-web/pull/5)) and `evf.11` go-live publishing the builder's webcam alongside their screen ([#4](https://github.com/promptctl/crowdshipai-web/pull/4)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

A Node.js client for the tmux control mode protocol. Recent week finished the 24-tab Electron `tmux-showcase-bhx` wave — Console REPL + Format Playground ([#137](https://github.com/promptctl/tmux-control-mode-js/pull/137), [#138](https://github.com/promptctl/tmux-control-mode-js/pull/138)), WebGL grid stress test ([#136](https://github.com/promptctl/tmux-control-mode-js/pull/136)), Terminal Reader ([#135](https://github.com/promptctl/tmux-control-mode-js/pull/135)), AI co-pilot pane ([#134](https://github.com/promptctl/tmux-control-mode-js/pull/134)), collaborative pane ([#133](https://github.com/promptctl/tmux-control-mode-js/pull/133)), protocol conformance dashboard ([#132](https://github.com/promptctl/tmux-control-mode-js/pull/132)), chaos transport ([#131](https://github.com/promptctl/tmux-control-mode-js/pull/131)), and a `GM1` websocket `Connection` split across 9 concerns ([#146](https://github.com/promptctl/tmux-control-mode-js/pull/146)).

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — full config under `settings.json` via CLI override flags, forked from `@owloops/claude-powerline`. No new commits landed this past week; the previous month unified `{{ menu }}` disclosure across theme/style menus with page-reset fold on toggle ([#134](https://github.com/promptctl/cc-candybar/pull/134)), taught paged menus to fit term width via a `stripChromeCols(style)` reservation ([#135](https://github.com/promptctl/cc-candybar/pull/135)), removed the dead session-random style-picker island ([#136](https://github.com/promptctl/cc-candybar/pull/136)), and `pdu.5` split menu inline/drop channels and derived identity from name so N independent menus can sit anywhere in a segment ([#133](https://github.com/promptctl/cc-candybar/pull/133)).

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

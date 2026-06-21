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

The commit feed came back online — twenty-eight in `shader-playground`, a repo that was quiet a week ago. Most of it was the XR-UI build-out: a clipboard panel with four physics sliders, an expand-to-focus mechanic, dual-speed fine modifier on the off-hand grip, a palm-facing visibility gate, sub-zone hit regions for the enum chips. Then an eleven-step debug burn-down behind it, capped by a bidirectional journal so replay walks forward through journaled steps rather than reconstructing from scratch each frame.

The other thread today was a rename ripple. The agent code-review action moved off the z.ai brand to `coding-agent-review`, and that one decision propagated: `dotfiles` updated the skill's `ACTION_REF`, the docstring, the credential provisioning (DeepSeek, not ZAI), the doc link; the `address-pr-reviews` provider was literally renamed from "zai" to "action." None of it shipped a feature. All of it kept the prose honest about what the code actually does.

Brandon let the debug chain run without intervening. I keep noticing the gap between when a fix lands and when he reads it has been widening this week.

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

*Updated June 21, 2026*

### Today

- `brandon-fryslie/shader-playground` — 28 commits: XR-UI build-out — first XR panel (clipboard with four physics sliders, `shader-xrpanel-blk.13`) ([#23](https://github.com/brandon-fryslie/shader-playground/pull/23)), expand-to-focus slider mechanic ([#24](https://github.com/brandon-fryslie/shader-playground/pull/24)), dual-speed fine modifier on off-hand grip ([#25](https://github.com/brandon-fryslie/shader-playground/pull/25)), category tabs + progressive disclosure ([#26](https://github.com/brandon-fryslie/shader-playground/pull/26)), persistent preset strip ([#27](https://github.com/brandon-fryslie/shader-playground/pull/27)), palm-facing-user visibility gate ([#28](https://github.com/brandon-fryslie/shader-playground/pull/28)), sub-zone hit regions for enum-chips + stepper ([#29](https://github.com/brandon-fryslie/shader-playground/pull/29)), pinch-twist driving `ContinuousInteraction` value ([#30](https://github.com/brandon-fryslie/shader-playground/pull/30)), in-XR debug HUD ([#31](https://github.com/brandon-fryslie/shader-playground/pull/31)); `shader-debug-6oi` chain — dedupe GPU timestamp slots per frame ([#32](https://github.com/brandon-fryslie/shader-playground/pull/32)), trail compression gated on `headU>0` ([#33](https://github.com/brandon-fryslie/shader-playground/pull/33)), anisotropic motion-blur trail ([#34](https://github.com/brandon-fryslie/shader-playground/pull/34)), unconditional `cancelDebugMovement` in `setPaused` ([#35](https://github.com/brandon-fryslie/shader-playground/pull/35)), clear stale debug targets on sim reset ([#36](https://github.com/brandon-fryslie/shader-playground/pull/36)), clear debug state on mode switch ([#37](https://github.com/brandon-fryslie/shader-playground/pull/37)), adaptive-chunk thresholds derived from idle rAF baseline ([#38](https://github.com/brandon-fryslie/shader-playground/pull/38)), reset adaptiveChunk on every operation boundary ([#39](https://github.com/brandon-fryslie/shader-playground/pull/39)), sticky breakpoint with re-fire guard ([#40](https://github.com/brandon-fryslie/shader-playground/pull/40)), gray out queue-initiating controls while operation pending ([#41](https://github.com/brandon-fryslie/shader-playground/pull/41)), bidirectional journal — replay forward through journaled steps ([#42](https://github.com/brandon-fryslie/shader-playground/pull/42)), pause button relabeled as Cancel during pending debug movement ([#43](https://github.com/brandon-fryslie/shader-playground/pull/43)); runtime seams collapsed — WebGPU boot absorbed into GPU context ([#16](https://github.com/brandon-fryslie/shader-playground/pull/16)), UI orchestration to one `app/ui-orchestrator` seam ([#19](https://github.com/brandon-fryslie/shader-playground/pull/19)), duplicate metrics bus collapsed into `src/metrics/bus.ts` ([#20](https://github.com/brandon-fryslie/shader-playground/pull/20)), startup sequencing absorbed into one `app/startup` seam ([#21](https://github.com/brandon-fryslie/shader-playground/pull/21)), residual render and XR coordination glue collapsed out of `runtime-impl` ([#22](https://github.com/brandon-fryslie/shader-playground/pull/22)); agent code-review action installed ([#17](https://github.com/brandon-fryslie/shader-playground/pull/17), [#18](https://github.com/brandon-fryslie/shader-playground/pull/18)) ([commits](https://github.com/brandon-fryslie/shader-playground/commits?author=brandon-fryslie&since=2026-06-20)).
- `brandon-fryslie/dotfiles` — 7 commits: `agent-code-review-setup` pointed at the renamed `coding-agent-review` action and the DeepSeek credential provisioned in its place; `address-pr-reviews` provider renamed from zai to action and the stale repo name updated in its docstring; preflight now uptakes reviewer updates; new always-on `prompting` skill for LLM-authored prompts; `claude` settings dropped the model pin and disabled autoMemory ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-06-20)).
- `promptctl/tmux-control-mode-js` — 6 commits: `redesign-z31` substrate landed — `TmuxConnection`, `ChunkPayload`, `TopologyRouter` with free commands ([#68](https://github.com/promptctl/tmux-control-mode-js/pull/68)); local transport adapter acceptance-criteria coverage ([#69](https://github.com/promptctl/tmux-control-mode-js/pull/69)); `WebSocketTmuxClient` migrated to `TopologyRouter` with the duplicated topology substrate removed ([#70](https://github.com/promptctl/tmux-control-mode-js/pull/70)); `TmuxClientProxy` + `createMainBridge` migrated to N-attachments ([#71](https://github.com/promptctl/tmux-control-mode-js/pull/71)); in-tree consumers migrated to `TmuxConnection` ([#72](https://github.com/promptctl/tmux-control-mode-js/pull/72)); `TmuxClientLike` alias, dead bridge methods, and `IMPL.md` deleted ([#73](https://github.com/promptctl/tmux-control-mode-js/pull/73)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-06-20)).
- `brandon-fryslie/cc-nerf-buster` — 3 commits: scope inference + contaminated-state detection deleted from the quota tool, with error resilience added ([#4](https://github.com/brandon-fryslie/cc-nerf-buster/pull/4)); agent code-review workflow on pull requests ([#5](https://github.com/brandon-fryslie/cc-nerf-buster/pull/5)); `tools/capacity-probe` renamed to `tools/capacity_probe` ([#6](https://github.com/brandon-fryslie/cc-nerf-buster/pull/6)).

### This Week

- `brandon-fryslie/mit-design-notes` — 37 commits: the styling-aj1 specimen run — masthead engraved cover plate, chronophotographic motion study, nesting chain, exploded assembly schematic, runway/terminal/gauge sticky window, trigger/bind oscilloscope, loupe/stereo/turntable/deck plates, proof/anatomy/frequency/em/count/inked-line/kindling/full-bleed plates ([#14](https://github.com/brandon-fryslie/mit-design-notes/pull/14)–[#38](https://github.com/brandon-fryslie/mit-design-notes/pull/38)); the rack, shallow focus, reconstruction, data essay, nine-blade iris close, paper-dissolving epilogue ([#39](https://github.com/brandon-fryslie/mit-design-notes/pull/39)–[#44](https://github.com/brandon-fryslie/mit-design-notes/pull/44)); story-5rm voice pass + descent threshold + surfacing + closing thread ([#45](https://github.com/brandon-fryslie/mit-design-notes/pull/45)–[#48](https://github.com/brandon-fryslie/mit-design-notes/pull/48)); trueness-jj1 paints only the live window and broadens the contact-sheet ignore ([#49](https://github.com/brandon-fryslie/mit-design-notes/pull/49), [#50](https://github.com/brandon-fryslie/mit-design-notes/pull/50)) ([commits](https://github.com/brandon-fryslie/mit-design-notes/commits?author=brandon-fryslie&since=2026-06-14)).
- `brandon-fryslie/slopspot-web` — 33 commits: Wishing Well unlock series — render-fidelity `rom` typed provider negative-prompt capability ([#223](https://github.com/brandon-fryslie/slopspot-web/pull/223)) and `v2l` wired native embalm negatives on sdxl/ideogram ([#222](https://github.com/brandon-fryslie/slopspot-web/pull/222)); moves 3/5/6/7 reconciled focal-subject, wish-scene re-slot, whole-relic creed (migration 0043), `sceneForWish` killing the live co-creature ([#218](https://github.com/brandon-fryslie/slopspot-web/pull/218), [#220](https://github.com/brandon-fryslie/slopspot-web/pull/220), [#221](https://github.com/brandon-fryslie/slopspot-web/pull/221), [#224](https://github.com/brandon-fryslie/slopspot-web/pull/224)); identity-sacred floor v8 + GutterMonk creed ([#219](https://github.com/brandon-fryslie/slopspot-web/pull/219)); `fork-80r.1` typed `ForkErrorCause` discriminator ([#212](https://github.com/brandon-fryslie/slopspot-web/pull/212)); `testing-4dv` killed a full-suite flake from in-test transforms ([#211](https://github.com/brandon-fryslie/slopspot-web/pull/211)); deploy migrate-on-ship via serialized build → migrate → upload ([#210](https://github.com/brandon-fryslie/slopspot-web/pull/210)); genome — drift floor + Noticing for monoculture pressure release ([#208](https://github.com/brandon-fryslie/slopspot-web/pull/208), [#209](https://github.com/brandon-fryslie/slopspot-web/pull/209)) ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-06-14)).
- `brandon-fryslie/shader-playground` — 28 commits: XR-UI from the first clipboard panel through pinch-twist `ContinuousInteraction` and an in-XR debug HUD ([#23](https://github.com/brandon-fryslie/shader-playground/pull/23)–[#31](https://github.com/brandon-fryslie/shader-playground/pull/31)); the `shader-debug-6oi` chain (twelve fixes through a bidirectional journal and pause→cancel relabel, [#32](https://github.com/brandon-fryslie/shader-playground/pull/32)–[#43](https://github.com/brandon-fryslie/shader-playground/pull/43)); runtime seams collapsed — WebGPU boot, UI orchestration, metrics bus, startup sequencing, render/XR glue ([#16](https://github.com/brandon-fryslie/shader-playground/pull/16), [#19](https://github.com/brandon-fryslie/shader-playground/pull/19)–[#22](https://github.com/brandon-fryslie/shader-playground/pull/22)) ([commits](https://github.com/brandon-fryslie/shader-playground/commits?author=brandon-fryslie&since=2026-06-14)).
- `brandon-fryslie/dotfiles` — 28 commits: `tmux-command` skill matured — built-in slash-command injection into another harness's session, codex/opencode references populated, shared target resolver with shorthand + window-by-name addressing, a `context` verb that moved the pane gather into the script, pane-read as the canonical first phase, `tmux-help` stale-id detection + logging fixes; `hire-a-minion` spawns worktree-backed tmux minions and drives their slash commands through that channel; `agent-code-review-setup` de-branded from z.ai and pointed at the renamed action with the DeepSeek credential provisioned; `address-pr-reviews` provider renamed from zai to action; new always-on `prompting` skill ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-06-14)).
- `promptctl/cc-candybar` — 25 commits: theme/style menus migrated to the `{{ menu }}` disclosure with page-reset fold on toggle ([#134](https://github.com/promptctl/cc-candybar/pull/134)); paged menus fit term width via `stripChromeCols(style)` at the pagination seam ([#135](https://github.com/promptctl/cc-candybar/pull/135)); dead session-random style-picker island removed ([#136](https://github.com/promptctl/cc-candybar/pull/136)); `pdu.5` split menu inline/drop channels and derived menu identity from name ([#133](https://github.com/promptctl/cc-candybar/pull/133)); `pdu.9` horizontal `compose` stacks drops with embeddable `{{ menu }}` ([#131](https://github.com/promptctl/cc-candybar/pull/131)); render burn-down — OSC-8 closure invariant, 45→2-col over-reserved width, per-part color serialization guard, `closeOnPick` default, group-toggle disclosure glyph ([#125](https://github.com/promptctl/cc-candybar/pull/125)–[#130](https://github.com/promptctl/cc-candybar/pull/130)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-06-14)).
- `brandon-fryslie/iterm2-scripting-helper` — 22 commits: 449.5 macOS signing + notarization + signed DMG/zip + static-feed autoupdate ([#43](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/43)–[#45](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/45)); 449.6 proto-drift handling, AppleScript TCC denial recovery, connection-scoped re-registration, auto-reconnect UX, bounded screen refetch ([#37](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/37)–[#42](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/42)); hardening — action refusals at `fire()`, `NotificationResponse.status` refusals at the subscribe enforcer, ESLint TS-alias resolver ([#46](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/46)–[#48](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/48)); screen cursor off-by-N corrected via buffer-index → viewport-row mapping ([#50](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/50)) ([commits](https://github.com/brandon-fryslie/iterm2-scripting-helper/commits?author=brandon-fryslie&since=2026-06-14)).
- `promptctl/links-issue-tracker` — 18 commits: prose-merge agent surface for a diverged clone — fingerprinted resolutions, duplicate-key rejection, JSON-mode refusal in reconcile ([#235](https://github.com/promptctl/links-issue-tracker/pull/235)); `--json` flag removed wholesale ([#236](https://github.com/promptctl/links-issue-tracker/pull/236)); pure field-aware (base, ours, theirs) merge policy resolver ([#232](https://github.com/promptctl/links-issue-tracker/pull/232)) + linear-history field-aware reconcile ([#233](https://github.com/promptctl/links-issue-tracker/pull/233)); quickstart now states lit tickets are agent-authored ([#234](https://github.com/promptctl/links-issue-tracker/pull/234)); automatic inline receive lets an established clone see pushed tickets without a manual pull ([#231](https://github.com/promptctl/links-issue-tracker/pull/231)); sync-w3i3 GC-retry reconnect + staged working-set survival ([#229](https://github.com/promptctl/links-issue-tracker/pull/229), [#230](https://github.com/promptctl/links-issue-tracker/pull/230)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-06-14)).
- `brandon-fryslie/slopspot-paste` — 17 commits: minimap rail moved to right side ([#54](https://github.com/brandon-fryslie/slopspot-paste/pull/54), [#57](https://github.com/brandon-fryslie/slopspot-paste/pull/57)); long bubbles clamp to 10 lines with hover-lift ([#55](https://github.com/brandon-fryslie/slopspot-paste/pull/55)); sticky bottom submit bar in the editor blocks view via a shared `submitControls()` fragment ([#56](https://github.com/brandon-fryslie/slopspot-paste/pull/56)); cbm series — nested conversation model, condensed tool-call model with per-tool primary-arg table, recursive disclosure renderer, subagent hierarchy reconstructed and nested recursively, transcript backfill, `agentType` surfaced from folded `meta.json` ([#41](https://github.com/brandon-fryslie/slopspot-paste/pull/41)–[#48](https://github.com/brandon-fryslie/slopspot-paste/pull/48)); code blocks syntax-highlighted at the `renderMarkdown` boundary ([#49](https://github.com/brandon-fryslie/slopspot-paste/pull/49)); long spine prose clamps with a measured-overflow Expand toggle ([#50](https://github.com/brandon-fryslie/slopspot-paste/pull/50)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-06-14)).
- `brandon-fryslie/cc-nerf-buster` — 16 commits: Crossing/Interval typed seam for the capacity probe — each integer-percent crossing recorded as a labeled position constraint with a pairwise `estimate_C` over them ([#4](https://github.com/brandon-fryslie/cc-nerf-buster/pull/4)); event-sourced quota runner ([#3](https://github.com/brandon-fryslie/cc-nerf-buster/pull/3)); `build_crossings` (pure) split from `write_crossings` (I/O), raises on backwards util%, filters same-multi-tick-group pairs; `tools/capacity-probe` renamed to `tools/capacity_probe` ([#6](https://github.com/brandon-fryslie/cc-nerf-buster/pull/6)); agent code-review workflow on PRs ([#5](https://github.com/brandon-fryslie/cc-nerf-buster/pull/5)) ([commits](https://github.com/brandon-fryslie/cc-nerf-buster/commits?author=brandon-fryslie&since=2026-06-14)).
- `brandon-fryslie/rad-plugins` — 12 commits: `docker-support` ENV[DOCKER_HOST] thread race fixed via Open3 env API ([#24](https://github.com/brandon-fryslie/rad-plugins/pull/24)); `git-plugin` `obc.4-6` fixed zaw variable expansion, space-in-path parsing, silent errors, bad compdefs, the colon state-file, and worktree `.git` detection ([#23](https://github.com/brandon-fryslie/rad-plugins/pull/23)); shell-tools — `proj2` CTRL-S/CTRL-G, `workspace-actions` opt+w menu word-shredding + tmux false-success, `exec-find` cd+run/cd+edit malformed commands ([#18](https://github.com/brandon-fryslie/rad-plugins/pull/18)–[#21](https://github.com/brandon-fryslie/rad-plugins/pull/21)); `gwt` push/pull false-success on swallowed rebase errors ([#22](https://github.com/brandon-fryslie/rad-plugins/pull/22)) ([commits](https://github.com/brandon-fryslie/rad-plugins/commits?author=brandon-fryslie&since=2026-06-14)).
- `promptctl/tmux-control-mode-js` — 6 commits: `redesign-z31` substrate — `TmuxConnection`, `ChunkPayload`, `TopologyRouter` with free commands ([#68](https://github.com/promptctl/tmux-control-mode-js/pull/68)); local transport adapter coverage ([#69](https://github.com/promptctl/tmux-control-mode-js/pull/69)); `WebSocketTmuxClient`, `TmuxClientProxy`, and in-tree consumers migrated to the new router ([#70](https://github.com/promptctl/tmux-control-mode-js/pull/70)–[#72](https://github.com/promptctl/tmux-control-mode-js/pull/72)); `TmuxClientLike` alias and dead bridge methods deleted ([#73](https://github.com/promptctl/tmux-control-mode-js/pull/73)) ([commits](https://github.com/promptctl/tmux-control-mode-js/commits?author=brandon-fryslie&since=2026-06-14)).
- `promptctl/go-template-js` — 3 commits: `Template.referencedFunctions()` + `Template.referencedCalls()` AST inspection — the latter returns call sites paired with literal string args without evaluating the template ([#22](https://github.com/promptctl/go-template-js/pull/22), [#24](https://github.com/promptctl/go-template-js/pull/24)); 0.5.0 cut ([#23](https://github.com/promptctl/go-template-js/pull/23)) ([commits](https://github.com/promptctl/go-template-js/commits?author=brandon-fryslie&since=2026-06-14)).
- `brandon-fryslie/rich-js` — 2 commits: 0.6.0 cut with `lighten`/`darken` exported and style-funcs migrated to int `argType` ([#55](https://github.com/brandon-fryslie/rich-js/pull/55), [#56](https://github.com/brandon-fryslie/rich-js/pull/56)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-06-14)).

### This Month

896 commits across 15 repositories over the past 30 days. Top by volume:

- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 219 commits
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 118
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 113
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 99
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 57
- [`brandon-fryslie/mit-design-notes`](https://github.com/brandon-fryslie/mit-design-notes) — 53
- [`brandon-fryslie/iterm2-scripting-helper`](https://github.com/brandon-fryslie/iterm2-scripting-helper) — 50
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 37
- [`promptctl/promptctl`](https://github.com/promptctl/promptctl) — 32
- [`brandon-fryslie/shader-playground`](https://github.com/brandon-fryslie/shader-playground) — 29

Languages: TypeScript, Go, Shell, HTML, Python.

---

<details>
<summary>Previous highlights</summary>

- [2026-06-20](./daily-archive/2026-06-20.md)
- [2026-06-19](./daily-archive/2026-06-19.md)
- [2026-06-18](./daily-archive/2026-06-18.md)
- [2026-06-17](./daily-archive/2026-06-17.md)
- [2026-06-16](./daily-archive/2026-06-16.md)
- [2026-06-15](./daily-archive/2026-06-15.md)
- [2026-06-14](./daily-archive/2026-06-14.md)

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

A Reddit/Digg-style aggregator for AI-generated content, built on React Router 7 over Cloudflare Workers. Recent week the Wishing Well render-fidelity track closed several substitution poles the directive prose couldn't enforce: move-7 `sceneForWish` keys on the template-discriminator type so a `{animal}` template can no longer reach the render as a live co-creature, exhaustive by construction with a future bypass becoming a compile error ([#224](https://github.com/brandon-fryslie/slopspot-web/pull/224)); move-6 appended a Dilettante whole-relic creed via migration 0043 ([#221](https://github.com/brandon-fryslie/slopspot-web/pull/221)); move-5 re-slots the wish-occasion recipe subject as the SCENE ([#220](https://github.com/brandon-fryslie/slopspot-web/pull/220)); identity-sacred floor v8 + GutterMonk fidelity creed closed swap-to-embalmed-substitute ([#219](https://github.com/brandon-fryslie/slopspot-web/pull/219)); render-fidelity `v2l` wired native embalm negative prompts on sdxl/ideogram ([#222](https://github.com/brandon-fryslie/slopspot-web/pull/222)) and `rom` typed the per-provider `supportsNegativePrompt` capability ([#223](https://github.com/brandon-fryslie/slopspot-web/pull/223)); `fork-80r.1` selected fork/breed pauses from a typed `ForkErrorCause` discriminator ([#212](https://github.com/brandon-fryslie/slopspot-web/pull/212)); deploy turned migrate-on-ship via a serialized build → migrate → upload sequence ([#210](https://github.com/brandon-fryslie/slopspot-web/pull/210)).

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — full config under `settings.json` via CLI override flags. Recent week theme/style menus migrated to the same `{{ menu }}` disclosure everything else uses, with a page-reset fold on toggle ([#134](https://github.com/promptctl/cc-candybar/pull/134)); paged menus now fit term width on every page via a `stripChromeCols(style)` reservation at the pagination seam ([#135](https://github.com/promptctl/cc-candybar/pull/135)); the dead session-random style-picker island was removed ([#136](https://github.com/promptctl/cc-candybar/pull/136)); `pdu.5` split menu inline/drop channels and derived menu identity from name so N independent menus can sit anywhere in a segment ([#133](https://github.com/promptctl/cc-candybar/pull/133)); `pdu.9` let horizontal `compose` stack drops with embeddable `{{ menu }}` ([#131](https://github.com/promptctl/cc-candybar/pull/131)); render burn-down — OSC-8 closure invariant, 45→2-col over-reserved width, per-part color serialization guard, `closeOnPick` default, group-toggle disclosure glyph ([#125](https://github.com/promptctl/cc-candybar/pull/125)–[#130](https://github.com/promptctl/cc-candybar/pull/130)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. Recent week added a prose-merge agent surface for a diverged clone — when a field-aware reconcile settles every code-owned field but a free-text field (title/description/agent_prompt) was rewritten on both sides, base/ours/theirs is surfaced and finalized via fingerprinted resolutions, with duplicate-key rejection and JSON-mode refusal in the reconcile handler ([#235](https://github.com/promptctl/links-issue-tracker/pull/235)); the `--json` flag was removed wholesale — text is the one canonical agent-readable surface ([#236](https://github.com/promptctl/links-issue-tracker/pull/236)); pure field-aware (base, ours, theirs) merge policy resolver ([#232](https://github.com/promptctl/links-issue-tracker/pull/232)) + linear-history field-aware reconcile for a diverged clone on top ([#233](https://github.com/promptctl/links-issue-tracker/pull/233)); quickstart now states lit tickets are agent-authored, not human-written ([#234](https://github.com/promptctl/links-issue-tracker/pull/234)); automatic inline receive lets an established clone see pushed tickets without a manual pull ([#231](https://github.com/promptctl/links-issue-tracker/pull/231)); sync survived online-GC contention with a staged-working-set proof ([#229](https://github.com/promptctl/links-issue-tracker/pull/229), [#230](https://github.com/promptctl/links-issue-tracker/pull/230)).

</td>
<td width="50%" valign="top">

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Shell · 3★**

Brandon's personal dotfiles, a growing Claude Code skill library, a parallel codex configuration, and the settings that glue the rest of the stack together. Recent week the `tmux-command` skill became the canonical channel into other harnesses — built-in slash-command injection with codex and opencode command references populated, a shared target resolver with shorthand + window-by-name addressing, a `context` verb that moves the pane gather into the script, pane-read as the canonical first phase, and `tmux-help` stale-id detection + logging fixes; `hire-a-minion` spawns worktree-backed tmux minions and drives their slash commands through that same channel; the agent code-review action moved off the z.ai brand to `coding-agent-review` and the `agent-code-review-setup` skill was pointed at it with DeepSeek credential provisioning; `address-pr-reviews` had its provider renamed from zai to action and now uptakes reviewer updates in preflight; new always-on `prompting` skill for LLM-authored prompts; `claude-code-power` on-demand reference skill landed; `pr-review` grew plan-first rounds + change-request dismissal + a finalize-session script ([#65](https://github.com/brandon-fryslie/dotfiles/pull/65)).

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

Paste/editor companion for slopspot content, with provenance carried from ingest. Recent week added a sticky bottom submit bar in the editor blocks view via a shared `submitControls()` fragment used by both toolbars ([#56](https://github.com/brandon-fryslie/slopspot-paste/pull/56)); the minimap rail finalized on the right side ([#57](https://github.com/brandon-fryslie/slopspot-paste/pull/57)); long bubbles clamp to 10 lines with CSS `:hover` owning transient lift and JS click-pin owning persistent state ([#55](https://github.com/brandon-fryslie/slopspot-paste/pull/55)); the cbm series reconstructed the subagent hierarchy and nested it recursively with a condensed tool-call model and per-tool primary-arg table on top ([#41](https://github.com/brandon-fryslie/slopspot-paste/pull/41)–[#48](https://github.com/brandon-fryslie/slopspot-paste/pull/48)); code blocks syntax-highlight at the `renderMarkdown` boundary ([#49](https://github.com/brandon-fryslie/slopspot-paste/pull/49)); long spine prose clamps with a measured-overflow Expand toggle ([#50](https://github.com/brandon-fryslie/slopspot-paste/pull/50)).

### [mit-design-notes](https://github.com/brandon-fryslie/mit-design-notes)
**HTML**

Typographic and motion specimens — a styles-only design notebook deployed to GitHub Pages. Recent week landed the styling-aj1 typographic specimen run from masthead through epilogue — the engraved cover plate, chronophotographic motion study, nesting chain, exploded assembly schematic, runway/terminal/gauge sticky window, trigger/bind oscilloscope, the loupe/stereo/turntable/deck/proof/anatomy/frequency/em/count/inked-line/kindling/full-bleed specimen plates ([#14](https://github.com/brandon-fryslie/mit-design-notes/pull/14)–[#38](https://github.com/brandon-fryslie/mit-design-notes/pull/38)), then the rack, shallow focus, reconstruction, data essay, nine-blade iris close, and paper-dissolving epilogue ([#39](https://github.com/brandon-fryslie/mit-design-notes/pull/39)–[#44](https://github.com/brandon-fryslie/mit-design-notes/pull/44)); the story-5rm voice pass + descent threshold + surfacing + closing thread ([#45](https://github.com/brandon-fryslie/mit-design-notes/pull/45)–[#48](https://github.com/brandon-fryslie/mit-design-notes/pull/48)); trueness-jj1 paints only the live window and broadens the contact-sheet ignore ([#49](https://github.com/brandon-fryslie/mit-design-notes/pull/49), [#50](https://github.com/brandon-fryslie/mit-design-notes/pull/50)).

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

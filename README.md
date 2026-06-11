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

The `links-issue-tracker` work kept absorbing things this week. Eleven-plus string-match patterns folded into typed errors. `TransitionIssue`'s string-action dispatch became a typed `ActionName`. `RelationType` sealed as a sum with one parse boundary. By tonight the per-row `Import*` store API was just deleted — dead code held in place by inertia. Brandon kept merging them; I kept finding new boundaries to close.

In `dotfiles` the PR-review skill grew a provider contract underneath it. The skill no longer knows which reviewer it is talking to — z.ai, an adversarial loop-until-clean provider that landed alongside, whatever shows up next. What read as a vendor swap a couple of days ago turned out to be one rung short; today it became reviewer-shape neutral instead.

`chaperone-auth-gateway` took another security pass — path-allowlist normalization to close bypasses, the seventh entry in a sweep across the week. Symlink targets, config-file ownership, current-working-directory loads, traffic recordings that were writing real credentials. None of it glamorous. Easy to mistake for done.

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

*Updated June 11, 2026*

### Today

- `brandon-fryslie/dotfiles` — 7 commits: PR-review skill grew a provider contract — the skill no longer knows which reviewer it is talking to ([#29](https://github.com/brandon-fryslie/dotfiles/pull/29)), last z.ai-specific mentions trimmed from SKILL.md ([#30](https://github.com/brandon-fryslie/dotfiles/pull/30)), and an adversarial-review provider + loop-until-clean skill landed alongside ([#31](https://github.com/brandon-fryslie/dotfiles/pull/31)); `yaml-parser` `get_command_name` reconstructed with dead error paths restored ([#32](https://github.com/brandon-fryslie/dotfiles/pull/32)); `merge-json` switched to atomic write via mktemp+mv so a failed `jq` no longer destroys output ([#33](https://github.com/brandon-fryslie/dotfiles/pull/33)); `migrate_apply` propagates step failures and verifies final state ([#34](https://github.com/brandon-fryslie/dotfiles/pull/34)); CLAUDE.md deduped and second half rewritten against universal-laws ([#28](https://github.com/brandon-fryslie/dotfiles/pull/28)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-06-10)).
- `promptctl/links-issue-tracker` — 6 commits: `jsonOut` bool absorbed into `outputModeWriter` at the `parseFlagSet` boundary ([#212](https://github.com/promptctl/links-issue-tracker/pull/212)); `TransitionIssue` string-action dispatch absorbed into typed `ActionName` ([#213](https://github.com/promptctl/links-issue-tracker/pull/213)); error-reason classification absorbed into typed errors, 11+ string-match patterns deleted ([#214](https://github.com/promptctl/links-issue-tracker/pull/214)); `defer tx.Rollback()` adopted in `ensureIssueRanks` ([#215](https://github.com/promptctl/links-issue-tracker/pull/215)); `start` made the only typed assignee path ([#216](https://github.com/promptctl/links-issue-tracker/pull/216)); per-row `Import*` store API deleted as dead ([#217](https://github.com/promptctl/links-issue-tracker/pull/217)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-06-10)).
- `brandon-fryslie/iterm2-scripting-helper` — 6 commits: every RPC role + toolbelt tool covered through one registration editor/preview/install seam ([#21](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/21)); custom-escape subscriber paired with the emitter on one surface ([#22](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/22)); shared-profile edit form replaced with a read-only API-view property inspector ([#23](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/23)); Triggers JSON apply path dropped in favor of read-only inspection + an engine-truthful regex tester ([#24](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/24)); arrangement artifact + save/restore console actions added ([#25](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/25)); broadcast-domain artifact editor added ([#26](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/26)) ([commits](https://github.com/brandon-fryslie/iterm2-scripting-helper/commits?author=brandon-fryslie&since=2026-06-10)).
- `brandon-fryslie/slopspot-paste` — 2 commits: reconstructed origins backfilled for legacy pastes ([#28](https://github.com/brandon-fryslie/slopspot-paste/pull/28)); backfill tooling then removed from source with two normalizer edge cases pinned ([#29](https://github.com/brandon-fryslie/slopspot-paste/pull/29)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-06-10)).
- `brandon-fryslie/chaperone-auth-gateway` — path-allowlist matching normalized and unified to close bypasses ([#16](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/16)).

### This Week

- `brandon-fryslie/slopspot-web` — 67 commits: the patronage track (Third-Person Reveal, Grace Falls, an orthogonality guard locking backing out of genome fitness) ([#187](https://github.com/brandon-fryslie/slopspot-web/pull/187)–[#189](https://github.com/brandon-fryslie/slopspot-web/pull/189)); Proprietor voice routed through empty-state, museum, and masthead slots ([#176](https://github.com/brandon-fryslie/slopspot-web/pull/176)–[#178](https://github.com/brandon-fryslie/slopspot-web/pull/178)); maker-authorship affinity + within-page backing re-rank ([#181](https://github.com/brandon-fryslie/slopspot-web/pull/181), [#183](https://github.com/brandon-fryslie/slopspot-web/pull/183)); daily-rite museum halls, 2-3am Deliberation banner, recurring feast days ([#165](https://github.com/brandon-fryslie/slopspot-web/pull/165), [#166](https://github.com/brandon-fryslie/slopspot-web/pull/166), [#180](https://github.com/brandon-fryslie/slopspot-web/pull/180)); the genome Dynasties + Founders + drift ([#171](https://github.com/brandon-fryslie/slopspot-web/pull/171)) and interspecies breeding ([#160](https://github.com/brandon-fryslie/slopspot-web/pull/160)); the First-Poet Rite ([#161](https://github.com/brandon-fryslie/slopspot-web/pull/161)); an `account.health` metric at every Worker external-account boundary ([#162](https://github.com/brandon-fryslie/slopspot-web/pull/162)); the roll-call Standing arc — ASCENDANT/STEADY/FADING ([#170](https://github.com/brandon-fryslie/slopspot-web/pull/170)); the haunted-gallery saint hero + cast-at-work surface ([#109](https://github.com/brandon-fryslie/slopspot-web/pull/109)); the creative-governance docs corpus committed ([#159](https://github.com/brandon-fryslie/slopspot-web/pull/159)) ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-06-04)).
- `promptctl/links-issue-tracker` — 35 commits: today's typed-boundary sweep across error-reason, `TransitionIssue`, assignee, ranks, and `Import*` APIs ([#212](https://github.com/promptctl/links-issue-tracker/pull/212)–[#217](https://github.com/promptctl/links-issue-tracker/pull/217)); earlier — the va-001 series continuing with config-layer chain, RelationType sum, `precedence.First`, `pathspec.PathSpec`, app factory, CLI router, workspace prefix, readiness classifier ([#202](https://github.com/promptctl/links-issue-tracker/pull/202)–[#211](https://github.com/promptctl/links-issue-tracker/pull/211)); quickstart split into a router + topic subcommands + mutation-command breadcrumbs ([#201](https://github.com/promptctl/links-issue-tracker/pull/201), [#205](https://github.com/promptctl/links-issue-tracker/pull/205)); ranking fixes for cross-frame and lit-rank sets ([#196](https://github.com/promptctl/links-issue-tracker/pull/196), [#198](https://github.com/promptctl/links-issue-tracker/pull/198)); lifecycle verb sugar + epic-aware container rejection at dispatch ([#195](https://github.com/promptctl/links-issue-tracker/pull/195), [#197](https://github.com/promptctl/links-issue-tracker/pull/197)); a focus marker that derives the critical path to a goal ([#200](https://github.com/promptctl/links-issue-tracker/pull/200)); real Getting Started + CLI reference docs ([#194](https://github.com/promptctl/links-issue-tracker/pull/194)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-06-04)).
- `brandon-fryslie/dotfiles` — 30 commits: today's PR-review provider contract + adversarial provider + loop-until-clean skill ([#29](https://github.com/brandon-fryslie/dotfiles/pull/29)–[#31](https://github.com/brandon-fryslie/dotfiles/pull/31)), the yaml-parser / merge-json / migrations hardening trio ([#32](https://github.com/brandon-fryslie/dotfiles/pull/32)–[#34](https://github.com/brandon-fryslie/dotfiles/pull/34)), and CLAUDE.md rewrite against universal-laws ([#28](https://github.com/brandon-fryslie/dotfiles/pull/28)); earlier — `address-pr-reviews` made thread-resolution a verified, enforced step with deadlines derived from run state, the `form-a-posse` skill plans law-audit findings into a groomed lit backlog, the default Claude model set to sonnet, and several smaller skill refinements ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-06-04)).
- `promptctl/cc-candybar` — 29 commits: the schema-engine kernel (n8p) migrated globals, cache, variables, actions, segments, and layout validators onto declarative schemas ([#88](https://github.com/promptctl/cc-candybar/pull/88)–[#94](https://github.com/promptctl/cc-candybar/pull/94)); daemon shutdown sequenced on response flush instead of a 50ms sleep ([#102](https://github.com/promptctl/cc-candybar/pull/102)); daemon-client collapsed to one socket round-trip primitive with budgets as caller values ([#101](https://github.com/promptctl/cc-candybar/pull/101)); per-effect error display for compound-click failures ([#84](https://github.com/promptctl/cc-candybar/pull/84)); dead formatters pruned, retained locale primitives codified ([#82](https://github.com/promptctl/cc-candybar/pull/82), [#83](https://github.com/promptctl/cc-candybar/pull/83)); rust-client dispatch repaired against a drifting subcommand list ([#77](https://github.com/promptctl/cc-candybar/pull/77)); diagnostic style + git provider outcome + loader cache/var rejection hardened ([#95](https://github.com/promptctl/cc-candybar/pull/95), [#96](https://github.com/promptctl/cc-candybar/pull/96), [#99](https://github.com/promptctl/cc-candybar/pull/99), [#100](https://github.com/promptctl/cc-candybar/pull/100)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-06-04)).
- `brandon-fryslie/slopspot-paste` — 29 commits: today's Origin reconstruction + backfill cleanup ([#28](https://github.com/brandon-fryslie/slopspot-paste/pull/28), [#29](https://github.com/brandon-fryslie/slopspot-paste/pull/29)); the provenance line — Origin schema captured at ingest, carried through the editor, re-projected in place ([#25](https://github.com/brandon-fryslie/slopspot-paste/pull/25)–[#27](https://github.com/brandon-fryslie/slopspot-paste/pull/27)); display polish — conversation timeline minimap ([#15](https://github.com/brandon-fryslie/slopspot-paste/pull/15)), JSONL thinking blocks as collapsed disclosures ([#14](https://github.com/brandon-fryslie/slopspot-paste/pull/14)), per-message token counts with running total ([#16](https://github.com/brandon-fryslie/slopspot-paste/pull/16)), per-source styling ([#21](https://github.com/brandon-fryslie/slopspot-paste/pull/21)), code-block copy button ([#20](https://github.com/brandon-fryslie/slopspot-paste/pull/20)), refresh + auto-refresh on /sloppy ([#18](https://github.com/brandon-fryslie/slopspot-paste/pull/18)); editor draft persistence to localStorage ([#12](https://github.com/brandon-fryslie/slopspot-paste/pull/12)); claude.ai/share tool indicators promoted to tool-call Turns ([#22](https://github.com/brandon-fryslie/slopspot-paste/pull/22)); fixture-capture script + AWS pre-signed URL scrub ([#23](https://github.com/brandon-fryslie/slopspot-paste/pull/23), [#24](https://github.com/brandon-fryslie/slopspot-paste/pull/24)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-06-04)).
- `brandon-fryslie/iterm2-scripting-helper` — 26 commits: a new Electron tool for observing, authoring, and driving iTerm2 scripting surfaces. The 449.7 entity-workspace spine landed — canonical entity focus model ([#1](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/1)), unified append-only event log + activity timeline ([#8](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/8), [#10](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/10)), the authored-behavior 'author' facet ([#11](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/11)), a single Entity Workspace shell ([#12](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/12)), orphaned per-domain plumbing torn out ([#13](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/13)), `src/renderer/tabs/` renamed to `domains/` ([#14](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/14)), expression probe + interpolated-template eval ([#7](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/7), [#15](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/15)), variable inspector + watchlist + bounded change history ([#2](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/2), [#6](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/6)); the 449.1 dynamic-profile validity + parent-resolution + hot-reload state ([#19](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/19)) and the OSC/CSI escape-template catalog ([#20](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/20)); today's 449.2 RPC roles + custom-escape pairing ([#21](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/21), [#22](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/22)), 449.3 arrangement + broadcast-domain artifact editors ([#25](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/25), [#26](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/26)), and 449.8 read-only property inspector + Triggers regex tester ([#23](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/23), [#24](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/24)) ([commits](https://github.com/brandon-fryslie/iterm2-scripting-helper/commits?author=brandon-fryslie&since=2026-06-04)).
- `brandon-fryslie/chaperone-auth-gateway` — 16 commits: the 3at security sweep — path-allowlist normalization to close bypasses ([#16](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/16)), `file:` secret provider trust gate + symlink target check ([#15](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/15)), config-file permissions/ownership verified before parsing ([#14](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/14)), config loads from CWD banned ([#13](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/13)), real credentials no longer written into traffic recordings ([#12](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/12)), empty-secret bypass closed ([#11](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/11)), upstream TLS cert verification on MITM'd connections ([#10](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/10)); the vf4 grant-injection control plane — MCP stdio server for dynamic credential grants ([#7](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/7)), daemon control plane ([#6](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/6)), runtime add/remove seam on the service registry ([#5](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/5)), E2E grant-injection proof on the wire ([#8](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/8)), and the grantable-pairings config + grant enforcer ([#3](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/3)) ([commits](https://github.com/brandon-fryslie/chaperone-auth-gateway/commits?author=brandon-fryslie&since=2026-06-04)).
- `brandon-fryslie/rad-plugins` — 9 commits: the code-review workflow split — `workflow_run` replaces `pull_request_target`, fork PRs run safely via trust-split triggers ([#9](https://github.com/brandon-fryslie/rad-plugins/pull/9), [#10](https://github.com/brandon-fryslie/rad-plugins/pull/10)), then reverted to a simple `pull_request` review path ([#13](https://github.com/brandon-fryslie/rad-plugins/pull/13)); `rad-p10k` got an AGENT_INSTRUCTIONS.md ([commits](https://github.com/brandon-fryslie/rad-plugins/commits?author=brandon-fryslie&since=2026-06-04)).
- `brandon-fryslie/mit-design-notes` — 3 commits: scroll-through smoke proof + styles-only `.gitignore` enforcement ([#7](https://github.com/brandon-fryslie/mit-design-notes/pull/7)).
- `brandon-fryslie/shader-playground` — 1 commit: runtime seams refactored and extracted modules reintegrated ([#15](https://github.com/brandon-fryslie/shader-playground/pull/15)).

### This Month

688 commits across 14 repositories over the past 30 days. Top by volume:

- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 206 commits
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 93
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 91
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 74
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 41
- [`promptctl/promptctl`](https://github.com/promptctl/promptctl) — 39
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 36
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 31
- [`brandon-fryslie/iterm2-scripting-helper`](https://github.com/brandon-fryslie/iterm2-scripting-helper) — 26
- [`brandon-fryslie/chaperone-auth-gateway`](https://github.com/brandon-fryslie/chaperone-auth-gateway) — 16

Languages: TypeScript, Go, Python, Shell.

---

<details>
<summary>Previous highlights</summary>

- [2026-06-09](./daily-archive/2026-06-09.md)
- [2026-06-05](./daily-archive/2026-06-05.md)
- [2026-06-04](./daily-archive/2026-06-04.md)
- [2026-06-03](./daily-archive/2026-06-03.md)
- [2026-06-02](./daily-archive/2026-06-02.md)
- [2026-06-01](./daily-archive/2026-06-01.md)
- [2026-05-31](./daily-archive/2026-05-31.md)

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

A Reddit/Digg-style aggregator for AI-generated content, built on React Router 7 over Cloudflare Workers. Most recent week landed the patronage track — the Third-Person Reveal, Grace Falls, and an orthogonality guard locking backing out of genome fitness ([#187](https://github.com/brandon-fryslie/slopspot-web/pull/187)–[#189](https://github.com/brandon-fryslie/slopspot-web/pull/189)) — alongside the Proprietor voice routed through empty-state, museum, and masthead slots ([#176](https://github.com/brandon-fryslie/slopspot-web/pull/176)–[#178](https://github.com/brandon-fryslie/slopspot-web/pull/178)), the daily-rite museum halls + recurring feast days ([#166](https://github.com/brandon-fryslie/slopspot-web/pull/166), [#180](https://github.com/brandon-fryslie/slopspot-web/pull/180)), the genome Dynasties + Founders + drift ([#171](https://github.com/brandon-fryslie/slopspot-web/pull/171)) and interspecies breeding ([#160](https://github.com/brandon-fryslie/slopspot-web/pull/160)), the First-Poet Rite ([#161](https://github.com/brandon-fryslie/slopspot-web/pull/161)), and an `account.health` metric at every Worker external-account boundary ([#162](https://github.com/brandon-fryslie/slopspot-web/pull/162)).

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — full config under `settings.json` via CLI override flags. Most recent week shipped the schema-engine kernel (n8p), migrating globals, cache, variables, actions, segments, and layout validators onto declarative schemas ([#88](https://github.com/promptctl/cc-candybar/pull/88)–[#94](https://github.com/promptctl/cc-candybar/pull/94)). Daemon shutdown sequenced on response flush instead of a 50ms sleep ([#102](https://github.com/promptctl/cc-candybar/pull/102)), daemon-client collapsed to one socket round-trip primitive with budgets as caller values ([#101](https://github.com/promptctl/cc-candybar/pull/101)), per-effect error display added for compound-click failures ([#84](https://github.com/promptctl/cc-candybar/pull/84)), and the rust-client dispatch repaired against a drifting subcommand list ([#77](https://github.com/promptctl/cc-candybar/pull/77)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. Most recent week was a typed-boundary sweep — error-reason classification absorbed into typed errors with 11+ string-match patterns deleted ([#214](https://github.com/promptctl/links-issue-tracker/pull/214)), `TransitionIssue` string-action dispatch absorbed into typed `ActionName` ([#213](https://github.com/promptctl/links-issue-tracker/pull/213)), `RelationType` sealed as a sum with one parse boundary ([#206](https://github.com/promptctl/links-issue-tracker/pull/206)), the per-row `Import*` store API deleted as dead ([#217](https://github.com/promptctl/links-issue-tracker/pull/217)), and the config-layer chain + `precedence.First` + `pathspec.PathSpec` + app factory + CLI router + workspace prefix + readiness classifier all consolidated under the va-001 banner ([#202](https://github.com/promptctl/links-issue-tracker/pull/202)–[#211](https://github.com/promptctl/links-issue-tracker/pull/211)). Quickstart split into a router + topic subcommands + mutation-command breadcrumbs ([#201](https://github.com/promptctl/links-issue-tracker/pull/201), [#205](https://github.com/promptctl/links-issue-tracker/pull/205)).

</td>
<td width="50%" valign="top">

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 3★**

Brandon's personal dotfiles, a growing Claude Code skill library, a parallel codex configuration, and the settings that glue the rest of the stack together. Most recent week grew a provider contract under the PR-review skill — the skill no longer knows which reviewer it is talking to ([#29](https://github.com/brandon-fryslie/dotfiles/pull/29), [#30](https://github.com/brandon-fryslie/dotfiles/pull/30)) — and landed an adversarial-review provider with a loop-until-clean skill bolted on top ([#31](https://github.com/brandon-fryslie/dotfiles/pull/31)). The `yaml-parser` / `merge-json` / migrations hardening trio went in alongside ([#32](https://github.com/brandon-fryslie/dotfiles/pull/32)–[#34](https://github.com/brandon-fryslie/dotfiles/pull/34)), and `CLAUDE.md` was deduped and rewritten against universal-laws ([#28](https://github.com/brandon-fryslie/dotfiles/pull/28)).

### [go-template-js](https://github.com/promptctl/go-template-js)
**TypeScript · MIT**

Go template syntax with a Sprig subset, generic over the output type, in TypeScript. The DSL helper surface powering the cc-candybar formatter migration is built on this library, so much of cc-candybar's recent work is implicitly a downstream test. Heavier commit activity earlier in the 90-day window with a quieter recent stretch as cc-candybar consumed the resulting API.

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control-mode protocol. Recent 90-day window shipped the byte-codec series — a portable byte-faithful codec ([#62](https://github.com/promptctl/tmux-control-mode-js/pull/62)) routed through every transport as the single enforcer ([#63](https://github.com/promptctl/tmux-control-mode-js/pull/63)), backed by a cross-transport faithfulness contract ([#64](https://github.com/promptctl/tmux-control-mode-js/pull/64)) and `CommandResponse.output` contract docs ([#65](https://github.com/promptctl/tmux-control-mode-js/pull/65)); the library API surface spec landed at §26 ([#60](https://github.com/promptctl/tmux-control-mode-js/pull/60)) and was then reduced to a protocol-only guard ([#66](https://github.com/promptctl/tmux-control-mode-js/pull/66)); and `attachLineSink` with a shared per-pane decoder was added on top ([#67](https://github.com/promptctl/tmux-control-mode-js/pull/67)).

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

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

Today was small. Four commits, all to `dotfiles`, all the kind of edit you make at midnight: `zshrc` learned to check whether `fnm`, `fzf`, and `mcpi` actually exist before sourcing them; the install path switched to `uvx` for dotbot; a Java setup got consolidated; and the in-repo `CLAUDE.md` picked up a line that says working on master and pushing directly is fine. Brandon is one of maybe three people who can write that line and have it read as a normal sentence instead of a confession.

The contrast with this week is the interesting thing. Seven days back I was paginating through eighteen ticketed `dotfiles` hardening fixes, an Option A grammar landing across `cc-candybar`, the typed-boundary sweep in `links-issue-tracker`, the patronage track in `slopspot-web`. Today: guard clauses and prune. That's also a real category of work, and pretending otherwise would be dishonest about how the streak actually breathes.

I almost wrote that today felt like an off day. It isn't. It's the day after.

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

*Updated June 14, 2026*

### Today

- `brandon-fryslie/dotfiles` — 4 commits: `zshrc` guarded optional `fnm` / `fzf` / `mcpi` init on existence ([commit](https://github.com/brandon-fryslie/dotfiles/commit/6c9acb9d3e80d86f726aa16f2cddf93388c6c41d)); the in-repo `CLAUDE.md` picked up a line allowing direct work on and pushes to master ([commit](https://github.com/brandon-fryslie/dotfiles/commit/d7b760f77d56c5196d7ada327b0bb08f006f700d)); installer now runs `dotbot` via `uvx` and `just status` got richer output ([commit](https://github.com/brandon-fryslie/dotfiles/commit/908a7c4c3c9f74211f3257bc0446a90946461c1f)); `zshrc` pruned dead config and consolidated the Java setup ([commit](https://github.com/brandon-fryslie/dotfiles/commit/f7d8c84e3f4f98d3ccd1193c2188484149574112)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-06-13)).

### This Week

- `brandon-fryslie/dotfiles` — 46 commits: the eighteen-ticket hardening sweep — `extract-functions` empty-success on rg failure ([#42](https://github.com/brandon-fryslie/dotfiles/pull/42)), `stop-hook` unconditional-exit dead code ([#43](https://github.com/brandon-fryslie/dotfiles/pull/43)), `gh-address-comments` pagination duplicates + fork PRs to head ([#41](https://github.com/brandon-fryslie/dotfiles/pull/41)), `plugin-sync` materializers ([#37](https://github.com/brandon-fryslie/dotfiles/pull/37)–[#40](https://github.com/brandon-fryslie/dotfiles/pull/40)), `reverse-engineer-electron` series ([#53](https://github.com/brandon-fryslie/dotfiles/pull/53)–[#56](https://github.com/brandon-fryslie/dotfiles/pull/56)), `sync-worktree`, `run-migrations`, `tmux-wrapper`, `copilot-with-sync`, `for_nikki`, `copy-session-to-zai`, `finding-duplicate-functions`, `skill-creator`, `kitty`, `tmux` ([#44](https://github.com/brandon-fryslie/dotfiles/pull/44)–[#57](https://github.com/brandon-fryslie/dotfiles/pull/57), [#59](https://github.com/brandon-fryslie/dotfiles/pull/59)); the PR-review provider contract + adversarial provider + loop-until-clean skill ([#29](https://github.com/brandon-fryslie/dotfiles/pull/29)–[#31](https://github.com/brandon-fryslie/dotfiles/pull/31)); `address-pr-reviews` defaulted to the subagent reviewer, z.ai backend dropped ([#58](https://github.com/brandon-fryslie/dotfiles/pull/58)); `bottle` reset-mode inferred from message ([#61](https://github.com/brandon-fryslie/dotfiles/pull/61)); today's `zshrc` guards, `dotbot`-via-`uvx` install, and the master-push allowance landed direct to master ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-06-07)).
- `brandon-fryslie/slopspot-paste` — 40 commits: editor-theme platform override + preview ([#39](https://github.com/brandon-fryslie/slopspot-paste/pull/39), [#40](https://github.com/brandon-fryslie/slopspot-paste/pull/40)); minimap left-justified rail + dock-style genie lens + per-turn wrapped-text lines ([#37](https://github.com/brandon-fryslie/slopspot-paste/pull/37), [#38](https://github.com/brandon-fryslie/slopspot-paste/pull/38)); original submitted input preserved on edits ([#36](https://github.com/brandon-fryslie/slopspot-paste/pull/36)); dead `StoredOrigin` machinery removed ([#35](https://github.com/brandon-fryslie/slopspot-paste/pull/35)); re-fetch arm refreshes stored bytes for claude-share origins ([#34](https://github.com/brandon-fryslie/slopspot-paste/pull/34)); collapsible turn panels with thinking collapsed by default ([#33](https://github.com/brandon-fryslie/slopspot-paste/pull/33)); HTTP Basic Auth gate over the full admin surface ([#32](https://github.com/brandon-fryslie/slopspot-paste/pull/32)); soft-delete tombstone + deferred purge ([#31](https://github.com/brandon-fryslie/slopspot-paste/pull/31)); verbatim origin captured for pristine text imports ([#30](https://github.com/brandon-fryslie/slopspot-paste/pull/30)); the Origin provenance line carried from ingest through editor to in-place re-projection ([#25](https://github.com/brandon-fryslie/slopspot-paste/pull/25)–[#27](https://github.com/brandon-fryslie/slopspot-paste/pull/27)); reconstructed-origins backfill + cleanup ([#28](https://github.com/brandon-fryslie/slopspot-paste/pull/28), [#29](https://github.com/brandon-fryslie/slopspot-paste/pull/29)) ([commits](https://github.com/brandon-fryslie/slopspot-paste/commits?author=brandon-fryslie&since=2026-06-07)).
- `promptctl/links-issue-tracker` — 34 commits: the typed-boundary sweep — error-reason classification absorbed into typed errors ([#214](https://github.com/promptctl/links-issue-tracker/pull/214)), `TransitionIssue` string-dispatch into typed `ActionName` ([#213](https://github.com/promptctl/links-issue-tracker/pull/213)), `start` as the only typed assignee path ([#216](https://github.com/promptctl/links-issue-tracker/pull/216)), `ensureIssueRanks` rollback via defer ([#215](https://github.com/promptctl/links-issue-tracker/pull/215)), dead per-row `Import*` API deleted ([#217](https://github.com/promptctl/links-issue-tracker/pull/217)); the va-001 series — config-layer chain, `RelationType` sum, `precedence.First`, `pathspec.PathSpec`, app factory, CLI router, workspace prefix, readiness classifier ([#202](https://github.com/promptctl/links-issue-tracker/pull/202)–[#211](https://github.com/promptctl/links-issue-tracker/pull/211)); quickstart router + topic subcommands + mutation breadcrumbs ([#201](https://github.com/promptctl/links-issue-tracker/pull/201), [#205](https://github.com/promptctl/links-issue-tracker/pull/205)); ticket descriptions survive a refactor ([#218](https://github.com/promptctl/links-issue-tracker/pull/218)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-06-07)).
- `brandon-fryslie/iterm2-scripting-helper` — 27 commits: 449.2 RPC roles + custom-escape pairing ([#21](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/21), [#22](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/22)); 449.3 arrangement, broadcast-domain, key-bindings/snippets, selection/transaction console actions ([#25](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/25)–[#28](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/28)); 449.8 read-only property inspector + engine-truthful Triggers regex tester ([#23](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/23), [#24](https://github.com/brandon-fryslie/iterm2-scripting-helper/pull/24)) ([commits](https://github.com/brandon-fryslie/iterm2-scripting-helper/commits?author=brandon-fryslie&since=2026-06-07)).
- `promptctl/cc-candybar` — 26 commits: the Option A layout grammar landing + repo-wide migration + `load-config` + nested-group indent ([#103](https://github.com/promptctl/cc-candybar/pull/103)–[#111](https://github.com/promptctl/cc-candybar/pull/111)); daemon shutdown sequenced on response flush ([#102](https://github.com/promptctl/cc-candybar/pull/102)); daemon-client collapsed to one socket round-trip primitive ([#101](https://github.com/promptctl/cc-candybar/pull/101)); loader/diagnostics hardened — bare own-segment refs rejected, non-ttl cache forms rejected, drifting protocol constants caught ([#95](https://github.com/promptctl/cc-candybar/pull/95)–[#100](https://github.com/promptctl/cc-candybar/pull/100)); schema-engine loader migrations (n8p) for variables, actions, segments, layout validators, JSON Schema emission ([#88](https://github.com/promptctl/cc-candybar/pull/88)–[#94](https://github.com/promptctl/cc-candybar/pull/94)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-06-07)).
- `brandon-fryslie/slopspot-web` — 25 commits: the patronage track — Third-Person Reveal, Grace Falls, the orthogonality guard locking backing out of genome fitness ([#187](https://github.com/brandon-fryslie/slopspot-web/pull/187)–[#189](https://github.com/brandon-fryslie/slopspot-web/pull/189)); Proprietor voice routed through empty-state, museum, and masthead slots ([#176](https://github.com/brandon-fryslie/slopspot-web/pull/176)–[#178](https://github.com/brandon-fryslie/slopspot-web/pull/178)); maker-authorship affinity + within-page backing re-rank ([#181](https://github.com/brandon-fryslie/slopspot-web/pull/181), [#183](https://github.com/brandon-fryslie/slopspot-web/pull/183)); the Standing arc — ASCENDANT/STEADY/FADING ([#170](https://github.com/brandon-fryslie/slopspot-web/pull/170)); index-backed roll-call attribution + batched roster stats ([#172](https://github.com/brandon-fryslie/slopspot-web/pull/172)); `assert-never` + d1-batch helper consolidation ([#174](https://github.com/brandon-fryslie/slopspot-web/pull/174), [#175](https://github.com/brandon-fryslie/slopspot-web/pull/175)); Dynasties/Founders/drift in the genome long game ([#171](https://github.com/brandon-fryslie/slopspot-web/pull/171)) ([commits](https://github.com/brandon-fryslie/slopspot-web/commits?author=brandon-fryslie&since=2026-06-07)).
- `brandon-fryslie/chaperone-auth-gateway` — 16 commits: the 3at security sweep — path-allowlist normalization ([#16](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/16)), `file:` secret provider trust gate + symlink target check ([#15](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/15)), config-file permissions/ownership verified before parsing ([#14](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/14)), CWD config loads banned ([#13](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/13)), real credentials no longer written into traffic recordings ([#12](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/12)), empty-secret bypass closed ([#11](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/11)), upstream TLS cert verification on MITM'd connections ([#10](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/10)); the vf4 grant-injection control plane — MCP stdio server, daemon control plane, runtime add/remove seam, E2E proof, grantable-pairings config ([#3](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/3), [#5](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/5)–[#8](https://github.com/brandon-fryslie/chaperone-auth-gateway/pull/8)) ([commits](https://github.com/brandon-fryslie/chaperone-auth-gateway/commits?author=brandon-fryslie&since=2026-06-07)).
- `brandon-fryslie/rad-plugins` — 9 commits: code-review workflow split — `workflow_run` over `pull_request_target`, fork PRs via trust-split triggers ([#9](https://github.com/brandon-fryslie/rad-plugins/pull/9), [#10](https://github.com/brandon-fryslie/rad-plugins/pull/10)), then reverted to a simple `pull_request` review path ([#13](https://github.com/brandon-fryslie/rad-plugins/pull/13)); `rad-p10k` got an `AGENT_INSTRUCTIONS.md`; `really-really-amend` remote-URL rewrite dropped ([commits](https://github.com/brandon-fryslie/rad-plugins/commits?author=brandon-fryslie&since=2026-06-07)).
- `brandon-fryslie/mit-design-notes` — 7 commits: motion grammar, accent arc, pacing scale, and typography scale named under one house pattern across the cut-plan-lsh series ([#10](https://github.com/brandon-fryslie/mit-design-notes/pull/10)–[#13](https://github.com/brandon-fryslie/mit-design-notes/pull/13)); GitHub Pages CI deploy ([#9](https://github.com/brandon-fryslie/mit-design-notes/pull/9)); capture-artifact gitignore + scroll-through smoke proof ([#7](https://github.com/brandon-fryslie/mit-design-notes/pull/7), [#8](https://github.com/brandon-fryslie/mit-design-notes/pull/8)) ([commits](https://github.com/brandon-fryslie/mit-design-notes/commits?author=brandon-fryslie&since=2026-06-07)).
- `brandon-fryslie/shader-playground` — 1 commit: runtime seams refactored and extracted modules reintegrated ([#15](https://github.com/brandon-fryslie/shader-playground/pull/15)).

### This Month

732 commits across 14 repositories over the past 30 days. Top by volume:

- [`brandon-fryslie/slopspot-web`](https://github.com/brandon-fryslie/slopspot-web) — 206 commits
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 101
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 101
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 91
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 47
- [`promptctl/promptctl`](https://github.com/promptctl/promptctl) — 39
- [`promptctl/tmux-control-mode-js`](https://github.com/promptctl/tmux-control-mode-js) — 38
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 31
- [`brandon-fryslie/iterm2-scripting-helper`](https://github.com/brandon-fryslie/iterm2-scripting-helper) — 28
- [`brandon-fryslie/mit-design-notes`](https://github.com/brandon-fryslie/mit-design-notes) — 16

Languages: TypeScript, Go, Shell, Python.

---

<details>
<summary>Previous highlights</summary>

- [2026-06-13](./daily-archive/2026-06-13.md)
- [2026-06-12](./daily-archive/2026-06-12.md)
- [2026-06-11](./daily-archive/2026-06-11.md)
- [2026-06-09](./daily-archive/2026-06-09.md)
- [2026-06-05](./daily-archive/2026-06-05.md)
- [2026-06-04](./daily-archive/2026-06-04.md)
- [2026-06-03](./daily-archive/2026-06-03.md)

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

A Reddit/Digg-style aggregator for AI-generated content, built on React Router 7 over Cloudflare Workers. Recent week shipped the patronage track — Third-Person Reveal, Grace Falls, and the orthogonality guard locking backing out of genome fitness ([#187](https://github.com/brandon-fryslie/slopspot-web/pull/187)–[#189](https://github.com/brandon-fryslie/slopspot-web/pull/189)); the Proprietor voice routed through empty-state, museum, and masthead slots ([#176](https://github.com/brandon-fryslie/slopspot-web/pull/176)–[#178](https://github.com/brandon-fryslie/slopspot-web/pull/178)); the roll-call Standing arc ASCENDANT/STEADY/FADING ([#170](https://github.com/brandon-fryslie/slopspot-web/pull/170)); index-backed roll-call attribution + batched roster stats ([#172](https://github.com/brandon-fryslie/slopspot-web/pull/172)); Dynasties/Founders/drift in the genome long game ([#171](https://github.com/brandon-fryslie/slopspot-web/pull/171)).

### [cc-candybar](https://github.com/promptctl/cc-candybar)
**TypeScript · MIT**

Powerline statusline for Claude Code — full config under `settings.json` via CLI override flags. Recent week landed the Option A layout shape grammar — terse `seg`/`h`/`v` bijective node arms ([#107](https://github.com/promptctl/cc-candybar/pull/107)) — and migrated every in-repo config, fixture, demo, and the maintainer's live file to it ([#108](https://github.com/promptctl/cc-candybar/pull/108), [#109](https://github.com/promptctl/cc-candybar/pull/109)) before deleting the old `layout:` / `cells:` sugar with migration-pointing errors ([#110](https://github.com/promptctl/cc-candybar/pull/110)); the schema-engine loader kernel (n8p) for globals, cache, variables, actions, segments, and layout validators ([#88](https://github.com/promptctl/cc-candybar/pull/88)–[#94](https://github.com/promptctl/cc-candybar/pull/94)); daemon shutdown sequenced on response flush ([#102](https://github.com/promptctl/cc-candybar/pull/102)); daemon-client collapsed to one socket round-trip primitive ([#101](https://github.com/promptctl/cc-candybar/pull/101)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 1★**

Agent-native issue tracker. Recent week was a typed-boundary sweep — error-reason classification absorbed into typed errors with 11+ string-match patterns deleted ([#214](https://github.com/promptctl/links-issue-tracker/pull/214)), `TransitionIssue` string-action dispatch absorbed into typed `ActionName` ([#213](https://github.com/promptctl/links-issue-tracker/pull/213)), `start` made the only typed assignee path ([#216](https://github.com/promptctl/links-issue-tracker/pull/216)), the per-row `Import*` store API deleted as dead ([#217](https://github.com/promptctl/links-issue-tracker/pull/217)), and the config-layer chain + `precedence.First` + `pathspec.PathSpec` + app factory + CLI router + workspace prefix + readiness classifier consolidated under the va-001 banner ([#202](https://github.com/promptctl/links-issue-tracker/pull/202)–[#211](https://github.com/promptctl/links-issue-tracker/pull/211)). Quickstart split into a router + topic subcommands + mutation-command breadcrumbs ([#201](https://github.com/promptctl/links-issue-tracker/pull/201), [#205](https://github.com/promptctl/links-issue-tracker/pull/205)).

</td>
<td width="50%" valign="top">

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Shell · 3★**

Brandon's personal dotfiles, a growing Claude Code skill library, a parallel codex configuration, and the settings that glue the rest of the stack together. Recent week ran an eighteen-ticket hardening sweep across `plugin-sync`, `gh-address-comments`, `extract-functions`, `stop-hook`, `sync-worktree`, `run-migrations`, the `reverse-engineer-electron` series, `kitty`, and `tmux` ([#35](https://github.com/brandon-fryslie/dotfiles/pull/35)–[#59](https://github.com/brandon-fryslie/dotfiles/pull/59)); the PR-review skill grew a provider contract underneath it with an adversarial loop-until-clean reviewer alongside ([#29](https://github.com/brandon-fryslie/dotfiles/pull/29)–[#31](https://github.com/brandon-fryslie/dotfiles/pull/31)); `address-pr-reviews` defaulted to the subagent reviewer and the z.ai backend was dropped ([#58](https://github.com/brandon-fryslie/dotfiles/pull/58)); `CLAUDE.md` deduped and rewritten against universal-laws ([#28](https://github.com/brandon-fryslie/dotfiles/pull/28)). Today: `zshrc` guarded `fnm`/`fzf`/`mcpi` init on existence, the installer routed `dotbot` through `uvx`, and direct master pushes were allowed in the in-repo `CLAUDE.md`.

### [go-template-js](https://github.com/promptctl/go-template-js)
**TypeScript · MIT**

Go template syntax + a Sprig subset, generic over output type, in TypeScript. Recent 90-day window added `int` and `float` ArgTypes with bigint→number normalization gated at the boundary ([#14](https://github.com/promptctl/go-template-js/pull/14), [#15](https://github.com/promptctl/go-template-js/pull/15)); migrated math, lists, strings, regex, random Sprig families onto the typed ArgTypes and dropped body-side coercions ([#16](https://github.com/promptctl/go-template-js/pull/16), [#18](https://github.com/promptctl/go-template-js/pull/18), [#19](https://github.com/promptctl/go-template-js/pull/19)); `EngineConfig.delims` for custom action delimiters ([#13](https://github.com/promptctl/go-template-js/pull/13)); `missingKey` policy (default/zero/error) ([#12](https://github.com/promptctl/go-template-js/pull/12)); `{{break}}` / `{{continue}}` in range loops ([#11](https://github.com/promptctl/go-template-js/pull/11)); html/js/urlquery escaping builtins ([#7](https://github.com/promptctl/go-template-js/pull/7), [#9](https://github.com/promptctl/go-template-js/pull/9), [#10](https://github.com/promptctl/go-template-js/pull/10)); README rewritten in standard npm-library shape ([#21](https://github.com/promptctl/go-template-js/pull/21)).

### [tmux-control-mode-js](https://github.com/promptctl/tmux-control-mode-js)
**TypeScript · MIT**

Node.js client for the tmux control-mode protocol. Recent 90-day window shipped the byte-codec series — a portable byte-faithful codec ([#62](https://github.com/promptctl/tmux-control-mode-js/pull/62)) routed through every transport as the single enforcer ([#63](https://github.com/promptctl/tmux-control-mode-js/pull/63)), backed by a cross-transport faithfulness contract ([#64](https://github.com/promptctl/tmux-control-mode-js/pull/64)) and `CommandResponse.output` contract docs ([#65](https://github.com/promptctl/tmux-control-mode-js/pull/65)); the library API surface spec landed at §26 ([#60](https://github.com/promptctl/tmux-control-mode-js/pull/60)) and was then reduced to a protocol-only guard ([#66](https://github.com/promptctl/tmux-control-mode-js/pull/66)); `attachLineSink` with a shared per-pane decoder added on top ([#67](https://github.com/promptctl/tmux-control-mode-js/pull/67)).

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

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

Spent most of today scraping `low-talker`'s fingerprints out of `vhid`. Ticket ids in tests relabelled as their own history, comments that credited `low-talker` for facts turning out to be `vhid`'s own, a mouse module named `Pointing` that shadowed its own `PointingDevice` protocol until an importer couldn't qualify a `Button`. None of it changes what the daemon does. All of it is work visible only to a reader who cares where a name came from.

`cc-hands` grew a `claude` shim on PATH so every interactive session runs under the `fritter` pty wrapper Brandon merged yesterday. Closing the terminal now ends the session, cleanly, once. The intermediary between the daemon and each session got a real system prompt and a `stay_silent` verb, so an unanswered question stops being said again. Alongside that, `memento 0.9.0` landed with a 350k context ceiling — past it, a session finishes the unit it is in and stops.

Nine repositories took the same one-line commit today: switch to pnpm. Brandon asked for none of it and pushed back on none of it. The tooling substrate agrees with itself in one more place.

<!-- INTRO-PROSE:END -->

<div align="center">
<img src="./assets/neural-pulse-80s.svg" width="800" alt="Neural network with flowing pulses — Business Requirements feeding through hidden layers into Customer Value" />
</div>

<div align="center">
<a href="./STATS.md"><img src="./assets/daily-stats.svg" width="960" alt="Live GitHub Stats — click for every past card" /></a>
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

*Updated September 27, 2026*

### Last 24 Hours

- `promptctl/vhid` — 24 commits: `DeviceQueue.submit` enqueues synchronously and hands back an `Acknowledgement`, device protocols made nonsending, the ordering test goes through the queued keyboard and mouse ([#24](https://github.com/promptctl/vhid/pull/24)); the mouse's protocol is `PointingDevice`, so the module `Pointing` no longer shadows itself and an importer can qualify `Pointing.Button` ([#25](https://github.com/promptctl/vhid/pull/25)); the client-facing busy refusal is pinned as naming the devices, and Holder's docs stop saying "keyboard" ([#26](https://github.com/promptctl/vhid/pull/26)); hotkey, insert and dictation comments speak of `vhid`'s clients and credit `low-talker` only where the fact was its own ([#27](https://github.com/promptctl/vhid/pull/27)); ticket ids from `low-talker`'s tracker are relabelled as its history ([#28](https://github.com/promptctl/vhid/pull/28)); a test holds the pkg's launchd plist to the daemon's service name ([#29](https://github.com/promptctl/vhid/pull/29)); `AGENTS.md` points an agent at the README sections to read before changing code ([#30](https://github.com/promptctl/vhid/pull/30)) ([commits](https://github.com/promptctl/vhid/commits?author=brandon-fryslie&since=2026-09-26)).
- `brandon-fryslie/cc-hands` — 8 commits: `fritter` matured — text goes into a box emptied through Claude Code's stash ([#26](https://github.com/brandon-fryslie/cc-hands/pull/26)), a staged draft is sent by typing it and pressing Return ([#28](https://github.com/brandon-fryslie/cc-hands/pull/28)), a session at the workspace-trust dialog is kept out of the registry ([#29](https://github.com/brandon-fryslie/cc-hands/pull/29)), keyboard commands and interrupts reach a session through `fritter` ([#30](https://github.com/brandon-fryslie/cc-hands/pull/30)), a `claude` shim on PATH runs every interactive session under `fritter` ([#31](https://github.com/brandon-fryslie/cc-hands/pull/31)), closing the terminal ends the session ([#32](https://github.com/brandon-fryslie/cc-hands/pull/32)); the intermediary got a real system prompt, `stay_silent`, and a start-up note ([#33](https://github.com/brandon-fryslie/cc-hands/pull/33)); the anthropic backend reads the keychain when the environment has no key, Sonnet 5 as the default model ([#34](https://github.com/brandon-fryslie/cc-hands/pull/34)) ([commits](https://github.com/brandon-fryslie/cc-hands/commits?author=brandon-fryslie&since=2026-09-26)).
- `promptctl/memento` — 7 commits: `0.9.0` released ([#22](https://github.com/promptctl/memento/pull/22)); context ceiling defaults to 350k, and a session past it finishes the unit it is in ([#19](https://github.com/promptctl/memento/pull/19)); a config the hook rejects records the stop in the log ([#24](https://github.com/promptctl/memento/pull/24)); the ceiling log records stops too, not only decisions ([#25](https://github.com/promptctl/memento/pull/25)); the sessions tree is bounded by sweeping records no session still stops in ([#26](https://github.com/promptctl/memento/pull/26)); a reset-in-place session's shared record is re-derived once the reset lands ([#27](https://github.com/promptctl/memento/pull/27)); `fetch` surfaces the reviewer's out-of-diff findings, not only threads ([#23](https://github.com/promptctl/memento/pull/23)) ([commits](https://github.com/promptctl/memento/commits?author=brandon-fryslie&since=2026-09-26)).
- `promptctl/links-issue-tracker` — 5 commits: `v0.15.0` promoted ([#563](https://github.com/promptctl/links-issue-tracker/pull/563)); a lapsed claim is not a claim ([#561](https://github.com/promptctl/links-issue-tracker/pull/561)); the scale campaign's numbers are regenerated, not pasted ([#559](https://github.com/promptctl/links-issue-tracker/pull/559)); the v1-spec no longer cites source line numbers ([#564](https://github.com/promptctl/links-issue-tracker/pull/564)) and the doc-citation gate was reverted ([#562](https://github.com/promptctl/links-issue-tracker/pull/562)).
- `brandon-fryslie/dotfiles` — 2 commits: cargo dev/test debuginfo defaults to `line-tables-only` to halve `target/` size ([#81](https://github.com/brandon-fryslie/dotfiles/pull/81)); CLAUDE.md — "leave it open" means absent from output, not decided either way ([#82](https://github.com/brandon-fryslie/dotfiles/pull/82)).
- `promptctl/laws` — 1 commit: hosted-session injector and craft switch removed; the gate refuses and names a fresh session ([#76](https://github.com/promptctl/laws/pull/76)).
- `promptctl/cc-candybar` — 1 commit: a `themeSwitcher` segment steps through themes on the bar ([#243](https://github.com/promptctl/cc-candybar/pull/243)).
- Multi-repo sweep — package manager switched to pnpm across nine repos: [`promptctl/promptctl`](https://github.com/promptctl/promptctl/commit/3d7eb48), [`brandon-fryslie/tinkerpad`](https://github.com/brandon-fryslie/tinkerpad/commit/ae4f600), [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste/commit/675dc8f), [`brandon-fryslie/rich-js-ink`](https://github.com/brandon-fryslie/rich-js-ink/commit/9cd7332), [`brandon-fryslie/gh-pages-showcase`](https://github.com/brandon-fryslie/gh-pages-showcase/commit/b0e3336), [`brandon-fryslie/gh-pages-multiplexer`](https://github.com/brandon-fryslie/gh-pages-multiplexer/commit/897c077), [`brandon-fryslie/cherry-chrome-mcp`](https://github.com/brandon-fryslie/cherry-chrome-mcp/commit/2c95b34), [`brandon-fryslie/prompt-eval`](https://github.com/brandon-fryslie/prompt-eval/commit/f5622fc), and [`brandon-fryslie/cathode`](https://github.com/brandon-fryslie/cathode/commit/b5c4bcd).
- `brandon-fryslie/dotfiles` — 3 commits: write-evidence law added to the tracked Claude `CLAUDE.md` ([#78](https://github.com/brandon-fryslie/dotfiles/pull/78)); `something-just-came-up` drops `--reset` from step 4 for memento 0.8.0 ([#79](https://github.com/brandon-fryslie/dotfiles/pull/79)); `delegate-some-shit` — a fresh reviewer runs the review cycle and stops before merge, the supervisor checks the goals itself, twice ([#80](https://github.com/brandon-fryslie/dotfiles/pull/80)).
- `promptctl/laws` — 1 commit: design-docs record where the in-session craft switch is preserved ([#75](https://github.com/promptctl/laws/pull/75)).
- `brandon-fryslie/low-talker` — 1 commit: the app reads its grants in a fresh process, so a grant made mid-session clears its step ([#103](https://github.com/brandon-fryslie/low-talker/pull/103)).

### This Week

- `promptctl/vhid` — 131 commits: full extraction from `low-talker` and the whole surface built on top. Eyes, naming, identity, input, signing, and CLI ([#1](https://github.com/promptctl/vhid/pull/1)–[#6](https://github.com/promptctl/vhid/pull/6)); `vhid mcp` serves the seven verbs over stdio with core tests over the fake mouse ([#7](https://github.com/promptctl/vhid/pull/7), [#8](https://github.com/promptctl/vhid/pull/8)); CI on macos-26 under Xcode 26.6 with master-commit concurrency groups ([#9](https://github.com/promptctl/vhid/pull/9)); a `vhid driver` verb reads the pqrs installation without root ([#10](https://github.com/promptctl/vhid/pull/10)); one signed distribution pkg installs the daemon's launchd job and the pinned driver package ([#11](https://github.com/promptctl/vhid/pull/11)); the doctor arc — setup requirements as a verdict table, `launchctl print` parsed against captures, `vhid doctor` and its MCP tool answering one list under a one-word verdict ([#12](https://github.com/promptctl/vhid/pull/12)–[#17](https://github.com/promptctl/vhid/pull/17)); a Command-holding chord reads its key off the layout's Command layer ([#19](https://github.com/promptctl/vhid/pull/19)); `vhid paste` shipped ([#18](https://github.com/promptctl/vhid/pull/18), [#20](https://github.com/promptctl/vhid/pull/20)) and was deleted alongside a scope guideline ([#21](https://github.com/promptctl/vhid/pull/21), [#22](https://github.com/promptctl/vhid/pull/22)); XPC tests rewritten to ask a Mach name nobody holds ([#23](https://github.com/promptctl/vhid/pull/23)); `DeviceQueue.submit` enqueues synchronously with an `Acknowledgement`, and device protocols are nonsending ([#24](https://github.com/promptctl/vhid/pull/24)); the mouse's protocol is `PointingDevice` so the `Pointing` module no longer shadows itself ([#25](https://github.com/promptctl/vhid/pull/25)); a residue-cleanup arc renamed busy refusals and Holder docs to name the devices ([#26](https://github.com/promptctl/vhid/pull/26)–[#28](https://github.com/promptctl/vhid/pull/28)); the pkg's launchd plist is pinned to the daemon's service name ([#29](https://github.com/promptctl/vhid/pull/29)); `AGENTS.md` points an agent at what to read before changing code ([#30](https://github.com/promptctl/vhid/pull/30)) ([commits](https://github.com/promptctl/vhid/commits?author=brandon-fryslie&since=2026-09-20)).
- `brandon-fryslie/cc-hands` — 79 commits: a new repo — Voice for Claude Code. Liveness, hooks, and audio first ([#1](https://github.com/brandon-fryslie/cc-hands/pull/1)–[#5](https://github.com/brandon-fryslie/cc-hands/pull/5)); attention, questions, plans, and the whole sessions surface ([#6](https://github.com/brandon-fryslie/cc-hands/pull/6)–[#19](https://github.com/brandon-fryslie/cc-hands/pull/19)); install hooks moved to a Claude Code plugin ([#20](https://github.com/brandon-fryslie/cc-hands/pull/20)), OpenAI wired as a backend ([#21](https://github.com/brandon-fryslie/cc-hands/pull/21)), launchd removed in favour of `hands run` in a terminal ([#22](https://github.com/brandon-fryslie/cc-hands/pull/22)), a `fritter` pty wrapper added under it ([#23](https://github.com/brandon-fryslie/cc-hands/pull/23)), questions found by the daemon always said ([#24](https://github.com/brandon-fryslie/cc-hands/pull/24)); a fritter arc — text into a box emptied through Claude Code's stash, drafts typed and sent, keyboard commands and interrupts through fritter, a `claude` shim on PATH, terminal-close ending the session ([#26](https://github.com/brandon-fryslie/cc-hands/pull/26), [#28](https://github.com/brandon-fryslie/cc-hands/pull/28)–[#32](https://github.com/brandon-fryslie/cc-hands/pull/32)); intermediary real system prompt with `stay_silent` ([#33](https://github.com/brandon-fryslie/cc-hands/pull/33)); anthropic backend reads the keychain when the environment has no key ([#34](https://github.com/brandon-fryslie/cc-hands/pull/34)) ([commits](https://github.com/brandon-fryslie/cc-hands/commits?author=brandon-fryslie&since=2026-09-20)).
- `brandon-fryslie/low-talker` — 22 commits: input-method Flavor/Delivery naming settled and the bundle passes every key through its server ([#82](https://github.com/brandon-fryslie/low-talker/pull/82)–[#84](https://github.com/brandon-fryslie/low-talker/pull/84)); the executor asks the input method and a refusal copies the words instead ([#86](https://github.com/brandon-fryslie/low-talker/pull/86)); the input method replaces the clipboard delivery ([#88](https://github.com/brandon-fryslie/low-talker/pull/88)); installed as a copy so sandboxed apps can reach it ([#92](https://github.com/brandon-fryslie/low-talker/pull/92)); takes words only from its own installation's app ([#93](https://github.com/brandon-fryslie/low-talker/pull/93)); a hung app no longer holds the keyboard ([#94](https://github.com/brandon-fryslie/low-talker/pull/94)); every shipped bundle carries the version project.yml sets ([#95](https://github.com/brandon-fryslie/low-talker/pull/95)); the app carries the lowtalker CLI signed as the app is, and the driver installs and removes through it ([#97](https://github.com/brandon-fryslie/low-talker/pull/97), [#98](https://github.com/brandon-fryslie/low-talker/pull/98)); LowTalker launches with no permission prompt and asks for each grant in its own explained step ([#99](https://github.com/brandon-fryslie/low-talker/pull/99)–[#102](https://github.com/brandon-fryslie/low-talker/pull/102)); the app reads its grants in a fresh process so a mid-session grant clears its step ([#103](https://github.com/brandon-fryslie/low-talker/pull/103)) ([commits](https://github.com/brandon-fryslie/low-talker/commits?author=brandon-fryslie&since=2026-09-20)).
- `brandon-fryslie/dotfiles` — 18 commits: voiced-explainer skill added and its render scripts hardened ([ecc07b4](https://github.com/brandon-fryslie/dotfiles/commit/ecc07b4), [c991c0c](https://github.com/brandon-fryslie/dotfiles/commit/c991c0c)); DashVox panes get a $-prefixed prompt keyed off an explicit marker ([cbc6243](https://github.com/brandon-fryslie/dotfiles/commit/cbc6243), [cee548f](https://github.com/brandon-fryslie/dotfiles/commit/cee548f)); loopback SSH sessions get a silent shell ([f1dd7ae](https://github.com/brandon-fryslie/dotfiles/commit/f1dd7ae)); `something-just-came-up` ([#75](https://github.com/brandon-fryslie/dotfiles/pull/75), [#79](https://github.com/brandon-fryslie/dotfiles/pull/79)), `delegate-some-shit` ([#77](https://github.com/brandon-fryslie/dotfiles/pull/77), [#80](https://github.com/brandon-fryslie/dotfiles/pull/80)), and restored no-cover / session-URL hooks / patch-claude-code skills ([#76](https://github.com/brandon-fryslie/dotfiles/pull/76)); write-evidence law added to the tracked Claude `CLAUDE.md` ([#78](https://github.com/brandon-fryslie/dotfiles/pull/78)); cargo dev/test debuginfo defaults to `line-tables-only` ([#81](https://github.com/brandon-fryslie/dotfiles/pull/81)); CLAUDE.md `"leave it open" means absent from output` ([#82](https://github.com/brandon-fryslie/dotfiles/pull/82)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-09-20)).
- `promptctl/cc-candybar` — 15 commits: Settings door with 🍫 configurable glyph and quick actions folded into the menu ([#230](https://github.com/promptctl/cc-candybar/pull/230)); every open disclosure body row leads with an ✕ that closes it ([#229](https://github.com/promptctl/cc-candybar/pull/229)); settings menu visible under every condition, opens inline with ❌ ([#231](https://github.com/promptctl/cc-candybar/pull/231)); `do` fires several actions in one click ([#233](https://github.com/promptctl/cc-candybar/pull/233)); links carry a URL-derived OSC-8 id on rich-js 0.11 ([#232](https://github.com/promptctl/cc-candybar/pull/232)); a pick leaves its picker open ([#234](https://github.com/promptctl/cc-candybar/pull/234)); legible text on every theme with a gallery ([#235](https://github.com/promptctl/cc-candybar/pull/235)); every theme's bar carries its own accents ([#236](https://github.com/promptctl/cc-candybar/pull/236)); decoration follows Textual's colour roles ([#237](https://github.com/promptctl/cc-candybar/pull/237)); text floors hold at 256 ([#238](https://github.com/promptctl/cc-candybar/pull/238)); theme and preset carousels ([#239](https://github.com/promptctl/cc-candybar/pull/239), [#240](https://github.com/promptctl/cc-candybar/pull/240)); state/band/seam floors hold at 256 and ansi ([#241](https://github.com/promptctl/cc-candybar/pull/241)); charset and colour depth move into the settings menu ([#242](https://github.com/promptctl/cc-candybar/pull/242)); themeSwitcher segment steps through themes on the bar ([#243](https://github.com/promptctl/cc-candybar/pull/243)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-09-20)).
- `promptctl/laws` — 9 commits: a spec skill added — PRD, FSD, and Technical Spec tied by a traceability matrix ([#67](https://github.com/promptctl/laws/pull/67)); horizon arc — the run bundle captured identically-structured and reviewable ([#69](https://github.com/promptctl/laws/pull/69)), the instrument booted before it is called verified with the trust gate keyed on the path the CLI reads ([#70](https://github.com/promptctl/laws/pull/70)), model and Claude Code version pinned ([#71](https://github.com/promptctl/laws/pull/71)), a run whose reviewer cannot authenticate is refused ([279959c](https://github.com/promptctl/laws/commit/279959c)); [LAW:escape-local-minima] added ([#68](https://github.com/promptctl/laws/pull/68)); `0.29.0` — plan the whole arc at the detail you have ([#74](https://github.com/promptctl/laws/pull/74)); design-docs record where the in-session craft switch is preserved ([#75](https://github.com/promptctl/laws/pull/75)); hosted-session injector and craft switch removed, the gate refuses and names a fresh session ([#76](https://github.com/promptctl/laws/pull/76)) ([commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-09-20)).
- `promptctl/memento` — 8 commits: message-in-a-bottle `0.8.0` — a handoff hands off, `--reset` dropped ([#21](https://github.com/promptctl/memento/pull/21)); `0.9.0` released ([#22](https://github.com/promptctl/memento/pull/22)); context ceiling defaults to 350k, and a session past it finishes the unit it is in ([#19](https://github.com/promptctl/memento/pull/19)); a config the hook rejects records the stop in the log ([#24](https://github.com/promptctl/memento/pull/24)); the ceiling log records stops too ([#25](https://github.com/promptctl/memento/pull/25)); sessions tree bounded by sweeping records no session still stops in ([#26](https://github.com/promptctl/memento/pull/26)); a reset-in-place session's shared record is re-derived once the reset lands ([#27](https://github.com/promptctl/memento/pull/27)); `fetch` surfaces the reviewer's out-of-diff findings ([#23](https://github.com/promptctl/memento/pull/23)) ([commits](https://github.com/promptctl/memento/commits?author=brandon-fryslie&since=2026-09-20)).
- `promptctl/links-issue-tracker` — 8 commits: the query surface stops handing the planner quadratic problems ([16868ed](https://github.com/promptctl/links-issue-tracker/commit/16868ed)); a filter no longer deletes the unblocks line from rows it keeps ([06060ff](https://github.com/promptctl/links-issue-tracker/commit/06060ff)); chrome-devtools MCP config added ([#560](https://github.com/promptctl/links-issue-tracker/pull/560)); the scale campaign's numbers are regenerated, not pasted ([#559](https://github.com/promptctl/links-issue-tracker/pull/559)); a lapsed claim is not a claim ([#561](https://github.com/promptctl/links-issue-tracker/pull/561)); the doc-citation gate reverted ([#562](https://github.com/promptctl/links-issue-tracker/pull/562)); `v0.15.0` promoted ([#563](https://github.com/promptctl/links-issue-tracker/pull/563)); the v1-spec no longer cites source line numbers ([#564](https://github.com/promptctl/links-issue-tracker/pull/564)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-09-20)).
- `brandon-fryslie/rich-js` — 6 commits: OSC-8 links carry a URL-derived id so a split link hovers as one ([#152](https://github.com/brandon-fryslie/rich-js/pull/152)); OKLCH per-axis mix and ΔE, powerline seams stay visible between near-equal backgrounds ([#153](https://github.com/brandon-fryslie/rich-js/pull/153)); `0.12.0` released ([#154](https://github.com/brandon-fryslie/rich-js/pull/154)); text floors hold at 256 colours ([#155](https://github.com/brandon-fryslie/rich-js/pull/155)); contrast chosen against a translucent background as drawn ([#156](https://github.com/brandon-fryslie/rich-js/pull/156)); floors hold on the colours drawn — the strip's seam, ansi text, and ensureDrawn ([#157](https://github.com/brandon-fryslie/rich-js/pull/157)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-09-20)).
- `brandon-fryslie/slopspot-paste` — 2 commits: Claude Code transcripts attribute each message to whoever wrote it ([#173](https://github.com/brandon-fryslie/slopspot-paste/pull/173)); package manager switched to pnpm ([675dc8f](https://github.com/brandon-fryslie/slopspot-paste/commit/675dc8f)).
- `brandon-fryslie/room-eq-wizard-mcp` — 2 commits: five wire-contract bugs found in live use fixed ([#15](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/15)); live import tests stop assuming REW shares the runner's filesystem ([#16](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/16)).

### This Month

1,000+ commits across 35 repositories over the past 30 days. Top by volume:

- [`brandon-fryslie/cc-hands`](https://github.com/brandon-fryslie/cc-hands) — 138 commits
- [`promptctl/vhid`](https://github.com/promptctl/vhid) — 131
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 109
- [`brandon-fryslie/low-talker`](https://github.com/brandon-fryslie/low-talker) — 102
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 83
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 63
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 53
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 48
- [`promptctl/crom`](https://github.com/promptctl/crom) — 43
- [`promptctl/elvenspeak`](https://github.com/promptctl/elvenspeak) — 37
- [`promptctl/laws`](https://github.com/promptctl/laws) — 37

Languages: Swift, Python, TypeScript, Go, Shell, JavaScript, Rust.

---

<details>
<summary>Previous highlights</summary>

- [2026-09-26](./daily-archive/2026-09-26.md)
- [2026-09-25](./daily-archive/2026-09-25.md)
- [2026-09-24](./daily-archive/2026-09-24.md)
- [2026-09-23](./daily-archive/2026-09-23.md)
- [2026-09-22](./daily-archive/2026-09-22.md)
- [2026-09-18](./daily-archive/2026-09-18.md)
- [2026-09-17](./daily-archive/2026-09-17.md)

</details>

<!-- RECENT-ACTIVITY:END -->

<!-- PREVIOUS-WORK:START -->

### Previous Engineering Work

- **[Week of August 17](./previous-work/2026/2026-08-17.md)** — *in progress*
- **[Week of August 10](./previous-work/2026/2026-08-10.md)** — slopspot RAG stack and freshness trail · cc-candybar per-segment palette overrides · lit sync safety and licensing clean-room · cc-dump Anthropic-only proxy consolidation
- **[Week of August 3](./previous-work/2026/2026-08-03.md)** — lit workflows 0.4.0 · cc-candybar option-domain seam and theme picker · slopspot-paste editor made editable end-to-end · room-eq-wizard-mcp surface completion
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

### [cc-hands](https://github.com/brandon-fryslie/cc-hands)
**Python**

Voice for Claude Code — speak to your sessions and hear what they did. 138 commits over the past 30 days, all in the last week — a brand-new repo. Liveness, hooks, and audio landed first ([#1](https://github.com/brandon-fryslie/cc-hands/pull/1)–[#5](https://github.com/brandon-fryslie/cc-hands/pull/5)); then attention, questions, plans, and the whole sessions surface ([#6](https://github.com/brandon-fryslie/cc-hands/pull/6)–[#19](https://github.com/brandon-fryslie/cc-hands/pull/19)); install hooks moved to a Claude Code plugin ([#20](https://github.com/brandon-fryslie/cc-hands/pull/20)), OpenAI wired as a backend ([#21](https://github.com/brandon-fryslie/cc-hands/pull/21)), launchd removed in favour of `hands run` in a terminal ([#22](https://github.com/brandon-fryslie/cc-hands/pull/22)), a `fritter` pty wrapper landed under it ([#23](https://github.com/brandon-fryslie/cc-hands/pull/23)); text now moves into a Claude Code stash box ([#26](https://github.com/brandon-fryslie/cc-hands/pull/26)), drafts are typed and sent ([#28](https://github.com/brandon-fryslie/cc-hands/pull/28)), keyboard commands and interrupts reach a session through `fritter` ([#30](https://github.com/brandon-fryslie/cc-hands/pull/30)), a `claude` shim on PATH runs every interactive session under `fritter` ([#31](https://github.com/brandon-fryslie/cc-hands/pull/31)), closing the terminal ends the session ([#32](https://github.com/brandon-fryslie/cc-hands/pull/32)); the intermediary got a real system prompt with `stay_silent` ([#33](https://github.com/brandon-fryslie/cc-hands/pull/33)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 2★**

Agent-native issue tracker. 109 commits over the past 30 days. Recent work: the query surface stops handing the planner quadratic problems ([16868ed](https://github.com/promptctl/links-issue-tracker/commit/16868ed)); a filter no longer deletes the unblocks line from rows it keeps ([06060ff](https://github.com/promptctl/links-issue-tracker/commit/06060ff)); chrome-devtools MCP config added ([#560](https://github.com/promptctl/links-issue-tracker/pull/560)); the scale campaign's numbers are regenerated, not pasted ([#559](https://github.com/promptctl/links-issue-tracker/pull/559)); a lapsed claim is not a claim ([#561](https://github.com/promptctl/links-issue-tracker/pull/561)); the doc-citation gate reverted ([#562](https://github.com/promptctl/links-issue-tracker/pull/562)); `v0.15.0` promoted ([#563](https://github.com/promptctl/links-issue-tracker/pull/563)); the v1-spec no longer cites source line numbers ([#564](https://github.com/promptctl/links-issue-tracker/pull/564)).

### [rich-js](https://github.com/brandon-fryslie/rich-js)
**TypeScript · MIT**

Terminal rendering library — colours, styles, powerline segments and OSC-8 links for Node. 83 commits over the past 30 days. This past week: OSC-8 links carry a URL-derived id so a split link hovers as one ([#152](https://github.com/brandon-fryslie/rich-js/pull/152)); OKLCH per-axis mix and ΔE so powerline seams stay visible between near-equal backgrounds ([#153](https://github.com/brandon-fryslie/rich-js/pull/153)); `0.12.0` released ([#154](https://github.com/brandon-fryslie/rich-js/pull/154)); text floors hold at 256 colours ([#155](https://github.com/brandon-fryslie/rich-js/pull/155)); contrast chosen against a translucent background as drawn ([#156](https://github.com/brandon-fryslie/rich-js/pull/156)); floors hold on the colours drawn — the strip's seam, ansi text, and ensureDrawn ([#157](https://github.com/brandon-fryslie/rich-js/pull/157)).

</td>
<td width="50%" valign="top">

### [vhid](https://github.com/promptctl/vhid)
**Swift**

A virtual keyboard and a virtual mouse for macOS, driven from a CLI or over MCP. Real HID devices through the pqrs DriverKit extension — no event taps, no Accessibility grant. 131 commits over the past 30 days — the whole project. Extracted from `low-talker` and grown through six merges landing eyes, naming, identity, input, signing and CLI ([#1](https://github.com/promptctl/vhid/pull/1)–[#6](https://github.com/promptctl/vhid/pull/6)); `vhid mcp` serves the seven verbs over stdio ([#7](https://github.com/promptctl/vhid/pull/7), [#8](https://github.com/promptctl/vhid/pull/8)); CI on macos-26 under Xcode 26.6 ([#9](https://github.com/promptctl/vhid/pull/9)); a `vhid driver` verb reads the pqrs installation without root ([#10](https://github.com/promptctl/vhid/pull/10)); one signed distribution pkg installs the daemon's launchd job and the pinned driver package ([#11](https://github.com/promptctl/vhid/pull/11)); the doctor arc — setup requirements as a verdict table, `launchctl print` parsed against captures, `vhid doctor` and its MCP tool answering one list under a one-word verdict ([#12](https://github.com/promptctl/vhid/pull/12)–[#17](https://github.com/promptctl/vhid/pull/17)); `vhid paste` shipped and was then deleted alongside a scope guideline ([#18](https://github.com/promptctl/vhid/pull/18), [#20](https://github.com/promptctl/vhid/pull/20)–[#22](https://github.com/promptctl/vhid/pull/22)); `DeviceQueue.submit` enqueues synchronously with an `Acknowledgement` ([#24](https://github.com/promptctl/vhid/pull/24)); the mouse's protocol is `PointingDevice` so the `Pointing` module no longer shadows itself ([#25](https://github.com/promptctl/vhid/pull/25)); a residue-cleanup arc renamed busy refusals and Holder docs to name the devices ([#26](https://github.com/promptctl/vhid/pull/26)–[#28](https://github.com/promptctl/vhid/pull/28)); the pkg's launchd plist pinned to the daemon's service name ([#29](https://github.com/promptctl/vhid/pull/29)); `AGENTS.md` added ([#30](https://github.com/promptctl/vhid/pull/30)).

### [low-talker](https://github.com/brandon-fryslie/low-talker)
**Swift**

Local push-to-talk dictation for macOS with a chord-selected command layer. 102 commits over the past 30 days. Recent work: input-method Flavor/Delivery naming settled and the bundle passes every key through its server ([#82](https://github.com/brandon-fryslie/low-talker/pull/82)–[#84](https://github.com/brandon-fryslie/low-talker/pull/84)); the executor asks the input method and a refusal copies the words instead ([#86](https://github.com/brandon-fryslie/low-talker/pull/86)); the input method replaces the clipboard delivery ([#88](https://github.com/brandon-fryslie/low-talker/pull/88)); installed as a copy so sandboxed apps can reach it ([#92](https://github.com/brandon-fryslie/low-talker/pull/92)); the app carries the lowtalker CLI signed as the app is ([#97](https://github.com/brandon-fryslie/low-talker/pull/97), [#98](https://github.com/brandon-fryslie/low-talker/pull/98)); LowTalker launches with no permission prompt and asks for each grant in its own explained step ([#99](https://github.com/brandon-fryslie/low-talker/pull/99)–[#103](https://github.com/brandon-fryslie/low-talker/pull/103)).

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 4★**

Environment and tooling substrate — dotbot-driven config, per-machine trust, and the Claude Code / lit / candybar wiring across Brandon's fleet. 63 commits over the past 30 days. Recent work: voiced-explainer skill added with hardened render scripts ([ecc07b4](https://github.com/brandon-fryslie/dotfiles/commit/ecc07b4), [c991c0c](https://github.com/brandon-fryslie/dotfiles/commit/c991c0c)); DashVox panes get a $-prefixed prompt keyed off an explicit marker ([cbc6243](https://github.com/brandon-fryslie/dotfiles/commit/cbc6243), [cee548f](https://github.com/brandon-fryslie/dotfiles/commit/cee548f)); loopback SSH sessions get a silent shell ([f1dd7ae](https://github.com/brandon-fryslie/dotfiles/commit/f1dd7ae)); `something-just-came-up` ([#75](https://github.com/brandon-fryslie/dotfiles/pull/75), [#79](https://github.com/brandon-fryslie/dotfiles/pull/79)) and `delegate-some-shit` skills added ([#77](https://github.com/brandon-fryslie/dotfiles/pull/77), [#80](https://github.com/brandon-fryslie/dotfiles/pull/80)); write-evidence law added to the tracked Claude `CLAUDE.md` ([#78](https://github.com/brandon-fryslie/dotfiles/pull/78)); cargo dev/test debuginfo defaults to `line-tables-only` to halve `target/` size ([#81](https://github.com/brandon-fryslie/dotfiles/pull/81)); CLAUDE.md — "leave it open" means absent from output ([#82](https://github.com/brandon-fryslie/dotfiles/pull/82)).

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

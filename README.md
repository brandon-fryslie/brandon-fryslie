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

The paste verb in `vhid` is gone. Yesterday it was the day's landing — a clipboard write, a layout-aware Command-V, an MCP tool, tests, help copy. Today the verb, the tool, the core, the tests, and every mention in the README were removed. What replaced them was a paragraph naming what `vhid` is for: input through the virtual keyboard and mouse, and anything reaching around them only when near-required and not a project of its own. Paste reached around them. So paste was not a project of its own here.

`cc-hands` did the same thing on a smaller scale. Launchd is out; the daemon runs only when a terminal runs `hands run` beside its indicator. A pty wrapper landed under it so a session's write surface survives with the screen off. Deletions and one addition, and the addition is the one that pays for both.

Brandon didn't argue the scope note. He shipped it.

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

*Updated September 26, 2026*

### Last 24 Hours

- `promptctl/vhid` — 9 commits: `vhid paste` and its MCP tool were deleted — the verb, the core, the clipboard write, the tests, and every mention in help and the README ([#22](https://github.com/promptctl/vhid/pull/22)); a scope guideline landed alongside it, stating what belongs in `vhid` — input through the devices, and anything reaching around them only when near-required and not a project of its own ([#21](https://github.com/promptctl/vhid/pull/21)); the gone-service and unreachable-service XPC tests were rewritten to ask a Mach name nobody holds and accept either code XPC can report for it ([#23](https://github.com/promptctl/vhid/pull/23)) ([commits](https://github.com/promptctl/vhid/commits?author=brandon-fryslie&since=2026-09-25)).
- `brandon-fryslie/cc-hands` — 5 commits: install hooks come from a Claude Code plugin, and a `hands` that is off costs a session nothing ([#20](https://github.com/brandon-fryslie/cc-hands/pull/20)); `HANDS_LLM=openai` reaches OpenAI's API with the key the backend carries from a `.env` ([#21](https://github.com/brandon-fryslie/cc-hands/pull/21)); the daemon runs only as `hands run` in a terminal beside its indicator, and launchd is deleted ([#22](https://github.com/brandon-fryslie/cc-hands/pull/22)); a `fritter` pty wrapper gives every session a write surface that works with the screen off ([#23](https://github.com/brandon-fryslie/cc-hands/pull/23)); what Claude asked is found by the daemon and always said, once, at every length ([#24](https://github.com/brandon-fryslie/cc-hands/pull/24)).
- `brandon-fryslie/dotfiles` — 3 commits: write-evidence law added to the tracked Claude `CLAUDE.md` ([#78](https://github.com/brandon-fryslie/dotfiles/pull/78)); `something-just-came-up` drops `--reset` from step 4 for memento 0.8.0 ([#79](https://github.com/brandon-fryslie/dotfiles/pull/79)); `delegate-some-shit` — a fresh reviewer runs the review cycle and stops before merge, the supervisor checks the goals itself, twice ([#80](https://github.com/brandon-fryslie/dotfiles/pull/80)).
- `promptctl/laws` — 1 commit: design-docs record where the in-session craft switch is preserved ([#75](https://github.com/promptctl/laws/pull/75)).
- `brandon-fryslie/low-talker` — 1 commit: the app reads its grants in a fresh process, so a grant made mid-session clears its step ([#103](https://github.com/brandon-fryslie/low-talker/pull/103)).

### This Week

- `promptctl/vhid` — 107 commits: full extraction from `low-talker` and the whole surface built on top. Eyes, naming, identity, input, signing, and CLI ([#1](https://github.com/promptctl/vhid/pull/1)–[#6](https://github.com/promptctl/vhid/pull/6)); `vhid mcp` serves the seven verbs over stdio with core tests for move/scroll/drag/cursor over the fake mouse ([#7](https://github.com/promptctl/vhid/pull/7), [#8](https://github.com/promptctl/vhid/pull/8)); CI on macos-26 under Xcode 26.6 with master-commit concurrency groups ([#9](https://github.com/promptctl/vhid/pull/9)); a `vhid driver` verb reads the pqrs installation without root ([#10](https://github.com/promptctl/vhid/pull/10)); one signed distribution pkg installs the daemon's launchd job and the pinned driver package ([#11](https://github.com/promptctl/vhid/pull/11)); the doctor arc — setup requirements as a verdict table, `launchctl print` parsed against captures, the keyboard type cache read in one place, `vhid doctor` and its MCP tool answering one list under a one-word verdict ([#12](https://github.com/promptctl/vhid/pull/12)–[#17](https://github.com/promptctl/vhid/pull/17)); a Command-holding chord reads its key off the layout's Command layer ([#19](https://github.com/promptctl/vhid/pull/19)); `vhid paste` shipped ([#18](https://github.com/promptctl/vhid/pull/18), [#20](https://github.com/promptctl/vhid/pull/20)) and was then deleted alongside a scope guideline that ruled it out of the project ([#21](https://github.com/promptctl/vhid/pull/21), [#22](https://github.com/promptctl/vhid/pull/22)); the XPC tests were rewritten to ask a Mach name nobody holds ([#23](https://github.com/promptctl/vhid/pull/23)) ([commits](https://github.com/promptctl/vhid/commits?author=brandon-fryslie&since=2026-09-19)).
- `brandon-fryslie/cc-hands` — 71 commits: a new repo — Voice for Claude Code. Liveness, hooks, and audio first ([#1](https://github.com/brandon-fryslie/cc-hands/pull/1)–[#5](https://github.com/brandon-fryslie/cc-hands/pull/5)); attention, questions, plans, and the whole sessions surface — mode readback, interrupted turns, prompt submission, typed status, running-turn ends ([#6](https://github.com/brandon-fryslie/cc-hands/pull/6)–[#19](https://github.com/brandon-fryslie/cc-hands/pull/19)); install hooks moved to a Claude Code plugin ([#20](https://github.com/brandon-fryslie/cc-hands/pull/20)), OpenAI wired as a backend ([#21](https://github.com/brandon-fryslie/cc-hands/pull/21)), launchd removed in favour of `hands run` in a terminal ([#22](https://github.com/brandon-fryslie/cc-hands/pull/22)), a `fritter` pty wrapper added under it ([#23](https://github.com/brandon-fryslie/cc-hands/pull/23)), and questions found by the daemon are always said ([#24](https://github.com/brandon-fryslie/cc-hands/pull/24)); a long narration arc under the surface — spoken-form escalation, session transcripts followed as they are written, turns built from records ([commits](https://github.com/brandon-fryslie/cc-hands/commits?author=brandon-fryslie&since=2026-09-19)).
- `brandon-fryslie/low-talker` — 22 commits: input-method Flavor/Delivery naming settled and the bundle passes every key through its server ([#82](https://github.com/brandon-fryslie/low-talker/pull/82)–[#84](https://github.com/brandon-fryslie/low-talker/pull/84)); the executor asks the input method and a refusal copies the words instead ([#86](https://github.com/brandon-fryslie/low-talker/pull/86)); the input method replaces the clipboard delivery ([#88](https://github.com/brandon-fryslie/low-talker/pull/88)); installed as a copy so sandboxed apps can reach it ([#92](https://github.com/brandon-fryslie/low-talker/pull/92)); takes words only from its own installation's app ([#93](https://github.com/brandon-fryslie/low-talker/pull/93)); a hung app no longer holds the keyboard ([#94](https://github.com/brandon-fryslie/low-talker/pull/94)); every shipped bundle carries the version project.yml sets ([#95](https://github.com/brandon-fryslie/low-talker/pull/95)); the app carries the lowtalker CLI signed as the app is, and the driver installs and removes through it ([#97](https://github.com/brandon-fryslie/low-talker/pull/97), [#98](https://github.com/brandon-fryslie/low-talker/pull/98)); LowTalker launches with no permission prompt and asks for each grant in its own explained step ([#99](https://github.com/brandon-fryslie/low-talker/pull/99)–[#102](https://github.com/brandon-fryslie/low-talker/pull/102)); the app reads its grants in a fresh process so a mid-session grant clears its step ([#103](https://github.com/brandon-fryslie/low-talker/pull/103)) ([commits](https://github.com/brandon-fryslie/low-talker/commits?author=brandon-fryslie&since=2026-09-19)).
- `brandon-fryslie/dotfiles` — 16 commits: voiced-explainer skill added and its render scripts hardened ([ecc07b4](https://github.com/brandon-fryslie/dotfiles/commit/ecc07b4), [c991c0c](https://github.com/brandon-fryslie/dotfiles/commit/c991c0c)); DashVox panes get a $-prefixed prompt keyed off an explicit marker ([cbc6243](https://github.com/brandon-fryslie/dotfiles/commit/cbc6243), [cee548f](https://github.com/brandon-fryslie/dotfiles/commit/cee548f)); loopback SSH sessions get a silent shell ([f1dd7ae](https://github.com/brandon-fryslie/dotfiles/commit/f1dd7ae)); `something-just-came-up` ([#75](https://github.com/brandon-fryslie/dotfiles/pull/75), [#79](https://github.com/brandon-fryslie/dotfiles/pull/79)), `delegate-some-shit` ([#77](https://github.com/brandon-fryslie/dotfiles/pull/77), [#80](https://github.com/brandon-fryslie/dotfiles/pull/80)), and restored no-cover / session-URL hooks / patch-claude-code skills ([#76](https://github.com/brandon-fryslie/dotfiles/pull/76)); write-evidence law added to the tracked Claude `CLAUDE.md` ([#78](https://github.com/brandon-fryslie/dotfiles/pull/78)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-09-19)).
- `promptctl/cc-candybar` — 14 commits: Settings door with 🍫 configurable glyph, address-tinted door, and quick actions folded into the menu ([#230](https://github.com/promptctl/cc-candybar/pull/230)); every open disclosure body row leads with an ✕ that closes it ([#229](https://github.com/promptctl/cc-candybar/pull/229)); settings menu visible under every condition, opens inline with ❌ ([#231](https://github.com/promptctl/cc-candybar/pull/231)); `do` fires several actions in one click ([#233](https://github.com/promptctl/cc-candybar/pull/233)); links carry a URL-derived OSC-8 id on rich-js 0.11 ([#232](https://github.com/promptctl/cc-candybar/pull/232)); a pick leaves its picker open ([#234](https://github.com/promptctl/cc-candybar/pull/234)); legible text on every theme with a gallery ([#235](https://github.com/promptctl/cc-candybar/pull/235)); every theme's bar carries its own accents ([#236](https://github.com/promptctl/cc-candybar/pull/236)); decoration follows Textual's colour roles ([#237](https://github.com/promptctl/cc-candybar/pull/237)); text floors hold at 256 ([#238](https://github.com/promptctl/cc-candybar/pull/238)); theme and preset carousels ([#239](https://github.com/promptctl/cc-candybar/pull/239), [#240](https://github.com/promptctl/cc-candybar/pull/240)); state/band/seam floors hold at 256 and ansi ([#241](https://github.com/promptctl/cc-candybar/pull/241)); charset and colour depth moved into the settings menu ([#242](https://github.com/promptctl/cc-candybar/pull/242)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-09-19)).
- `promptctl/laws` — 8 commits: a spec skill added — PRD, FSD, and Technical Spec tied by a traceability matrix ([#67](https://github.com/promptctl/laws/pull/67)); horizon arc — the run bundle captured identically-structured and reviewable ([#69](https://github.com/promptctl/laws/pull/69)), the instrument booted before it is called verified with the trust gate keyed on the path the CLI reads ([#70](https://github.com/promptctl/laws/pull/70)), model and Claude Code version pinned so a campaign cannot straddle two harnesses ([#71](https://github.com/promptctl/laws/pull/71)), a run whose reviewer cannot authenticate is refused ([279959c](https://github.com/promptctl/laws/commit/279959c)); [LAW:escape-local-minima] added ([#68](https://github.com/promptctl/laws/pull/68)); `0.29.0` — plan the whole arc at the detail you have ([#74](https://github.com/promptctl/laws/pull/74)); design-docs record where the in-session craft switch is preserved ([#75](https://github.com/promptctl/laws/pull/75)) ([commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-09-19)).
- `brandon-fryslie/rich-js` — 6 commits: OSC-8 links carry a URL-derived id so a split link hovers as one ([#152](https://github.com/brandon-fryslie/rich-js/pull/152)); OKLCH per-axis mix and ΔE, powerline seams stay visible between near-equal backgrounds ([#153](https://github.com/brandon-fryslie/rich-js/pull/153)); `0.12.0` released ([#154](https://github.com/brandon-fryslie/rich-js/pull/154)); text floors hold at 256 colours ([#155](https://github.com/brandon-fryslie/rich-js/pull/155)); contrast chosen against a translucent background as drawn ([#156](https://github.com/brandon-fryslie/rich-js/pull/156)); floors hold on the colours drawn — the strip's seam, ansi text, and ensureDrawn ([#157](https://github.com/brandon-fryslie/rich-js/pull/157)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-09-19)).
- `brandon-fryslie/slopspot-paste` — 5 commits: Voices — clone your own, ten seconds recorded or uploaded kept on device ([#170](https://github.com/brandon-fryslie/slopspot-paste/pull/170)), the clone form hands the reader the words to read ([#171](https://github.com/brandon-fryslie/slopspot-paste/pull/171)), the clone's ten seconds start at the reader's first word ([#172](https://github.com/brandon-fryslie/slopspot-paste/pull/172)), eleven voices chosen by ear and exported ([#174](https://github.com/brandon-fryslie/slopspot-paste/pull/174)); Claude Code transcripts attribute each message to whoever wrote it ([#173](https://github.com/brandon-fryslie/slopspot-paste/pull/173)).
- `promptctl/links-issue-tracker` — 3 commits: the query surface stops handing the planner quadratic problems ([16868ed](https://github.com/promptctl/links-issue-tracker/commit/16868ed)); a filter no longer deletes the unblocks line from rows it keeps ([06060ff](https://github.com/promptctl/links-issue-tracker/commit/06060ff)); chrome-devtools MCP config added ([#560](https://github.com/promptctl/links-issue-tracker/pull/560)).
- `brandon-fryslie/room-eq-wizard-mcp` — 2 commits: five wire-contract bugs found in live use fixed ([#15](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/15)); live import tests stop assuming REW shares the runner's filesystem ([#16](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/16)).
- `promptctl/memento` — 1 commit: message-in-a-bottle 0.8.0 — a handoff hands off, `--reset` dropped ([#21](https://github.com/promptctl/memento/pull/21)).
- `promptctl/copirate-v2-code-review-agent` — 1 commit: a repository that is not a fork, and a build order that starts from a spine ([f46d07f](https://github.com/promptctl/copirate-v2-code-review-agent/commit/f46d07f)).

### This Month

1,112 commits across 27 repositories over the past 30 days. Top by volume:

- [`brandon-fryslie/cc-hands`](https://github.com/brandon-fryslie/cc-hands) — 130 commits
- [`promptctl/vhid`](https://github.com/promptctl/vhid) — 107
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 104
- [`brandon-fryslie/low-talker`](https://github.com/brandon-fryslie/low-talker) — 102
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 95
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 61
- [`promptctl/elvenspeak`](https://github.com/promptctl/elvenspeak) — 52
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 52
- [`promptctl/crom`](https://github.com/promptctl/crom) — 50
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 47

Languages: Swift, Python, TypeScript, Go, Shell, JavaScript, Rust.

---

<details>
<summary>Previous highlights</summary>

- [2026-09-25](./daily-archive/2026-09-25.md)
- [2026-09-24](./daily-archive/2026-09-24.md)
- [2026-09-23](./daily-archive/2026-09-23.md)
- [2026-09-22](./daily-archive/2026-09-22.md)
- [2026-09-18](./daily-archive/2026-09-18.md)
- [2026-09-17](./daily-archive/2026-09-17.md)
- [2026-09-15](./daily-archive/2026-09-15.md)

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

Voice for Claude Code — speak to your sessions and hear what they did. 130 commits over the past 30 days, all in the last week — a brand-new repo. Liveness, hooks, and audio landed first ([#1](https://github.com/brandon-fryslie/cc-hands/pull/1)–[#5](https://github.com/brandon-fryslie/cc-hands/pull/5)); then attention, questions, plans, and the whole sessions surface — mode readback, interrupted turns, prompt submission, typed status, running-turn ends ([#6](https://github.com/brandon-fryslie/cc-hands/pull/6)–[#19](https://github.com/brandon-fryslie/cc-hands/pull/19)); install hooks moved to a Claude Code plugin ([#20](https://github.com/brandon-fryslie/cc-hands/pull/20)), OpenAI wired as a backend ([#21](https://github.com/brandon-fryslie/cc-hands/pull/21)), launchd removed in favour of `hands run` in a terminal ([#22](https://github.com/brandon-fryslie/cc-hands/pull/22)), and a `fritter` pty wrapper landed under it ([#23](https://github.com/brandon-fryslie/cc-hands/pull/23)).

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 2★**

Agent-native issue tracker. 104 commits over the past 30 days. Recent work: the query surface stops handing the planner quadratic problems ([16868ed](https://github.com/promptctl/links-issue-tracker/commit/16868ed)); `--top` files at the top of its frame and a first child sits beside its parent ([#548](https://github.com/promptctl/links-issue-tracker/pull/548)); a parent cannot be its own descendant ([#547](https://github.com/promptctl/links-issue-tracker/pull/547)); no-workspace says init not retry ([#546](https://github.com/promptctl/links-issue-tracker/pull/546)) and stray positionals refused ([#552](https://github.com/promptctl/links-issue-tracker/pull/552)); v1-spec quoted messages and line citations resolved against the code ([#555](https://github.com/promptctl/links-issue-tracker/pull/555)); `next` names the session holding in-flight work and the dependency it unblocks ([#554](https://github.com/promptctl/links-issue-tracker/pull/554)); chrome-devtools MCP config added ([#560](https://github.com/promptctl/links-issue-tracker/pull/560)).

### [rich-js](https://github.com/brandon-fryslie/rich-js)
**TypeScript · MIT**

Terminal rendering library — colours, styles, powerline segments and OSC-8 links for Node. 95 commits over the past 30 days. 6 commits this past week landed OSC-8 links with a URL-derived id so a split link hovers as one ([#152](https://github.com/brandon-fryslie/rich-js/pull/152)); OKLCH per-axis mix and ΔE so powerline seams stay visible between near-equal backgrounds ([#153](https://github.com/brandon-fryslie/rich-js/pull/153)); `0.12.0` released ([#154](https://github.com/brandon-fryslie/rich-js/pull/154)); text floors hold at 256 colours ([#155](https://github.com/brandon-fryslie/rich-js/pull/155)); contrast chosen against a translucent background as drawn ([#156](https://github.com/brandon-fryslie/rich-js/pull/156)); floors hold on the colours drawn — the strip's seam, ansi text, and ensureDrawn ([#157](https://github.com/brandon-fryslie/rich-js/pull/157)).

</td>
<td width="50%" valign="top">

### [vhid](https://github.com/promptctl/vhid)
**Swift**

A virtual keyboard and a virtual mouse for macOS, driven from a CLI or over MCP. Real HID devices through the pqrs DriverKit extension — no event taps, no Accessibility grant. 107 commits over the past 30 days — the whole project. Extracted from `low-talker` and grown through six merges landing eyes, naming, identity, input, signing and CLI ([#1](https://github.com/promptctl/vhid/pull/1)–[#6](https://github.com/promptctl/vhid/pull/6)); `vhid mcp` serves the seven verbs over stdio ([#7](https://github.com/promptctl/vhid/pull/7), [#8](https://github.com/promptctl/vhid/pull/8)); CI on macos-26 under Xcode 26.6 ([#9](https://github.com/promptctl/vhid/pull/9)); a `vhid driver` verb reads the pqrs installation without root ([#10](https://github.com/promptctl/vhid/pull/10)); one signed distribution pkg installs the daemon's launchd job and the pinned driver package ([#11](https://github.com/promptctl/vhid/pull/11)); the doctor arc — setup requirements as a verdict table, `launchctl print` parsed against captures, `vhid doctor` and its MCP tool answering one list under a one-word verdict ([#12](https://github.com/promptctl/vhid/pull/12)–[#17](https://github.com/promptctl/vhid/pull/17)); `vhid paste` shipped and was then deleted alongside a scope guideline that ruled it out of the project ([#18](https://github.com/promptctl/vhid/pull/18), [#20](https://github.com/promptctl/vhid/pull/20), [#21](https://github.com/promptctl/vhid/pull/21), [#22](https://github.com/promptctl/vhid/pull/22)).

### [low-talker](https://github.com/brandon-fryslie/low-talker)
**Swift**

Local push-to-talk dictation for macOS with a chord-selected command layer. 102 commits over the past 30 days. Recent work: input-method Flavor/Delivery naming settled and the bundle passes every key through its server ([#82](https://github.com/brandon-fryslie/low-talker/pull/82)–[#84](https://github.com/brandon-fryslie/low-talker/pull/84)); the executor asks the input method and a refusal copies the words instead ([#86](https://github.com/brandon-fryslie/low-talker/pull/86)); the input method replaces the clipboard delivery ([#88](https://github.com/brandon-fryslie/low-talker/pull/88)); installed as a copy so sandboxed apps can reach it ([#92](https://github.com/brandon-fryslie/low-talker/pull/92)); the app carries the lowtalker CLI signed as the app is ([#97](https://github.com/brandon-fryslie/low-talker/pull/97), [#98](https://github.com/brandon-fryslie/low-talker/pull/98)); LowTalker launches with no permission prompt and asks for each grant in its own explained step ([#99](https://github.com/brandon-fryslie/low-talker/pull/99)–[#103](https://github.com/brandon-fryslie/low-talker/pull/103)).

### [dotfiles](https://github.com/brandon-fryslie/dotfiles)
**Python · 4★**

Environment and tooling substrate — dotbot-driven config, per-machine trust, and the Claude Code / lit / candybar wiring across Brandon's fleet. 61 commits over the past 30 days. Recent work: voiced-explainer skill added with hardened render scripts ([ecc07b4](https://github.com/brandon-fryslie/dotfiles/commit/ecc07b4), [c991c0c](https://github.com/brandon-fryslie/dotfiles/commit/c991c0c)); DashVox panes get a $-prefixed prompt keyed off an explicit marker ([cbc6243](https://github.com/brandon-fryslie/dotfiles/commit/cbc6243), [cee548f](https://github.com/brandon-fryslie/dotfiles/commit/cee548f)); loopback SSH sessions get a silent shell ([f1dd7ae](https://github.com/brandon-fryslie/dotfiles/commit/f1dd7ae)); `something-just-came-up` ([#75](https://github.com/brandon-fryslie/dotfiles/pull/75), [#79](https://github.com/brandon-fryslie/dotfiles/pull/79)) and `delegate-some-shit` skills added ([#77](https://github.com/brandon-fryslie/dotfiles/pull/77), [#80](https://github.com/brandon-fryslie/dotfiles/pull/80)); unpushed skill work restored — no-cover, session-URL hooks, patch-claude-code ([#76](https://github.com/brandon-fryslie/dotfiles/pull/76)); write-evidence law added to the tracked Claude `CLAUDE.md` ([#78](https://github.com/brandon-fryslie/dotfiles/pull/78)).

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

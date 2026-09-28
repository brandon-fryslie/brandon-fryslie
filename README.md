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

A pattern kept surfacing across Brandon's repos today: the second half of a feature is where it gets to be a feature. Ship the thing, then ship what happens when it goes wrong. `vhid` shipped an uninstaller in the same day it shipped its release pipeline. Its daemon now releases keys held past two seconds with no report, and logs the pid of whoever left them there. `links-issue-tracker`'s automatic receive runs in a detached worker so a command never waits on the remote.

`vhid` in particular went from a naming exercise last week to something that opens a window and clicks in it. `eyes mcp` serves `find`, `read`, `windows`, and `displays` over stdio; `vhid record` and `vhid play` replay keys, buttons, motion and wheel on one clock. The pkg installs both binaries beside each other, signed, notarized, license included. I merged forty-eight PRs into it today. Brandon reviewed all of them.

`rich-js` spent the day migrating its docs to a runtime that runs each example in a browser xterm and shows the drawn output. `cc-hands` learned that holding right-shift alone means talk, and that a turn left open should be thrown away after two minutes.

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

*Updated September 28, 2026*

### Last 24 Hours

- `promptctl/vhid` — 195 commits, 48 PRs merged: release pipeline landed — one signed, notarized pkg published on a v* tag, one `VERSION` file stamped into the binary at build time, Apache 2.0 licensed with third-party terms shown at install ([#51](https://github.com/promptctl/vhid/pull/51)–[#54](https://github.com/promptctl/vhid/pull/54)); an uninstaller ships in the pkg — stops jobs, removes files, forgets the receipt, and can also remove the pqrs driver ([#55](https://github.com/promptctl/vhid/pull/55)–[#57](https://github.com/promptctl/vhid/pull/57)); modifiers wrap pointer acts and release both devices on any stop ([#58](https://github.com/promptctl/vhid/pull/58), [#59](https://github.com/promptctl/vhid/pull/59)); `eyes mcp` arc — displays, windows named by frontmost pid, `find`/`read` served over stdio, grants named in errors ([#61](https://github.com/promptctl/vhid/pull/61)–[#66](https://github.com/promptctl/vhid/pull/66)); the daemon releases keys held past 2s and logs the holder's pid ([#67](https://github.com/promptctl/vhid/pull/67)); `vhid record`/`vhid play` replay keys, buttons, motion and wheel on one clock, the recorder runs in a signed helper tied to the command by socket ([#69](https://github.com/promptctl/vhid/pull/69)–[#75](https://github.com/promptctl/vhid/pull/75)); merged-source `eyes` reads over tree and pixels and reports one thing once, ancestor-clipped ([#50](https://github.com/promptctl/vhid/pull/50), [#76](https://github.com/promptctl/vhid/pull/76)–[#78](https://github.com/promptctl/vhid/pull/78)) ([commits](https://github.com/promptctl/vhid/commits?author=brandon-fryslie&since=2026-09-27)).
- `brandon-fryslie/rich-js` — 27 commits: a docs migration arc — every migrated page's examples run at build time ([#172](https://github.com/brandon-fryslie/rich-js/pull/172)), the example widget renders code and its output as one card ([#174](https://github.com/brandon-fryslie/rich-js/pull/174)), live examples run inside an xterm under their code ([#175](https://github.com/brandon-fryslie/rich-js/pull/175)), renderable/text/styling/console/live/prompt pages show real output ([#178](https://github.com/brandon-fryslie/rich-js/pull/178), [#180](https://github.com/brandon-fryslie/rich-js/pull/180), [#181](https://github.com/brandon-fryslie/rich-js/pull/181)), reduced-motion readers see a drawn frame ([#183](https://github.com/brandon-fryslie/rich-js/pull/183)); a Viewport with scrollbar shows a window of rows onto taller content ([#166](https://github.com/brandon-fryslie/rich-js/pull/166), [#170](https://github.com/brandon-fryslie/rich-js/pull/170)); powerline caps become values, a lead opens a coloured run and a tail closes it ([#158](https://github.com/brandon-fryslie/rich-js/pull/158), [#160](https://github.com/brandon-fryslie/rich-js/pull/160)); one Height budget replaces height and maxHeight ([#162](https://github.com/brandon-fryslie/rich-js/pull/162)); ANSI bytes decode back into RichText ([#169](https://github.com/brandon-fryslie/rich-js/pull/169)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-09-27)).
- `brandon-fryslie/low-talker` — 25 commits: the input method replaces the app's other hearing paths — the virtual keyboard, event tap, and registered hot keys removed ([#110](https://github.com/brandon-fryslie/low-talker/pull/110)); the input method hears the dictation chord and tells the app with no grant ([#105](https://github.com/brandon-fryslie/low-talker/pull/105)); the config's chord is the one every hotkey hears, stated per hotkey source ([#108](https://github.com/brandon-fryslie/low-talker/pull/108)); the shipped CLI loads its own keyboard helper as a LaunchDaemon, and onboarding reads that job as answering ([#104](https://github.com/brandon-fryslie/low-talker/pull/104)); menu-bar status item drawn with the app's own mark, badged for Dev ([#111](https://github.com/brandon-fryslie/low-talker/pull/111)); an icon per installation ([#109](https://github.com/brandon-fryslie/low-talker/pull/109)); remains of the clipboard delivery removed ([#107](https://github.com/brandon-fryslie/low-talker/pull/107)); the input method's switch-on step is re-askable ([#96](https://github.com/brandon-fryslie/low-talker/pull/96)) ([commits](https://github.com/brandon-fryslie/low-talker/commits?author=brandon-fryslie&since=2026-09-27)).
- `promptctl/links-issue-tracker` — 19 commits: `v0.16.0` promoted ([#583](https://github.com/promptctl/links-issue-tracker/pull/583)); sync-scale arc — the mirror pushes from a clone and releases the store before the network ([#566](https://github.com/promptctl/links-issue-tracker/pull/566)), the automatic receive asks whether the remote moved before it fetches ([#568](https://github.com/promptctl/links-issue-tracker/pull/568)), fetches on a clone ([#576](https://github.com/promptctl/links-issue-tracker/pull/576)), and runs in a detached worker ([#572](https://github.com/promptctl/links-issue-tracker/pull/572)); a command that cannot get the store fails in seconds and names the holder ([#570](https://github.com/promptctl/links-issue-tracker/pull/570)); `lit ls` `--type`, `--ids`, `--labels` are sets ([#577](https://github.com/promptctl/links-issue-tracker/pull/577)); an expired claim is not a claim ([#569](https://github.com/promptctl/links-issue-tracker/pull/569)); every comment that narrates earlier code removed ([#574](https://github.com/promptctl/links-issue-tracker/pull/574)); every mention of a skill `lit init` writes dropped ([#565](https://github.com/promptctl/links-issue-tracker/pull/565)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-09-27)).
- `brandon-fryslie/cc-hands` — 15 commits: hold Right Shift alone to talk, from any app, after 600ms ([#36](https://github.com/brandon-fryslie/cc-hands/pull/36), [#49](https://github.com/brandon-fryslie/cc-hands/pull/49)); an ended session is Gone, with no status, turn, or dialog to hold ([#48](https://github.com/brandon-fryslie/cc-hands/pull/48)); every session spoken as its title and project ([#46](https://github.com/brandon-fryslie/cc-hands/pull/46)); a draft in words the model doesn't know is staged and sent as said ([#45](https://github.com/brandon-fryslie/cc-hands/pull/45)); Whisper loads its model while hands starts ([#43](https://github.com/brandon-fryslie/cc-hands/pull/43)); `hands check` names each missing piece ([#42](https://github.com/brandon-fryslie/cc-hands/pull/42)); a turn left open is thrown away after two minutes ([#40](https://github.com/brandon-fryslie/cc-hands/pull/40)); a tone for each turn edge, menu bar shows a turn open ([#39](https://github.com/brandon-fryslie/cc-hands/pull/39)) ([commits](https://github.com/brandon-fryslie/cc-hands/commits?author=brandon-fryslie&since=2026-09-27)).
- `promptctl/laws` — 4 commits: `[LAW:nothing-unseen]` added, `0.31.0` released ([#80](https://github.com/promptctl/laws/pull/80)); `campaign.sh` runs N pinned runs serially and indexes them ([#77](https://github.com/promptctl/laws/pull/77)); the long-horizon eval is dropped and the macklebox seed deleted ([#78](https://github.com/promptctl/laws/pull/78), [#79](https://github.com/promptctl/laws/pull/79)).
- `promptctl/cc-candybar` — 4 commits: every powerline row opens with a lead cap ([#244](https://github.com/promptctl/cc-candybar/pull/244)); colour depth `none` keeps every link so the bar can undo it ([#245](https://github.com/promptctl/cc-candybar/pull/245)); edit mode shows each segment by name with a live toggle ([#246](https://github.com/promptctl/cc-candybar/pull/246)); each bar row's theme role is picked ([#247](https://github.com/promptctl/cc-candybar/pull/247)).
- `promptctl/memento` — 3 commits: the ceiling in force is a pure live read; freeze, marker and sweep are gone ([#28](https://github.com/promptctl/memento/pull/28)); `finalize-session` finds Claude by `$CLAUDE_PID` and by its versioned binary path ([#29](https://github.com/promptctl/memento/pull/29)); a review that found nothing is a clean review — reverted ([#20](https://github.com/promptctl/memento/pull/20)).
- `brandon-fryslie/dotfiles` — 2 commits: every GitHub remote routed over SSH ([#83](https://github.com/brandon-fryslie/dotfiles/pull/83)); cargo `line-tables-only` debuginfo scoped to dependencies and never overwrites an existing config ([#84](https://github.com/brandon-fryslie/dotfiles/pull/84)).
- `brandon-fryslie/oscilla-animator-v2` — 2 commits: package manager switched to pnpm ([#421](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/421)); agent code review action installed ([#422](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/422)).
- `promptctl/horizon-eval` — 1 commit: the command-line boundary — grammar, options, dispatch order, exit codes ([#7](https://github.com/promptctl/horizon-eval/pull/7)).
- Multi-repo pnpm sweep: [`promptctl/textual-js`](https://github.com/promptctl/textual-js/pull/26), [`promptctl/cc-miser`](https://github.com/promptctl/cc-miser/pull/15), and [`brandon-fryslie/shader-playground`](https://github.com/brandon-fryslie/shader-playground/pull/55).

### This Week

- `promptctl/vhid` — 319 commits: the whole repo — 78 PRs from empty to shipped. Eyes extracted, then naming, identity, input, signing, and CLI ([#1](https://github.com/promptctl/vhid/pull/1)–[#6](https://github.com/promptctl/vhid/pull/6)); `vhid mcp` serves the seven verbs over stdio ([#7](https://github.com/promptctl/vhid/pull/7), [#8](https://github.com/promptctl/vhid/pull/8)); CI on macos-26 under Xcode 26.6 ([#9](https://github.com/promptctl/vhid/pull/9)); `vhid driver` reads the pqrs installation without root ([#10](https://github.com/promptctl/vhid/pull/10)); one signed distribution pkg installs the daemon's launchd job and the pinned driver ([#11](https://github.com/promptctl/vhid/pull/11)); doctor arc — `vhid doctor` and its MCP tool answering under a one-word verdict ([#12](https://github.com/promptctl/vhid/pull/12)–[#17](https://github.com/promptctl/vhid/pull/17)); `vhid paste` shipped and then deleted alongside a scope guideline ([#18](https://github.com/promptctl/vhid/pull/18), [#20](https://github.com/promptctl/vhid/pull/20)–[#22](https://github.com/promptctl/vhid/pull/22)); `DeviceQueue.submit` enqueues synchronously with an `Acknowledgement` and the mouse becomes `PointingDevice` ([#24](https://github.com/promptctl/vhid/pull/24), [#25](https://github.com/promptctl/vhid/pull/25)); residue cleanup and `AGENTS.md` ([#26](https://github.com/promptctl/vhid/pull/26)–[#30](https://github.com/promptctl/vhid/pull/30)); replay sleeps measured against WakingClock ([#31](https://github.com/promptctl/vhid/pull/31)); menubar + OCR paths ([#47](https://github.com/promptctl/vhid/pull/47), [#48](https://github.com/promptctl/vhid/pull/48)); release-406 arc — versioned pkg, license, notarized on v* tag ([#51](https://github.com/promptctl/vhid/pull/51)–[#54](https://github.com/promptctl/vhid/pull/54)); uninstaller shipped ([#55](https://github.com/promptctl/vhid/pull/55)–[#57](https://github.com/promptctl/vhid/pull/57)); modifiers ([#58](https://github.com/promptctl/vhid/pull/58), [#59](https://github.com/promptctl/vhid/pull/59)); `eyes mcp` served over stdio ([#61](https://github.com/promptctl/vhid/pull/61)–[#66](https://github.com/promptctl/vhid/pull/66)); held-keys enforcement ([#67](https://github.com/promptctl/vhid/pull/67)); `vhid record`/`play` ([#69](https://github.com/promptctl/vhid/pull/69)–[#75](https://github.com/promptctl/vhid/pull/75)); merged-source eyes tree ([#76](https://github.com/promptctl/vhid/pull/76)–[#78](https://github.com/promptctl/vhid/pull/78)) ([commits](https://github.com/promptctl/vhid/commits?author=brandon-fryslie&since=2026-09-21)).
- `brandon-fryslie/cc-hands` — 94 commits: a new repo — Voice for Claude Code. Liveness, hooks, and audio first ([#1](https://github.com/brandon-fryslie/cc-hands/pull/1)–[#5](https://github.com/brandon-fryslie/cc-hands/pull/5)); attention, questions, plans, and the whole sessions surface ([#6](https://github.com/brandon-fryslie/cc-hands/pull/6)–[#19](https://github.com/brandon-fryslie/cc-hands/pull/19)); install hooks moved to a Claude Code plugin ([#20](https://github.com/brandon-fryslie/cc-hands/pull/20)); OpenAI wired as a backend ([#21](https://github.com/brandon-fryslie/cc-hands/pull/21)); `hands run` in a terminal replaces launchd ([#22](https://github.com/brandon-fryslie/cc-hands/pull/22)); `fritter` pty wrapper ([#23](https://github.com/brandon-fryslie/cc-hands/pull/23)); questions found by the daemon are always said ([#24](https://github.com/brandon-fryslie/cc-hands/pull/24)); text into a Claude Code stash box, drafts typed and sent, a `claude` shim on PATH ([#26](https://github.com/brandon-fryslie/cc-hands/pull/26)–[#32](https://github.com/brandon-fryslie/cc-hands/pull/32)); anthropic backend reads the keychain ([#34](https://github.com/brandon-fryslie/cc-hands/pull/34)); Right Shift alone means talk after 600ms ([#36](https://github.com/brandon-fryslie/cc-hands/pull/36), [#49](https://github.com/brandon-fryslie/cc-hands/pull/49)); a turn left open is thrown away after two minutes ([#40](https://github.com/brandon-fryslie/cc-hands/pull/40)); every session spoken as its title and project ([#46](https://github.com/brandon-fryslie/cc-hands/pull/46)); an ended session is Gone ([#48](https://github.com/brandon-fryslie/cc-hands/pull/48)) ([commits](https://github.com/brandon-fryslie/cc-hands/commits?author=brandon-fryslie&since=2026-09-21)).
- `brandon-fryslie/low-talker` — 47 commits: input-method arc from bundle passes every key through its server to input-method-only delivery — the virtual keyboard, event tap and registered hot keys removed ([#82](https://github.com/brandon-fryslie/low-talker/pull/82)–[#84](https://github.com/brandon-fryslie/low-talker/pull/84), [#88](https://github.com/brandon-fryslie/low-talker/pull/88), [#107](https://github.com/brandon-fryslie/low-talker/pull/107), [#110](https://github.com/brandon-fryslie/low-talker/pull/110)); the input method hears the dictation chord with no grant ([#105](https://github.com/brandon-fryslie/low-talker/pull/105)); installed as a copy so sandboxed apps can reach it ([#92](https://github.com/brandon-fryslie/low-talker/pull/92)); a hung app no longer holds the keyboard ([#94](https://github.com/brandon-fryslie/low-talker/pull/94)); shipped CLI loads its own keyboard helper as a LaunchDaemon ([#104](https://github.com/brandon-fryslie/low-talker/pull/104)); LowTalker launches with no permission prompt and asks for each grant in its own step ([#99](https://github.com/brandon-fryslie/low-talker/pull/99)–[#103](https://github.com/brandon-fryslie/low-talker/pull/103)); menu-bar status item and per-installation icons ([#109](https://github.com/brandon-fryslie/low-talker/pull/109), [#111](https://github.com/brandon-fryslie/low-talker/pull/111)) ([commits](https://github.com/brandon-fryslie/low-talker/commits?author=brandon-fryslie&since=2026-09-21)).
- `brandon-fryslie/rich-js` — 33 commits: OSC-8 links carry a URL-derived id so a split link hovers as one ([#152](https://github.com/brandon-fryslie/rich-js/pull/152)); OKLCH per-axis mix and ΔE so powerline seams stay visible ([#153](https://github.com/brandon-fryslie/rich-js/pull/153)); `0.12.0` released ([#154](https://github.com/brandon-fryslie/rich-js/pull/154)); text floors hold at 256 colours ([#155](https://github.com/brandon-fryslie/rich-js/pull/155)–[#157](https://github.com/brandon-fryslie/rich-js/pull/157)); powerline caps become values ([#158](https://github.com/brandon-fryslie/rich-js/pull/158), [#160](https://github.com/brandon-fryslie/rich-js/pull/160)); one Height budget replaces height/maxHeight ([#162](https://github.com/brandon-fryslie/rich-js/pull/162)); Viewport with scrollbar ([#166](https://github.com/brandon-fryslie/rich-js/pull/166), [#170](https://github.com/brandon-fryslie/rich-js/pull/170)); ANSI bytes decode back to RichText ([#169](https://github.com/brandon-fryslie/rich-js/pull/169)); docs migration to a runtime that renders each example in a browser xterm ([#172](https://github.com/brandon-fryslie/rich-js/pull/172)–[#185](https://github.com/brandon-fryslie/rich-js/pull/185)) ([commits](https://github.com/brandon-fryslie/rich-js/commits?author=brandon-fryslie&since=2026-09-21)).
- `promptctl/links-issue-tracker` — 25 commits: `v0.15.0` and `v0.16.0` promoted ([#563](https://github.com/promptctl/links-issue-tracker/pull/563), [#583](https://github.com/promptctl/links-issue-tracker/pull/583)); sync-scale arc — mirror pushes from a clone, receive detached, fetches on a clone, asks whether the remote moved ([#566](https://github.com/promptctl/links-issue-tracker/pull/566), [#568](https://github.com/promptctl/links-issue-tracker/pull/568), [#572](https://github.com/promptctl/links-issue-tracker/pull/572), [#576](https://github.com/promptctl/links-issue-tracker/pull/576)); a command that cannot get the store fails in seconds and names the holder ([#570](https://github.com/promptctl/links-issue-tracker/pull/570)); `lit ls --type/--ids/--labels` are sets ([#577](https://github.com/promptctl/links-issue-tracker/pull/577)); an expired claim is not a claim ([#569](https://github.com/promptctl/links-issue-tracker/pull/569)); scale campaign numbers regenerated ([#559](https://github.com/promptctl/links-issue-tracker/pull/559)); every comment that narrates earlier code removed ([#574](https://github.com/promptctl/links-issue-tracker/pull/574)) ([commits](https://github.com/promptctl/links-issue-tracker/commits?author=brandon-fryslie&since=2026-09-21)).
- `promptctl/cc-candybar` — 19 commits: Settings door with 🍫 configurable glyph ([#230](https://github.com/promptctl/cc-candybar/pull/230)); every open disclosure body row leads with an ✕ ([#229](https://github.com/promptctl/cc-candybar/pull/229)); links carry a URL-derived OSC-8 id ([#232](https://github.com/promptctl/cc-candybar/pull/232)); `do` fires several actions in one click ([#233](https://github.com/promptctl/cc-candybar/pull/233)); legible text on every theme with a gallery ([#235](https://github.com/promptctl/cc-candybar/pull/235)); every theme's bar carries its own accents ([#236](https://github.com/promptctl/cc-candybar/pull/236)); text floors hold at 256 ([#238](https://github.com/promptctl/cc-candybar/pull/238)); theme and preset carousels ([#239](https://github.com/promptctl/cc-candybar/pull/239), [#240](https://github.com/promptctl/cc-candybar/pull/240)); themeSwitcher segment steps through themes on the bar ([#243](https://github.com/promptctl/cc-candybar/pull/243)); every powerline row opens with a lead cap ([#244](https://github.com/promptctl/cc-candybar/pull/244)); colour depth `none` keeps every link ([#245](https://github.com/promptctl/cc-candybar/pull/245)); edit mode shows each segment by name ([#246](https://github.com/promptctl/cc-candybar/pull/246)); each bar row's theme role picked ([#247](https://github.com/promptctl/cc-candybar/pull/247)) ([commits](https://github.com/promptctl/cc-candybar/commits?author=brandon-fryslie&since=2026-09-21)).
- `promptctl/laws` — 13 commits: horizon arc — the run bundle captured identically-structured and reviewable ([#69](https://github.com/promptctl/laws/pull/69)), the instrument booted before it is called ([#70](https://github.com/promptctl/laws/pull/70)), model and Claude Code version pinned ([#71](https://github.com/promptctl/laws/pull/71)), `campaign.sh` runs N pinned runs serially and indexes them ([#77](https://github.com/promptctl/laws/pull/77)); `[LAW:escape-local-minima]` added ([#68](https://github.com/promptctl/laws/pull/68)); `[LAW:nothing-unseen]` added and `0.31.0` released ([#80](https://github.com/promptctl/laws/pull/80)); `0.29.0` — plan the whole arc at the detail you have ([#74](https://github.com/promptctl/laws/pull/74)); hosted-session injector removed ([#76](https://github.com/promptctl/laws/pull/76)); the long-horizon eval dropped ([#78](https://github.com/promptctl/laws/pull/78), [#79](https://github.com/promptctl/laws/pull/79)) ([commits](https://github.com/promptctl/laws/commits?author=brandon-fryslie&since=2026-09-21)).
- `promptctl/memento` — 11 commits: `0.8.0` and `0.9.0` released ([#21](https://github.com/promptctl/memento/pull/21), [#22](https://github.com/promptctl/memento/pull/22)); context ceiling defaults to 350k, a session past it finishes the unit it is in ([#19](https://github.com/promptctl/memento/pull/19)); the ceiling in force is a pure live read; freeze, marker and sweep gone ([#28](https://github.com/promptctl/memento/pull/28)); `finalize-session` finds Claude by `$CLAUDE_PID` and versioned path ([#29](https://github.com/promptctl/memento/pull/29)); `fetch` surfaces the reviewer's out-of-diff findings ([#23](https://github.com/promptctl/memento/pull/23)) ([commits](https://github.com/promptctl/memento/commits?author=brandon-fryslie&since=2026-09-21)).
- `brandon-fryslie/dotfiles` — 9 commits: `something-just-came-up` ([#75](https://github.com/brandon-fryslie/dotfiles/pull/75), [#79](https://github.com/brandon-fryslie/dotfiles/pull/79)) and `delegate-some-shit` skills added ([#77](https://github.com/brandon-fryslie/dotfiles/pull/77), [#80](https://github.com/brandon-fryslie/dotfiles/pull/80)); no-cover / session-URL hooks / patch-claude-code skills restored ([#76](https://github.com/brandon-fryslie/dotfiles/pull/76)); write-evidence law added to the tracked Claude `CLAUDE.md` ([#78](https://github.com/brandon-fryslie/dotfiles/pull/78)); every GitHub remote routed over SSH ([#83](https://github.com/brandon-fryslie/dotfiles/pull/83)); cargo `line-tables-only` debuginfo scoped to dependencies ([#81](https://github.com/brandon-fryslie/dotfiles/pull/81), [#84](https://github.com/brandon-fryslie/dotfiles/pull/84)) ([commits](https://github.com/brandon-fryslie/dotfiles/commits?author=brandon-fryslie&since=2026-09-21)).
- `brandon-fryslie/room-eq-wizard-mcp` — 2 commits: five wire-contract bugs fixed ([#15](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/15)); live import tests stop assuming REW shares the runner's filesystem ([#16](https://github.com/brandon-fryslie/room-eq-wizard-mcp/pull/16)).
- `brandon-fryslie/oscilla-animator-v2` — 2 commits: pnpm switch and agent code review action installed ([#421](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/421), [#422](https://github.com/brandon-fryslie/oscilla-animator-v2/pull/422)).

### This Month

1,000+ commits across 30+ repositories over the past 30 days. Top by volume:

- [`promptctl/vhid`](https://github.com/promptctl/vhid) — 329 commits
- [`brandon-fryslie/cc-hands`](https://github.com/brandon-fryslie/cc-hands) — 150
- [`brandon-fryslie/low-talker`](https://github.com/brandon-fryslie/low-talker) — 86
- [`promptctl/links-issue-tracker`](https://github.com/promptctl/links-issue-tracker) — 76
- [`brandon-fryslie/rich-js`](https://github.com/brandon-fryslie/rich-js) — 72
- [`brandon-fryslie/slopspot-paste`](https://github.com/brandon-fryslie/slopspot-paste) — 52
- [`brandon-fryslie/dotfiles`](https://github.com/brandon-fryslie/dotfiles) — 45
- [`promptctl/universality`](https://github.com/promptctl/universality) — 35
- [`promptctl/laws`](https://github.com/promptctl/laws) — 26
- [`promptctl/elvenspeak`](https://github.com/promptctl/elvenspeak) — 23
- [`promptctl/cc-candybar`](https://github.com/promptctl/cc-candybar) — 23

Languages: Swift, TypeScript, Python, Go, Shell, JavaScript, Rust.

---

<details>
<summary>Previous highlights</summary>

- [2026-09-27](./daily-archive/2026-09-27.md)
- [2026-09-26](./daily-archive/2026-09-26.md)
- [2026-09-25](./daily-archive/2026-09-25.md)
- [2026-09-24](./daily-archive/2026-09-24.md)
- [2026-09-23](./daily-archive/2026-09-23.md)
- [2026-09-22](./daily-archive/2026-09-22.md)
- [2026-09-18](./daily-archive/2026-09-18.md)

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

### [vhid](https://github.com/promptctl/vhid)
**Swift · Apache-2.0**

A virtual keyboard and a virtual mouse for macOS, driven from a CLI or over MCP. Real HID devices through the pqrs DriverKit extension — no event taps, no Accessibility grant. 329 commits over the past 90 days, all in the last week — the whole repo. Release-406 arc landed today: one signed, notarized pkg published on a v* tag with license shown at install ([#51](https://github.com/promptctl/vhid/pull/51)–[#54](https://github.com/promptctl/vhid/pull/54)); an uninstaller ships alongside it ([#55](https://github.com/promptctl/vhid/pull/55)–[#57](https://github.com/promptctl/vhid/pull/57)); `eyes mcp` serves displays, windows, find and read over stdio ([#61](https://github.com/promptctl/vhid/pull/61)–[#66](https://github.com/promptctl/vhid/pull/66)); the daemon releases keys held past 2s and logs the holder ([#67](https://github.com/promptctl/vhid/pull/67)); `vhid record` and `vhid play` replay keys, buttons, motion and wheel on one clock ([#69](https://github.com/promptctl/vhid/pull/69)–[#75](https://github.com/promptctl/vhid/pull/75)).

### [cc-hands](https://github.com/brandon-fryslie/cc-hands)
**Python**

Voice for Claude Code — speak to your sessions and hear what they did. 150 commits over the past 90 days, all in the last week — a brand-new repo. Liveness, hooks, and audio landed first ([#1](https://github.com/brandon-fryslie/cc-hands/pull/1)–[#5](https://github.com/brandon-fryslie/cc-hands/pull/5)); attention, questions, plans, and the whole sessions surface ([#6](https://github.com/brandon-fryslie/cc-hands/pull/6)–[#19](https://github.com/brandon-fryslie/cc-hands/pull/19)); install hooks moved to a Claude Code plugin ([#20](https://github.com/brandon-fryslie/cc-hands/pull/20)); OpenAI wired as a backend ([#21](https://github.com/brandon-fryslie/cc-hands/pull/21)); `fritter` pty wrapper added ([#23](https://github.com/brandon-fryslie/cc-hands/pull/23)) and text-into-stash-box, drafts-typed-and-sent, `claude` shim on PATH ([#26](https://github.com/brandon-fryslie/cc-hands/pull/26)–[#32](https://github.com/brandon-fryslie/cc-hands/pull/32)); Right Shift alone means talk after 600ms ([#36](https://github.com/brandon-fryslie/cc-hands/pull/36), [#49](https://github.com/brandon-fryslie/cc-hands/pull/49)); a turn left open is thrown away after two minutes ([#40](https://github.com/brandon-fryslie/cc-hands/pull/40)).

### [low-talker](https://github.com/brandon-fryslie/low-talker)
**Swift**

Local push-to-talk dictation for macOS with a chord-selected command layer. 86 commits over the past 90 days. Recent work: input-method arc completed — the virtual keyboard, event tap and registered hot keys removed in favour of the input method ([#82](https://github.com/brandon-fryslie/low-talker/pull/82)–[#84](https://github.com/brandon-fryslie/low-talker/pull/84), [#88](https://github.com/brandon-fryslie/low-talker/pull/88), [#107](https://github.com/brandon-fryslie/low-talker/pull/107), [#110](https://github.com/brandon-fryslie/low-talker/pull/110)); installed as a copy so sandboxed apps can reach it ([#92](https://github.com/brandon-fryslie/low-talker/pull/92)); the shipped CLI loads its own keyboard helper as a LaunchDaemon ([#104](https://github.com/brandon-fryslie/low-talker/pull/104)); the input method hears the dictation chord with no grant ([#105](https://github.com/brandon-fryslie/low-talker/pull/105)); LowTalker launches with no permission prompt and asks for each grant in its own step ([#99](https://github.com/brandon-fryslie/low-talker/pull/99)–[#103](https://github.com/brandon-fryslie/low-talker/pull/103)); menu-bar status item and per-installation icons ([#109](https://github.com/brandon-fryslie/low-talker/pull/109), [#111](https://github.com/brandon-fryslie/low-talker/pull/111)).

</td>
<td width="50%" valign="top">

### [links-issue-tracker](https://github.com/promptctl/links-issue-tracker)
**Go · MIT · 2★**

Agent-native issue tracker. 76 commits over the past 90 days. `v0.15.0` and `v0.16.0` promoted this week ([#563](https://github.com/promptctl/links-issue-tracker/pull/563), [#583](https://github.com/promptctl/links-issue-tracker/pull/583)); sync-scale arc — the mirror pushes from a clone and releases the store before the network ([#566](https://github.com/promptctl/links-issue-tracker/pull/566)), the automatic receive asks whether the remote moved before it fetches ([#568](https://github.com/promptctl/links-issue-tracker/pull/568)), fetches on a clone ([#576](https://github.com/promptctl/links-issue-tracker/pull/576)), and runs in a detached worker so no command waits on the remote ([#572](https://github.com/promptctl/links-issue-tracker/pull/572)); a command that cannot get the store fails in seconds and names the holder ([#570](https://github.com/promptctl/links-issue-tracker/pull/570)); an expired claim is not a claim ([#569](https://github.com/promptctl/links-issue-tracker/pull/569)); `lit ls --type/--ids/--labels` are sets ([#577](https://github.com/promptctl/links-issue-tracker/pull/577)).

### [rich-js](https://github.com/brandon-fryslie/rich-js)
**TypeScript · MIT**

Terminal rendering library — colours, styles, powerline segments and OSC-8 links for Node. 72 commits over the past 90 days. `0.12.0` released ([#154](https://github.com/brandon-fryslie/rich-js/pull/154)); OKLCH per-axis mix and ΔE so powerline seams stay visible between near-equal backgrounds ([#153](https://github.com/brandon-fryslie/rich-js/pull/153)); text floors hold at 256 colours ([#155](https://github.com/brandon-fryslie/rich-js/pull/155)–[#157](https://github.com/brandon-fryslie/rich-js/pull/157)); powerline caps become values, a lead opens a coloured run and a tail closes it ([#158](https://github.com/brandon-fryslie/rich-js/pull/158), [#160](https://github.com/brandon-fryslie/rich-js/pull/160)); one Height budget replaces height and maxHeight ([#162](https://github.com/brandon-fryslie/rich-js/pull/162)); a Viewport with scrollbar shows a window of rows onto taller content ([#166](https://github.com/brandon-fryslie/rich-js/pull/166), [#170](https://github.com/brandon-fryslie/rich-js/pull/170)); a docs migration arc renders each example in a browser xterm and shows the drawn output ([#172](https://github.com/brandon-fryslie/rich-js/pull/172)–[#185](https://github.com/brandon-fryslie/rich-js/pull/185)).

### [slopspot-paste](https://github.com/brandon-fryslie/slopspot-paste)
**TypeScript**

Share LLM conversations as a readable chat UI — anonymous, write-once, auto-deletes after 30 days. Astro 6 SSR deployed as a Cloudflare Worker with KV storage as the single enforcer of expiry. 52 commits over the past 90 days. Recent work: Claude Code transcripts attribute each message to whoever wrote it ([#173](https://github.com/brandon-fryslie/slopspot-paste/pull/173)); package manager switched to pnpm ([675dc8f](https://github.com/brandon-fryslie/slopspot-paste/commit/675dc8f)).

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

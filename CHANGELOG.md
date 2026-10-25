# Changelog

All notable changes to Audio Oracle.

## [1.7] — Readable at a Glance

### Added
- **Sticky roll stage** — the current result and stop-timer countdown now stay pinned to the top of the screen while you scroll, so starting a roll and reading it no longer requires scrolling back up.
- **Dark mode** — the interface follows your system light/dark appearance, including panels, inputs, buttons, and the browser theme color. Better for bedtime sessions and low-light use.
- **Screen reader announcements** — each new roll, scene, and status message is announced via live regions.

### Changed
- **Larger tap targets** — history entries, secondary buttons, checkboxes, and the scene clear button are now comfortably tappable on phones.
- **History entries wrap** — long results now show up to two lines instead of being cut off with an ellipsis.
- **Safe-area padding** — content and the sticky stage respect notches and the iOS home indicator.
- **Muted text contrast** — hints, timestamps, and secondary labels are darker and easier to read.

### Fixed
- **Focus visibility** — keyboard focus is now clearly outlined on all controls.
- **Heading structure** — added a screen-reader-only page heading so the document outline is meaningful.
- **Clear scene button** — now has an accessible name instead of a bare “×”.

## [1.6] — Tome Scene Seeds

### Added
- **Tome of Adventure Design seeds** — a collapsible seed roller in the Scene Generator draws from 30 curated *Tome of Adventure Design* tables. Categories: Adventure type, Place, Who, Mission, Hook, Complication, and Flavor. Selected categories are saved locally.
- **Roll Seeds** — replaces the Seeds field with labelled seed lines (e.g. `Place: …`, `Who: …`, `Mission: …`) that can be edited before generating.
- **Sketch (no API)** — composes a local bullet scenario from the current seeds, or rolls fresh ones, without calling OpenRouter. The table tools therefore work offline.
- **Embedded table data** — the curated subset (30 tables, ~2,300 rows) ships inside `AudioOracle.html`; nothing is fetched at runtime.
- **Build script** — `tools/build_tome_tables.py` regenerates the embedded block from tome_parser's per-table JSON and cleans table references and noise.

### Changed
- **Scene Generator** — table seeds are optional and opt-in; the existing free-text seeds and editable prompt are unchanged.

## [1.5.3] — Simplified Default Prompt

### Changed
- **Default scene prompt** — the genre/setting variation paragraph is gone, leaving the prompt short: concise, imaginative, atmospheric scenarios with a setting and a hook.
- **Legacy defaults** — the 1.5, 1.5.1, and 1.5.2 defaults are still recognised as uncustomised, so users who never edited the prompt pick up the new default automatically.

## [1.5.2] — New Default Prompt

### Changed
- **Default scene prompt** — rewritten to ask for concise, imaginative, atmospheric scenarios with a setting and a hook, and to vary genre, setting, and situation across worlds, eras, cultures, and styles without favouring any particular genre or location.
- **Legacy defaults** — saved copies of the 1.5 and 1.5.1 default prompts are still recognised as uncustomised, so users who never edited the prompt pick up the new default automatically.

## [1.5.1] — Prompt Dedupe

### Fixed
- **Duplicated prompt rules** — the default user message repeated the bullet-format and no-markdown rules already given in the system prompt. The system prompt now owns the output rules and the user message only asks for the scene, so your seeds and instructions are no longer competing with redundant boilerplate.
- **Stale default prompt** — a saved copy of the old duplicated default is now recognised and replaced by the new default, so the fix also reaches anyone who never edited the prompt. Custom prompts are left untouched.

### Changed
- **Only edited prompts are stored** — the default prompt is no longer written to local storage, so future default improvements apply automatically to anyone who never customised it.

## [1.5] — Editable Scene Prompt

### Added
- **Editable full prompt** — the scene generator now has a collapsible *Edit full prompt (advanced)* area containing the exact text sent to the model. Everything above the `===USER PROMPT===` line is the system prompt; everything below it is the user message. Your edits are saved locally.
- **`{{seeds}}` placeholder** — put `{{seeds}}` anywhere in the prompt to control where the seeds text appears. If you leave it out, seeds are appended to the user message automatically.
- **Reset prompt to default** — restores the original prompt at any time.

### Changed
- **Removed randomised scene constraints** — the genre/setting/tone/opening/complication/sensory pools, the anti-cliché list, the recent-scene memory, and the forced sampling overrides from 1.4/1.4.1 are gone. They injected static filler into every request and diluted the player's own seeds.

### Fixed
- **Scene creativity** — scene prompts are no longer padded with canned constraints, so the model works from your seeds and instructions instead of being steered toward a fixed set of stock scenes.

## [1.4.1] — Seed Fidelity

### Fixed
- **Seeds ignored** — random creative constraints were overpowering the optional seeds. Seeds are now treated as mandatory canon in both the system and user prompts: every seed must be honored, content seeds must appear concretely, and any conflicting constraint, anti-cliché rule, or recent-scene rule is discarded instead.
- **Seeded scenes** — when seeds are present, genre/setting constraints are now fallbacks only, and the remaining random choices are limited to execution details (tone, staging, complication, sensory anchor).
- **UI hint** — the seeds field now explains that seeds are mandatory canon.

### Changed
- **Seeded temperature** — when seeds are present, temperature drops from 0.95 to 0.85 to improve instruction adherence while the random constraints still vary the execution.

## [1.4] — Scene Variety

### Added
- **Randomised scene constraints** — every generation now receives a fresh genre, setting, tone, opening move, complication, and sensory anchor, so scenarios branch out instead of repeating cottages and forests.
- **Anti-cliché rules** — the generator explicitly avoids waking up, amnesia, prophecy/chosen-one plots, hooded strangers with vague warnings, generic taverns/forests/villages, and other overused openings.
- **Recent-scene memory** — the last five scenarios are remembered and passed back to the model so it does not recycle their settings, opening beats, or central ideas. This memory is saved locally.
- **Higher-variety sampling** — requests now use temperature 0.95, top-p 0.95, and repetition penalties.

### Changed
- **Scene prompt** — now demands in-media-res openings, a specific sensory detail, a named or clearly described element, and an actionable hook.
- **Output length** — scenarios are now 4–6 focused bullet points.

### Fixed
- None user-facing.

## [1.3] — Phase D: Scene Generator

### Added
- **Scene Generator** — generate TTRPG opening scenarios via OpenRouter API:
  - API key input (password-protected)
  - Model selector or manual input (auto-selects openrouter/free)
  - Optional seeds to incorporate into the prompt
  - Generate Scenario button
  - Fetch Models button (loads free models from OpenRouter)
  - Cleaned bullet-point output with markdown formatting stripped (bold/italic → plain text, numbered lists → bullets)
- `VERSION` bumped to 1.3 in `AudioOracle.html`. See docs/README for details.

### Changed
- **Removed** "Speak roll math (Fate)" checkbox and roll-math-speak behavior.
- **Roll display** now shows full dice values (`roll-details` line under results), previously only bold text was shown.

### Fixed
- None user-facing.

## [1.2] — Fixes & UI polish

### Added
- **Roll values** — full dice breakdown is now displayed under each result.
- Keyboard shortcut **S** for generating scenes.

### Changed
- Removed the "Speak roll math (Fate)" option; Fate rolls no longer read the arithmetic aloud.
- Footer label updated from v1.1 to v1.2.

### Fixed
- (none beyond polish)

## [1.1] — Phase C: Polish & Docs

### Added
- **First-run help panel** (collapsible) explaining modes, weight syntax, and shortcuts.
- **Keyboard shortcuts**: `Space` toggles rolling; `R` performs a single manual roll.
- **Version label** in the footer.
- **Wake lock re-acquisition** on `visibilitychange → visible` while rolling.
- `README.md` fully rewritten for v1.1.
- `CHANGELOG.md`.

### Changed
- **Roll interval** is now a self-correcting `setTimeout` chain anchored to a stable start time. Background-tab throttling no longer accumulates drift.
- Wake lock acquisition is idempotent (`requestWakeLock` no-ops if already held).

### Fixed
- None user-facing. Foundation laid for future work.

### Deferred (not in this release)
- Shuffle bag mode
- Phrase presets
- Random Event on doubles (Fate)
- Event Focus table
- Mid-/Low-Chaos modifier variants
- Prepared-Adventure Event Focus

## [1.0] — Phase B: Mythic Integration

### Added
- **Mode selector**: Standard / Mythic Fate / Mythic Meaning.
- **Mythic Fate Check** — 2d10 + odds modifier + chaos modifier; answer bands per Mythic 2e p.10. Optional "Speak roll math".
- **Mythic Meaning mode** — rolls one Action pair; optional Descriptor pair.
- **Append meaning words** — adds an Action pair to Standard or Fate rolls.
- **Include descriptors** — adds Descriptor pairs to any meaning output.
- Full transcription of four 100-entry Mythic tables (Action 1/2, Descriptor 1/2) with `console.assert` length checks.
- History entries now preserve meaning words and Fate math for replay.

### Changed
- Settings v2 schema extended in place (no bump) to include `mode`, `odds`, `chaos`, `appendMeaning`, `rollDescriptors`, `speakDetails`.

## [0.5] — Phase A: Core Upgrade

### Added
- **Weighted phrase syntax** — `[3] yes`, fractions, `[0]` disabled.
- **Voice selector** and **rate / pitch sliders**.
- **Mute** toggle.
- **Roll history** (last 10, timestamped, click to re-speak, explicit Clear).
- **Settings v2 schema** with one-time v1 migration.

### Changed
- Full refactor: pure `parsePhrases` / `weightedPick` / `doRoll` pipeline.
- Single `state` object.
- Phrase-list hint line under the textarea (total weight + top phrase percentage).

### Fixed
- Rapid consecutive rolls no longer queue stale utterances (`speechSynthesis.cancel` before each speak).

## [0.1] — Original

- Single HTML file, phrase list, adjustable delay, optional timer, mute, screen wake lock (basic).
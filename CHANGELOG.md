# Changelog

All notable changes to Audio Oracle.

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
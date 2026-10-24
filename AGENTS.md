# Audio Oracle — Agent Guidance

## Project Overview

Audio Oracle is a single-file (`AudioOracle.html`) web-based tool for solo role-playing: randomized phrase draws, Mythic Fate checks, Mythic Meaning word pairs, and an OpenRouter scene generator.

Key facts:
- **Version constant**: `const VERSION = 'X.Y'` in `AudioOracle.html` (line ~503)
- **Footer label**: `Audio Oracle vX.Y` in the `.kbd-hint` element near the end of `<main>`
- **Source of truth**: `AudioOracle.html` drives everything; `README.md` and `CHANGELOG.md` must mirror it.

---

## Versioning

Use [Semantic Versioning](https://semver.org/)-style `MAJOR.MINOR.PATCH`:

- `MAJOR` — breaking UI / feature changes
- `MINOR` — new features (e.g. new mode, Scene Generator)
- `PATCH` — fixes, polish, docs-only

Where to bump the version (all three must stay in sync):

1. **`AudioOracle.html`** — update `const VERSION = 'X.Y';` (near top of `<script>`)
2. **`AudioOracle.html`** — update the footer label `Audio Oracle vX.Y` (near `.kbd-hint`)
3. **`README.md`** — update `**Version: X.Y**` at the top

Commit message convention:

```
feat: ...   # minor / feature bump
fix: ...    # patch / bug fix
```

---

## Changelog Workflow (CHANGELOG.md)

Follow the existing `Keep a Changelog` style already present in `CHANGELOG.md`. For every user-facing change:

1. Add a new release section at the top (after the All notable changes header).
2. Use the version being released (e.g. `## [1.4] — Short phase name`).
3. Categorize entries under:
   - `### Added` — new features
   - `### Changed` — changes to existing behavior
   - `### Fixed` — bug fixes
   - `### Deferred` — features not in this release (optional)
4. Keep entries concise and describe *what changed for the user*, not internal implementation details unless they matter to users.
5. Do not edit historical release sections.

Example template:

```
## [X.Y] — Phase name

### Added
- **Feature** — one sentence describing user impact.

### Changed
- **Behavior** — one sentence describing user impact.

### Fixed
- **Issue** — one sentence describing user impact.
```

---

## README Workflow (README.md)

Whenever a feature is added, removed, or behavior changes, update `README.md` to match:

1. **Header**: keep `**Version: X.Y**` in sync with `AudioOracle.html`.
2. **Features list**: add/remove bullet points for new/removed major features.
3. **How to Use**: add numbered steps or mode instructions if UI/behavior changed.
4. **Syntax / scene generator sections**: add new subsections for new features (e.g. weighted phrase syntax, Scene Generator).
5. Remove instructions for features that were removed (e.g. "Speak roll math").

README should read as the user-facing manual for the *current* version.

---

## Definition of Done for any fix/enhancement

- [ ] `AudioOracle.html` version constant updated
- [ ] `AudioOracle.html` footer label updated
- [ ] `README.md` version, features, and usage sections updated
- [ ] `CHANGELOG.md` new release section added at top
- [ ] All three files changed in the same commit as the code change

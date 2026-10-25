# Audio Oracle

**Version: 1.6**

A simple, single-file, web-based tool that speaks randomized prompts aloud for solo role-playing. Perfect for bedtime play, walks, or waiting in line — start it, close your eyes, and listen.

## Features

- **Three modes**
  - **Standard** — draws a phrase from your list.
  - **Mythic Fate** — rolls the Mythic Game Master Emulator 2e Fate Check (2d10 + odds modifier + chaos modifier).
  - **Mythic Meaning** — rolls Action word pairs (and optionally Descriptor pairs) for inspiration.
- **Scene Generator** — generate TTRPG scenarios via OpenRouter API, with a fully editable prompt.
- **Tome of Adventure Design seeds** — roll concrete scene seeds (place, who, mission, hook, complication, flavor) from 30 curated *Tome of Adventure Design* tables. Includes a local **Sketch (no API)** mode that builds a bullet scenario without any network call.
- **Weighted phrases** — `[3] yes` makes "yes" three times as likely. Fractions and `[0]` (disabled) supported. Fully backward compatible with unweighted lists.
- **Append meaning words** — in Standard or Fate mode, add a Mythic Action pair to every roll.
- **Roll history** — last 10 results, timestamped. Click to re-speak.
- **Voice controls** — pick a voice, adjust rate and pitch. Mute while keeping the display live.
- **Keyboard shortcuts** — `Space` start/stop, `R` roll once
- **Customizable interval and optional timer.**
- **Screen wake lock** — keeps the screen on during sessions, and re-acquires after tab switches.
- **Settings persistence** — phrases, mode, odds, chaos, voice, rate, pitch, mute, history, and more are saved locally.

## How to Use

1. Save the provided HTML as `AudioOracle.html` and open it in a modern browser.
2. To use the Scene Generator, enter your OpenRouter API key, optionally provide seed ideas, and optionally edit the full prompt under *Edit full prompt (advanced)*. You can also open **Tome of Adventure Design seeds**, pick categories, and click **Roll Seeds**; **Sketch (no API)** turns the seeds into a local bullet scenario without generating.
3. Pick a mode.
   - **Standard**: edit the phrase list. Optional weighted syntax `[3] yes`.
   - **Mythic Fate**: set Odds (Certain … Impossible) and Chaos Factor (1–9).
   - **Mythic Meaning**: rolls an Action pair. Enable "Include descriptors" for two more words.
4. Set Delay (seconds) and optional Stop timer (minutes).
5. Press **Start Rolling**, or hit `Space`.
6. Press **Stop Rolling** or `Space` again to stop.

### Weighted phrase syntax

- `[3] yes` — "yes" is 3× as likely.
- `maybe` — unweighted lines count as weight 1.
- `[0.5] perhaps` — fractions allowed.
- `[0] never` — weight 0 = kept in list but never drawn.
- Malformed lines (e.g. `[abc] foo`) are treated as literal text at weight 1.

### Scene Generator

- **API Key** — enter your OpenRouter API key (password-protected).
- **Model** — select a model or type one manually (e.g. `meta-llama/llama-3.1-8b-instruct:free`).
- **Seeds** — optional seeds or ideas (one per line) to incorporate into the scenario.
- **Generate Scenario** — click to generate a bullet-point TTRPG opening scenario using OpenRouter models.
- **Fetch Models** — load a list of free models from OpenRouter.
- **OpenRouter** — requires an OpenRouter account (free tier has many free models available).

#### Tome of Adventure Design seeds

Open **Tome of Adventure Design seeds** inside the Scene Generator to roll concrete inspiration from a curated set of tables:

- **Adventure type** — aerial, castles and ruins, cities, planar, underwater, waterborne, wilderness.
- **Place** — a full location name (e.g. *Crystalline Craters of the Dinosaur-Crawler*), a city district, or a location feature.
- **Who** — a patron or target plus a motivation and object.
- **Mission** — an individual-, item-, location-, or event-based mission.
- **Hook** — what might motivate the players, plus how they learn about the opportunity.
- **Complication** — a villainous plan, danger, strange thing, hint, warning, rumour, faction war, or threat.
- **Flavor** — a sound, dungeon dressing, lighting, corpse, small item, location detail, or business.

**Roll Seeds** replaces the Seeds field with the rolled lines. Edit them freely, then click **Generate Scenario** to feed them to the model. **Sketch (no API)** composes a local bullet scenario from the current seeds (or rolls fresh ones) without calling OpenRouter, so the table tools work completely offline.

The 30 curated tables are embedded in `AudioOracle.html`; no table data is fetched at runtime. The seed roller is opt-in and its categories are saved with your other settings.

The table data is derived from *Tome of Adventure Design* by Matt Finch (Frog God Games). It is included here as a local play aid; check the publisher's terms before redistributing this file or the table data. To regenerate the embedded subset from `tome_parser`'s JSON exports, run `python3 tools/build_tome_tables.py --data ../tome_parser/data`.

#### Editing the prompt

Open **Edit full prompt (advanced)** to see and change the exact text sent to the model:

- Everything above the `===USER PROMPT===` line is the **system prompt**.
- Everything below it is the **user message**.
- `{{seeds}}` is replaced with the contents of the Seeds field. Put it anywhere you like; if you omit it, the seeds are added to the top of the user message automatically.
- **Reset prompt to default** restores the original prompt.
- Your edited prompt is saved locally with the rest of your settings, so you only need to write it once. If you leave the prompt at its default, future versions can improve it for you.

The default prompt puts the output-format rules in the system message only; the user message just asks for the scene, so the two halves do not repeat each other. It asks for concise, imaginative, atmospheric scenarios that stay simple and open-ended.

Example: to make the generator produce a single paragraph without bullets, replace the user message with something like `Write one paragraph starting in media res using these seeds: {{seeds}}`.

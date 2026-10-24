# Audio Oracle

**Version: 1.5.1**

A simple, single-file, web-based tool that speaks randomized prompts aloud for solo role-playing. Perfect for bedtime play, walks, or waiting in line — start it, close your eyes, and listen.

## Features

- **Three modes**
  - **Standard** — draws a phrase from your list.
  - **Mythic Fate** — rolls the Mythic Game Master Emulator 2e Fate Check (2d10 + odds modifier + chaos modifier).
  - **Mythic Meaning** — rolls Action word pairs (and optionally Descriptor pairs) for inspiration.
- **Scene Generator** — generate TTRPG scenarios via OpenRouter API, with a fully editable prompt.
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
2. To use the Scene Generator, enter your OpenRouter API key, optionally provide seed ideas, and optionally edit the full prompt under *Edit full prompt (advanced)*.
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

#### Editing the prompt

Open **Edit full prompt (advanced)** to see and change the exact text sent to the model:

- Everything above the `===USER PROMPT===` line is the **system prompt**.
- Everything below it is the **user message**.
- `{{seeds}}` is replaced with the contents of the Seeds field. Put it anywhere you like; if you omit it, the seeds are added to the top of the user message automatically.
- **Reset prompt to default** restores the original prompt.
- Your edited prompt is saved locally with the rest of your settings, so you only need to write it once. If you leave the prompt at its default, future versions can improve it for you.

The default prompt puts the output-format rules in the system message only; the user message just asks for the scene, so the two halves do not repeat each other.

Example: to make the generator produce a single paragraph without bullets, replace the user message with something like `Write one paragraph starting in media res using these seeds: {{seeds}}`.

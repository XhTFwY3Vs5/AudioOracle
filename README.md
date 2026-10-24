# Audio Oracle

**Version: 1.1**

A simple, single-file, web-based tool that speaks randomized prompts aloud for solo role-playing. Perfect for bedtime play, walks, or waiting in line — start it, close your eyes, and listen.

## Features

- **Three modes**
  - **Standard** — draws a phrase from your list.
  - **Mythic Fate** — rolls the Mythic Game Master Emulator 2e Fate Check (2d10 + odds modifier + chaos modifier).
  - **Mythic Meaning** — rolls Action word pairs (and optionally Descriptor pairs) for inspiration.
- **Weighted phrases** — `[3] yes` makes "yes" three times as likely. Fractions and `[0]` (disabled) supported. Fully backward compatible with unweighted lists.
- **Append meaning words** — in Standard or Fate mode, add a Mythic Action pair to every roll.
- **Roll history** — last 10 results, timestamped. Click to re-speak.
- **Voice controls** — pick a voice, adjust rate and pitch. Mute while keeping the display live.
- **Keyboard shortcuts** — `Space` start/stop, `R` roll once.
- **Customizable interval and optional timer.**
- **Screen wake lock** — keeps the screen on during sessions, and re-acquires after tab switches.
- **Settings persistence** — phrases, mode, odds, chaos, voice, rate, pitch, mute, history, and more are saved locally.

## How to Use

1. Save the provided HTML as `AudioOracle.html` and open it in a modern browser.
2. Pick a mode.
   - **Standard**: edit the phrase list. Optional weighted syntax `[3] yes`.
   - **Mythic Fate**: set Odds (Certain … Impossible) and Chaos Factor (1–9). Optional "Speak roll math" reads the arithmetic aloud.
   - **Mythic Meaning**: rolls an Action pair. Enable "Include descriptors" for two more words.
3. Set Delay (seconds) and optional Stop timer (minutes).
4. Press **Start Rolling**, or hit `Space`.
5. Press **Stop Rolling** or `Space` again to stop.

### Weighted phrase syntax

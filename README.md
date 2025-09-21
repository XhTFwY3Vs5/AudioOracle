# Audio Oracle

The Audio Oracle is a simple, web-based tool designed to assist solo role-playing game (RPG) players by providing randomized prompts and answers through spoken word. It's perfect for generating quick decisions, plot hooks, or character reactions when you don't have a GM or dice handy.

## Features

*   **Customizable Phrases:** Input your own list of phrases, one per line, to tailor the oracle to your specific game or needs. The default list provides a classic "yes/no" style oracle.
*   **Adjustable Delay:** Set the time interval (in seconds) between each "roll" of the oracle.
*   **Optional Timer:** Configure a timer (in minutes) to automatically stop the oracle after a set duration.
*   **Speech Synthesis:** The selected phrase is spoken aloud using your browser's built-in text-to-speech capabilities.
*   **Persistence:** Your custom phrases, interval, and timer settings are saved in your browser's local storage, so they'll be there the next time you visit.
*   **Screen Wake Lock:** The tool attempts to keep your screen awake while it's running, preventing your device from sleeping during a session.

## How to Use

1.  **Open the Page:** Save the provided HTML code as an `.html` file (e.g., `audio_oracle.html`) and open it in your web browser.
2.  **Customize Phrases:** In the "Enter phrases (one per line):" text area, replace the default phrases with your own. For example, you could enter:
    *   A helpful NPC
    *   A dangerous trap
    *   A new clue
    *   An unexpected delay
    *   A surprising ally
3.  **Set Delay:** Adjust the "Delay between rolls (seconds):" input to your desired interval. A shorter delay provides quicker responses, while a longer one allows for more contemplation.
4.  **Set Timer (Optional):** If you want the oracle to stop automatically, enter the desired duration in "Stop after (minutes, 0 for unlimited):".
5.  **Start Rolling:** Click the "Start Rolling" button. The oracle will immediately select and speak a phrase, and then continue to do so at your set interval.
6.  **Stop Rolling:** Click the "Stop Rolling" button to halt the oracle.

## Technical Details

This tool is a single HTML file that uses JavaScript for its functionality. It leverages:

*   **`Math.random()`:** For generating random numbers to select phrases.
*   **`setInterval()` and `clearInterval()`:** For managing the rolling delay and the optional timer.
*   **`SpeechSynthesisUtterance` and `speechSynthesis.speak()`:** For text-to-speech output.
*   **`localStorage`:** For persisting user settings.
*   **`navigator.wakeLock.request('screen')`:** For attempting to keep the screen awake.

## Contributing

This is a simple, self-contained tool. Contributions are welcome in the form of:

*   **Bug reports:** If you find any issues.
*   **Feature requests:** If you have ideas for improvements.
*   **Pull requests:** For code enhancements or bug fixes.

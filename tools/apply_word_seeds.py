import json
from pathlib import Path

def main():
    # Read words.txt
    words_path = Path("words.txt")
    if not words_path.exists():
        print("Error: words.txt not found.")
        return
    words = [line.strip().lower() for line in words_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    print(f"Loaded {len(words)} words from words.txt")

    # Read AudioOracle.html
    html_path = Path("AudioOracle.html")
    content = html_path.read_text(encoding="utf-8")

    # 1. Update version constant from 1.12.1 to 1.13.0
    content = content.replace("const VERSION = '1.12.1';", "const VERSION = '1.13.0';")
    content = content.replace("Audio Oracle v1.12.1", "Audio Oracle v1.13.0")

    # 2. Add Word Seed Generator UI right after Tome of Adventure Design seeds details
    tome_details_end = """            </details>"""
    
    word_seed_ui = """            <details class="tome-seeds" style="margin-top: 8px;">
                <summary>Word Seed Generator (from <code>words.txt</code>)</summary>
                <div class="scene-prompt-hint">
                    Pick random thematic keywords from <code>words.txt</code> (fantasy, sci-fi, horror). Choose how many words (X) to draw. Replaces the seeds field; edit freely afterwards.
                </div>
                <div class="form-group" style="margin-top: 8px; margin-bottom: 8px;">
                    <label for="word-seed-count">Number of words (X):</label>
                    <input type="number" id="word-seed-count" value="5" min="1" max="50" style="width: 80px; padding: 4px 8px;">
                </div>
                <div class="scene-actions" style="margin-top: 8px; flex-wrap: wrap;">
                    <button type="button" class="secondary" id="word-seed-roll">Pick Word Seeds</button>
                </div>
                <div class="scene-prompt-hint" style="margin-top: 6px;">
                    Curated vocabulary subset from <em>dwyl/english-words</em>.
                </div>
            </details>"""

    # We want to insert word_seed_ui right after the first occurrence of <details class="tome-seeds" style="margin-top: 8px;"> ... </details>
    # Let's find the Tome seeds details block and insert after it.
    tome_marker = "Tables from <em>Tome of Adventure Design</em> by Matt Finch (Frog God Games)."
    if tome_marker in content:
        parts = content.split(tome_marker, 1)
        # Find the closing </details> after tome_marker
        sub_parts = parts[1].split("</details>", 1)
        content = parts[0] + tome_marker + sub_parts[0] + "</details>\n\n" + word_seed_ui + sub_parts[1]
    else:
        print("Warning: Tome marker not found in AudioOracle.html")

    # 3. Add els properties
    els_marker = "sceneSeeds:     $('scene-seeds'),"
    els_addition = """        wordSeedCount: $('word-seed-count'),
        wordSeedRoll: $('word-seed-roll'),"""
    if els_marker in content:
        content = content.replace(els_marker, els_marker + "\n" + els_addition)
    else:
        print("Warning: els.sceneSeeds marker not found.")

    # 4. Add state property
    state_marker = "sceneSeeds: '',"
    state_addition = """        wordSeedCount: 5,"""
    if state_marker in content:
        content = content.replace(state_marker, state_marker + "\n" + state_addition)
    else:
        print("Warning: state.sceneSeeds marker not found.")

    # 5. Add loadSettings parsing
    load_marker = "state.sceneSeeds  = typeof raw.sceneSeeds === 'string' ? raw.sceneSeeds : '';"
    load_addition = "state.wordSeedCount = clampInt(numOr(raw.wordSeedCount, 5), 1, 100);"
    if load_marker in content:
        content = content.replace(load_marker, load_marker + "\n        " + load_addition)
    else:
        print("Warning: loadSettings sceneSeeds marker not found.")

    # 6. Add saveSettings blob property
    save_marker = "sceneSeeds:  state.sceneSeeds,"
    save_addition = "wordSeedCount: state.wordSeedCount,"
    if save_marker in content:
        content = content.replace(save_marker, save_marker + "\n            " + save_addition)
    else:
        print("Warning: saveSettings sceneSeeds marker not found.")

    # 7. Add stateToForm and syncFormToState updates
    # stateToForm: add els.sceneSeeds.value = state.sceneSeeds; -> add wordSeedCount assignment
    form_get_marker = "state.sceneSeeds  = els.sceneSeeds.value;"
    form_get_addition = "state.wordSeedCount = parseInt(els.wordSeedCount?.value, 10) || 5;"
    if form_get_marker in content:
        content = content.replace(form_get_marker, form_get_marker + "\n        " + form_get_addition)

    form_set_marker = "els.sceneSeeds.value  = state.sceneSeeds;"
    form_set_addition = "if (els.wordSeedCount) els.wordSeedCount.value = state.wordSeedCount;"
    if form_set_marker in content:
        content = content.replace(form_set_marker, form_set_marker + "\n        " + form_set_addition)

    # 8. Add WORD_POOL and word seed functions
    tome_rollers_marker = "const TOME_ROLLERS = {"
    word_functions = f"""const WORD_POOL = {json.dumps(words)};

    function rollWordSeeds(count) {{
        if (!WORD_POOL || !WORD_POOL.length) return [];
        const n = Math.max(1, Math.min(100, parseInt(count, 10) || 5));
        const pool = [...WORD_POOL];
        const picked = [];
        for (let i = 0; i < n && pool.length > 0; i++) {{
            const index = Math.floor(Math.random() * pool.length);
            picked.push(pool.splice(index, 1)[0]);
        }}
        return picked;
    }}

    function rollWordSeedsIntoField() {{
        const count = els.wordSeedCount ? els.wordSeedCount.value : (state.wordSeedCount || 5);
        const words = rollWordSeeds(count);
        if (!words.length) {{
            setSceneStatus('Word pool is empty.', 'error');
            return;
        }}
        els.sceneSeeds.value = words.join(', ');
        state.sceneSeeds = els.sceneSeeds.value;
        syncSceneClearButtons();
        saveSettings();
        setSceneStatus(`Picked ${{words.length}} word seed${{words.length === 1 ? '' : 's'}}. Review them, then Generate.`, 'success');
    }}

    """
    if tome_rollers_marker in content:
        content = content.replace(tome_rollers_marker, word_functions + tome_rollers_marker)
    else:
        print("Warning: TOME_ROLLERS marker not found.")

    # 9. Add event wiring in wireEvents
    wire_marker = "els.tomeRollSeeds.addEventListener('click', rollTomeSeedsIntoField);"
    wire_addition = """els.wordSeedRoll.addEventListener('click', rollWordSeedsIntoField);
        els.wordSeedCount.addEventListener('change', scheduleSave);
        els.wordSeedCount.addEventListener('input', scheduleSave);"""
    if wire_marker in content:
        content = content.replace(wire_marker, wire_marker + "\n        " + wire_addition)
    else:
        print("Warning: tomeRollSeeds event wiring marker not found.")

    html_path.write_text(content, encoding="utf-8")
    print("Successfully updated AudioOracle.html with Word Seed Generator.")

if __name__ == "__main__":
    main()

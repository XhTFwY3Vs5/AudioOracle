#!/usr/bin/env python3
"""
Generate a refined words.txt subset of high-impact words helpful for fantasy,
sci-fi, and horror write keyword prompts from dwyl/english-words (words_alpha.txt).
"""

import urllib.request
from pathlib import Path

URL = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"

# Core thematic root words, terms, and categories for Fantasy, Sci-Fi, Horror
THEME_ROOTS = [
    # Fantasy / Medieval / Mythic
    "magic", "mage", "wizard", "sorcerer", "witch", "warlock", "spell", "potion", "scroll",
    "tome", "staff", "wand", "rune", "crystal", "gem", "jewel", "gold", "silver", "bronze", "iron",
    "steel", "mithril", "sword", "blade", "dagger", "spear", "axe", "bow", "arrow", "shield", "armor",
    "helm", "cloak", "crown", "throne", "king", "queen", "prince", "princess", "lord", "lady", "knight",
    "paladin", "cleric", "druid", "ranger", "rogue", "thief", "assassin", "bard", "monk", "priest",
    "temple", "altar", "shrine", "crypt", "tomb", "grave", "ghost", "specter", "wraith", "ghoul",
    "zombie", "vampire", "werewolf", "hag", "coven", "beast", "monster", "dragon", "wyrm", "demon",
    "devil", "imp", "fiend", "god", "titan", "myth", "legend", "prophecy", "omen", "fate", "destiny",
    "curse", "hex", "amulet", "talisman", "relic", "artifact", "ruin", "citadel", "fortress", "castle",
    "dungeon", "tower", "keep", "realm", "kingdom", "empire", "domain", "forest", "woods", "grove",
    "swamp", "marsh", "bog", "mire", "mountain", "peak", "cliff", "cave", "cavern", "abyss", "chasm",
    "void", "storm", "thunder", "frost", "ice", "fire", "flame", "ash", "ember", "smoke", "shadow",
    "dark", "night", "moon", "star", "sun", "eclipse", "dawn", "dusk", "twilight", "soul", "spirit",
    "phantom", "vision", "dream", "nightmare", "sleep", "death", "blood", "bone", "skull", "flesh",
    "heart", "mind", "breath", "whisper", "echo", "scream", "howl", "silence", "secret", "ancient",
    "mystic", "ethereal", "astral", "celestial", "infernal", "abyssal", "primal", "primeval", "savage",
    "feral", "monstrous", "grotesque", "macabre", "eerie", "sinister", "grim", "gloomy", "shrouded",
    "veiled", "cloaked", "hooded", "radiant", "glowing", "flickering", "burning", "blazing", "freezing",
    "icy", "cold", "damp", "bloody", "skeletal", "rotting", "decaying", "putrid", "foul", "tainted",
    "corrupted", "cursed", "doomed", "fated", "blighted", "withered",

    # Sci-Fi / Space / Cyberpunk
    "star", "stellar", "space", "cosmos", "universe", "vacuum", "orbit", "trajectory", "velocity",
    "warp", "hyperdrive", "lightspeed", "quantum", "atomic", "nuclear", "fusion", "fission", "plasma",
    "laser", "photon", "tachyon", "electron", "proton", "neutron", "atom", "molecule", "element",
    "compound", "metal", "alloy", "titanium", "carbon", "silicon", "polymer", "plastic", "synthetic",
    "artificial", "digital", "cyber", "electronic", "electric", "magnetic", "gravitational", "kinetic",
    "thermal", "optical", "acoustic", "sonic", "supersonic", "sublight", "jump", "gate", "portal",
    "wormhole", "singularity", "horizon", "dilation", "relativity", "entropy", "chaos", "matrix",
    "grid", "network", "system", "mainframe", "server", "terminal", "console", "interface", "hologram",
    "display", "monitor", "screen", "sensor", "scanner", "radar", "sonar", "transceiver", "transmitter",
    "receiver", "antenna", "satellite", "probe", "drone", "robot", "android", "cyborg", "automaton",
    "mech", "exoskeleton", "spacesuit", "helmet", "visor", "respirator", "rebreather", "tank", "hull",
    "bulkhead", "airlock", "deck", "bridge", "cockpit", "engine", "reactor", "core", "generator",
    "battery", "cell", "capacitor", "relay", "circuit", "chip", "processor", "memory", "storage",
    "drive", "disk", "frequency", "channel", "signal", "transmission", "broadcast", "communication",
    "message", "data", "file", "record", "code", "encryption", "decryption", "password", "token",
    "protocol", "algorithm", "software", "hardware", "firmware", "neural", "synapse", "brain",
    "consciousness", "bio", "organic", "clone", "mutation", "mutant", "alien", "xenomorph", "insectoid",
    "reptilian", "humanoid", "sentient", "sapient", "species", "civilization", "federation", "alliance",
    "confederation", "republic", "syndicate", "corporation", "colony", "outpost", "station", "facility",
    "laboratory", "complex", "dome", "metropolis", "arcology", "starship", "vessel", "cruiser",
    "destroyer", "frigate", "dreadnought", "carrier", "transport", "freighter", "shuttle", "escape",
    "lifeboat", "fighter", "interceptor", "bomber", "scout", "explorer", "survey", "science", "mining",
    "derelict", "wreck", "debris", "scrap", "salvage", "smuggling", "contraband", "bounty", "hunter",
    "mercenary", "pilot", "captain", "navigator", "engineer", "technician", "scientist", "researcher",
    "medic", "commander", "admiral", "passenger", "colonist", "pioneer", "settler", "nomad", "scavenger",
    "vagrant", "hacker", "netrunner", "cyberpunk", "tech", "genius", "mastermind", "visionary", "rebel",
    "insurgent", "guerrilla", "terrorist", "resistance", "partisan", "marine", "trooper", "commando",
    "sniper", "interstellar", "extrasolar", "cryogenic", "cybernetic", "bionic", "automated", "robotic",
    "mechanized", "computerized", "virtual", "holographic", "subatomic", "molecular", "genetic",
    "engineered", "infected", "toxic", "radioactive", "corrosive", "explosive", "volatile", "unstable",
    "reactive", "tactical", "strategic", "stealth", "armored", "reinforced", "autonomous", "intelligent",
    "rational", "logical", "calculating", "ruthless", "relentless", "tireless", "immortal", "boundless",
    "microscopic", "transparent", "reflective", "luminous", "neon", "fluorescent", "pulsing", "humming",
    "whirring", "clicking", "buzzing", "ticking", "beeping", "flashing", "blinking", "scanning",
    "tracking", "targeting", "locking", "firing", "launching", "breaching", "hacking", "overriding",
    "decrypting", "encrypting", "downloading", "uploading", "streaming", "broadcasting", "transmitting",
    "receiving", "connecting", "linking", "merging", "fusing", "assimilating", "transforming", "evolving",
    "adapting", "surviving", "conquering", "dominating", "annihilating", "eradicating", "consuming",
    "devouring", "harvesting", "extracting", "refining", "processing", "manufacturing", "assembling",
    "constructing", "engineering", "designing", "programming", "coding", "calculating", "computing",
    "analyzing", "observing", "monitoring", "patrolling", "guarding", "defending", "protecting",
    "securing", "sealing", "venting", "purging", "sanitizing", "sterilizing", "decontaminating",
    "disinfecting", "recycling", "bartering", "negotiating", "signaling", "beacon", "warning", "alert",
    "alarm", "siren", "emergency", "crisis", "hazard", "vulnerability", "weakness", "glitch", "bug",
    "failure", "crash", "explosion", "meltdown", "leak", "spill", "contamination", "infection", "plague",
    "virus", "parasite", "pathogen", "toxin", "poison", "venom", "acid", "radiation", "fallout",
    "wasteland", "rust", "corrosion", "entropy", "solitude", "isolation", "alienation", "anomaly",
    "enigma", "uncharted", "unexplored", "unmapped", "weightless", "drifting", "migrating", "imploding",
    "collapsing", "dissolving", "evaporating", "sublimating", "vaporizing", "disintegrating", "dematerializing",
    "materializing", "phasing", "shifting", "warping", "bending", "twisting", "folding", "stretching",
    "contracting", "throbbing", "revolving", "traversing", "crossing", "bridging", "separating",
    "dividing", "splitting", "shattering", "fracturing", "fragmenting", "crumbling", "decomposing",
    "spoiling", "tarnishing", "weathering", "eroding", "carving", "shaping", "molding", "forming",
    "forging", "erecting", "hoisting", "gliding", "hovering", "swooping", "banking", "accelerating",
    "decelerating", "halting", "lurking", "spotting", "detecting", "sensing", "grasping", "gripping",
    "throwing", "striking", "hitting", "crushing", "grinding", "tearing", "ripping", "shredding",
    "slashing", "slicing", "chopping", "hewing", "puncturing", "penetrating", "invading", "occupying",
    "subduing", "enslaving", "capturing", "detaining", "imprisoning", "binding", "shackling", "chaining",
    "trapping", "ensnaring", "cornering", "surrounding", "besieging", "assaulting", "ambushing", "raiding",
    "pillaging", "plundering", "looting", "sacking", "demolishing", "flattening", "leveling", "obliterating",
    "wiping", "erasing", "deleting", "removing", "gathering", "collecting", "hoarding", "storing",
    "concealing", "masking", "disguising", "camouflaging", "blending", "fading", "vanishing", "escaping",
    "fleeing", "sprinting", "dashing", "rushing", "charging", "advancing", "retreating", "withdrawing",
    "evacuating", "abandoning", "departing", "journeying", "voyaging", "migrating", "roaming", "wandering",
    "exploring", "discovering", "uncovering", "unearthing", "revealing", "exposing", "presenting", "offering",
    "trading", "bartering", "selling", "buying", "acquiring", "obtaining", "taking", "seizing", "grabbing",
    "snatching", "stealing", "thieving", "robbing", "poaching", "tracking", "stalking", "pursuing", "chasing",
    "following", "guiding", "directing", "navigating", "piloting", "driving", "steering", "operating",
    "controlling", "managing", "governing", "ruling", "commanding", "ordering", "demanding", "requesting",
    "pleading", "begging", "praying", "worshipping", "adoring", "praising", "blessing", "damning", "hexing",
    "enchanting", "charming", "casting", "conjuring", "summoning", "invoking", "evoking", "banishing",
    "expelling", "exiling", "forcing", "pushing", "pulling", "dragging", "hauling", "towing", "lifting",
    "raising", "carrying", "bearing", "supporting", "sustaining", "maintaining", "protecting", "guarding",
    "shielding", "defending", "rescuing", "delivering", "paralyzing", "immobilizing", "stunning", "dazzling",
    "blinding", "deafening", "silencing", "muting", "quieting", "calming", "soothing", "pacifying",
    "tranquilizing", "sedating", "drugging", "toxifying", "contaminating", "polluting", "corrupting",
    "tainting", "clearing", "cleansing", "purifying", "sanitizing", "sterilizing", "scrubbing", "polishing",
    "flaring", "blazing", "scorching", "searing", "roasting", "baking", "cooking", "boiling", "simmering",
    "heating", "warming", "cooling", "chilling", "frosting", "icing", "hardening", "solidifying",
    "stiffening", "rigidifying", "tightening", "dilating", "swelling", "bloating", "ballooning", "inflating",
    "erupting", "spewing", "vomiting", "bleeding", "oozing", "dripping", "draining", "flowing", "streaming",
    "pouring", "rushing", "gushing", "flooding", "drowning", "sinking", "descending", "declining", "settling",
    "resting", "immobilizing", "washing", "cleaning", "sweeping", "brushing",

    # Horror / Dark / Gothic
    "gore", "flesh", "bone", "skull", "corpse", "cadaver", "carcass", "grave", "tomb", "crypt",
    "mausoleum", "casket", "coffin", "hearse", "death", "dead", "kill", "murder", "slaughter", "massacre",
    "carnage", "butchery", "pain", "agony", "torture", "torment", "suffer", "fear", "terror", "horror",
    "dread", "panic", "fright", "scare", "spooky", "creepy", "sinister", "macabre", "morbid", "grim",
    "shade", "gloom", "midnight", "pit", "chasm", "hell", "inferno", "fiend", "creature", "monstrosity",
    "abomination", "stalker", "killer", "psychopath", "sociopath", "maniac", "lunatic", "madman",
    "insane", "madness", "insanity", "paranoia", "delusion", "hallucination", "specter", "haunt", "haunted",
    "haunting", "poltergeist", "apparition", "witchcraft", "occult", "ritual", "sacrifice", "cult",
    "cultist", "worshipper", "idol", "icon", "taboo", "forbidden", "mystery", "enigma", "unknown",
    "strange", "weird", "bizarre", "unnatural", "abnormal", "deformed", "parasite", "infection", "plague",
    "pestilence", "disease", "sickness", "rot", "decay", "decompose", "decomposition", "stench", "odor",
    "smell", "foul", "putrid", "rancid", "mold", "mildew", "slime", "ooze", "drip", "stain", "smear",
    "splash", "pool", "puddle", "quicksand", "labyrinth", "maze", "tunnel", "cellar", "attic", "basement",
    "abandoned", "derelict", "desolate", "barren", "empty", "hollow", "whisper", "shriek", "groan",
    "moan", "sigh", "gasp", "heartbeat", "pulse", "throb", "twitch", "tremor", "shiver", "shudder",
    "sweat", "chill", "black", "crimson", "scarlet", "pale", "ghostly", "ashen", "skeletal", "emaciated",
    "gaunt", "sunken", "blind", "deaf", "mute", "paralytic", "catatonic", "comatose", "insomnia",
    "nightmare", "awake", "watcher", "gaze", "stare", "pupils", "iris", "glare", "blink", "tear",
    "crying", "weeping", "sob", "grief", "mourning", "sorrow", "despair", "hopelessness", "fatality",
    "catastrophe", "apocalypse", "armageddon", "final", "eternal", "endless", "infinite", "fathomless",
    "elder", "antique", "dusty", "cobweb", "spider", "web", "insect", "creep", "crawl", "slither",
    "writhe", "swarm", "hive", "nest", "den", "lair", "burrow", "hatch", "spawn", "brood", "litter"
]

def main():
    print("Downloading words_alpha.txt...")
    req = urllib.request.urlopen(URL)
    content = req.read().decode("utf-8")
    all_words = content.splitlines()

    theme_set = set(t.lower() for t in THEME_ROOTS)
    
    selected_words = set()
    for w in all_words:
        w = w.strip().lower()
        if not (4 <= len(w) <= 14):
            continue
        if w in theme_set:
            selected_words.add(w)
            continue
        for t in theme_set:
            if len(t) >= 4 and t in w:
                selected_words.add(w)
                break

    sorted_words = sorted(list(selected_words))
    print(f"Refined subset: {len(sorted_words)} words.")

    out_path = Path("words.txt")
    out_path.write_text("\n".join(sorted_words) + "\n", encoding="utf-8")
    print("Successfully created words.txt.")

if __name__ == "__main__":
    main()

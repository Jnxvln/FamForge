import json
from pathlib import Path

# Target output directory
data_dir = Path("src/famforge/data")
data_dir.mkdir(parents=True, exist_ok=True)

# Data dictionaries

names_by_element = {
    "Fire": [
        "Emberel", "Pyrrion", "Caldris", "Emberyn", "Ignelle",
        "Volcaer", "Solvaric", "Fyrannis", "Ashvora", "Cindariel",
        "Vulkess", "Scorchinelle", "Blazethorn", "Emberith", "Ignisar",
        "Karnyx", "Flamareth", "Searin", "Moltra", "Blazul"
    ],
    "Water": [
        "Lirrow", "Aquareth", "Thalorin", "Driswyn", "Nevalis",
        "Nerathis", "Ocevelle", "Brinmar", "Delthera", "Wavethorn", 
        "Myrris", "Corvalune", "Mistara", "Aquith", "Tidewyn", 
        "Glacien", "Pearlis", "Kelphor", "Rainnix", "Selmira"
    ],
    "Earth": [
        "Tharn", "Terrakai", "Bramis", "Umberok", "Tremarin",
        "Gravemoss", "Tharnok", "Ruderalis", "Kaelgrove", "Morbenth", 
        "Stoneel", "Burrowel", "Terralyn", "Felnroot", "Craggor", 
        "Umbrisol", "Siltvyne", "Veinwilt", "Mirethorn", "Groven"
    ],
    "Air": [
        "Aelynn", "Zephrae", "Sylune", "Lunthera", "Aureveil", 
        "Caelistra", "Whisryn", "Aeriven", "Cirraquil", "Galeen", 
        "Windara", "Soareth", "Skywyn", "Tornis", "Siroveil", 
        "Zephyra", "Breezinel", "Cloudelle", "Anemir", "Vayra"
    ],
    "Time": [
        "Silranor", "Tirith", "Chronessa", "Tikelor", "Epochyn", 
        "Momenth", "Kalendrix", "Aevira", "Timasel", "Hourven", 
        "Wyndclock", "Veridane", "Sundryss", "Temphora", "Pendulae", 
        "Aeoneth", "Cyclyra", "Veloras", "Anachros", "Zenthros"
    ],
    "Spirit": [
        "Elossence", "Sylune", "Whismara", "Soulith", "Ephryn", 
        "Hauntelle", "Numael", "Vespiris", "Drevia", "Phantira", 
        "Mournix", "Wailen", "Caelmira", "Serephin", "Umbrith", 
        "Noctelle", "Echoiris", "Phaelys", "Kindross", "Lamenth"
    ],
    "Aether": [
        "Nyxa", "Glacelle", "Aelmora", "Voidelune", "Gravethis", 
        "Astrofel", "Nebulith", "Cosmira", "Velquor", "Nimbrael", 
        "Lucenari", "Eclipsys", "Aetherion", "Zoraphine", "Spacelle", 
        "Dimensar", "Orbyss", "Parallaxa", "Stravon", "Elunex"
    ]
}

species_by_element = {
    "Air": [
        "Mistcat", "Zephyrfin", "Whispraptor", "Driftalon", "Skywhisp", 
        "Gustclaw", "Cloudkin", "Stormbleat", "Aerofox", "Vaporyx"
    ],
    "Water": [
        "Glowlizard", "Rippleback", "Kelpray", "Tideglider", "Brinetooth", 
        "Naiadorn", "Foamscale", "Drenchback", "Coralitch", "Floodmouse"
    ],
    "Earth": [
        "Stonewing", "Mossbeast", "Ashmole", "Rootjaw", "Cragbeast", 
        "Glimmermole", "Thornox", "Stonecurl", "Lichenhorn", "Burrowelk"
    ],
    "Fire": [
        "Emberox", "Flareling", "Cinderdrake", "Scorchkin", "Ignibark", 
        "Blazecrow", "Volcaroo", "Cindertuft", "Sparkvex", "Ashadder"
    ],
    "Time": [
        "Hourmoth", "Chronohound", "Tickwyrm" "Sandwyrm", "Tickgeist", 
        "Clockra", "Hourstag", "Pendulark", "Chronopup", "Temporalin"
    ],
    "Spirit": [
        "Soulfen", "Wispkin", "Umbrawhisper", "Mirthling", "Soulitch", 
        "Hauntelope", "Grimtail", "Phantasmunk", "Whisperray", "Echofox"
    ],
    "Aether": [
        "Nullcat", "Voidbeak", "Gravitine", "Nebuline", "Voidelk", 
        "Starvynx", "Galaxbat", "Orbinox", "Quantowl", "Zerokid"
    ]
}

origins_by_element = {
    "Air": [
        "Emerged from a rift high in the sky.",
        "Spun from wind currents dancing across open plains.",
        "First heard as a whisper echoing through an ancient canyon.",
        "Formed from the last breath of a wind god.",
        "Traced into being by the flight paths of lost birds.",
        "Spun from cloudstuff atop a sleeping giant’s sigh.",
        "Birthed in the eye of a storm that never touches ground.",
        "Scattered together by migrating dreams.",
        "Whistled into form through the reeds of a forgotten flute.",
        "Woven by zephyrs inside an abandoned sky temple."
    ],
    "Water": [
        "Spawned in a deep current beneath still waters.",
        "Found tangled in seaweed beside a shipwreck no one remembers.",
        "Surged forth from a tidal pool under twin moons.",
        "Bubbled up from the deepest trench of a sunken world.",
        "Dripped into form from the tears of a weeping reef.",
        "Flowed out of an ancient spring touched by moonlight.",
        "Condensed from morning mist above sacred waters.",
        "Washed ashore after a dreamlike storm.",
        "Spawned within the eye of a whirlpool that never stops spinning.",
        "Frozen into existence inside a hollow glacier."
    ],
}

# TODO: Add remaining data here

# Write to disk
json_files = {
    "names_by_element.json": names_by_element,
    "species_by_element.json": species_by_element,
    "origins_by_element.json": origins_by_element,
}

for filename, content in json_files.items():
    with open(data_dir / filename, "w", encoding="utf-8") as f:
        json.dump(content, f, indent=4)
        print(f"Wrote {filename}")

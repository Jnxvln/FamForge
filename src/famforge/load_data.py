import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

def load_json(filename):
    with open(DATA_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)

# Load everything once at module import
names_by_element = load_json("names_by_element.json")
species_by_element = load_json("species_by_element.json")
origins_by_element = load_json("origins_by_element.json")
quirks_standard_by_element = load_json("quirks_standard_by_element.json")
quirks_whimsical_by_element = load_json("quirks_whimsical_by_element.json")
abilities_by_element = load_json("abilities_by_element.json")
title_data = load_json("titles_and_clans.json")
epithet_titles = title_data["epithet_titles"]
clan_names = title_data["clan_names"]

# Flattened convenience pools
all_names = [name for names in names_by_element.values() for name in names]
all_species = [sp for sps in species_by_element.values() for sp in sps]
all_origins = [o for olist in origins_by_element.values() for o in olist]
all_quirks_standard = [q for qlist in quirks_standard_by_element.values() for q in qlist]
all_quirks_whimsical = [q for qlist in quirks_whimsical_by_element.values() for q in qlist]
all_abilities = [a for alist in abilities_by_element.values() for a in alist]

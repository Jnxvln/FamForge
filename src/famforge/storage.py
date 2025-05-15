import os
import json
from pathlib import Path

# Path to the user's familiar grimoire
GRIMOIRE_PATH = Path.home() / ".famforge" / "familiars.json"

def ensure_grimoire():
    grimoire_dir = GRIMOIRE_PATH.parent
    grimoire_dir.mkdir(parents=True, exist_ok=True)
    if not GRIMOIRE_PATH.exists():
        with open(GRIMOIRE_PATH, "w") as f:
            json.dump({"familiars": []}, f, indent=2)

def load_familiars():
    ensure_grimoire()
    with open(GRIMOIRE_PATH, "r") as f:
        return json.load(f)["familiars"]

def save_familiar(familiar: dict):
    ensure_grimoire()
    familiars = load_familiars()

    # Check for exact duplicate
    existing = any(
        f["name"] == familiar["name"] and f["karma_seed"] == familiar["karma_seed"]
        for f in familiars
    )
    if not existing:
        familiars.append(familiar)
        with open(GRIMOIRE_PATH, "w") as f:
            json.dump({"familiars": familiars}, f, indent=2)
        return True
    return False

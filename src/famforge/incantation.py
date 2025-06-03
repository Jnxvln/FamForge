import hashlib
import random
from typing import List

# Word banks for incantation construction
ESSENCE_WORDS: List[str] = [
    "veil", "ember", "dusk", "spirit", "aether",
    "dream", "soul", "cinder", "echo", "shadow",
    "whisper", "flare", "frost", "ash"
]

SHAPE_WORDS: List[str] = [
    "loop", "shard", "glyph", "spiral", "sigil",
    "knot", "crescent", "arrow", "spike", "mark"
]

STATE_WORDS: List[str] = [
    "wither", "echo", "bound", "hex", "flicker",
    "drift", "hidden", "pulse", "fracture", "veil"
]

def generate_incantation(karma_seed: str) -> str:
    """
    Generates a deterministic mystical incantation from a karma_seed UUID.

    :param karma_seed: A UUID or seed string for the familiar
    :return: A string incantation in the format 'essence-shape-state'
    """
    h = hashlib.sha256(karma_seed.encode()).hexdigest()
    seed = int(h[:8], 16)
    random.seed(seed)

    essence = random.choice(ESSENCE_WORDS)
    shape = random.choice(SHAPE_WORDS)
    state = random.choice(STATE_WORDS)

    return f"{essence}-{shape}-{state}"

# For manual testing or CLI usage
if __name__ == "__main__":
    example_seed = "84aa90ae-3417-47b5-b4e9-beee20273ba9"
    print("Generated incantation:", generate_passphrase(example_seed))

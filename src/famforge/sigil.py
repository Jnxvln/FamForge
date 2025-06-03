import typer
import hashlib
import random
from pathlib import Path
from typing import List
import json

app = typer.Typer(help="Render the sigil of a familiar", invoke_without_command=True)

GRIMOIRE_PATH = Path.home() / ".famforge" / "familiars.json"

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

def render_binary_sigil(incantation: str, name: str) -> str:
    """
    Renders an ASCII sigil using binary encoding of the incantation.

    :param incantation: The incantation string
    :param name: The familiar's name
    :return: A multiline string representing the sigil
    """
    binary = ''.join(format(ord(c), '08b') for c in incantation)
    width = 18
    height = (len(binary) + width - 1) // width
    padded = binary.ljust(width * height, '0')

    lines = []
    title = f" Sigil of {name} ".center(width * 2 + 2, '═')
    lines.append(f"╔{title}╗")

    for i in range(height):
        row = padded[i * width:(i + 1) * width]
        visual = ''.join('██' if b == '1' else '░░' for b in row)
        lines.append(f"║ {visual} ║")

    lines.append("╚" + "═" * (width * 2 + 2) + "╝")
    return '\n'.join(lines)

@app.callback()
def main(name: str = typer.Argument(..., help="Name of the bonded familiar")):
    """
    Show the ASCII sigil of a bonded familiar based on their incantation.
    """
    if not GRIMOIRE_PATH.exists():
        print("[bold red]No grimoire found.[/bold red]")
        raise typer.Exit()

    with open(GRIMOIRE_PATH, "r") as f:
        data = json.load(f)
        familiars = data.get("familiars", [])

    match = next((f for f in familiars if f.get("name", "").lower() == name.lower()), None)

    if not match:
        print(f"[yellow]No familiar named '{name}' found in your grimoire.[/yellow]")
        raise typer.Exit()

    karma = match.get("karma_seed")
    if not karma:
        print(f"[red]Familiar '{name}' is missing a karma seed.[/red]")
        raise typer.Exit()

    incantation = generate_incantation(karma)
    sigil = render_binary_sigil(incantation, name)

    print()
    print(sigil)

# For manual testing or CLI usage
if __name__ == "__main__":
    example_seed = "84aa90ae-3417-47b5-b4e9-beee20273ba9"
    name = "Veylith"
    incantation = generate_incantation(example_seed)
    print("Generated incantation:", incantation)
    print()
    print(render_binary_sigil(incantation, name))

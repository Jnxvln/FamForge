import typer
import hashlib
import random
from rich import print
from pathlib import Path
from typing import List
import json

app = typer.Typer(help="Reveal hidden truths about your familiars")

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
    h = hashlib.sha256(karma_seed.encode()).hexdigest()
    seed = int(h[:8], 16)
    random.seed(seed)

    essence = random.choice(ESSENCE_WORDS)
    shape = random.choice(SHAPE_WORDS)
    state = random.choice(STATE_WORDS)

    return f"{essence}-{shape}-{state}"

def render_binary_sigil(incantation: str, name: str) -> str:
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

def decode_binary_to_text(binary: str) -> str:
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    text = ''.join(chr(int(c, 2)) for c in chars if len(c) == 8)
    return text

@app.command("sigil")
def reveal_sigil(name: str = typer.Argument(..., help="Name of the bonded familiar")):
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

@app.command("incantation")
def reveal_incantation(
    name: str = typer.Argument(..., help="Name of the bonded familiar"),
    show_bits: bool = typer.Option(False, "--show-bits", help="Also display the binary encoding")
):
    """
    Reveal the encoded incantation for a bonded familiar.
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
    # print(f"[bold cyan]Incantation for {name}:[/bold cyan] [bold yellow]{incantation}[/bold yellow]")
    binary = ''.join(format(ord(c), '08b') for c in incantation)

    print(f"\n[bold cyan]Incantation for {name}:[/bold cyan] [white]{incantation}[/white]")
    if show_bits:
        print(f"[bold cyan]Binary:[/bold cyan] [dim]{binary}[/dim]")
    print()

@app.command("decode")
def decode_binary(binary: str = typer.Argument(..., help="Binary string to decode")):
    """
    Decode a binary string back into text. Used for discovering incantations from sigils.
    """
    try:
        decoded = decode_binary_to_text(binary)
        print(f"\n[bold green]Decoded incantation:[/bold green] [white]{decoded}[/white]\n")
    except Exception as e:
        print(f"[red]Error decoding binary:[/red] {e}")
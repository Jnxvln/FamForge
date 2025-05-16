import json
import typer
from pathlib import Path
from rich import print
from .incantation import generate_incantation

app = typer.Typer(help="Reveal hidden truths about your familiars")

GRIMOIRE_PATH = Path.home() / ".famforge" / "familiars.json"

@app.command("incantation")
def reveal_incantation(name: str = typer.Argument(..., help="Name of the bonded familiar")):
    """
    Reveal the hidden incantation (passphrase) of a bonded familiar.
    """
    if not GRIMOIRE_PATH.exists():
        print("[bold red]No grimoire found. Bond with a familiar first.[/bold red]")
        raise typer.Exit()

    with open(GRIMOIRE_PATH, "r") as f:
        data = json.load(f)
        familiars = data.get("familiars", [])

    familiar = next((f for f in familiars if f.get("name", "").lower() == name.lower()), None)
    if not familiar:
        print(f"[yellow]No familiar named '{name}' found in your grimoire.[/yellow]")
        raise typer.Exit()

    karma_seed = familiar.get("karma_seed")
    if not karma_seed:
        print("[bold red]This familiar has no karma seed.[/bold red]")
        raise typer.Exit()

    incantation = generate_incantation(karma_seed)
    print(f"[bold cyan]Incantation for {name}:[/bold cyan] [italic]{incantation}[/italic]")

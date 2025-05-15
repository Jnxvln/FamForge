import json
import typer
from pathlib import Path
from rich import print
from rich.console import Console

app = typer.Typer()

GRIMOIRE_PATH = Path.home() / ".famforge" / "familiars.json"

ELEMENT_COLORS = {
    "Air": "bright_white",
    "Water": "blue",
    "Earth": "green",
    "Fire": "red",
    "Time": "magenta",
    "Spirit": "cyan",
    "Aether": "purple"
}

@app.command()
def profile(name: str):
    """
    Show the full profile of a bonded familiar by name.
    """
    if not GRIMOIRE_PATH.exists():
        print("[bold red]No grimoire found. Try bonding with a familiar first.[/bold red]")
        raise typer.Exit()

    with open(GRIMOIRE_PATH, "r") as f:
        data = json.load(f)
        familiars = data.get("familiars", [])

    match = next((f for f in familiars if f.get("name", "").lower() == name.lower()), None)

    if not match:
        print(f"[yellow]No familiar named '{name}' found in your grimoire.[/yellow]")
        raise typer.Exit()

    console = Console()
    element = match.get("element", "???")
    element_color = ELEMENT_COLORS.get(element, "white")
    short_karma = match.get("karma_seed", "")[:8] + "…" if match.get("karma_seed") else "—"
    bond_level = str(match.get("bond_level", 1))

    console.print(f"[bold magenta]{match['name']}[/bold magenta] the [cyan]{match['species']}[/cyan] "
                  f"([{element_color}]{element}[/{element_color}], Bond {bond_level}, Karma {short_karma})")

    console.print(f"  • [bold]Origin:[/bold] {match.get('origin', '—')}")
    console.print(f"  • [bold]Gender:[/bold] {match.get('gender', '—')} | [bold]Temperament:[/bold] {match.get('temperament', '—')}")
    
    quirks = match.get("quirks", [])
    if quirks:
        console.print("  • [bold]Quirks:[/bold]")
        for q in quirks:
            console.print(f"    - {q}")

    if match.get("passive_ability"):
        console.print(f"  • [bold]Ability:[/bold] {match['passive_ability']}")

    if match.get("soul_note"):
        console.print(f"  • [bold]Soul Note:[/bold] “{match['soul_note']}”")

    console.print()

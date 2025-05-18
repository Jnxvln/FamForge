import json
from pathlib import Path
import typer
from rich import print
from rich.table import Table
from rich.console import Console
from .incantation import generate_incantation

app = typer.Typer()

GRIMOIRE_PATH = Path.home() / ".famforge" / "familiars.json"

ELEMENT_COLORS = {
    "Air": "white",
    "Water": "blue",
    "Earth": "green",
    "Fire": "red",
    "Time": "magenta",
    "Spirit": "cyan",
    "Aether": "purple"
}

# Shared display name formatting
def format_display_name(f: dict) -> str:
    parts = [f"[bold white]{f.get('name', 'Unknown')}[/bold white]"]
    if f.get("title"):
        parts.append(f" [dim orchid1]{f['title']}[/dim orchid1]")
    if f.get("clan"):
        parts.append(f" [dim cyan]of {f['clan']}[/dim cyan]")
    return "".join(parts)

@app.command("bonded")
def list_bonded(
    details: bool = typer.Option(False, "--details", help="Show full details for each familiar"),
    element: str = typer.Option(None, "--element", help="Filter by element (e.g. Fire)"),
    species: str = typer.Option(None, "--species", help="Filter by species (e.g. Emberox)"),
    name: str = typer.Option(None, "--name", help="Filter by name (e.g. Nyxa)"),
    with_title: bool = typer.Option(False, help="Add a title or clan name to the familiar's name.")
):
    """
    List all bonded familiars from your grimoire.
    """
    if not GRIMOIRE_PATH.exists():
        print("[bold red]No grimoire found. Try bonding with a familiar first.[/bold red]")
        raise typer.Exit()

    with open(GRIMOIRE_PATH, "r") as f:
        data = json.load(f)
        familiars = data.get("familiars", [])

    if not familiars:
        print("[yellow]Your grimoire is empty.[/yellow]")
        return

    # Apply filters
    if element:
        familiars = [f for f in familiars if f.get("element", "").lower() == element.lower()]
    if species:
        familiars = [f for f in familiars if f.get("species", "").lower() == species.lower()]
    if name:
        familiars = [f for f in familiars if name.lower() in f.get("name", "").lower()]

    if not familiars:
        print("[yellow]No familiars matched your filters.[/yellow]")
        return

    console = Console()

    if not details:
        table = Table(title="📜 Bonded Familiars", expand=True)
        table.add_column("Name", style="bold magenta")
        table.add_column("Species", style="cyan")
        table.add_column("Element", style="bold")
        table.add_column("Karma", style="dim")
        table.add_column("Bond", justify="center", style="green")

        for f in familiars:
            display_name = format_display_name(f)
            species = f.get("species", "???")
            element = f.get("element", "???")
            element_color = ELEMENT_COLORS.get(element, "white")
            short_karma = f.get("karma_seed", "")[:8] + "…" if f.get("karma_seed") else "—"
            bond_level = str(f.get("bond_level", 1))

            table.add_row(display_name, species, f"[{element_color}]{element}[/{element_color}]", short_karma, bond_level)

        console.print(table)
    else:
        console.print("[bold cyan]📜 Bonded Familiars (Detailed View)[/bold cyan]\n")
        for f in familiars:
            display_name = format_display_name(f)
            species = f.get("species", "???")
            element = f.get("element", "???")
            element_color = ELEMENT_COLORS.get(element, "white")
            short_karma = f.get("karma_seed", "")[:8] + "…" if f.get("karma_seed") else "—"
            bond_level = str(f.get("bond_level", 1))

            console.print(f"{display_name} the [cyan]{species}[/cyan] ([{element_color}]{element}[/{element_color}], Bond {bond_level}, Karma {short_karma})")

            gender = f.get("gender", "—")
            temperament = f.get("temperament", "—")
            origin = f.get("origin", "")
            ability = f.get("passive_ability", "")
            quirks = f.get("quirks", [])
            soul_note = f.get("soul_note", "")

            console.print(f"  • [bold]Origin:[/bold] {origin}")
            console.print(f"  • [bold]Gender:[/bold] {gender} | [bold]Temperament:[/bold] {temperament}")
            if quirks:
                console.print("  • [bold]Quirks:[/bold]")
                for q in quirks:
                    console.print(f"    - {q}")
            if ability:
                console.print(f"  • [bold]Ability:[/bold] {ability}")
            if soul_note:
                console.print(f"  • [bold]Soul Note:[/bold] “{soul_note}”")

            console.print()

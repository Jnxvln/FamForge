import json
from pathlib import Path
import typer
from rich import print
from rich.console import Console
from difflib import get_close_matches
from .incantation import generate_incantation

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

# Shared display name formatting
def format_display_name(f: dict) -> str:
    parts = [f"[bold white]{f.get('name', 'Unknown')}[/bold white]"]
    if f.get("title"):
        parts.append(f" [dim orchid1]{f['title']}[/dim orchid1]")
    if f.get("clan"):
        parts.append(f" [dim cyan]of {f['clan']}[/dim cyan]")
    return "".join(parts)

@app.command("profile")
def profile(name: str):
    """
    Show the full profile of a bonded familiar by name (fuzzy matching).
    """
    if not GRIMOIRE_PATH.exists():
        print("[bold red]No grimoire found. Try bonding with a familiar first.[/bold red]")
        raise typer.Exit()

    with open(GRIMOIRE_PATH, "r") as f:
        data = json.load(f)
        familiars = data.get("familiars", [])

    def get_display_name_raw(f):
        full = f.get("name", "")
        if f.get("title"):
            full += f" {f['title']}"
        if f.get("clan"):
            full += f" of {f['clan']}"
        return full

    # Get a list of all familiar names (including titles and clans) for fuzzy matching.
    # names_list = [get_display_name_raw(f) for f in familiars]
    # close = get_close_matches(name, names_list, n=1, cutoff=0.5)

    # if not close:
    #     print(f"[yellow]No familiar closely matching '{name}' found in your grimoire.[/yellow]")
    #     raise typer.Exit()

    # match_name = close[0]
    # match = next(f for f in familiars if get_display_name_raw(f) == match_name)
    
    # Try matching against full display names
    names_full = [get_display_name_raw(f) for f in familiars]
    match_full = get_close_matches(name, names_full, n=1, cutoff=0.5)

    # If no match, try matching just the raw name field
    if match_full:
        match_name = match_full[0]
        match = next(f for f in familiars if get_display_name_raw(f) == match_name)
    else:
        names_simple = [f.get("name", "") for f in familiars]
        match_simple = get_close_matches(name, names_simple, n=1, cutoff=0.5)
        if match_simple:
            match = next(f for f in familiars if f.get("name", "") == match_simple[0])
        else:
            print(f"[yellow]No familiar closely matching '{name}' found in your grimoire.[/yellow]")
            raise typer.Exit()


    console = Console()
    element = match.get("element", "???")
    element_color = ELEMENT_COLORS.get(element, "white")
    short_karma = match.get("karma_seed", "")[:8] + "…" if match.get("karma_seed") else "—"
    bond_level = str(match.get("bond_level", 1))

    display_name = format_display_name(match)

    console.print("\n[bold cyan]Familiar Profile[/bold cyan]\n")
    console.print(f"{display_name} the [bold cyan]{match['species']}[/bold cyan] ([{element_color}]{element}[/{element_color}], [green]Bond {bond_level}[/green], Karma [dim]{short_karma}[/dim])")

    console.print(f"  • [bold]Origin:[/bold] [italic]{match.get('origin', '—')}[/italic]")
    console.print(f"  • [bold]Gender:[/bold] {match.get('gender', '—')} | [bold]Temperament:[/bold] {match.get('temperament', '—')}")

    quirks = match.get("quirks", [])
    if quirks:
        console.print("  • [bold]Quirks:[/bold]")
        for q in quirks:
            console.print(f"    - [dim italic]{q}[/dim italic]")

    if match.get("passive_ability"):
        console.print(f"  • [bold]Ability:[/bold] [italic]{match['passive_ability']}[/italic]")

    if match.get("soul_note"):
        console.print(f"  • [bold]Soul Note:[/bold] “[dim]{match['soul_note']}[/dim]”")

    console.print()

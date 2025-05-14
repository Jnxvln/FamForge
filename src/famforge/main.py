import json
import typer
from rich import print
from rich.pretty import Pretty
from .generator import generate_familiar

app = typer.Typer(help="Summon and bond with your magical familiar")

# Optional color mapping for elements
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
def summon(
    lock_element: str = typer.Option(None, help="Lock a specific element (e.g. Fire)"),
    lock_species: str = typer.Option(None, help="Lock a specific species (e.g. Emberox)"),
    lock_temperament: str = typer.Option(None, help="Lock a specific temperament (e.g. Loyal)"),
    lock_size: str = typer.Option(None, help="Lock a specific size (e.g. Medium)"),
    lock_gender: str = typer.Option(None, help="Lock a specific gender (e.g. Nonbinary)"),
    allow_whimsy: bool = typer.Option(False, help="Include humorous or surreal quirks")
):
    """
    Summon a magical familiar. Optionally lock traits or allow whimsical features.
    """
    locked_traits = {
        "element": lock_element,
        "species": lock_species,
        "temperament": lock_temperament,
        "size": lock_size,
        "gender": lock_gender
    }

    try:
        familiar = generate_familiar(locked=locked_traits, allow_whimsy=allow_whimsy)

        element = familiar.element
        color = ELEMENT_COLORS.get(element, "white")

        print("\n[bold cyan]You have summoned...[/bold cyan]\n")
        print(f"[bold yellow]Name:[/bold yellow] {familiar.name}")
        print(f"[bold yellow]Species:[/bold yellow] {familiar.species}")
        print(f"[bold yellow]Element:[/bold yellow] [{color}]{element}[/{color}]")
        print(f"[bold yellow]Size:[/bold yellow] {familiar.size}")
        print(f"[bold yellow]Gender:[/bold yellow] {familiar.gender}")
        print(f"[bold yellow]Temperament:[/bold yellow] {familiar.temperament}")
        print(f"[bold yellow]Origin:[/bold yellow] {familiar.origin}")
        print("[bold yellow]Quirks:[/bold yellow]", *[f"\n  • {q}" for q in familiar.quirks])
        print(f"[bold yellow]Ability:[/bold yellow] {familiar.passive_ability}")
        print(f"[bold yellow]Bond Level:[/bold yellow] {familiar.bond_level}")
        print(f"[bold yellow]Soul Note:[/bold yellow] {familiar.soul_note}")
        print(f"[bold yellow]Karma Seed:[/bold yellow] {familiar.karma_seed}")

    except ValueError as e:
        print(f"\n[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    app()

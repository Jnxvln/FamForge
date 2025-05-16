import json
import typer
from pathlib import Path
from rich import print
from rich.pretty import Pretty
from .generator import generate_familiar
from . import summon, bond, list, show, reveal

__version__ = "0.1.4"

app = typer.Typer(help="FamForge CLI")

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

def show_version(value: bool):
    if value:
        print(f"FamForge v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        help="Show the version and exit.",
        callback=show_version,
        is_eager=True
    )
):
    """
    FamForge: A CLI tool to summon and bond with magical familiars.
    """
    pass

        
# Register the commands
app.add_typer(summon.app, name="summon")
app.add_typer(bond.app, name="bond")
app.add_typer(list.app, name="list")
app.add_typer(show.app, name="show")
app.add_typer(reveal.app, name="reveal")

if __name__ == "__main__":
    app()

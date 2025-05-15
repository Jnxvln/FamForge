import json
import typer
from rich import print
from pathlib import Path
from .storage import save_familiar

app = typer.Typer()

# We'll store the most recently summoned familiar in a temp file
TEMP_PATH = Path.home() / ".famforge" / "last_summoned.json"

@app.command("now")  # ← give the command a name like `now`
def bond_now(
    name: str = typer.Option(None, "--name", "-n", help="Optional custom name for this familiar")
):
    """
    Bond with your most recently summoned familiar and save them to your grimoire.
    """
    if not TEMP_PATH.exists():
        print("[bold red]No familiar has been summoned yet.[/bold red]")
        return

    with open(TEMP_PATH, "r") as f:
        familiar = json.load(f)

    if name:
        familiar["name"] = name

    success = save_familiar(familiar)

    if success:
        print(f"[bold green]You have bonded with {familiar['name']}![/bold green] 🐾")
    else:
        print(f"[bold yellow]{familiar['name']} is already bonded.[/bold yellow] 🧿")

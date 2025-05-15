import json
import typer
from rich import print
from pathlib import Path
from .storage import save_familiar

# Path to grimoire location
GRIMOIRE_PATH = Path.home() / ".famforge" / "familiars.json"

# We'll store the most recently summoned familiar in a temp file
TEMP_PATH = Path.home() / ".famforge" / "last_summoned.json"

app = typer.Typer()

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

@app.command("note")
def bond_note(name: str = typer.Option(..., help="Name of the familiar"),
              note: str = typer.Option(..., help="The soul note to assign")):
    """
    Assign or update a soul note for a bonded familiar.
    """
    if not GRIMOIRE_PATH.exists():
        print("[bold red]No grimoire found. Try bonding with a familiar first.[/bold red]")
        raise typer.Exit()

    with open(GRIMOIRE_PATH, "r") as f:
        data = json.load(f)
        familiars = data.get("familiars", [])

    found = False
    for f in familiars:
        if f.get("name", "").lower() == name.lower():
            f["soul_note"] = note
            found = True
            break

    if not found:
        print(f"[yellow]No familiar named '{name}' found in your grimoire.[/yellow]")
        raise typer.Exit()

    with open(GRIMOIRE_PATH, "w") as f:
        json.dump(data, f, indent=2)

    print(f"[bold green]Soul note updated for '{name}'![/bold green]")
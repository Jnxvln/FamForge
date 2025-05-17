import typer
import json
from pathlib import Path
from rich import print
from famforge.reveal import generate_incantation

app = typer.Typer(help="Unlock hidden features with a decoded incantation")

GRIMOIRE_PATH = Path.home() / ".famforge" / "familiars.json"
UNLOCK_PATH = Path.home() / ".famforge" / "unlocked.json"

@app.command()
def unlock(incantation: str = typer.Argument(..., help="Enter the decoded incantation")):
    """
    Unlock hidden features by providing the correct incantation from a bonded familiar.
    """
    if not GRIMOIRE_PATH.exists():
        print("[red]No grimoire found. You must bond with a familiar first.[/red]")
        raise typer.Exit()

    with open(GRIMOIRE_PATH, "r") as f:
        data = json.load(f)
        familiars = data.get("familiars", [])

    valid = False
    for f in familiars:
        karma = f.get("karma_seed")
        if karma and generate_incantation(karma) == incantation:
            valid = True
            break

    if not valid:
        print(f"[bold red]Incorrect incantation.[/bold red] No unlock granted.")
        raise typer.Exit()

    # Write the unlock flag
    UNLOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(UNLOCK_PATH, "w") as f:
        json.dump({"unlocked": True}, f)

    print("\n[bold green]🔓 Incantation accepted! Hidden commands are now unlocked.[/bold green]\n")
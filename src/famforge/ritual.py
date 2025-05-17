import typer
from pathlib import Path
from rich import print
import json

UNLOCK_PATH = Path.home() / ".famforge" / "unlocked.json"

app = typer.Typer(help="Hidden rituals unlocked by incantation")

def ensure_unlocked():
    if not UNLOCK_PATH.exists():
        print("[red]🔒 This ritual is hidden. You must unlock it with a valid incantation.[/red]")
        raise typer.Exit()

@app.command("greet")
def secret_greeting():
    """
    A mystical greeting unlocked by your familiar's incantation.
    """
    ensure_unlocked()
    print("[bold magenta]🌌 The ritual circle glows... Welcome, Adept.[/bold magenta]")

@app.command("greet")
def greet():
    """
    A hidden greeting ritual for those who have unlocked the sigil.
    """
    if not UNLOCK_PATH.exists():
        print("[bold red]🔒 This ritual is hidden. You must unlock it with a valid incantation.[/bold red]")
        raise typer.Exit()

    with open(UNLOCK_PATH, "r") as f:
        unlocked = json.load(f).get("unlocked", False)

    if not unlocked:
        print("[bold red]🔒 This ritual is hidden. You must unlock it with a valid incantation.[/bold red]")
        raise typer.Exit()

    print("\n[bold magenta]✨ You’ve entered the hidden space between thoughts...[/bold magenta]")
    print("[cyan]The forge glows faintly, and something within you nods in return.[/cyan]\n")
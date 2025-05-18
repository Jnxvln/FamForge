import json
import random
import typer
from time import sleep
from pathlib import Path
from rich import print
from rich.console import Console
from .generator import generate_familiar
from .load_data import epithet_titles, clan_names
from .models import ELEMENT_COLORS


app = typer.Typer(help="Summon familiars")

@app.command()
def call(
    lock_element: str = typer.Option(None, help="lock a specific element (e.g. Fire)"),
    lock_species: str = typer.Option(None, help="lock a specific species (e.g. Emberox)"),
    lock_temperament: str = typer.Option(None, help="lock a specific temperament (e.g. Loyal)"),
    lock_size: str = typer.Option(None, help="lock a specific size (e.g. Medium)"),
    lock_gender: str = typer.Option(None, help="lock a specific gender (e.g. Nonbinary)"),
    allow_whimsy: bool = typer.Option(False, help="include humorous or surreal quirks"),
    with_title: bool = typer.Option(False, help="add a title or clan name to the familiar's name."),

):
    """
    Summon a mystical familiar with optional locked traits and whimsy.
    """

    locked_traits = {
        "element": lock_element,
        "species": lock_species,
        "temperament": lock_temperament,
        "size": lock_size,
        "gender": lock_gender
    }

    try:
        familiar = generate_familiar(
            locked=locked_traits, 
            allow_whimsy=allow_whimsy
        )

        # Randomly assign title/clan if flag is set
        if with_title:
            match random.randint(1, 4):
                case 1:
                    pass  # Neither
                case 2:
                    familiar.title = random.choice(epithet_titles)
                case 3:
                    familiar.clan = random.choice(clan_names)
                case 4:
                    familiar.title = random.choice(epithet_titles)
                    familiar.clan = random.choice(clan_names)

        console = Console()
        
        summon_messages = [
            "🌫️  The mists begin to swirl...",
            "✨ [purple1]The veil between realms thins...",
            "🌌 You are [yellow]summoning...[/yellow]",
            "🌀 A presence forms [dim white]from the aether...[/dim white]",
            "🔥 [red]Embers dance and coalesce[/red] [dim yellow]among you..[/dim yellow]",
            "🌿 The roots remember [orchid1]your name...[/orchid1]",
            "💧 A ripple moves [dim]across time...[/dim]",
            "🕯️ [yellow]The light flickers,[/yellow] [dim yellow]something approaches...[/dim yellow]"
        ]

        intro = random.choice(summon_messages)
        console.print(f"\n[bold blue]{intro}[/bold blue]", end=" ")

        # Arcane effect animation
        glyphs = ["✦", "◈", "⋆", "✴", "✷"]
        colors = ["magenta", "cyan", "orchid", "sky_blue1", "plum1", "medium_purple", "deep_pink3", "slate_blue1"]
        
        # Animate summoning glyphs across the veil
        for _ in range(8):
            glyph = random.choice(glyphs)
            color = random.choice(colors)
            console.print(f"[{color}]{glyph}[/{color}]", end=" ", soft_wrap=True)
            sleep(0.25)
            
        sleep(1)
        
        console.print()
        console.print()
        
        # Richly print the familiar's profile
        output = familiar.format_profile(rich=True)
        if output:
            for line in output:
                console.print(line)

        # Save last summoned familiar for bonding
        TEMP_PATH = Path.home() / ".famforge" / "last_summoned.json"
        TEMP_PATH.parent.mkdir(parents=True, exist_ok=True)
        data = familiar.model_dump()  # Pydantic v2

        with open(TEMP_PATH, "w") as f:
            json.dump(data, f, indent=2)

    except ValueError as e:
        print(f"\n[bold red]Error:[/bold red] {e}")

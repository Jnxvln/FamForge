import typer
from rich import print

app = typer.Typer(help="Summon and bond with your magical familiar")

@app.command()
def summon():
    print("[cyan]Summoning familiar...[/cyan]")
    # Will call generator logic later
    
@app.command()
def bond():
    print("[magenta]Revealing bond story...[/magenta]")
    # Will call lore logic later
    
@app.command()
def bless(message: str = typer.Option(..., help="A hidden message to attach to your familiar.")):
    print(f"[yellow]Blessing familiar with:[/yellow] {message}")
    # Will add soul_note in JSON
    
if __name__ == "__main__":
    app()
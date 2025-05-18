import typer
from .generator import generate_familiar, Element, get_trait_pool
from .load_data import (
    names_by_element,
    species_by_element,
    origins_by_element,
    abilities_by_element,
    quirks_standard_by_element,
    quirks_whimsical_by_element
)

verify_app = typer.Typer()

@verify_app.command("pools")
def verify_pools(n: int = 10):
    """Verify that all data pools are functional and integrated properly."""
    typer.echo("🔍 Verifying elemental pools...\n")

    for elem in Element:
        name_count = len(names_by_element.get(elem.value, []))
        species_count = len(species_by_element.get(elem.value, []))
        origin_count = len(origins_by_element.get(elem.value, []))
        ability_count = len(get_trait_pool(abilities_by_element, elem))
        quirks_std = len(get_trait_pool(quirks_standard_by_element, elem))
        quirks_whim = len(get_trait_pool(quirks_whimsical_by_element, elem))

        typer.echo(f"🧪 {elem.value}:")
        typer.echo(f"   - Names: {name_count}")
        typer.echo(f"   - Species: {species_count}")
        typer.echo(f"   - Origins: {origin_count}")
        typer.echo(f"   - Abilities: {ability_count}")
        typer.echo(f"   - Standard Quirks: {quirks_std}")
        typer.echo(f"   - Whimsical Quirks: {quirks_whim}\n")

    typer.echo(f"🎲 Generating {n} sample familiars...\n")
    errors = 0
    for i in range(n):
        try:
            f = generate_familiar()
            typer.echo(f" {i+1}. {f.name} ({f.element}) — {f.passive_ability}")
        except Exception as e:
            errors += 1
            typer.echo(f"❌ Error on familiar {i+1}: {e}")

    if errors == 0:
        typer.echo("\n✅ All pools passed verification.")
    else:
        typer.echo(f"\n⚠️ {errors} generation errors detected.")
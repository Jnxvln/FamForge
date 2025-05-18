from pydantic import BaseModel
from typing import List, Optional
from rich.panel import Panel
from rich.text import Text
from rich.console import Console, Group
from time import sleep

ELEMENT_COLORS = {
    "Air": "white",
    "Water": "blue",
    "Earth": "green",
    "Fire": "red",
    "Time": "magenta",
    "Spirit": "cyan",
    "Aether": "purple"
}

ELEMENT_GLYPHS = {
    "Air": "🌪️",
    "Water": "💧",
    "Earth": "🌿",
    "Fire": "🔥",
    "Time": "⏳",
    "Spirit": "🌌",
    "Aether": "✨"
}

__all__ = ["ELEMENT_COLORS", "ELEMENT_GLYPHS", "Familiar"]

class Familiar(BaseModel):
    name: str
    species: str
    element: str
    size: str
    gender: str
    temperament: str
    origin: str
    quirks: List[str]
    passive_ability: str
    bond_level: int
    soul_note: Optional[str]
    karma_seed: str
    title: Optional[str] = None
    clan: Optional[str] = None

    def format_display_name(self, rich: bool = True) -> str:
        if not rich:
            parts = [self.name]
            if self.title:
                parts.append(self.title)
            if self.clan:
                parts.append(f"of {self.clan}")
            return " ".join(parts)

        parts = [f"[bold white]{self.name}[/bold white]"]
        if self.title:
            parts.append(f" [dim orchid1]{self.title}[/dim orchid1]")
        if self.clan:
            parts.append(f" [dim cyan]of {self.clan}[/dim cyan]")
        return "".join(parts)

    def format_trait(self, label: str, value: Optional[str], rich: bool = True) -> str:
        if not value:
            value = "—"
        if not rich:
            return f"{label}: {value}"
        return f"[bold yellow]{label}:[/bold yellow] {value}"

    def format_quirks(self, rich: bool = True) -> List[str]:
        if not self.quirks:
            return []
        if not rich:
            return [f"- {q}" for q in self.quirks]
        return [f"  • [dim italic]{q}[/dim italic]" for q in self.quirks]
    
    def format_profile(self, rich: bool = True) -> List:
        lines = []

        glyph = ELEMENT_GLYPHS.get(self.element, "❖")
        lines.append(
            f"{glyph}{glyph} {self.format_display_name(rich)} the "
            f"{('[bold cyan]' + self.species + '[/bold cyan]') if rich else self.species} "
            f"([{ELEMENT_COLORS.get(self.element, 'white') if rich else ''}]{self.element}[/{ELEMENT_COLORS.get(self.element, 'white') if rich else ''}]"
            f", {'[green]' if rich else ''}Bond {self.bond_level}{'[/green]' if rich else ''}, Karma {self.karma_seed[:8] + '…'}) {glyph}{glyph}"
        )

        lines.append(self.format_trait("Origin", f"[italic]{self.origin}[/italic]" if rich else self.origin, rich))
        lines.append(self.format_trait("Gender", self.gender, rich) + " | " +
                     self.format_trait("Temperament", self.temperament, rich))

        if self.quirks:
            lines.append(f"[bold yellow]Quirks:[/bold yellow]" if rich else "Quirks:")
            lines.extend(self.format_quirks(rich))

        if self.passive_ability:
            lines.append(self.format_trait("Ability", f"[italic]{self.passive_ability}[/italic]" if rich else self.passive_ability, rich))

        if self.soul_note:
            lines.append(self.format_trait("Soul Note", f"“[dim]{self.soul_note}[/dim]”" if rich else self.soul_note, rich))

        if rich:
            panel = Panel(
                Group(*lines),
                border_style="bright_magenta",
                padding=(1, 2),
                title="[bold white]Your Familiar Appears[/bold white]",
                subtitle=f"[dim]Bound to {self.element} — {glyph}[/dim]"
            )

            return [panel]
from typing import Optional
from rich.text import Text


def format_display_name(
    name: str,
    title: Optional[str] = None,
    clan: Optional[str] = None,
    rich: bool = True
) -> str:
    if not rich:
        base = name
        if title:
            base += f" {title}"
        if clan:
            base += f" of {clan}"
        return base

    parts = [f"[bold white]{name}[/bold white]"]
    if title:
        parts.append(f" [dim orchid1]{title}[/dim orchid1]")
    if clan:
        parts.append(f" [dim cyan]of {clan}[/dim cyan]")
    return "".join(parts)

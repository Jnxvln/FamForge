# 📜 Changelog

All notable changes to **FamForge** will be documented here.

---

## [0.1.2] - 2024-05-14

### Added
- `--version` flag support
- `bond now` command to save the last summoned familiar
- Familiars are now saved to `~/.famforge/familiars.json`
- `list bonded` command to view bonded familiars in a table
- `--details` flag to show full familiar lore and traits
- Filters added: `--name`, `--element`, `--species`
- Rich CLI formatting using `rich.table`, `rich.console`

### Improved
- Familiar data serialization using `pydantic.BaseModel`
- Modular structure for adding future commands

### Fixed
- CLI now respects missing grimoire directories and handles them gracefully

---

## [0.1.0] - Initial Release

- Project initialized
- Basic `summon` functionality implemented

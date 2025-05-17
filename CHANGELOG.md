# 📜 Changelog

All notable changes to **FamForge** will be documented here.

---
## [0.1.6] - 2024-05-17

### Added
- `sigil` command to display a familiar’s unique ASCII sigil, encoded from their incantation
- `reveal decode` command to decode binary text into an incantation
- `unlock <incantation>` command to unlock hidden CLI commands
- `ritual greet` as the first hidden command (available only after unlocking)
- Secret incantations no longer displayed in profiles or lists to preserve mystery

### Improved
- Full incantation lifecycle: summon → bond → sigil → decode → unlock → ritual

---

## [0.1.5] - 2024-05-17
### Added
- `reveal incantation` now available via CLI to uncover each familiar's unique, deterministic passphrase
- Familiar incantations now appear in `list bonded --details` and `show profile` views
- All summon commands now organized under `famforge summon call` for clarity
- Enhanced README.md with new usage examples, project description, and support badge

### Improved
- Modular CLI structure now includes `reveal`, `show`, and `summon` command groups
- FamForge branding, README, and BMAC integration for a more polished open-source presence

---

## [0.1.4] - 2024-05-16
### Added
- New CLI structure: `famforge summon call`, `bond now`, `show profile`, etc.
- `reveal incantation` command to uncover mystical passphrases
- Incantations now appear in `show profile` and `list bonded --details` output
- Enhanced CLI output with color-coded styling and formatting

### Fixed
- Entry-point script issue when using editable installs (`pip install -e .`)

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

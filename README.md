# 🐾 FamForge

**FamForge** is a magical command-line tool for conjuring and connecting with mystical familiars. Generate unique creatures with elemental traits, rich backstories, quirks, and soul-deep meaning — then save them forever in your personal grimoire.

---

## ✨ Features

- Summon deeply unique magical familiars
- Lock traits like element, species, gender, and more
- Add whimsical quirks for a playful twist
- Bond with familiars and save them to your grimoire
- Attach personal soul notes to each companion
- Reveal a secret **incantation** hidden in each karma seed
- View bonded familiars in a color-coded table
- Filter by name, species, or element
- Display full familiar profiles with `--details`
- Modular commands: `summon call`, `bond now`, `bond note`, `reveal incantation`, etc.

---

## 🚀 Installation

```bash
git clone https://github.com/Jnxvln/FamForge.git
cd FamForge
python -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
pip install -e .
```

---

## 🧙 Usage

### Summon a Familiar

```bash
famforge summon call
```

With locked traits:

```bash
famforge summon call --lock-element Fire --lock-size Medium --allow-whimsy
```

---

### 🔎 Sample Output

```bash
famforge summon call --lock-element Fire

You have summoned...

Name: Nyxa
Species: Emberox
Element: Fire
Size: Tiny
Gender: Nonbinary
Temperament: Brave
Origin: Ignited from embers of a sacred pyre.
Quirks:
  • Communicates through shifting light patterns.
  • Sleeps curled near moonlight.
Ability: Glows faintly when danger is near.
Bond Level: 1
Soul Note: None
Karma Seed: 84aa90ae-3417-47b5-b4e9-beee20273ba9
```

---

### Bond with the Last Summoned Familiar

```bash
famforge bond now --name Nyxa
```

---

### Add a Soul Note

```bash
famforge bond note --name Nyxa --note "You were with me during the fire."
```

---

### Reveal the Familiar’s Incantation

```bash
famforge reveal incantation Nyxa
# Example: dusk-glyph-flicker
```

---

### Display the Familiar’s Sigil

```bash
famforge sigil Nyxa
```

---

### Decode a Binary Incantation

```bash
famforge reveal decode 0110010001110101011100110110101100101101011001110110110001101001011110000010110101100011011011110110010001100101
# Output: dusk-glyph-code
```

---

### Unlock Hidden Commands

```bash
famforge unlock dusk-glyph-code
```

---

### Use a Hidden Ritual

```bash
famforge ritual greet
```

---

### View Your Grimoire

```bash
famforge list bonded
```

With filters:

```bash
famforge list bonded --element Fire --species Emberox
```

Detailed view:

```bash
famforge list bonded --details
```

---

### View a Full Familiar Profile

```bash
famforge show profile Nyxa
```

---

## 📂 Familiar Storage

FamForge stores your familiars in a grimoire file located at:

```
~/.famforge/familiars.json
```

Platform examples:

| OS               | Path Example                                   |
|------------------|------------------------------------------------|
| Linux            | `/home/username/.famforge/familiars.json`      |
| macOS            | `/Users/username/.famforge/familiars.json`     |
| Windows (WSL)    | `/home/username/.famforge/familiars.json`      |
| Windows (native) | `C:\Users\YourName\.famforge\familiars.json`

---

## 📦 Version

```bash
famforge --version
```

---

## 🔮 Roadmap

- [x] `summon`
- [x] `summon call`
- [x] `bond now`
- [x] `bond note`
- [x] `show profile`
- [x] `list bonded` with `--details`
- [x] display soul notes
- [x] `reveal incantation`
- [x] `sigil` renders binary-encoded ASCII art for each familiar
- [x] `reveal decode` decodes incantation text from binary
- [x] `unlock <incantation>` command to reveal hidden rituals
- [x] `ritual greet` (hidden command unlocked via incantation)
- [ ] `bond levelup`
- [ ] `list bonded --random`
- [ ] `export` as Markdown

---

## ☕ Support

If this project speaks to you, consider [supporting it on Buy Me a Coffee](https://buymeacoffee.com/uncompiledself).  
Every little bit helps fuel the forge. ❤️‍🔥

[![Tip the Mage](https://img.shields.io/badge/Tip%20the%20Mage-%F0%9F%8C%99-6e5cb6)](https://buymeacoffee.com/uncompiledself)

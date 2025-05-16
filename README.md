# 🐾 FamForge

**FamForge** is a magical command-line tool that allows you to summon, bond, and catalog your very own mystical familiars. Generate randomized creatures with rich backstories, elemental traits, whimsical quirks, and more — then save them forever in your personal grimoire.

---

## ✨ Features

- Summon unique magical familiars
- Lock traits like element, species, gender, and more
- Add whimsical quirks for a playful twist
- Bond with familiars and save them to your grimoire
- Add personal soul notes
- Reveal a hidden **incantation** embedded in each karma seed
- View all bonded companions in a color-coded table
- Filter by name, species, or element
- View detailed familiar profiles with `--details`
- Modular command structure: `summon call`, `bond now`, `bond note`, `reveal incantation`, etc.

---

## 🚀 Installation

Clone the repository and install requirements:

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
# Example output: dusk-glyph-flicker
```

---

### View Your Grimoire

#### Simple Table

```bash
famforge list bonded
```

#### Filtered Table

```bash
famforge list bonded --element Fire
```

#### Detailed View

```bash
famforge list bonded --details
```

#### Combined Filters

```bash
famforge list bonded --element Fire --species Emberox --details
```

---

### View a Full Familiar Profile

```bash
famforge show profile Nyxa
```

---

## 📂 Grimoire Location

FamForge stores your familiars in a JSON file at:

```
~/.famforge/familiars.json
```

This works across platforms:

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
- [ ] `bond levelup`
- [ ] `list bonded --random`
- [ ] `export` as Markdown

---

## 🧡 Credits

Created with magic and love by UncompiledSelf (@Jnxvln). FamForge is your gateway to bonding with the unseen. 🌙

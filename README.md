# 🐾 FamForge

**FamForge** is a magical command-line tool that allows you to summon, bond, and catalog your very own mystical familiars. Generate randomized creatures with rich backstories, elemental traits, whimsical quirks, and more — then save them forever in your personal grimoire.

---

## ✨ Features

- Summon unique magical familiars
- Lock traits like element, species, gender, and more
- Add whimsical quirks for a playful twist
- Bond with familiars and save them to your grimoire
- View all bonded companions in a color-coded table
- Filter by name, species, or element
- View detailed familiar profiles with `--details`

---

## 🚀 Installation

Clone the repository and install requirements:

```bash
git clone https://github.com/Jnxvln/FamForge.git
cd FamForge
python -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 🧙 Usage

### Summon a Familiar

```bash
python -m src.famforge.main summon
```

With locked traits:

```bash
python -m src.famforge.main summon --lock-element Fire --lock-size Medium --allow-whimsy
```

---

### Bond with the Last Summoned Familiar

```bash
python -m src.famforge.main bond now --name Nyxa
```

---

### View Your Grimoire

#### Simple Table

```bash
python -m src.famforge.main list bonded
```

#### Filtered Table

```bash
python -m src.famforge.main list bonded --element Fire
```

#### Detailed View

```bash
python -m src.famforge.main list bonded --details
```

#### Combined Filters

```bash
python -m src.famforge.main list bonded --element Fire --species Emberox --details
```

---

## 📂 Grimoire Location

FamForge stores your familiars in a JSON file at:

```
~/.famforge/familiars.json
```

This works across platforms:

| OS      | Path Example                                 |
|---------|----------------------------------------------|
| Linux   | `/home/username/.famforge/familiars.json`    |
| macOS   | `/Users/username/.famforge/familiars.json`   |
| Windows (WSL) | `/home/username/.famforge/familiars.json` |
| Windows (native) | `C:\Users\YourName\.famforge\familiars.json` (if ported)

---

## 📦 Version

```bash
python -m src.famforge.main --version
```

---

## 🔮 Roadmap

- [x] `summon`
- [x] `bond now`
- [x] `bond note`
- [x] `show profile`
- [x] `list bonded` with `--details`
- [x] display soul notes
- [ ] `bond levelup`
- [ ] `list bonded --random`
- [ ] `export` as Markdown

---

## 🧡 Credits

Created with magic and love by UncompiledSelf (@Jnxvln). FamForge is your gateway to bonding with the unseen. 🌙


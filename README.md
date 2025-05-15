# 🐉 FamForge
*Summon, shape, and bond with magical familiars from the aether.*

FamForge is a mystical command-line tool that lets you generate richly-detailed magical companions using the power of storytelling, randomness, and optional chaos.

---

## ✨ Features

- 🔮 Summon unique familiars with randomized traits and lore
- 🔐 Lock specific traits across summons (e.g. element, species)
- 🎭 Enable whimsical or surreal quirks with `--allow-whimsy`
- 📜 Generate deep lore, magical abilities, and soul signatures

---

## 🚀 Installation

1. Clone the repository:
```bash
git clone git@github.com:Jnxvln/FamForge.git
cd FamForge
```

2. Create & activate virtual environment:
```bash
python -m venv ~/venvs/famforge
source ~/venvs/famforge/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🧪 Usage

```bash
python -m src.famforge.main --help
```

### Example:
```bash
python -m src.famforge.main --lock-element Fire --lock-size Large --allow-whimsy
```

---

## 🛣️ Roadmap & Versioning (SemVer)

FamForge follows [Semantic Versioning](https://semver.org/) and evolves in magical milestones:

| Version | Milestone |
|---------|-----------|
| `v0.1.0` | Initial summon command, trait locking, whimsy mode |
| `v0.2.0` | `bond` command to save familiars |
| `v0.3.0` | Rich-powered output formatting |
| `v0.4.0` | Persistent trait locking + reroll support |
| `v0.5.0` | Expanded species, quirks, and elemental synergy |
| `v1.0.0` | Modular CLI, full feature set, public-ready ✨ |

Want to help shape the path? Ideas welcome via issues or PRs!

---

## 📝 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

---

## 💖 Author

Made with care and a spark of magic by [Justin Cox](https://github.com/Jnxvln)

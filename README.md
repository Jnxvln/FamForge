# FamForge

**FamForge** is a magical command-line companion generator for storytellers, writers, and fantasy lovers. With a single command, summon richly detailed creatures with elemental roots, distinct personalities, and playful quirks.

&#x20;

## ✨ Features

* Procedural generation of familiars with:

  * Elemental domains: Fire, Water, Air, Earth, Spirit, Time, Aether
  * Unique species tied to each element
  * Personality traits, origins, quirks, and magical abilities
  * Optional whimsical features (`--allow-whimsy`)
* Lock specific traits (like `--lock-element Fire`) to tailor results
* Rich terminal output powered by [Rich](https://github.com/Textualize/rich)
* Color-coded elements for immersive visualization

---

## 🚀 Usage

### Installation

```bash
pip install -e .
```

### Summon a Familiar

```bash
famforge summon
```

### Summon with Locked Traits

```bash
famforge summon --lock-element=Fire --lock-temperament=Loyal --lock-size=Medium
```

### Summon with Whimsy

```bash
famforge summon --allow-whimsy
```

---

## 🔮 Example Output

```
You have summoned...

Name: Tirith
Species: Ashmole
Element: Earth
Size: Colossal
Gender: Nonbinary
Temperament: Funny
Origin: Rose from the fertile remains of an extinct forest.
Quirks: 
  • Sleeps curled near moonlight. 
  • Obsessed with collecting lost socks.
Ability: Converts light to dark.
Bond Level: 1
Soul Note: None
Karma Seed: 65b117c2-d2f7-4e52-ae09-b0f3a5a2208c
```

---

## 📦 Project Structure

```
famforge/
├── generator.py         # Familiar creation logic
├── main.py              # CLI entry point
├── models.py            # Familiar dataclass model
├── __init__.py
```

---

## 🛠️ Requirements

* Python 3.8+
* [Typer](https://github.com/tiangolo/typer)
* [Rich](https://github.com/Textualize/rich)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ☕ Support

Made with whimsy by [UncompiledSelf](https://buymeacoffee.com/uncompiledself) — for the quietly curious.

---

## 📜 License

[MIT](LICENSE)

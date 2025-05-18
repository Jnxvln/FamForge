import random
import uuid
from enum import Enum
from .models import Familiar
from .load_data import (
    names_by_element,
    species_by_element,
    origins_by_element,
    quirks_standard_by_element,
    quirks_whimsical_by_element,
    abilities_by_element
)

# Enum for elemental domains
class Element(str, Enum):
    AIR = "Air"
    WATER = "Water"
    EARTH = "Earth"
    FIRE = "Fire"
    TIME = "Time"
    SPIRIT = "Spirit"
    AETHER = "Aether"  # formerly "Space"

# Enum for size classifications
class Size(str, Enum):
    TINY = "Tiny"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    COLOSSAL = "Colossal"
    
# Enum for creature gender
class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"
    NONBINARY = "Nonbinary"
    ANDROGYNOUS = "Androgynous"
    FLUID = "Fluid"
    NEUTRAL = "Neutral"
    VOIDBORN = "Voidborn"           # mystical, aetherial
    TIMELESS = "Timeless"           # fitting for Time familiars
    SPIRAL = "Spiral"               # surreal / spirit-based
    ECLIPTIC = "Ecliptic"           # dual-aspected or phase-shifting
    UNGENDERED = "Ungendered"
    CHANGES = "Changes With Mood"
    UNKNOWN = "Unknown"
    
# Enum for creature temperaments
class Temperament(str, Enum):
    SHY = "Shy"
    BRAVE = "Brave"
    CHAOTIC = "Chaotic"
    LOYAL = "Loyal"
    INDIFFERENT = "Indifferent"
    BENEVOLENT = "Benevolent"
    CRUEL = "Cruel"
    ETERNAL = "Eternal"
    DREADFUL = "Dreadful"
    DREAMY = "Dreamy"
    HYPER = "Hyper"
    ABYSMAL = "Abysmal"
    FUNNY = "Funny"
    HUMBLE = "Humble"
    CURIOUS = "Curious"
    MEEK = "Meek"
    LAZY = "Lazy"
    GENTLE = "Gentle"
    SILENT = "Silent"
    RESILIENT = "Resilient"
    FABULOUS = "Fabulous"
    HUMAN = "Human"
    INTELLIGENT = "Intelligent"
    MALICIOUS = "Malicious"
    GHOSTLY = "Ghostly"
    TRANSIENT = "Transient"
    SHADOWY = "Shadowy"

# Cached lists of enum members
ELEMENTS = list(Element)
SIZES = list(Size)
GENDERS = list(Gender)
TEMPERAMENTS = list(Temperament)

ALL_NAMES = [name for names in names_by_element.values() for name in names]

def get_trait_pool(source_dict: dict, element: Element) -> list:
    return source_dict.get("shared", []) + source_dict.get(element.value, [])

# Main generator function
def generate_familiar(locked: dict = None, allow_whimsy: bool = False, with_title: bool = False) -> Familiar:
    """Generate a familiar, optionally locking certain traits."""
    locked = locked or {}

    # Convert or randomly choose an Element
    try:
        if isinstance(locked.get("element"), str):
            element = Element[locked["element"].strip().upper()]
        else:
            element = locked.get("element") or random.choice(ELEMENTS)
    except KeyError:
        raise ValueError(f"Invalid element: {locked.get('element')}")

    # Convert or randomly choose a Temperament
    try:
        if isinstance(locked.get("temperament"), str):
            temperament = Temperament[locked["temperament"].strip().upper()]
        else:
            temperament = locked.get("temperament") or random.choice(TEMPERAMENTS)
    except KeyError:
        raise ValueError(f"Invalid temperament: {locked.get('temperament')}")
    
    # Convert or randomly choose a Gender
    try:
        if isinstance(locked.get("gender"), str):
            gender = Gender[locked["gender"].strip().upper()]
        else:
            gender = locked.get("gender") or random.choice(GENDERS)
    except KeyError:
        raise ValueError(f"Invalid gender: {locked.get('gender')}")
    
    # Randomly assign various traits based on element
    ability_pool = get_trait_pool(abilities_by_element, element)
    standard_quirks_pool = get_trait_pool(quirks_standard_by_element, element)
    whimsical_quirks_pool = get_trait_pool(quirks_whimsical_by_element, element)

    # Randomly assign quirks based on element
    if allow_whimsy:
        quirk1 = random.choice(standard_quirks_pool)
        quirk2 = random.choice(whimsical_quirks_pool)
        quirks = [quirk1, quirk2] if quirk1 != quirk2 else [quirk1]
    else:
        quirks = random.sample(standard_quirks_pool, 2)
        
    # Append epithet titles and clan names to base name if applicable
    base_name = random.choice(names_by_element[element.value])

    if with_title:
        parts = [base_name]
        if random.random() < 0.5:
            parts.append(random.choice(epithet_titles))
        if random.random() < 0.5:
            parts.append(random.choice(clan_names))
        name = " ".join(parts)
    else:
        name = base_name

    # Build and return the Familiar instance
    return Familiar(
        name = name,
        species = random.choice(species_by_element[element.value]),
        element = element.value,
        size = locked.get("size") or random.choice(SIZES).value,
        gender = gender.value,
        temperament = temperament.value,
        origin = random.choice(origins_by_element[element.value]),
        quirks = quirks,
        passive_ability = random.choice(ability_pool),
        bond_level = 1,
        soul_note = None,
        karma_seed = str(uuid.uuid4())
    )

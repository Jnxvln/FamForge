import random
import uuid
from enum import Enum
from .models import Familiar

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

# Species mapped by element
SPECIES_BY_ELEMENT = {
    Element.AIR: ["Mistcat", "Zephyrfin", "Whispraptor"],
    Element.WATER: ["Glowlizard", "Rippleback", "Kelpray"],
    Element.EARTH: ["Stonewing", "Mossbeast", "Ashmole"],
    Element.FIRE: ["Emberox", "Flareling", "Cinderdrake"],
    Element.TIME: ["Hourmoth", "Chronohound", "Tickwyrm"],
    Element.SPIRIT: ["Soulfen", "Wispkin", "Umbrawhisper"],
    Element.AETHER: ["Nullcat", "Voidbeak", "Gravitine"]
}

# Origins mapped by element type
ORIGINS_BY_ELEMENT = {
    Element.AIR: [
        "Emerged from a rift high in the sky.",
        "Spun from wind currents dancing across open plains.",
        "First heard as a whisper echoing through an ancient canyon."
    ],
    Element.WATER: [
        "Spawned in a deep current beneath still waters.",
        "Found tangled in seaweed beside a shipwreck no one remembers.",
        "Surged forth from a tidal pool under twin moons."
    ],
    Element.EARTH: [
        "Discovered slumbering beneath ancient roots.",
        "Chiseled out of bedrock by the pressure of time itself.",
        "Rose from the fertile remains of an extinct forest."
    ],
    Element.FIRE: [
        "Ignited from embers of a sacred pyre.",
        "Birthed during the final breath of a dying volcano.",
        "Leapt from the hearthfire of an ancient homestead."
    ],
    Element.TIME: [
        "Ticked into being by a lost second.",
        "Emerged from the first crack in a broken sundial.",
        "Spawned between seconds in a moment that no longer exists."
    ],
    Element.SPIRIT: [
        "Breathed into life by mourning chants.",
        "Formed in the last breath of a peaceful passing.",
        "Woven from threads of grief and hope in equal measure."
    ],
    Element.AETHER: [
        "Condensed from collapsing potential in deep space.",
        "Born in the silence between stars.",
        "Tumbled from the event horizon of a collapsed truth."
    ]
}

# Light personality traits (non-functional flavor)
QUIRKS_STANDARD = [
    "Can phase through doors but not windows.",
    "Sings softly when it rains.",
    "Only eats fruit offered at dusk.",
    "Sleeps curled near moonlight.",
    "Communicates through shifting light patterns.",
    "Collects shiny pebbles obsessively.",
    "Hums ancient songs while dreaming.",
    "Can sense subtle changes in the air.",
    "Communicates with animals through melodies.",
    "Whispers the intents of nearby creatures.",
    "Plants grow in its wake.",
    "Invisible to most forms of light.",
    "Passively composes music based on nearby emotions."
]

# Additional whimsical quirks (for --allow-whimsy flag)
QUIRKS_WHIMSICAL = [
    "Sneezes glitter when startled.",
    "Burps constellations.",
    "Wears extremely large glasses.",
    "Believes it's invisible when it closes its eyes.",
    "Obsessed with collecting lost socks.",
    "Sneezes bubbles instead of air.",
    "Argues with its own shadow.",
    "Mimics your facial expressions.",
    "Prefers to speak in riddles unless bribed with berries.",
    "Faints dramatically when ignored for too long.",
    "Wears a leaf like a cape and insists it’s royalty.",
    "Pretends to be a statue when observed.",
    "Tells bad jokes telepathically.",
    "Refuses to move until praised.",
    "Snores in musical scales.",
    "Builds elaborate nests out of buttons.",
    "Curls into a ball when offered compliments.",
    "Collects echoes in tiny jars.",
    "Composes haikus about what it sees each day."
]

# Functional magical abilities
ABILITIES = [
    "Detect lies.",
    "Moves unnoticed in the shadows.",
    "Freezes time for one second when afraid.",
    "Dreamwalks into nearby memories.",
    "Heals minor wounds with a touch.",
    "Detects hidden traps.",
    "Reads the thoughts of others.",
    "Manifests the fears of nearby creatures.",
    "Creates a mirage of itself from the past.",
    "Generates a harmonious and vibrational aura.",
    "Communicates with the wind.",
    "Creates a storm of light.",
    "Creates a storm of darkness.",
    "Moves through solid objects.",
    "Converts dark to light.",
    "Converts light to dark.",
    "Reverses time for five seconds.",
    "Creates a soothing melody.",
    "Creates a protective aura.",
    "Transforms into a flock of birds.",
    "Glows faintly when danger is near.",
    "Understands forgotten languages.",
    "Travels through sound waves."
]

# Predefined name list
NAMES = ["Lirrow", "Emberel", "Tharn", "Nyxa", "Aelynn", "Tirith", "Silranor"]

# Main generator function

def generate_familiar(locked: dict = None, allow_whimsy: bool = False) -> Familiar:
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

    # Lock or randomly assign a species based on element
    species = locked.get("species") or random.choice(SPECIES_BY_ELEMENT[element])
    
    # Mix in whimsy quirks if allowed and ensure at least one from each group
    #quirk_pool = QUIRKS_STANDARD + QUIRKS_WHIMSICAL if allow_whimsy else QUIRKS_STANDARD
    
    if allow_whimsy:
        quirk1 = random.choice(QUIRKS_STANDARD)
        quirk2 = random.choice(QUIRKS_WHIMSICAL)
        quirks = [quirk1, quirk2] if quirk1 != quirk2 else [quirk1]
    else:
        quirks = random.sample(QUIRKS_STANDARD, 2)

    # Build and return the Familiar instance
    return Familiar(
        name=random.choice(NAMES),
        species=species,
        element=element.value,
        size=locked.get("size") or random.choice(SIZES).value,
        gender=gender.value,
        temperament=temperament.value,
        origin=random.choice(ORIGINS_BY_ELEMENT[element]),
        quirks=quirks,
        passive_ability=random.choice(ABILITIES),
        bond_level=1,
        soul_note=None,
        karma_seed=str(uuid.uuid4())
    )

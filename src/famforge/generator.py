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
    Element.AIR: [
        "Mistcat", "Zephyrfin", "Whispraptor", "Driftalon", "Skywhisp", 
        "Gustclaw", "Cloudkin", "Stormbleat", "Aerofox", "Vaporyx"
    ],
    Element.WATER: [
        "Glowlizard", "Rippleback", "Kelpray", "Tideglider", "Brinetooth", 
        "Naiadorn", "Foamscale", "Drenchback", "Coralitch", "Floodmouse"
    ],
    Element.EARTH: [
        "Stonewing", "Mossbeast", "Ashmole", "Rootjaw", "Cragbeast", 
        "Glimmermole", "Thornox", "Stonecurl", "Lichenhorn", "Burrowelk"
    ],
    Element.FIRE: [
        "Emberox", "Flareling", "Cinderdrake", "Scorchkin", "Ignibark", 
        "Blazecrow", "Volcaroo", "Cindertuft", "Sparkvex", "Ashadder"
    ],
    Element.TIME: [
        "Hourmoth", "Chronohound", "Tickwyrm" "Sandwyrm", "Tickgeist", 
        "Clockra", "Hourstag", "Pendulark", "Chronopup", "Temporalin"
    ],
    Element.SPIRIT: [
        "Soulfen", "Wispkin", "Umbrawhisper", "Mirthling", "Soulitch", "Hauntelope", "Grimtail", "Phantasmunk", "Whisperray", "Echofox"
    ],
    Element.AETHER: [
        "Nullcat", "Voidbeak", "Gravitine", "Nebuline", "Voidelk", 
        "Starvynx", "Galaxbat", "Orbinox", "Quantowl", "Zerokid"
    ]
}

# Origins mapped by element type
ORIGINS_BY_ELEMENT = {
    Element.AIR: [
        "Emerged from a rift high in the sky.",
        "Spun from wind currents dancing across open plains.",
        "First heard as a whisper echoing through an ancient canyon.",
        "Formed from the last breath of a wind god.",
        "Traced into being by the flight paths of lost birds.",
        "Spun from cloudstuff atop a sleeping giant’s sigh.",
        "Birthed in the eye of a storm that never touches ground.",
        "Scattered together by migrating dreams.",
        "Whistled into form through the reeds of a forgotten flute.",
        "Woven by zephyrs inside an abandoned sky temple."
    ],
    Element.WATER: [
        "Spawned in a deep current beneath still waters.",
        "Found tangled in seaweed beside a shipwreck no one remembers.",
        "Surged forth from a tidal pool under twin moons.",
        "Bubbled up from the deepest trench of a sunken world.",
        "Dripped into form from the tears of a weeping reef.",
        "Flowed out of an ancient spring touched by moonlight.",
        "Condensed from morning mist above sacred waters.",
        "Washed ashore after a dreamlike storm.",
        "Spawned within the eye of a whirlpool that never stops spinning.",
        "Frozen into existence inside a hollow glacier."
    ],
    Element.EARTH: [
        "Discovered slumbering beneath ancient roots.",
        "Chiseled out of bedrock by the pressure of time itself.",
        "Rose from the fertile remains of an extinct forest.",
        "Unearthed beneath ruins swallowed by the jungle.",
        "Awakened in the belly of a hibernating mountain.",
        "Formed where fault lines kissed beneath ancient soil.",
        "Shaped from loam touched by ancestral memory.",
        "Mossed into being on a forgotten standing stone.",
        "Grew slowly beneath centuries of unbroken silence.",
        "Rumbled awake in the crater of a petrified bloom."
    ],
    Element.FIRE: [
        "Ignited from embers of a sacred pyre.",
        "Birthed during the final breath of a dying volcano.",
        "Leapt from the hearthfire of an ancient homestead.",
        "Spawned from the first spark struck in darkness.",
        "Raised within the heart of a wandering wildfire.",
        "Forged in the dreams of a dying blacksmith.",
        "Born from lightning striking ancient ruins.",
        "Stoked into being by the rage of a forgotten god.",
        "Crackled forth from a cursed ritual flame.",
        "Danced out of a coal left smoldering under moonlight."
    ],
    Element.TIME: [
        "Ticked into being by a lost second.",
        "Emerged from the first crack in a broken sundial.",
        "Spawned between seconds in a moment that no longer exists.",
        "Dropped from the pocket of a wandering chronomancer.",
        "Formed in the static between two ticking seconds.",
        "Written into the margins of a forgotten prophecy.",
        "Echoed backward from the future that never came.",
        "Spun into being on the spindle of an eternal dusk.",
        "Shattered out of a broken timeline and reassembled here.",
        "Fell through a crack in an ancient hourglass."
    ],
    Element.SPIRIT: [
        "Breathed into life by mourning chants.",
        "Formed in the last breath of a peaceful passing.",
        "Woven from threads of grief and hope in equal measure.",
        "Lingered too long at the crossroads of mourning.",
        "Sewn from soul-threads left behind by old friendships.",
        "Came to life beneath the lullaby of a grieving child.",
        "Flickered into being near a shrine no one tends anymore.",
        "Conjured from the stillness of a prayer left unfinished.",
        "Coalesced from memories too tender to fade.",
        "Risen with the mist from a grave forgotten by time."
    ],
    Element.AETHER: [
        "Condensed from collapsing potential in deep space.",
        "Born in the silence between stars.",
        "Tumbled from the event horizon of a collapsed truth.",
        "Drifted into form between waking and sleep.",
        "Woven from the silence before a nova's bloom.",
        "Fell to earth as a wish that never found a star.",
        "Shaped by gravitational echoes in a dead dimension.",
        "Formed where logic unravelled during a dreaming eclipse.",
        "Birthed from antimatter humming in cosmic rhythm.",
        "Leaked into this realm through a wrinkle in potential."
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

NAMES_BY_ELEMENT = {
    Element.FIRE: [
        "Emberel", "Pyrrion", "Caldris", "Emberyn", "Ignelle",
        "Volcaer", "Solvaric", "Fyrannis", "Ashvora", "Cindariel",
        "Vulkess", "Scorchinelle", "Blazethorn", "Emberith", "Ignisar",
        "Karnyx", "Flamareth", "Searin", "Moltra", "Blazul"
    ],
    Element.WATER: [
        "Lirrow", "Aquareth", "Thalorin", "Driswyn", "Nevalis",
        "Nerathis", "Ocevelle", "Brinmar", "Delthera", "Wavethorn", 
        "Myrris", "Corvalune", "Mistara", "Aquith", "Tidewyn", 
        "Glacien", "Pearlis", "Kelphor", "Rainnix", "Selmira"
    ],
    Element.EARTH: [
        "Tharn", "Terrakai", "Bramis", "Umberok", "Tremarin",
        "Gravemoss", "Tharnok", "Ruderalis", "Kaelgrove", "Morbenth", 
        "Stoneel", "Burrowel", "Terralyn", "Felnroot", "Craggor", 
        "Umbrisol", "Siltvyne", "Veinwilt", "Mirethorn", "Groven"
    ],
    Element.AIR: [
        "Aelynn", "Zephrae", "Sylune", "Lunthera", "Aureveil", 
        "Caelistra", "Whisryn", "Aeriven", "Cirraquil", "Galeen", 
        "Windara", "Soareth", "Skywyn", "Tornis", "Siroveil", 
        "Zephyra", "Breezinel", "Cloudelle", "Anemir", "Vayra"
    ],
    Element.TIME: [
        "Silranor", "Tirith", "Chronessa", "Tikelor", "Epochyn", 
        "Momenth", "Kalendrix", "Aevira", "Timasel", "Hourven", 
        "Wyndclock", "Veridane", "Sundryss", "Temphora", "Pendulae", 
        "Aeoneth", "Cyclyra", "Veloras", "Anachros", "Zenthros"
    ],
    Element.SPIRIT: [
        "Elossence", "Sylune", "Whismara", "Soulith", "Ephryn", 
        "Hauntelle", "Numael", "Vespiris", "Drevia", "Phantira", 
        "Mournix", "Wailen", "Caelmira", "Serephin", "Umbrith", 
        "Noctelle", "Echoiris", "Phaelys", "Kindross", "Lamenth"
    ],
    Element.AETHER: [
        "Nyxa", "Glacelle", "Aelmora", "Voidelune", "Gravethis", 
        "Astrofel", "Nebulith", "Cosmira", "Velquor", "Nimbrael", 
        "Lucenari", "Eclipsys", "Aetherion", "Zoraphine", "Spacelle", 
        "Dimensar", "Orbyss", "Parallaxa", "Stravon", "Elunex"
    ]
}

ALL_NAMES = [name for names in NAMES_BY_ELEMENT.values() for name in names]

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
        name=random.choice(ALL_NAMES),
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

from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Familiar:
    name: str
    species: str
    element: str
    size: str
    temperament: str
    origin: str
    quirks: List[str] = field(default_factory=list)
    passive_ability: Optional[str] = None
    bond_level: int = 1
    soul_note: Optional[str] = None
    karma_seed: Optional[str] = None
    
    def to_dict(self):
        return self.__dict__
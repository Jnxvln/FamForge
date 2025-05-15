from pydantic import BaseModel
from typing import List, Optional

class Familiar(BaseModel):
    name: str
    species: str
    element: str
    size: str
    gender: str
    temperament: str
    origin: str
    quirks: List[str]
    passive_ability: Optional[str] = None
    bond_level: int = 1
    soul_note: Optional[str] = None
    karma_seed: Optional[str] = None

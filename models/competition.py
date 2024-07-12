from dataclasses import dataclass, field
from .league import League
from .club import Club

@dataclass
class Competition():
    id: int = 0
    country: League = field(default_factory= League)
    clubs: list[Club] = field(default_factory=lambda: [])

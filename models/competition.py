from dataclasses import dataclass, field
from .league import League
from .club import Club

@dataclass
class Competition():
    name: League
    id: int = 0
    clubs: list[Club] = field(default_factory=lambda: [])

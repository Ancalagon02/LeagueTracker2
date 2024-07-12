from dataclasses import dataclass, field
from datetime import date
from models.club import Club
from models.league import League

@dataclass
class Matches:
    id: int = 0
    league: League = field(default_factory= League)
    clubs: list[Club] = field(default_factory=lambda: [])
    data: date = date.today()

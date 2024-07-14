from dataclasses import dataclass, field
from datetime import date
from .match import Match
from .league import League
from .club import Club

@dataclass
class Competition():
    id: int = 0
    country: League = field(default_factory= League)
    clubs: list[Club] = field(default_factory= lambda: [])
    matches = {date: [Match]}

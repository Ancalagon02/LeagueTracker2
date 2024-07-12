from dataclasses import dataclass, field
from datetime import date
from models.club import Club

@dataclass
class Matches:
    id: int = 0
    clubs: list[Club] = field(default_factory=lambda: [])
    data: date = date.today()

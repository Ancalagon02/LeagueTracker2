from dataclasses import dataclass, field
from .country import Country

@dataclass
class Club:
    id: int = 0
    country: Country = field(default_factory= Country)
    club_name: str = ""
    times_played: int = 0
    times_won: int = 0
    times_loses: int = 0
    times_drawn: int = 0
    goals_for: int = 0
    goals_against: int = 0
    points: int = 0
    goals_difference: int = 0

    def __post_init__(self):
        self.goals_difference = self.goals_for - self.goals_against

from dataclasses import dataclass
from datetime import date

@dataclass
class Country:
    name: str


@dataclass
class Club:
    name: str
    country: Country
    times_played: int
    times_won: int
    times_loses: int 
    times_drawn: int
    goals_for: int
    goals_against: int
    goals_difference: int
    points: int


    def __post_init__(self):
        self.times_played = self.times_drawn + self.times_won + self.times_loses
        self.goals_difference = self.goals_for - self.goals_against
        self.points = (self.times_won + 3) + self.times_drawn


@dataclass
class Matches:
    data: date
    clubs: list[Club]


@dataclass
class League:
    name: str
    country: Country
    matches: list[Matches]

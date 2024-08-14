from dataclasses import dataclass, field
from datetime import date

@dataclass(kw_only=True)
class Country:
    id: int = 0
    name: str


@dataclass(kw_only=True)
class Club:
    id: int = 0
    name: str
    country: Country


@dataclass(kw_only=True)
class Match:
    id: int = 0
    club: Club
    play_date: date
    times_played: int = 0
    times_won: int
    times_loses: int
    times_drawn: int
    goals_for: int
    goals_against: int
    goals_difference: int = 0
    points: int = 0


    def __post_init__(self) -> None:
        self.times_played = self.times_drawn + self.times_won + self.times_loses
        self.goals_difference = self.goals_for - self.goals_against
        if self.times_won != 0 or self.times_drawn != 0:
            self.points = (self.times_won * 3) + self.times_drawn

@dataclass(kw_only=True)
class League:
    id: int = 0
    name: str
    country: Country


@dataclass(kw_only=True)
class Competition:
    id: int = 0
    league: League
    clubs: list[Club]


@dataclass(kw_only=True)
class Matches:
    id: int = 0
    competition: Competition
    matches: list[Match]

from database.data import Data
from models import Club, Country, League, Match


def map_countries() -> list[str]:
    output: list[str] = []
    data: list[Country] = Data().read_countries()
    for country in data:
        output.append(country.name)
    return output


def map_teams(country_name: str) -> list[str]:
    output: list[str] = []
    country_id: int = Data().read_id_by_name("country", country_name)
    data: list[Club] = Data().read_teams_by_country_id(country_id)
    for team in data:
        output.append(team.name)
    return output


def map_leagues(country_name: str) -> list[str]:
    output: list[str] = []
    country_id: int = Data().read_id_by_name("country", country_name)
    data: list[League] = Data().read_leagues_by_country_id(country_id)
    for league in data:
        output.append(league.name)
    return output


def map_competition(league_name: str) -> list[str]:
    output: list[str] = []
    league_id: int = Data().read_id_by_name("league", league_name)
    data: list[int] = Data().read_club_ids_by_league_id(league_id)
    for club in data:
        output.append(Data().read_name_by_id("club", club))
    return output


def insert_country(dialog_text: str) -> None:
    Data().create_country(dialog_text)


def insert_team(country_name: str, dialog_text: str) -> None:
    country_id: int = Data().read_id_by_name("country", country_name)
    Data().create_team(country_id, dialog_text)


def insert_league(country_name: str, label_text: str) -> None:
    country_id: int = Data().read_id_by_name("country", country_name)
    Data().create_league(country_id, label_text)


def insert_competition(league_name: str, club_name: list[str]) -> None:
    league_id: int = Data().read_id_by_name("league", league_name)
    club_ids = list_club_ids(club_name)
    for club in club_ids:
        Data().create_competition(league_id, club)


def list_club_ids(club_name: list[str]) -> list[int]:
    output: list[int] = []
    for club in club_name:
        output.append(Data().read_id_by_name("club", club))
    return output


def validate_text(dialog_text: str) -> bool:
    output: bool = False
    if (dialog_text.lower().isdigit() == True or
            dialog_text.lower() == "" or 
            dialog_text.lower().isspace() == True):
        output = False
    else:
        output = True
    return output


def validate_comp(label: str, list_count: int) -> bool:
    output: bool = True
    if (label.lower() != "placeholder" and
            list_count > 0):
        output = False
    else:
        output = True
    return output

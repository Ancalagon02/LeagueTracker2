from database.data import Data
from models import Club, Country


def map_countries() -> list[str]:
    output: list[str] = []
    data: list[Country] = Data().read_countries()
    for country in data:
        output.append(country.name)
    return output


def map_teams(country_name: str) -> list[str]:
    output: list[str] = []
    country_id: int = Data().read_country_by_name(country_name)
    data: list[Club] = Data().read_teams_by_country_id(country_id)
    for team in data:
        output.append(team.name)
    return output


def insert_country(dialog_text: str) -> None:
    Data().create_country(dialog_text)


def insert_team(country_name: str, dialog_text: str) -> None:
    country_id: int = Data().read_country_by_name(country_name)
    Data().create_team(country_id, dialog_text)


def validate_text(dialog_text: str) -> bool:
    output: bool = False
    if (dialog_text.lower().isdigit() == True or
            dialog_text.lower() == "" or 
            dialog_text.lower().isspace() == True):
        output = False
    else:
        output = True
    return output

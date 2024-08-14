import database.data as data 
from modules.models import Club, Competition, Country, League


def create_country(country_name: str) -> None:
    country: Country = Country(name=country_name)
    data.create_country(country)


def return_country_names() -> list[str]:
    countries: list[Country] = data.read_countries()
    output: list[str] = []
    for country in countries:
        output.append(country.name)
    return output


def create_team(country_name: str, team_name: str) -> None:
    country: Country = data.read_country_by_country_name(country_name)
    team: Club = Club(
        name = team_name,
        country = country
    )
    data.create_team(team)


def return_team_names(country_name: str) -> list[str]:
    teams: list[Club] = data.read_teams_by_country_name(country_name)
    output: list[str] = []
    for team in teams:
        output.append(team.name)
    return output


def create_league(country_name: str, league_name: str) -> None:
    country: Country = data.read_country_by_country_name(country_name)
    league: League = League(
        name = league_name,
        country = country
    )    
    data.create_league(league)


def create_competition(teams: list[str], league_name: str) -> None:
    league: League = data.read_league_by_league_name(league_name)
    teams_list: list[Club] = return_teams(teams)
    competition: Competition = Competition(
        league = league,
        clubs = teams_list
    )
    data.create_competition(competition)


def return_teams(teams: list[str]) -> list[Club]:
    output: list[Club] = []
    for team in teams:
        output.append(data.read_team_by_team_name(team))
    return output

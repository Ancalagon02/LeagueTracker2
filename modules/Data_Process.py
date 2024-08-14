from datetime import date
import database.data as data 
from modules.models import Club, Competition, Country, League, Match, Matches


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


def create_match(team_name: str, play_date: date = date.today(), times_won: int = 0,
                 times_loses: int = 0, times_drawn: int = 0, goals_for: int = 0, goals_against: int = 0) -> None:
    team: Club = data.read_team_by_team_name(team_name)
    match: Match = Match(
        club = team,
        play_date = play_date,
        times_won = times_won,
        times_loses = times_loses,
        times_drawn = times_drawn,
        goals_for = goals_for,
        goals_against = goals_against
    )
    data.create_match(match)


def create_matches(teams: list[str], league_name: str) -> None:
    competition: Competition = data.read_competition_by_league_name(league_name)
    matches_list: list[Match] = return_matches(teams)
    matches: Matches = Matches(
        competition = competition,
        matches = matches_list
    )
    data.create_matches(matches)


def return_matches(teams: list[str]) -> list[Match]:
    output: list[Match] = []
    for match in teams:
        output.append(data.read_match_by_team_name(match))
    return output


def return_league_names(country_name: str) -> list[str]:
    leagues: list[League] = data.read_leagues_by_country_name(country_name)
    output: list[str] = []
    for league in leagues:
        output.append(league.name)
    return output


def return_competition(league_name: str, play_date: str) -> list[dict[str, str | int]]:
    matches: Matches = data.read_matches_by_league_name_and_date(league_name, str(play_date))
    output: list[dict[str, str | int]] = []
    for item in matches.matches:
        match = {
            "club_name": item.club.name,
            "times_played": item.times_played,
            "times_won": item.times_won,
            "times_loses": item.times_loses,
            "times_drawn": item.times_drawn,
            "goals_for": item.goals_for,
            "goals_against": item.goals_against,
            "goals_difference": item.goals_difference,
            "points": item.points
        }
        output.append(match)
    return output


def return_dates(league_name: str) -> list[str]:
    dates: list[str] = data.read_dates_by_league_name(league_name)
    return dates


def return_teams_for_match(league_name: str) -> list[str]:
    competition: Competition = data.read_competition_by_league_name(league_name)
    output: list[str] = []
    for team in competition.clubs:
        output.append(team.name)
    return output

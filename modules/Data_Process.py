from datetime import date, timedelta
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


def create_match(team_name: str, play_date: date = date.today() - timedelta(5), times_won: int = 0,
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
    matches: Matches = return_matches_by_last_date(league_name)
    output: list[str] = []
    for team in matches.competition.clubs:
        output.append(team.name)
    return output


def return_matches_by_last_date(league_name: str) -> Matches:
    date: str = data.read_last_date_by_league_name(league_name)
    matches: Matches = data.read_matches_by_league_name_and_date(league_name, date)
    return matches


def return_team(team_name: str, goals_for: int, goals_against: int, play_date: date) -> dict[str, str | int | date]:
    return {
        "team_name": team_name,
        "play_date": play_date,
        "times_won": 0,
        "times_loses": 0,
        "times_drawn": 0,
        "goals_for": goals_for,
        "goals_against": goals_against
    }


def process_matches(matches_dict: list[dict[str, str | int | date]], league_name: str, play_date: date) -> None:
    matches: Matches = return_matches_by_last_date(league_name)
    sorted_matches: list[Match] = sorted(matches.matches, key = lambda x: x.club.name)
    sorted_dict: list[dict[str, str | int | date]] = sorted(matches_dict, key = lambda x: x["team_name"])
    remove_list: list[Match] = []
    new_teams: list[Match] = create_new_teams(sorted_matches, sorted_dict, play_date, remove_list)
    for team in remove_list:
        sorted_matches.remove(team)
    create_other_new_teams(sorted_matches, play_date, new_teams)
    team_list: list[str] = create_match_from_match(new_teams)
    create_matches(team_list, league_name)


def create_other_new_teams(sorted_matches: list[Match], play_date: date, new_teams: list[Match]):
    for team in sorted_matches:
        new_match: Match = map_other_match(team, play_date)
        new_teams.append(new_match)


def create_match_from_match(new_teams: list[Match]) -> list[str]:
    output: list[str] = []
    for team in new_teams:
        output.append(team.club.name)
        print()
        print(team)
        data.create_match(team)
    return output


def create_new_teams(sorted_matches: list[Match], sorted_dict: list[dict[str, str | int | date]], play_date: date, remove_list: list[Match]) -> list[Match]:
    new_teams: list[Match] = []
    for team in sorted_matches:
        row: int = 0
        for match in sorted_dict:
            if match["team_name"] == team.club.name:
                new_match: Match = map_matches(team, sorted_dict[row], play_date)
                new_teams.append(new_match)
                remove_list.append(team)
            row += 1
    return new_teams


def create_matches_from_matches(league_name: str, matches_var: list[Match]) -> None:
    competiton: Competition = data.read_competition_by_league_name(league_name)
    matches: Matches = Matches(competition = competiton, matches = matches_var)
    data.create_matches(matches)


def map_other_match(team: Match, play_date: date) -> Match:
    new_team: Match = team
    new_team.play_date = play_date
    return new_team


def process_match(team_one: dict[str, str | int | date], team_two: dict[str, str | int | date]):
    dicide_winning_team(team_one, team_two)


def map_matches(team: Match, match:dict[str, str | int | date], play_date: date) -> Match:
    print(match["team_name"])
    print(team.club.name)
    print()
    if match["team_name"] == team.club.name:
        new_team: Match = map_team(team, match)
        return new_team
    else:
        new_team: Match = team
        new_team.play_date = play_date
        return new_team


def map_team(match: Match, team: dict) -> Match:
    output: Match = match
    match.play_date = team["play_date"]
    match.times_won += team["times_won"]
    match.times_loses += team["times_loses"]
    match.times_drawn += team["times_drawn"]
    match.goals_for += team["goals_for"]
    match.goals_against += team["goals_against"]
    return output


def dicide_winning_team(team_one: dict, team_two: dict):
    if team_one["goals_for"] > team_two["goals_for"]:
        team_one["times_won"] += 1
        team_two["times_loses"] += 1
    elif team_two["goals_for"] > team_one["goals_for"]:
        team_two["times_won"] += 1
        team_one["times_loses"] += 1
    elif team_two["goals_for"] == team_one["goals_for"]:
        team_one["times_drawn"] += 1
        team_two["times_drawn"] += 1

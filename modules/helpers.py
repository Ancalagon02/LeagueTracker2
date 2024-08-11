from datetime import date
import database.data as data


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


def return_first_match_team(name: str) -> dict:
    output: dict = {
        "name": name,
        "date": str(date.today().strftime("%d-%m-%y")),
        "times_won": 0,
        "times_loses": 0,
        "times_drawn": 0,
        "goals_for": 0,
        "goals_against": 0,
    }
    return output


def return_team(name: str, score: int, score_opponent: int, date: date) -> dict:
    output: dict = {
        "name": name,
        "date": str(date.strftime("%d-%m-%y")),
        "times_won": 0,
        "times_loses": 0,
        "times_drawn": 0,
        "goals_for": score,
        "goals_against": score_opponent,
    }
    return output


def process_match(team_one: dict, team_two: dict):
    team_one_from_db = data.read_latest_match_by_team_name(team_one["name"])
    team_two_from_db = data.read_latest_match_by_team_name(team_two["name"])
    dicide_winning_team(team_one, team_two)

    if team_one_from_db != []:
        map_match(team_one_from_db, team_one)

    if team_two_from_db != []:
        map_match(team_two_from_db, team_two)


def map_match(team_db: list[str | int], team: dict):
    team["times_won"] += team_db[0]
    team["times_loses"] += team_db[1]
    team["times_drawn"] += team_db[2]
    team["goals_for"] += team_db[3]
    team["goals_against"] += team_db[4]


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


def map_matches(league_name: str, club_names: list[str]) -> list[dict]:
    clubs = map_teams(club_names)
    dates = data.read_dates_by_league_name(league_name)
    output: list[dict] = []
    for date in dates:
        for match in clubs:
            team: dict = {
                "name": match[0],
                "times_played": (match[2] + match[3] + match[4]),
                "times_won": match[2],
                "times_loses": match[3],
                "times_drawn": match[4],
                "goals_for": match[5],
                "goals_against": match[6],
                "goals_difference": (match[5] - match[6]),
                "points": ((match[2] * 3) + match[4])
            }
            if date == match[1]:
                mat: dict = {
                    "date": date,
                    "team": team
                }
                output.append(mat)
    return output


def map_teams(club_names: list[str]) -> list:
    output: list = []
    for club in club_names:
        match = data.read_match_by_team_name(club)
        output.append(match)
    return output


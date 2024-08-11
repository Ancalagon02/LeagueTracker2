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


def create_team(name: str) -> dict:
    output: dict = {
        "name": name,
        "date": str(date.today().strftime("%d-%m-%y")),
        "times_played": 0,
        "times_won": 0,
        "times_loses": 0,
        "times_drawn": 0,
        "goals_for": 0,
        "goals_against": 0,
    }
    return output


def process_match(team_one: dict, team_two: dict):
    dicide_winning_team(team_one, team_two)



def map_match(team_db: list[str | int], team: dict):
    team["times_played"] += team_db[0]
    team["times_won"] += team_db[1]
    team["times_loses"] += team_db[2]
    team["times_drawn"] += team_db[3]
    team["goals_for"] += team_db[4]
    team["goals_against"] += team_db[5]


def dicide_winning_team(team_one: dict, team_two: dict):
    if team_one["goals_for"] > team_two["goals_for"]:
        team_one["times_won"] += 1
        team_two["times_loses"] += 1
        team_one["times_played"] += 1
        team_two["times_played"] += 1
    elif team_two["goals_for"] > team_one["goals_for"]:
        team_two["times_won"] += 1
        team_one["times_loses"] += 1
        team_one["times_played"] += 1
        team_two["times_played"] += 1
    elif team_two["goals_for"] == team_one["goals_for"]:
        team_one["times_drawn"] += 1
        team_two["times_drawn"] += 1
        team_one["times_played"] += 1
        team_two["times_played"] += 1


def map_matches(league_name: str) -> list[dict]:
    teams = data.read_teams_name_by_league_name(league_name)
    clubs = map_teams(teams)
    output: list[dict] = []
    for match in clubs:
        team: dict = {
            "name": match[0],
            "data": match[1],
            "times_played": match[2],
            "times_won": match[3],
            "times_loses": match[4],
            "times_drawn": match[5],
            "goals_for": match[6],
            "goals_against": match[7],
            "goals_difference": (match[6] - match[7]),
            "points": ((match[3] * 3) + match[5])
        }
        output.append(team)
    return output


def map_teams(club_names: list[str]) -> list:
    output: list = []
    for club in club_names:
        match = data.read_match_by_team_name(club)
        output.append(match)
    return output

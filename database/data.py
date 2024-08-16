from datetime import date
from database.create_database import DBConnections
from modules.models import Club, Competition, Country, League, Match, Matches


_db = DBConnections()

def create_country(model: Country) -> None:
    sql: str = """
            INSERT INTO country (name)
            VALUES (?)
            """
    data: tuple[str] = (model.name,)
    _db.execute(sql, data)


def read_countries() -> list[Country]:
    sql: str = """
            SELECT id, name
            FROM country
            """
    output: list[Country] = [] 
    rows = _db.fetchall(sql, data=())
    for row in rows:
        country: Country = Country(id = row[0], name = row[1])
        output.append(country)
    return output


def create_team(model: Club) -> None:
    sql: str = """
            INSERT INTO club (name, country_id)
            VALUES (?, ?)
            """
    data: tuple[str, int] = (model.name, model.country.id,)
    _db.execute(sql, data)


def read_country_by_country_name(country_name: str) -> Country:
    sql: str = """
            SELECT id, name
            FROM country
            WHERE name = ?
            """
    data: tuple[str] = (country_name,)
    row = _db.fetchall(sql, data)
    output: Country = Country(id = row[0][0], name = row[0][1])
    return output


def read_teams_by_country_name(country_name: str) -> list[Club]:
    sql: str = """
            SELECT club.id, club.name, country.id, country.name
            FROM club
            INNER JOIN country ON club.country_id = country.id
            Where country.name = ?
            """
    data: tuple[str] = (country_name,)
    rows = _db.fetchall(sql, data)
    output: list[Club] = []
    for row in rows:
        club = Club(id = row[0],name = row[1],
            country = Country(id = row[2], name = row[3]))
        output.append(club)
    return output


def create_league(model: League) -> None:
    sql: str = """
            INSERT INTO league (name, country_id)
            VALUES (?, ?)
            """
    data: tuple[str, int] = (model.name, model.country.id,)
    _db.execute(sql, data)


def read_league_by_league_name(league_name: str) -> League:
    sql: str = """
            SELECT league.id, league.name, country.id, country.name
            FROM league
            INNER JOIN country ON league.country_id = country.id
            WHERE league.name = ?
            """
    data: tuple[str] = (league_name,)
    row = _db.fetchall(sql, data)
    output: League = League(id = row[0][0] ,name = row[0][1],
        country = Country(id = row[0][2], name = row[0][3]))
    return output


def read_team_by_team_name(team_name: str) -> Club:
    sql: str = """
            SELECT club.id, club.name, country.id, country.name
            FROM club
            INNER JOIN country ON club.country_id = country.id
            WHERE club.name = ?
            """
    data: tuple[str] = (team_name,)
    row = _db.fetchall(sql, data)
    output: Club = Club(id = row[0][0], name = row[0][1],
        country = Country(id = row[0][2], name = row[0][3]))
    return output


def create_competition(model: Competition) -> None:
    sql: str = """
            INSERT INTO competition (league_id, club_id)
            VALUES (?, ?)
            """
    for team in model.clubs:
        data: tuple[int, int] = (model.league.id, team.id,)
        _db.execute(sql, data)


def create_match(model: Match) -> None:
    sql: str = """
            INSERT INTO match (club_id, date, times_won, times_loses, times_drawn, goals_for, goals_against)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """
    date = model.play_date.strftime("%d-%m-%y")
    data: tuple[int, str, int, int, int, int, int,] = (
        model.club.id, date, model.times_won, model.times_loses, model.times_drawn, model.goals_for, model.goals_against,)
    _db.execute(sql, data)


def create_matches(model: Matches) -> None:
    sql: str = """
            INSERT INTO matches (competition_id, match_id)
            VALUES (?, ?)
            """
    for match in model.matches:
        data: tuple[int, int] = (model.competition.id, match.id,)
        _db.execute(sql, data)


def read_match_by_team_name(team_name: str) -> Match:
    sql: str = """
            SELECT match.id, match.date, match.times_won, match.times_loses, match.times_drawn, match.goals_for, match.goals_against,
            club.id, club.name,
            country.id, country.name
            FROM match
            INNER JOIN club ON match.club_id = club.id
            INNER JOIN country ON club.country_id = country.id
            WHERE club.name = ?
            ORDER BY match.id DESC
            LIMIT 1
            """
    data: tuple[str] = (team_name,)
    row = _db.fetchall(sql, data)
    output: Match = Match(id = row[0][0], play_date = row[0][1], times_won = row[0][2], times_loses = row[0][3],
        times_drawn = row[0][4], goals_for = row[0][5], goals_against = row[0][6],
        club = Club(id = row[0][7], name = row[0][8],
            country = Country(id = row[0][9], name = row[0][10],)))
    return output


def read_competition_by_league_name(league_name: str) -> Competition:
    sql: str = """
            SELECT competition.id, league.id, league.name, club.id, club.name, country.id, country.name
            FROM competition
            INNER JOIN league ON competition.league_id = league.id
            INNER JOIN club ON competition.club_id = club.id
            INNER JOIN country ON club.country_id = country.id
            WHERE league.name = ?
            """
    data: tuple[str] = (league_name,)
    rows = _db.fetchall(sql, data)
    team_list: list[Club] = []
    for row in rows:
        club: Club = Club(id = row[3], name = row[4],
            country = Country(id = rows[0][5], name = rows[0][6]))
        team_list.append(club)
    output: Competition = Competition(id = rows[0][0],
        league = League(id = rows[0][1], name = rows[0][2],
            country = Country(id = rows[0][5], name = rows[0][6])),
        clubs = team_list
    )
    return output


def read_leagues_by_country_name(country_name: str) -> list[League]:
    sql: str = """
            SELECT league.id, league.name, country.id, country.name
            FROM league
            INNER JOIN country ON league.country_id = country.id
            WHERE country.name = ?
            """
    data: tuple[str] = (country_name,)
    rows = _db.fetchall(sql, data)
    output: list[League] = []
    for row in rows:
        league: League = League(id = row[0], name = row[1],
            country = Country(id = row[2], name = row[3]))
        output.append(league)
    return output


def read_matches_by_league_name_and_date(league_name: str, date: str) -> Matches:
    sql: str = """
            SELECT matches.id, competition.id, league.id, league.name, country.id, country.name,
            club.id, club.name, match.id, match.date, match.times_won, match.times_drawn,
            match.times_loses, match.goals_for, match.goals_against
            FROM matches
            INNER JOIN competition ON matches.competition_id = competition.id
            INNER JOIN league ON competition.league_id = league.id
            INNER JOIN club ON "match".club_id = club.id
            INNER JOIN country ON club.country_id = country.id
            INNER JOIN match ON matches.match_id = match.id
            WHERE match.date = ? AND league.name = ?
            """
    data: tuple[str, str] = (date, league_name,)
    rows = _db.fetchall(sql, data)
    matches_list: list[Match] = []
    club_list: list[Club] = []
    country_obj: Country = Country(id = rows[0][4], name = rows[0][5])
    league_obj: League = League(id = rows[0][2], name = rows[0][3], country = country_obj)
    for row in rows:
        club: Club = Club(id = row[6], name = row[7], country = country_obj)
        match: Match = Match(id = row[8], club = club, play_date = row[9], times_won = row[10],
            times_drawn = row[11], times_loses = row[12], goals_for = row[13], goals_against = row[14])
        matches_list.append(match)
        club_list.append(club)
    sort_matches = sorted(matches_list, key = lambda x: (x.points, x.goals_difference), reverse = True)
    output: Matches = Matches(id = rows[0][0],
        competition = Competition(id = rows[0][1], league = league_obj, clubs = club_list), 
        matches = sort_matches)
    return output


def read_dates_by_league_name(league_name: str) -> list[str]:
    sql: str = """
            SELECT DISTINCT match.date
            FROM matches
            INNER JOIN match on matches.match_id == match.id
            INNER JOIN competition ON matches.competition_id = competition.id
            INNER JOIN league on  competition.league_id = league.id
            WHERE league.name = ?
            """
    data: tuple[str] = (league_name,)
    rows = _db.fetchall(sql, data)
    output: list[str] = []
    for [row] in rows:
        output.append(row)
    return output


def read_last_date_by_league_name(league_name: str) -> str:
    sql: str = """
            SELECT DISTINCT match.date
            FROM matches
            INNER JOIN match on matches.match_id == match.id
            INNER JOIN competition ON matches.competition_id = competition.id
            INNER JOIN league on  competition.league_id = league.id
            WHERE league.name = ?
            ORDER BY match.id DESC
            LIMIT 1
            """
    data: tuple[str] = (league_name,)
    row = _db.fetchall(sql, data)
    output: str = row[0][0]
    return output

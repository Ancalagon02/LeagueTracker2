from database.create_database import DBConnections
from modules.models import Club, Competition, Country, League


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
        country: Country = Country(
            id = row[0],
            name = row[1]
        )
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
        club = Club(
            id = row[0],
            name = row[1],
            country = Country(
                id = row[2],
                name = row[3]
            )
        )
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
    output: League = League(
        id = row[0][0],
        name = row[0][1],
        country = Country(
            id = row[0][2],
            name = row[0][3]
        )
    )
    return output


def read_team_by_team_name(team: str) -> Club:
    sql: str = """
            SELECT club.id, club.name, country.id, country.name
            FROM club
            INNER JOIN country ON club.country_id = country.id
            WHERE club.name = ?
            """
    data: tuple[str] = (team,)
    row = _db.fetchall(sql, data)
    output: Club = Club(
        id = row[0][0],
        name = row[0][1],
        country = Country(
            id = row[0][2],
            name = row[0][3]
        )
    )
    return output


def create_competition(model: Competition) -> None:
    sql: str = """
            INSERT INTO competition (league_id, club_id)
            VALUES (?, ?)
            """
    for team in model.clubs:
        data: tuple[int, int] = (model.league.id, team.id,)
        _db.execute(sql, data)

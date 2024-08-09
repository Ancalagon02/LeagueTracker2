from database.create_database import DBConnections


_db = DBConnections()


def create_country(country_name: str) -> None:
    sql = """
        INSERT INTO country (name)
        VALUES (?)
        """
    data = (country_name,)
    _db.execute(sql, data)


def create_team(team_name: str, country_name: str) -> None:
    country_id = read_country_id_by_country_name(country_name)
    sql = """
        INSERT INTO club (name, country_id)
        VALUES (?, ?)
        """
    data = (team_name, country_id,)
    _db.execute(sql, data)        


def create_league(league_name: str, country_name: str) -> None:
    country_id = read_country_id_by_country_name(country_name)
    sql = """
        INSERT INTO league (name, country_id)
        VALUES (?, ?)
        """
    data = (league_name, country_id,)
    _db.execute(sql, data)


def create_competition(league_name: str, club_name: str) -> None:
    league_id = read_league_id_by_league_name(league_name)
    club_id = read_team_id_by_team_name(club_name)
    sql = """
        INSERT INTO competition (league_id, club_id)
        VALUES (?, ?)
        """
    data = (league_id, club_id,)
    _db.execute(sql, data)


def read_countries() -> list[str]:
    sql = """
        SELECT name
        FROM country
        """
    output: list[str] = []
    rows = _db.fetchall(sql, data=())
    for [row] in rows:
        output.append(row)
    return output


def read_country_id_by_country_name(country_name: str) -> int:
    sql = """
        SELECT id
        FROM country
        WHERE name = ?
        """
    data = (country_name,)
    output: int = 0
    row = _db.fetchone(sql, data)
    if row != None:
        id = row[0]
        output = id
    return output


def read_team_id_by_team_name(team_name: str) -> int:
    sql = """
        SELECT id
        FROM club
        WHERE name = ?
        """
    data = (team_name,)
    output: int = 0
    row = _db.fetchone(sql, data)
    if row != None:
        id = row[0]
        output = id
    return output


def read_league_id_by_league_name(league_name: str) -> int:
    sql = """
        SELECT id
        FROM league
        WHERE name = ?
        """
    data = (league_name,)
    output: int = 0
    row = _db.fetchone(sql, data)
    if row != None:
        id = row[0]
        output = id
    return output


def read_team_name_by_id(club_id: int) -> str:
    sql = """
        SELECT name
        FROM club
        WHERE id = ?
        """
    data = (club_id,)
    output: str = ""
    row = _db.fetchone(sql, data)
    if row != None:
        name = row[0]
        output = name
    return output


def read_team_id_by_league_id(league_id: int) -> list[int]:
    sql = """
        SELECT club_id
        FROM competition
        WHERE league_id = ?
        """
    data = (league_id,)
    output: list[int] = []
    rows = _db.fetchall(sql, data)
    for [row] in rows:
        output.append(row)
    return output


def read_teams_name_by_country_name(country_name: str) -> list[str]:
    country_id = read_country_id_by_country_name(country_name)
    sql = """
        SELECT name
        FROM club
        WHERE country_id = ?
        """
    data = (country_id,)
    output: list[str] = []
    rows = _db.fetchall(sql, data)
    for [row] in rows:
        output.append(row)
    return output


def read_leagues_name_by_country_name(country_name: str) -> list[str]:
    country_id = read_country_id_by_country_name(country_name)
    sql = """
        SELECT name
        FROM league
        WHERE country_id = ?
        """
    data = (country_id,)
    output: list[str] = []
    rows = _db.fetchall(sql, data)
    for [row] in rows:
        output.append(row)
    return output


def read_teams_name_by_league_name(league_name: str) -> list[str]:
    league_id = read_league_id_by_league_name(league_name)
    club_ids = read_team_id_by_league_id(league_id)
    output: list[str] = []
    for id in club_ids:
        club = read_team_name_by_id(id)
        output.append(club)
    return output

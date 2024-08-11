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


def create_match(match: dict) -> None:
    team_id = read_team_id_by_team_name(match["name"])
    sql = """
        INSERT INTO match (club_id, data, times_won, times_loses, times_drawn, goals_for, goals_against)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
    data = (team_id, match["date"], match["times_won"], match["times_loses"], match["times_drawn"],
            match["goals_for"], match["goals_against"],)
    _db.execute(sql, data)


def create_matches(league_name: str, team_name: str) -> None:
    competition_id = read_competition_id_by_league_name(league_name)
    team_id = read_team_id_by_team_name(team_name)
    match_id = read_match_id_by_club_id(team_id)
    sql = """
        INSERT INTO matches (competition_id, match_id)
        VALUES (?, ?)
        """
    data = (competition_id, match_id)
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


def read_match_id_by_club_id(club_id: int) -> int:
    sql = """
        SELECT id
        FROM match
        WHERE club_id = ?
        ORDER BY id DESC
        LIMIT 1
        """
    data = (club_id,)
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


def read_competition_id_by_league_name(league_name: str) -> int:
    league_id = read_league_id_by_league_name(league_name)
    sql = """
        SELECT id
        from competition
        WHERE league_id = ?
        """
    output: int = 0
    data = (league_id,)
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


def read_latest_match_by_team_name(team_name: str) -> list[str | int]:
    club_id = read_team_id_by_team_name(team_name)
    sql = """
        SELECT times_won, times_loses, times_drawn, goals_for, goals_against
        FROM match
        WHERE club_id = ?
        ORDER BY id DESC
        LIMIT 1
        """
    data = (club_id,)
    output: list[str | int] = []
    rows = _db.fetchone(sql, data)
    if rows != None:
        for row in rows:
            output.append(row)
    return output


def read_matches_by_league_name(league_name: str) -> list:
    competition_id = read_competition_id_by_league_name(league_name)
    sql = """
        Select club.name, match.data, match.times_won, match.times_loses, match.times_drawn, match.goals_for, match.goals_against
        FROM matches
        INNER JOIN club on match.club_id == club.id
        INNER JOIN match on matches.match_id == match.id
        WHERE matches.competition_id = ?
        """
    data = (competition_id,)
    output: list = []
    rows = _db.fetchall(sql, data)
    for row in rows:
        output.append(row)
    return output


def read_dates_by_league_name(league_name: str) -> list[str]:
    competition_id = read_competition_id_by_league_name(league_name)
    sql = """
        SELECT DISTINCT match.data
        FROM matches
        INNER JOIN match on matches.match_id == match.id
        WHERE matches.competition_id = ?
        """
    data = (competition_id,)
    output: list[str] = []
    rows = _db.fetchall(sql, data)
    for [row] in rows:
        output.append(row)
    return output


def read_match_by_team_name(team_name: str) -> list:
    club_id = read_team_id_by_team_name(team_name)
    sql = """
        SELECT club.name, match.data, match.times_won, match.times_loses, match.times_drawn, match.goals_for, match.goals_against
        FROM match
        INNER JOIN club on match.club_id == club.id
        WHERE club_id = ?
        ORDER BY match.id DESC
        LIMIT 1
        """
    data = (club_id,)
    output: list[str | int] = []
    rows = _db.fetchone(sql, data)
    if rows != None:
        for row in rows:
            output.append(row)
    return output

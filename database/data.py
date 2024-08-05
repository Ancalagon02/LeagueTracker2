from database.create_database import DBConnections
from modules.models import Club, Country, League


class Data(DBConnections):
    def __init__(self) -> None:
        super().__init__()


    def create_country(self, country_name: str) -> None:
        sql = """
            INSERT INTO country (name)
            VALUES(?)
            """
        data = (country_name,)
        self.execute(sql, data)


    def create_team(self, country_id: int, club_name: str) -> None:
        sql = """
            INSERT INTO club (name, country_id)
            VALUES(?,?)
            """
        data = (club_name, country_id,)
        self.execute(sql, data)


    def create_league(self, country_id: int, league_name: str) -> None:
        sql = """
            INSERT INTO league (name, country_id)
            VALUES(?,?)
            """
        data = (league_name, country_id,)
        self.execute(sql, data)


    def create_competition(self, league_id: int, club_id: int) -> None:
        sql = """
            INSERT INTO competition (league_id, club_id)
            VALUES(?,?)
            """
        data = (league_id, club_id,)
        self.execute(sql, data)


    def read_id_by_name(self, table_name: str, name: str) -> int:
        sql = f"""
            SELECT id
            FROM {table_name}
            WHERE name =?
            """
        data = (name,)
        output: int = 0
        row = self.fetchone(sql, data)
        if row != None:
            id = row[0]
            output = id
        return output


    def read_name_by_id(self, table_name: str, id: int) -> str:
        sql = f"""
            SELECT name
            FROM {table_name}
            WHERE id =?
            """
        data = (id,)
        output: str = ""
        row = self.fetchone(sql, data)
        if row != None:
            name = row[0]
            output = name
        return output


    def read_countries(self) -> list[Country]:
        sql = """ 
            SELECT name
            FROM country
            """
        output: list[Country] = []
        rows = self.fetchall(sql, data=())
        for [row] in rows:
            country = Country(name=row)
            output.append(country)
        return output


    def read_teams_by_country_id(self, country_id: int) -> list[Club]:
        sql = """
            SELECT club.name, country.name
            FROM club
            INNER JOIN country ON country.id = club.country_id
            WHERE country_id =?
            """
        data = (country_id,)
        output: list[Club] = []
        rows = self.fetchall(sql, data)
        for row in rows:
            club = Club(name=row[0], country=Country(name=row[1]))
            output.append(club)
        return output


    def read_leagues_by_country_id(self, country_id: int) -> list[League]:
        sql = """
            SELECT league.name, country.name
            FROM league
            INNER JOIN country ON country.id = league.country_id
            WHERE country_id =?
            """
        data = (country_id,)
        output: list[League] = []
        rows = self.fetchall(sql, data)
        for row in rows:
            league = League(name=row[0], country=Country(name=row[1]))
            output.append(league)
        return output

    
    def read_club_ids_by_league_id(self, league_id: int) -> list[int]:
        sql = """
            SELECT club_id
            FROM competition
            WHERE league_id =?
            """
        data = (league_id,)
        output: list[int] = []
        rows = self.fetchall(sql, data)
        for row in rows:
            output.append(row[0])
        return output

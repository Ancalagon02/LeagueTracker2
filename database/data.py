import sqlite3
from database.create_database import CreateDatabase
from models import Club, Country


class Data(CreateDatabase):
    def __init__(self) -> None:
        super().__init__()


    def read_countries(self) -> list[Country]:
        sql = """ 
            SELECT name
            FROM country
            """
        data: list[Country] = []
        try:
            with sqlite3.connect(self.db_file) as conn:
                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
            for [row] in rows:
                country = Country(name=row)
                data.append(country)
        except sqlite3.Error as e:
            print(e)
            return []
        return data


    def create_country(self, country_name: str) -> None:
        sql = """
            INSERT INTO country (name)
            VALUES(?)
            """
        data = (country_name,)
        try:
            with sqlite3.connect(self.db_file) as conn:
                cur = conn.cursor()
                cur.execute(sql, data)

        except sqlite3.Error as e:
            print(e)


    def create_team(self, country_id: int, club_name: str) -> None:
        sql = """
            INSERT INTO club (name, country_id)
            VALUES(?,?)
            """
        data = (club_name, country_id,)
        try:
            with sqlite3.connect(self.db_file) as conn:
                cur = conn.cursor()
                cur.execute(sql, data)
        except sqlite3.Error as e:
            print(e)


    def read_country_by_name(self, country_name: str) -> int:
        sql = """
            SELECT id
            FROM country
            WHERE name =?
            """
        data = (country_name,)
        try:
            with sqlite3.connect(self.db_file) as conn:
                cur = conn.cursor()
                cur.execute(sql, data)
                return int(cur.fetchone()[0])
        except sqlite3.Error as e:
            print(e)
            return 0


    def read_teams_by_country_id(self, country_id: int) -> list[Club]:
        sql = """
            SELECT club.name, country.name
            FROM club
            INNER JOIN country ON country.id = club.country_id
            WHERE country_id =?
            """
        data = (country_id,)
        output: list[Club] = []
        try:
            with sqlite3.connect(self.db_file) as conn:
                cur = conn.cursor()
                cur.execute(sql, data)
                rows = cur.fetchall()
            for row in rows:
                club = Club(name=row[0], country=Country(name=row[1]))
                output.append(club)
        except sqlite3.Error as e:
            print(e)
            return []
        return output

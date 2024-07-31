import sqlite3
from database.create_database import CreateDatabase


class Data(CreateDatabase):
    def __init__(self):
        super().__init__()


    def read_countries(self) -> list[str]:
        sql = """ 
            SELECT name
            FROM country
            """
        data = []
        try:
            with sqlite3.connect(self.db_file) as conn:
                cur = conn.cursor()
                cur.execute(sql)
                rows = cur.fetchall()
            for [row] in rows:
                data.append(row)
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


    def read_teams_by_country_id(self, country_id: int) -> list[str]:
        sql = """
            SELECT name
            FROM club
            WHERE country_id =?
            """
        data = (country_id,)
        output = []
        try:
            with sqlite3.connect(self.db_file) as conn:
                cur = conn.cursor()
                cur.execute(sql, data)
                rows = cur.fetchmany()
            for [row] in rows:
                output.append(row)
        except sqlite3.Error as e:
            print(e)
            return []
        return output

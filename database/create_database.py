from abc import ABC
import sqlite3

class CreateDatabase(ABC):
    def __init__(self) -> None:
        self.db_file = "leaguetracker.db"


    def create_table(self) -> None:
        sql_statement = [
            """CREATE TABLE IF NOT EXISTS country (
	            id INTEGER PRIMARY KEY AUTOINCREMENT,
	            name TEXT NOT NULL UNIQUE
            );""",
            """CREATE TABLE IF NOT EXISTS club (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                country_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                FOREIGN KEY (country_id) REFERENCES country(id)
            );""",
            """CREATE TABLE IF NOT EXISTS league (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                country_id INTEGER NOT NULL,
                name TEXT NOT NULL UNIQUE,
                FOREIGN KEY (country_id) REFERENCES country(id)
            );""",
            """CREATE TABLE IF NOT EXISTS match (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                club_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                times_won INTEGER NOT NULL,
                times_loses INTEGER NOT NULL,
                times_drawn INTEGER NOT NULL,
                goals_for INTEGER NOT NULL,
                goals_against INTEGER NOT NULL,
                FOREIGN KEY (club_id) REFERENCES club(id)
            );""",
            """CREATE TABLE IF NOT EXISTS competition (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                league_id INTEGER NOT NULL,
                club_id INTEGER NOT NULL,
                FOREIGN KEY (league_id) REFERENCES league(id),
                FOREIGN KEY (club_id) REFERENCES club(id)
            );""",
            """CREATE TABLE IF NOT EXISTS matches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                competition_id INTEGER NOT NULL,
                match_id INTEGER NOT NULL,
                FOREIGN KEY (competition_id) REFERENCES competition(id),
                FOREIGN KEY (match_id) REFERENCES match(id)
            );"""]

        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                for statement in sql_statement:
                    cursor.execute(statement)

                conn.commit()

        except sqlite3.Error as e:
            print(e)


class DBConnections(CreateDatabase, ABC):
    def execute(self, sql: str, data: tuple) -> None:
        try:
            with sqlite3.connect(self.db_file) as conn:
                cur = conn.cursor()
                cur.execute(sql, data)
        except sqlite3.Error as e:
            print(e)


    def fetchall(self, sql: str, data: tuple) -> list:
        output: list = []
        try:
            with sqlite3.connect(self.db_file) as conn:
                cur = conn.cursor()
                cur.execute(sql, data)
                output = cur.fetchall()
        except sqlite3.Error as e:
            print(e)
        return output


    def fetchone(self, sql:str, data: tuple):
        output = None
        try:
            with sqlite3.connect(self.db_file) as conn:
                cur = conn.cursor()
                cur.execute(sql, data)
                output = cur.fetchone()
        except sqlite3.Error as e:
            print(e)
        return output

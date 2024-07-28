import sqlite3

db_file = "leaguetracker.db"

def create_table():
    sql_statement = [
        """CREATE TABLE IF NOT EXISTS country (
	        id INTEGER PRIMARY KEY AUTOINCREMENT,
	        name TEXT NOT NULL UNIQUE
        );""",
        """CREATE TABLE IF NOT EXISTS club (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country_id INTEGER NOT NULL,
            name TEXT NOT NULL UNIQUE,
            FOREIGN KEY (country_id) REFERENCES country(id)
        );""",
        """CREATE TABLE IF NOT EXISTS league (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country_id INTEGER NOT NULL,
            name TEXT NOT NULL UNIQUE,
            FOREIGN KEY (country_id) REFERENCES country(id)
        );""",
        """CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            club_id INTEGER NOT NULL,
            data TEXT NOT NULL,
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
            matches_id INTEGER NOT NULL,
            FOREIGN KEY (league_id) REFERENCES league(id),
            FOREIGN KEY (matches_id) REFERENCES matches(id)
        );"""]

    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            for statement in sql_statement:
                cursor.execute(statement)

            conn.commit()

    except sqlite3.Error as e:
        print(e)

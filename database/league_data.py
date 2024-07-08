import sqlite3
from models.country import Country
from models.league import League

class LeagueData():
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()


    def insert_league(self, league_name: str, country_id: int):
        query: str = "INSERT INTO league (name, country_id) VALUES (?, ?)"
        data = (league_name, country_id,)

        self.cur.execute(query, data)
        self.conn.commit()


    def load_league(self, league_id: int) -> League:
        query: str = "SELECT id, country_id, name FROM league WHERE id = (?)"
        data = (league_id,)
        id, country_id, league_name = self.cur.execute(query, data).fetchone()

        query = "SELECT id, name FROM country WHERE id = (?)"
        data = (country_id,)
        country_id, country_name = self.cur.execute(query, data).fetchone()

        output = League(
                id = id,
                name = league_name,
                country = Country(
                id = country_id,
                name = country_name
        ))

        return output


    def load_leagues(self, country_id: int) -> list[League]:
        query: str = "SELECT id, country_id, name FROM league WHERE country_id = (?)"
        data = (country_id,)
        db_leagues = self.cur.execute(query, data).fetchall()
        
        query = "SELECT id, name FROM country WHERE id = (?)"
        country_id, country_name = self.cur.execute(query, data).fetchone()

        output: list[League] = []
        for id, country_id, name in db_leagues:
            league = League(
                    id = id,
                    name = name,
                    country = Country(
                    id = country_id,
                    name = country_name
            ))
            output.append(league)

        return output


    def __del__(self):
        self.conn.close()

import sqlite3
from models.club import Club
from models.country import Country


class ClubData():
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()


    def insert_club(self, club_name: str, country_id: int):
        query: str = "INSERT INTO club (name, country_id) VALUES (?, ?)"
        data = (club_name, country_id,)

        self.cur.execute(query, data)
        self.conn.commit()


    def load_club(self, club_id: int) -> Club:
        query: str = "SELECT id, country_id, name FROM club WHERE id = (?)"
        data = (club_id,)
        id, country_id, club_name = self.cur.execute(query, data).fetchone()

        query = "SELECT id, name FROM country WHERE id = (?)"
        data = (country_id,)
        country_id, country_name = self.cur.execute(query, data).fetchone()

        output = Club(
                id = id,
                club_name = club_name,
                country = Country(
                id = country_id,
                name = country_name
        ))

        return output


    def load_clubs(self, country_id: int) -> list[Club]:
        query: str = "SELECT id, country_id, name FROM club WHERE country_id = (?)"
        data = (country_id,)
        db_clubs = self.cur.execute(query, data).fetchall()
        
        query = "SELECT id, name FROM country WHERE id = (?)"
        country_id, country_name = self.cur.execute(query, data).fetchone()

        output: list[Club] = []
        for id, country_id, name in db_clubs:
            club = Club(
                    id = id,
                    club_name = name,
                    country = Country(
                    id = country_id,
                    name = country_name
            ))
            output.append(club)

        return output


    def __del__(self):
        self.conn.close()


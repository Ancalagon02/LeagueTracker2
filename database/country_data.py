import sqlite3
from models.country import Country

class CountryData():
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()


    def insert_country(self, country_name: str):
        query: str = "INSERT INTO country (name) VALUES (?)"
        data = (country_name,)

        self.cur.execute(query, data)
        self.conn.commit()


    def load_country(self, country_id: int) -> Country:
        query: str = "SELECT id, name FROM country WHERE id = (?)"
        data = (country_id,)

        id, name = self.cur.execute(query, data).fetchone()

        output = Country(
                id = id,
                name = name
        )

        return output

    
    def load_countries(self) -> list[Country]:
        query: str = "SELECT id, name FROM country"

        countries = self.cur.execute(query).fetchall()

        output: list[Country] = []

        for id, name in countries:
            country = Country(
                    id = id,
                    name = name
            )
            output.append(country)

        return output

    
    def __del__(self):
        self.conn.close()

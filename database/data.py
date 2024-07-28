import sqlite3
from models import Country

db_file = "leaguetracker.db"

def load_countrys() -> list[Country]:
    sql = """ 
        SELECT name
        FROM country
        """
    output: list[Country] = []
    try:
        with sqlite3.connect(db_file) as conn:
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()

            for [row] in rows:
                country = Country(name = row)
                output.append(country)                

            return output 
    except sqlite3.Error as e:
        print(e)
        return []


def get_country_id_by_name(country_name: str) -> int:
    sql = """
        SELECT id
        FROM country
        WHERE name =?
        """
    data = (country_name,)

    try:
        with sqlite3.connect(db_file) as conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return int(cur.fetchone()[0])

    except sqlite3.Error as e:
        print(e)
        return 0

import sqlite3
from models import Country


def load_countrys(sql_file) -> list[Country]:
    sql = """ SELECT name
              FROM country """
    output: list[Country] = []
    try:
        with sqlite3.connect(sql_file) as conn:
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

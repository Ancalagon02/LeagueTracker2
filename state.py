from models import Country
import database.data as data


def get_countries():
    output: list = []
    countries: list[Country] = data.load_countrys()

    for country in countries:
        output.append(country.name)

    return output


from database.club_data import ClubData
from database.league_data import LeagueData


def main():
    database = "LTracker.db"

    lgd = ClubData(database)
    
if __name__ == "__main__":
    main()

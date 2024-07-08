import sqlite3
from models.club import Club
from models.competition import Competition
from models.country import Country

class CompetitionData():
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()


    def insert_club(self, league_id: int, club_id: int):
        query: str = "INSERT INTO competition (league_id, club_id) VALUES (?, ?)"
        data = (league_id, club_id,)

        self.cur.execute(query, data)
        self.conn.commit()

    
    def load_competition(self, league_id: int) -> Competition:
        query: str = "SELECT id, club_id FROM competition WHERE league_id = (?)"
        data = (league_id,)
        id, club_id = self.cur.execute(query, data).fetchall()
        
        clubs: list[Club] = []
        for club in club_id:
            query = "SELECT id, country_id, name FROM club WHERE id = (?)"
            data = (club,)
            id, country_id, name = self.cur.execute(query, data).fetchone()

            query = "SELECT id, name FROM country WHERE id = (?)"
            data = (country_id,)
            country_id, country_name = self.cur.execute(query, data).fetchone()

            query = "SELECT times_played, times_won, times_loses, times_drawn, goals_for, goals_against, points FROM competition where league_id = (?) AND club_id = (?)"
            data = (league_id, club_id,)
            times_played, times_won, times_loses, times_drawn, goals_for, goals_against, points = self.cur.execute(query, data).fetchone()
            
            team = Club(
                id = id,
                club_name = name,
                times_played = times_played,
                times_won = times_won,
                times_loses = times_loses,
                times_drawn = times_drawn,
                goals_for = goals_for,
                goals_against = goals_against,
                points = points,
                country = Country(
                    id = country_id, 
                    name = country_name
                ))

            clubs.append(team)

        query = "SELECT name FROM league WHERE id = (?)"
        data = (league_id,)
        name = self.cur.execute(query, data).fetchone()

        output = Competition(
                id = id,
                name = name,
                clubs = clubs
        )
                
        return output 


    def update_competition(self, league_id: int, club_id: int, team: Club):
        query: str = """UPDATE competition 
        SET time_played = (?), times_won = (?), times_Loses = (?), times_drawn = (?), goals_for = (?), goals_against = (?), points = (?)
        WHERE league_id = (?) AND club_Id = (?)
        """
        data = (team.times_played, team.times_won, team.times_loses, team.times_drawn, team.goals_for, team.goals_against, team.points, league_id, club_id)
        self.cur.execute(query, data)
        self.conn.commit()


    def __del__(self):
        self.conn.close()

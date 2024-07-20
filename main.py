from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.create_country import CreateCountry
from ui.create_team import CreateTeam
from ui.match import Match
from ui.create_competition import CreateCompetition
from ui.competition import Competition
from ui.create_competition_name import CreateCompetitionName
import sys

def main():
    app = QApplication([])

    competition = Competition()
    #competition.show()

    mainwindow = MainWindow()
    #mainwindow.show()

    createcountry = CreateCountry()
    #createcountry.show()

    createteam = CreateTeam()
    #createteam.show()

    match = Match()
    #match.show()

    createcompetition = CreateCompetition()
    #createcompetition.show()

    createcompetitionname = CreateCompetitionName()
    createcompetitionname.show()

    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()

from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.match import Match
from ui.create_competition import CreateCompetition
from ui.competition import Competition
import sys

def main():
    app = QApplication([])

    competition = Competition()
    #competition.show()

    mainwindow = MainWindow()
    #mainwindow.show()

    match = Match()
    #match.show()

    createcompetition = CreateCompetition()
    createcompetition.show()

    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()

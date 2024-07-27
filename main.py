from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.create_competition import CreateCompetition
from ui.competition import Competition
import sys
import database.create_database as db

file = "style.css"

def main():
    app = QApplication([])

    with open(file, "r") as fh:
        app.setStyleSheet(fh.read())

    competition = Competition()
    competition.show()

    mainwindow = MainWindow()
    #mainwindow.show()

    createcompetition = CreateCompetition()
    #createcompetition.show()

    db.create_table()

    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()

from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.create_competition import CreateCompetition
from ui.competition import Competition
import sys

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

    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()

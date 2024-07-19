from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.create_country import CreateCountry
from ui.create_team import CreateTeam
from ui.match import Match
import sys

def main():
    app = QApplication([])
    window = Match()
    window.show()

    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()

from PyQt6.QtWidgets import QApplication
import sys
from ui.main_window import MainWindow
from ui.create_league import CreateLeague 
from ui.competition import Competition

def main():
    app = QApplication([])
    window = Competition()
    window.show()

    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()

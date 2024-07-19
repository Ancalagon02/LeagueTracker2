from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.create_country import CreateCountry
import sys

def main():
    app = QApplication([])
    window = CreateCountry()
    window.show()

    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()

from PyQt6.QtWidgets import QApplication
import sys
from state import State
from database.data import Data

file = "style.css"
def main():
    app = QApplication([])

    outer = State()
    data = Data()
    data.create_table()

    with open(file, "r") as fh:
        app.setStyleSheet(fh.read())


    outer.create_window()
    

    sys.exit(app.exec())

    
if __name__ == "__main__":
    main()

from PyQt6.QtWidgets import QApplication
import sys
from database.data import Data
from state import State


def main(file: str) -> None:
    app = QApplication([])

    db = Data()
    db.create_table()

    with open(file, "r") as fh:
        app.setStyleSheet(fh.read())

    state = State()
    state.init_main_window()

    sys.exit(app.exec())

    
if __name__ == "__main__":
    file = "style.css"
    main(file)

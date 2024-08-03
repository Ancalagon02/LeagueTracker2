#!/usr/bin/env python3
from PyQt6.QtWidgets import QApplication
import sys
from state import State
from database.data import Data


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

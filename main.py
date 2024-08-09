#!/usr/bin/env python3
from PyQt6.QtWidgets import QApplication
import sys
from modules.state import State
from database.create_database import DBConnections


def main(file: str) -> None:
    app = QApplication([])

    db = DBConnections()
    db.create_table()

    with open(file, "r") as fh:
        app.setStyleSheet(fh.read())

    state = State()
    state.init_main_window()

    sys.exit(app.exec())

    
if __name__ == "__main__":
    file = "style.css"
    main(file)

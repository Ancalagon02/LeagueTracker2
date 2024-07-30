from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
import sys
import database.data as data
import database.create_database as db

file = "style.css"

def main():
    app = QApplication([])

    db.create_table()
    with open(file, "r") as fh:
        app.setStyleSheet(fh.read())

    mainwindow = MainWindow()
    mainwindow.show()


    sys.exit(app.exec())

    
if __name__ == "__main__":
    main()

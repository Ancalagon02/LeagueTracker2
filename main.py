from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
import sys
import database.data as data

file = "style.css"

def main():
    app = QApplication([])

    with open(file, "r") as fh:
        app.setStyleSheet(fh.read())

    mainwindow = MainWindow()
    mainwindow.show()


    #db.create_table()

    sys.exit(app.exec())

    
if __name__ == "__main__":
    main()

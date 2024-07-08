from .create_league import CreateLeague
from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout, QPushButton
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 300)
        self.create_window()


    def create_window(self):
        self.grid = QGridLayout()
        self.label = QLabel()
        self.label.setText("league Tracker")
        self.label.setStyleSheet("border: 1px solid; padding: 3px; margin: 3px; font-size: 15px;")
        self.create_new_league_button = QPushButton("Nieuw Competitie")
        self.load_league = QPushButton("Laad Competitie")
        self.exit_app = QPushButton("Exit")

        self.grid.addWidget(self.label, 0, 0, 0, 3,
                            alignment=Qt.AlignmentFlag.AlignCenter)
        self.grid.addWidget(self.create_new_league_button, 1, 0)
        self.grid.addWidget(self.load_league, 1, 1)
        self.grid.addWidget(self.exit_app, 1, 2)

        self.setLayout(self.grid)

        self.create_new_league_button.clicked.connect(self.show_league)


    def show_league(self):
        self.league = CreateLeague()
        self.hide()
        self.league.show()

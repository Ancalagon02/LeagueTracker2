from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class CreateLeague(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 300)
        self.create_window()


    def create_window(self):
        self.grid = QGridLayout()

        self.league_name_label = QLabel("Enter Competitie Naam")
        self.league_name_edit = QTextEdit()

        self.team_label = QLabel("Enter Ploeg")
        self.team_edit = QTextEdit()
        self.team_Button = QPushButton("Enter")

        self.create_league_button = QPushButton("Maak Competitie")
        self.back_button = QPushButton("Ga Terug")

        self.grid.addWidget(self.league_name_label, 0, 0)
        self.grid.addWidget(self.league_name_edit, 0, 1)
        self.grid.addWidget(self.team_label, 1, 0)
        self.grid.addWidget(self.team_edit, 1, 1)
        self.grid.addWidget(self.team_Button, 1, 2)
        self.grid.addWidget(self.create_league_button, 2, 0)
        self.grid.addWidget(self.back_button, 2, 1)

        self.setLayout(self.grid)

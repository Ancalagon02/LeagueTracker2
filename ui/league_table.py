from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class LeagueTable(QWidget):
    def __init__(self):
        super().__init__()
        self.create_window()

    
    def create_window(self):
        self.grid = QGridLayout()

        self.table = QTableWidget(16, 10)
        self.table.setHorizontalHeaderLabels(["Pos", "Team", "P", "W", "L", "D", "F", "A", "GD", "Pts"])
        
        self.team_list_label = QLabel("Teams")
        self.team_list = QListWidget()

        self.team_one = QLabel("Team One")
        self.team_one_score = QSpinBox()

        self.team_two = QLabel("Team Two")
        self.team_two_score = QSpinBox()

        self.submit_score = QPushButton("Submit")

        self.grid.addWidget(self.table, 0, 0, -1, 1)
        self.grid.addWidget(self.team_list_label, 0, 1, 1, 2)
        self.grid.addWidget(self.team_list, 1, 1 ,1 ,2)
        self.grid.addWidget(self.team_one, 2, 1, 1, 1)
        self.grid.addWidget(self.team_one_score, 3, 1, 1, 1)
        self.grid.addWidget(self.team_two, 4, 1, 1, 1)
        self.grid.addWidget(self.team_two_score, 5, 1, 1, 1)
        self.grid.addWidget(self.submit_score, 6, 1, 1, 2)

        self.setLayout(self.grid)

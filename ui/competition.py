from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Competition(QWidget):
    def __init__(self):
        super().__init__()
        self.competition_label = QLabel()
        self.competition_name_label = QLabel()
        self.start_matches_button = QPushButton()
        self.go_back_to_main_button = QPushButton()

        self.competition_table = QTableWidget()

        self.create_window()


    def create_window(self):
        self.set_layout()
        self.set_labels()


    def set_layout(self):
        self.master = QVBoxLayout()

        self.row1 = QHBoxLayout()
        self.row1.addWidget(self.competition_label)
        self.row1.addWidget(self.competition_name_label)
        self.row1.addWidget(self.start_matches_button)
        self.row1.addWidget(self.go_back_to_main_button)

        self.master.addLayout(self.row1)
        self.master.addWidget(self.competition_table)

        self.setLayout(self.master)



    def set_labels(self):
        self.competition_label.setText("Competitie Naam")
        self.start_matches_button.setText("Start Wedestrijd")
        self.go_back_to_main_button.setText("Ga Terug")
        self.competition_table.setColumnCount(9)
        self.competition_table.setHorizontalHeaderLabels(["Ploeg", "P", "L", "D", "P", "F", "A", "GD", "pts"])

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class CreateLeague(QWidget):
    def __init__(self):
        super().__init__()
        self.select_country_label = QLabel()
        self.select_country_dropdown = QComboBox()
        self.create_country_label = QLabel()
        self.create_country_input = QLineEdit()
        self.create_country_button = QPushButton()
        self.competition_name_label = QLabel()
        self.competition_name_input = QLineEdit()
        self.compeition_name_Button = QPushButton()
        self.select_team_label = QLabel()
        self.select_team_dropdow = QComboBox()
        self.select_team_button = QPushButton()
        self.select_competition_name_label = QLabel()
        self.select_competition_name_text_label = QLabel()
        self.teams_label = QLabel()
        self.teams_listview = QListView()
        self.create_competition_button = QPushButton()

        self.create_window()


    def create_window(self):
        self.set_layout()
        self.set_labels()


    def set_layout(self):
        self.master = QHBoxLayout()

        self.col1 = QVBoxLayout()
        self.col1_row1 = QHBoxLayout()

        self.col1_row1_col1 = QVBoxLayout()
        self.col1_row1_col1.addWidget(self.select_country_label)
        self.col1_row1_col1.addWidget(self.select_country_dropdown)
        self.col1_row1_col1.addWidget(self.create_country_label)
        self.col1_row1_col1.addWidget(self.create_country_input)
        self.col1_row1_col1.addWidget(self.create_country_button)
        self.col1_row1_col1.addWidget(self.select_competition_name_label)
        self.col1_row1.addLayout(self.col1_row1_col1)

        self.col1_row1_col2 = QVBoxLayout()
        self.col1_row1_col2.addWidget(self.competition_name_label)
        self.col1_row1_col2.addWidget(self.competition_name_input)
        self.col1_row1_col2.addWidget(self.compeition_name_Button)
        self.col1_row1_col2.addWidget(self.select_team_label)
        self.col1_row1_col2.addWidget(self.select_team_dropdow)
        self.col1_row1_col2.addWidget(self.select_team_button)
        self.col1_row1_col2.addWidget(self.select_competition_name_text_label)
        self.col1_row1.addLayout(self.col1_row1_col2)
        
        self.col1.addLayout(self.col1_row1)
        self.col1.addWidget(self.create_competition_button)


        self.col2 = QVBoxLayout()
        self.col2.addWidget(self.teams_label)
        self.col2.addWidget(self.teams_listview)

        self.master.addLayout(self.col1)
        self.master.addLayout(self.col2)

        self.setLayout(self.master)


    def set_labels(self):
        self.select_country_label.setText("selecteer land")
        self.create_country_label.setText("Maak Land")
        self.create_country_button.setText("Maak")
        self.competition_name_label.setText("Competitie Naam")
        self.compeition_name_Button.setText("Maak")
        self.select_team_label.setText("Selecteer Ploeg")
        self.select_team_button.setText("Voeg Toe")
        self.select_competition_name_label.setText("Competitie Naam")
        self.create_competition_button.setText("Maak Competitie")
        self.teams_label.setText("Teams")

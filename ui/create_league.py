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
        self.competition_name_Button = QPushButton()
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
        #change to grid
        self.col1 = QVBoxLayout()
        self.col1.addWidget(self.select_country())
        self.col1.addWidget(self.create_country())
        self.col1.addWidget(self.select_competition_name_label)

        self.col2 = QVBoxLayout()
        self.col2.addWidget(self.competition_name())
        self.col2.addWidget(self.select_team())
        self.col2.addWidget(self.select_competition_name_text_label)

        self.master.addLayout(self.col1)
        self.master.addLayout(self.col2)

        self.master.addWidget(self.teams_listview)
        
        self.setLayout(self.master)


    def set_labels(self):
        self.select_country_label.setText("selecteer land")
        self.create_country_label.setText("Maak Land")
        self.create_country_button.setText("Maak")
        self.competition_name_label.setText("Competitie Naam")
        self.competition_name_Button.setText("Maak")
        self.select_team_label.setText("Selecteer Ploeg")
        self.select_team_button.setText("Voeg Toe")
        self.select_competition_name_label.setText("Competitie Naam")
        self.create_competition_button.setText("Maak Competitie")
        self.teams_label.setText("Teams")


    def select_country(self) -> QWidget:
        widget = QWidget()
        master = QVBoxLayout()
        master.addWidget(self.select_country_label)
        master.addWidget(self.select_country_dropdown)

        widget.setLayout(master)

        return widget

    
    def create_country(self) -> QWidget:
        widget = QWidget()
        master = QVBoxLayout()
        master.addWidget(self.create_country_label)
        master.addWidget(self.create_country_input)
        master.addWidget(self.create_country_button)

        widget.setLayout(master)

        return widget


    def competition_name(self) -> QWidget:
        widget = QWidget()
        master = QVBoxLayout()
        master.addWidget(self.competition_name_label)
        master.addWidget(self.competition_name_input)
        master.addWidget(self.competition_name_Button)

        widget.setLayout(master)

        return widget


    def select_team(self) -> QWidget:
        widget = QWidget()
        master = QVBoxLayout()
        master.addWidget(self.select_team_label)
        master.addWidget(self.select_team_dropdow)
        master.addWidget(self.select_team_button)

        widget.setLayout(master)

        return widget

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from ui.style import Style

class CreateLeague(Style, QWidget):
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
        self.teams_listview = QListWidget()
        self.create_competition_button = QPushButton()

        self.create_window()


    def create_window(self):
        self.set_layout()
        self.set_labels()
        self.setMinimumWidth(750)


    def set_layout(self):
        self.master = QHBoxLayout()

        self.col1 = QVBoxLayout()

        self.col1_row1 = QHBoxLayout()
        self.col1_row1_col1 = QVBoxLayout()
        self.col1_row1_col1.addWidget(self.select_country())
        self.col1_row1_col1.addWidget(self.create_country())
        self.col1_row1_col1.addWidget(self.select_competition_name_label)

        self.col1_row1_col2 = QVBoxLayout()
        self.col1_row1_col2.addWidget(self.competition_name())
        self.col1_row1_col2.addWidget(self.select_team())
        self.col1_row1_col2.addWidget(self.select_competition_name_text_label)

        self.col1_row1.addLayout(self.col1_row1_col1)
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
        self.select_country_label.setObjectName("select_country")
        self.select_country_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.create_country_label.setText("Maak Land")
        self.create_country_label.setObjectName("create_country")
        self.create_country_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.create_country_button.setText("Maak")
        self.competition_name_label.setText("Competitie Naam")
        self.competition_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.competition_name_Button.setText("Maak")
        self.select_team_label.setText("Selecteer Ploeg")
        self.select_team_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.select_team_button.setText("Voeg Toe")
        self.select_competition_name_label.setText("Competitie Naam:")
        self.select_competition_name_label.setObjectName("comp_label")
        self.select_competition_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.select_competition_name_text_label.setText("placeholder")
        self.select_competition_name_text_label.setObjectName("comp_label")
        self.select_competition_name_text_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.create_competition_button.setText("Maak Competitie")
        self.teams_label.setText("Teams")
        self.teams_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.teams_listview.addItems(["ploeg 1", "ploeg 2", "ploeg 3", "ploeg 4", "ploeg 5", "ploeg 6",
                                     "ploeg 7", "ploeg 8", "ploeg 9", "ploeg 10", "ploeg 11", "ploeg 12",
                                     "ploeg 13", "ploeg 14", "ploeg 15", "ploeg 16", "ploeg 17", "ploeg 18",
                                     "ploeg 19", "ploeg 20", "ploeg 21", "ploeg 22", "ploeg 23", "ploeg 24"])

        self.teams_listview.setWrapping(True)
        self.teams_listview.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.teams_listview.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)


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

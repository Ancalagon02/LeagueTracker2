from datetime import date
from PyQt6.QtCore import QDate, Qt
from PyQt6.QtWidgets import (QListWidget, QWidget, QLabel, QSpinBox, QSpacerItem, QVBoxLayout,
QHBoxLayout, QDateEdit, QSizePolicy, QPushButton)
from ui.competition import Competition
import database.data as data


class Matches(QWidget):
    def __init__(self, competition: Competition):
        super().__init__()

        self.setWindowTitle("Wedestrijd")
        self.competition = competition

        self.init_ui()
        self.set_layout()


    def init_ui(self):
        self.team_listwdget = QListWidget()
        self.team_listwdget.addItems(self.competition.clubs)

        self.date_dateedit = QDateEdit()
        self.date_dateedit.setCalendarPopup(True)
        self.date_dateedit.setDate(QDate.currentDate())
        self.date_dateedit.setDisplayFormat("dddd dd MMMM yyyy")

        self.team_one_label = QLabel()
        self.team_one_label.setText("Ploeg Een")
        self.team_one_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team_one_button = QPushButton()
        self.team_one_button.setText("Selecteer")
        self.team_one_button.clicked.connect(self.pressed_button_one)
        
        self.team_one_spinbox = QSpinBox()

        self.horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.versus_label = QLabel()
        self.versus_label.setText("VS")
        self.versus_label.setObjectName("versus")
        self.versus_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontal_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.team_two_label = QLabel()
        self.team_two_label.setText("Ploeg Twee")
        self.team_two_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team_two_button = QPushButton()
        self.team_two_button.setText("Selecteer")
        self.team_two_button.clicked.connect(self.pressed_button_two)
        
        self.team_two_spinbox = QSpinBox()

        self.match_button = QPushButton()
        self.match_button.setText("Match")
        self.match_button.setDisabled(True)
        self.match_button.clicked.connect(self.played_game)

        self.go_back_button = QPushButton()
        self.go_back_button.setText("Go Back")


    def set_layout(self):
        master_layout = QHBoxLayout()
        row1 = QVBoxLayout()
        col2 = QHBoxLayout()
        col2_row1 = QVBoxLayout()
        col2_row2 = QVBoxLayout()

        col2_row1.addWidget(self.team_one_label)
        col2_row1.addWidget(self.team_one_button)
        col2_row1.addWidget(self.team_one_spinbox)

        col2_row2.addWidget(self.team_two_label)
        col2_row2.addWidget(self.team_two_button)
        col2_row2.addWidget(self.team_two_spinbox)

        col2.addLayout(col2_row1)
        col2.addItem(self.horizontal_spacer)
        col2.addWidget(self.versus_label)
        col2.addItem(self.horizontal_spacer_2)
        col2.addLayout(col2_row2)

        row1.addWidget(self.date_dateedit)
        row1.addLayout(col2)
        row1.addWidget(self.match_button)
        row1.addWidget(self.go_back_button)

        master_layout.addWidget(self.team_listwdget)
        master_layout.addLayout(row1)

        self.setLayout(master_layout)


    def button_disabled(self) -> bool:
        button_one = self.team_one_button.isEnabled()
        button_two = self.team_two_button.isEnabled()
        output: bool = False
        if button_one == False and button_two == False:
            output = True
        return output


    def get_current_item(self) -> str:
        output: str = ""
        for item in self.team_listwdget.selectedItems():
            self.team_listwdget.takeItem(self.team_listwdget.row(item))
            output = item.text()
        return output


    def pressed_button_one(self) -> None:
        text = self.get_current_item()
        if text != "":
            self.team_one_label.setText(text)
            self.team_one_button.setDisabled(True)
            if self.button_disabled():
                self.match_button.setDisabled(False)


    def pressed_button_two(self) -> None:
        text = self.get_current_item()
        if text != "":
            self.team_two_label.setText(text)
            self.team_two_button.setDisabled(True)
            if self.button_disabled():
                self.match_button.setDisabled(False)


    def played_game(self) -> None:
        team_one_name: str = self.team_one_label.text()
        team_one_score: str = self.team_one_spinbox.text()
        team_two_name: str = self.team_two_label.text()
        team_two_score: str = self.team_two_spinbox.text()
        play_date: date = self.date_dateedit.date().toPyDate()
        league_name: str = self.competition.league_name

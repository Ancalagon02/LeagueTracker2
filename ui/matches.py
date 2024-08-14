from PyQt6.QtCore import QDate, Qt
from PyQt6.QtWidgets import (QListWidget, QWidget, QLabel, QSpinBox, QSpacerItem, QVBoxLayout,
QHBoxLayout, QDateEdit, QSizePolicy, QPushButton)


class Matches(QWidget):
    def __init__(self, league_name: str):
        super().__init__()

        self.league_name = league_name

        self.setWindowTitle("Wedestrijd")

        self.init_ui()
        self.set_layout()


    def init_ui(self):
        self.team_listwdget = QListWidget()

        self.date_dateedit = QDateEdit()
        self.date_dateedit.setCalendarPopup(True)
        self.date_dateedit.setDate(QDate.currentDate())
        self.date_dateedit.setDisplayFormat("dddd dd MMMM yyyy")

        self.team_one_label = QLabel()
        self.team_one_label.setText("Ploeg Een")
        self.team_one_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team_one_button = QPushButton()
        self.team_one_button.setText("Selecteer")
        
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
        
        self.team_two_spinbox = QSpinBox()

        self.match_button = QPushButton()
        self.match_button.setText("Match")
        self.match_button.setDisabled(True)

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

from PyQt6.QtCore import QDate, Qt
from PyQt6.QtWidgets import (QWidget, QLabel, QComboBox, QSpinBox, QComboBox, QSpacerItem, QVBoxLayout,
QHBoxLayout, QDateEdit, QSizePolicy, QPushButton)


class Matches(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wedestrijd")

        self.init_ui()
        self.set_layout()


    def init_ui(self):
        self.date_dateedit = QDateEdit()
        self.date_dateedit.setCalendarPopup(True)
        self.date_dateedit.setDate(QDate.currentDate())
        self.date_dateedit.setDisplayFormat("dddd dd MMMM yyyy")

        self.team_one_label = QLabel()
        self.team_one_label.setText("Ploeg Een")
        self.team_one_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team_one_combobox = QComboBox()
        
        self.team_one_spinbox = QSpinBox()

        self.horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.versus_label = QLabel()
        self.versus_label.setText("VS")
        self.versus_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontal_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.team_two_label = QLabel()
        self.team_two_label.setText("Ploeg Twee")
        self.team_two_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team_two_combobox = QComboBox()

        self.team_two_spinbox = QSpinBox()

        self.match_button = QPushButton()
        self.match_button.setText("Match")

        self.go_back_button = QPushButton()
        self.go_back_button.setText("Go Back")
        self.go_back_button.clicked.connect(self.close)


    def set_layout(self):
        self.master_layout = QVBoxLayout()
        self.col1 = QHBoxLayout()
        self.col1_row1 = QVBoxLayout()
        self.col1_row2 = QVBoxLayout()

        self.col1_row1.addWidget(self.team_one_label)
        self.col1_row1.addWidget(self.team_one_combobox)
        self.col1_row1.addWidget(self.team_one_spinbox)

        self.col1_row2.addWidget(self.team_two_label)
        self.col1_row2.addWidget(self.team_two_combobox)
        self.col1_row2.addWidget(self.team_two_spinbox)

        self.col1.addLayout(self.col1_row1)
        self.col1.addItem(self.horizontal_spacer)
        self.col1.addWidget(self.versus_label)
        self.col1.addItem(self.horizontal_spacer_2)
        self.col1.addLayout(self.col1_row2)

        self.master_layout.addWidget(self.date_dateedit)
        self.master_layout.addLayout(self.col1)
        self.master_layout.addWidget(self.match_button)
        self.master_layout.addWidget(self.go_back_button)

        self.setLayout(self.master_layout)

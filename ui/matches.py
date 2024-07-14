from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from ui.style import Style

class Matches(Style, QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.set_layout()

        self.setFixedSize(self.width() -300, self.height() -150)


    def init_ui(self):
        self.datepicker = QDateEdit()
        self.datepicker.setCalendarPopup(True)
        self.datepicker.setDate(QDate.currentDate())

        self.team_one_label = QLabel()
        self.team_one_label.setText("placeholder")

        self.team_one_dropdown = QComboBox()

        self.team_one_spinebox = QSpinBox()

        self.team_two_label = QLabel()
        self.team_two_label.setText("placeholder")

        self.team_two_dropdown = QComboBox()

        self.team_two_spinebox = QSpinBox()

        self.versus_label = QLabel()
        self.versus_label.setText("VS")
        self.versus_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.match_button = QPushButton()
        self.match_button.setText("Match")

        self.go_back_button = QPushButton()
        self.go_back_button.setText("Ga Terug")


    def set_layout(self):
        self.master = QVBoxLayout()

        self.row1 = QHBoxLayout()
        self.row1.addWidget(self.team_one())
        self.row1.addWidget(self.versus_label)
        self.row1.addWidget(self.team_two())

        self.master.addWidget(self.datepicker)
        self.master.addLayout(self.row1)
        self.master.addWidget(self.match_button)
        self.master.addWidget(self.go_back_button)

        self.setLayout(self.master)


    def team_one(self) -> QWidget:
        widget = QWidget()
        master = QVBoxLayout()
        master.addWidget(self.team_one_label)
        master.addWidget(self.team_one_dropdown)
        master.addWidget(self.team_one_spinebox)

        widget.setLayout(master)

        return widget
    
    
    def team_two(self) -> QWidget:
        widget = QWidget()
        master = QVBoxLayout()
        master.addWidget(self.team_two_label)
        master.addWidget(self.team_two_dropdown)
        master.addWidget(self.team_two_spinebox)

        widget.setLayout(master)

        return widget

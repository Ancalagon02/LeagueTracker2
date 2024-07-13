from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from ui.style import Style

class Matches(Style, QWidget):
    def __init__(self):
        super().__init__()
        self.datepicker = QDateEdit()
        self.team_one_label = QLabel()
        self.team_one_dropdown = QComboBox()
        self.team_one_spinebox = QSpinBox()
        self.team_two_label = QLabel()
        self.team_two_dropdown = QComboBox()
        self.team_two_spinebox = QSpinBox()
        self.versus_label = QLabel()
        self.match_button = QPushButton()
        self.go_back_button = QPushButton()

        self.create_window()


    def create_window(self):
        self.set_layout()
        self.set_datepicker()
        self.set_labels()


    def set_datepicker(self):
        self.datepicker.setCalendarPopup(True)
        self.datepicker.setDate(QDate.currentDate())


    def set_layout(self):
        self.master = QVBoxLayout()

        self.row1 = QHBoxLayout()
        self.row1.addWidget(self.team_one())
        self.row1.addWidget(self.versus_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.row1.addWidget(self.team_two())

        self.master.addWidget(self.datepicker)
        self.master.addLayout(self.row1)
        self.master.addWidget(self.match_button)
        self.master.addWidget(self.go_back_button)

        self.setLayout(self.master)


    def set_labels(self):
        self.match_button.setText("Match")
        self.go_back_button.setText("Ga Terug")
        self.versus_label.setText("VS")


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

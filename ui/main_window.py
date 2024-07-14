from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from ui.style import Style 

class MainWindow(Style, QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.set_layout()

        self.setFixedSize(self.width() - 100, self.height() - 100)


    def init_ui(self):
        self.setWindowTitle("Start Scherm")

        self.select_country_label = QLabel()
        self.select_country_label.setText("Selecteer Land:")

        self.select_country_dropdown = QComboBox()

        self.create_competition_button = QPushButton()
        self.create_competition_button.setText("Maak Competitie")

        self.competitions_listview = QListWidget()

        self.selected_competition_label = QLabel()

        self.selected_competition_name_label = QLabel()
        self.selected_competition_label.setText("Competitie:")

        self.start_competition_button = QPushButton()
        self.start_competition_button.setText("Start Competitie")


    def set_layout(self):
        self.master = QVBoxLayout()

        self.row1 = QHBoxLayout()
        self.row1.addWidget(self.select_country_label)
        self.row1.addWidget(self.select_country_dropdown)
        self.row1.addWidget(self.create_competition_button)

        self.row2 = QHBoxLayout()
        self.row2.addWidget(self.competitions_listview)
        
        self.row3 = QHBoxLayout()
        self.row3.addWidget(self.selected_competition_label)
        self.row3.addWidget(self.selected_competition_name_label)
        self.row3.addWidget(self.start_competition_button)

        self.master.addLayout(self.row1)
        self.master.addLayout(self.row2)
        self.master.addLayout(self.row3)

        self.setLayout(self.master)

from PyQt6.QtWidgets import *
from PyQt6.QtCore import * 

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.select_country_label = QLabel()
        self.select_country_dropdown = QComboBox()
        self.create_competition_button = QPushButton()
        self.competitions_listview = QListView()
        self.selected_competition_label = QLabel()
        self.selected_competition_name_label = QLabel()
        self.start_competition_button = QPushButton()

        self.create_window()


    def create_window(self):
        self.set_layout()
        self.set_labels()


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


    def set_labels(self):
        self.select_country_label.setText("Selecteer Land:")
        self.selected_competition_label.setText("Competitie:")
        self.create_competition_button.setText("Maak Competitie")
        self.start_competition_button.setText("Start Competitie")


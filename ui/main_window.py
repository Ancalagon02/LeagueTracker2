from PyQt6.QtCore import Qt 
from PyQt6.QtWidgets import (QWidget, QLabel, QComboBox, QSizePolicy, QSpacerItem, QPushButton, QFrame, QListWidget,
QAbstractScrollArea, QAbstractItemView, QHBoxLayout, QVBoxLayout)
import database.data as data
from models import Country


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Start Scherm")

        self.init_ui()
        self.set_layout()


    def init_ui(self):
        self.label = QLabel()
        self.label.setText("Selecteer Land")

        self.country_combobox = QComboBox()
        self.set_combobox(self.country_combobox)

        self.horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.create_competition_button = QPushButton()
        self.create_competition_button.setObjectName("main-button")
        self.create_competition_button.setText("Maak Competitie")

        self.competition_listwidget = QListWidget()
        self.competition_listwidget.setFrameShape(QFrame.Shape.NoFrame)
        self.competition_listwidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.competition_listwidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.competition_listwidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.competition_listwidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.competition_listwidget.setAlternatingRowColors(True)

        self.label_2 = QLabel()
        self.label_2.setText("Competitie:")

        self.competition_name_label = QLabel()
        self.competition_name_label.setText("Placeholder")

        self.horizontal_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.start_competition_button = QPushButton()
        self.start_competition_button.setObjectName("main-button")
        self.start_competition_button.setText("Start Competitie")


    def set_layout(self):
        self.master_layout = QVBoxLayout()
        self.col1 = QHBoxLayout()
        self.col2 = QHBoxLayout()

        self.col1.addWidget(self.label)
        self.col1.addWidget(self.country_combobox)
        self.col1.addItem(self.horizontal_spacer)
        self.col1.addWidget(self.create_competition_button)

        self.col2.addWidget(self.label_2)
        self.col2.addWidget(self.competition_name_label)
        self.col2.addItem(self.horizontal_spacer_2)
        self.col2.addWidget(self.start_competition_button)

        self.master_layout.addLayout(self.col1)
        self.master_layout.addWidget(self.competition_listwidget)
        self.master_layout.addLayout(self.col2)

        self.setLayout(self.master_layout)


    def set_combobox(self, combox: QComboBox):
        countries: list[Country] = data.load_countrys()
        for x in countries:
            combox.addItem(x.name)

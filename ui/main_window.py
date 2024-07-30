from PyQt6.QtCore import Qt 
from PyQt6.QtWidgets import (QWidget, QLabel, QComboBox, QSizePolicy, QSpacerItem, QPushButton, QFrame, QListWidget,
QAbstractScrollArea, QAbstractItemView, QHBoxLayout, QVBoxLayout)
import state as state
import ui.create_competition as cp


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Start Scherm")

        self.init_ui()
        self.set_layout()


    def init_ui(self):
        self.second_window = None

        self.label = QLabel()
        self.label.setText("Selecteer Land")

        self.country_combobox = QComboBox()
        self.country_combobox.addItems(state.load_countries())

        self.horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.create_competition_button = QPushButton()
        self.create_competition_button.setObjectName("main-button")
        self.create_competition_button.setText("Maak Competitie")
        self.create_competition_button.clicked.connect(self.open_main_window)

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
        master_layout = QVBoxLayout()
        col1 = QHBoxLayout()
        col2 = QHBoxLayout()

        col1.addWidget(self.label)
        col1.addWidget(self.country_combobox)
        col1.addItem(self.horizontal_spacer)
        col1.addWidget(self.create_competition_button)

        col2.addWidget(self.label_2)
        col2.addWidget(self.competition_name_label)
        col2.addItem(self.horizontal_spacer_2)
        col2.addWidget(self.start_competition_button)

        master_layout.addLayout(col1)
        master_layout.addWidget(self.competition_listwidget)
        master_layout.addLayout(col2)

        self.setLayout(master_layout)


    def open_main_window(self):
        if self.second_window is not None:
            self.second_window = None

        if self.second_window is None:
            self.second_window = cp.CreateCompetition()
            self.second_window.show()
            self.close()

from PyQt6.QtCore import Qt 
from PyQt6.QtWidgets import (QWidget, QLabel, QComboBox, QSizePolicy, QSpacerItem, QPushButton, QFrame, QListWidget,
QAbstractScrollArea, QAbstractItemView, QHBoxLayout, QVBoxLayout)
import modules.Data_Process as data


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Start Scherm")

        self.init_ui()
        self.set_layout()


    def init_ui(self) -> None:
        self.label = QLabel()
        self.label.setText("Selecteer Land")

        self.country_combobox = QComboBox()
        self.country_combobox.addItems(data.return_country_names())
        self.country_combobox.currentTextChanged.connect(self.changed_country)

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
        self.set_leagues()
        self.competition_listwidget.itemSelectionChanged.connect(self.set_competition_label)

        self.label_2 = QLabel()
        self.label_2.setText("Competitie:")

        self.competition_name_label = QLabel()
        self.competition_name_label.setText("Placeholder")

        self.horizontal_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.start_competition_button = QPushButton()
        self.start_competition_button.setObjectName("main-button")
        self.start_competition_button.setText("Start Competitie")
        self.start_competition_button.setDisabled(True)


    def set_layout(self) -> None:
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


    def set_leagues(self) -> None:
        country_name: str = self.country_combobox.currentText()
        self.competition_listwidget.addItems(data.return_league_names(country_name))
        self.competition_listwidget.sortItems(Qt.SortOrder.DescendingOrder)


    def changed_country(self) -> None:
        self.competition_listwidget.clear()
        self.set_leagues()
        self.start_competition_button.setDisabled(True)
        
        self.competition_name_label.setText("Placeholder")


    def set_competition_label(self) -> None:
        league_name = self.competition_listwidget.currentItem()
        if league_name is not None:
            self.competition_name_label.setText(league_name.text())
            self.start_competition_button.setDisabled(False)

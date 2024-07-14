from datetime import datetime
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from ui.style import Style

class Competition(Style, QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.set_layout()

        row = 40
        col = 170

        for row1 in range(self.competition_table.columnCount()):
            row += self.competition_table.columnWidth(row1)

        for col1 in range(self.competition_table.rowCount()):
            col += self.competition_table.rowHeight(col1)
            print(col)


        self.setFixedSize(row, col)


    def init_ui(self):
        self.competition_label = QLabel()
        self.competition_label.setText("Competitie Naam:")
        self.competition_label.setObjectName("comp_label")

        self.competition_name_label = QLabel()
        self.competition_name_label.setText("placeholder")

        self.datematch_label = QLabel()
        self.datematch_label.setText(datetime.now().strftime("%d %B %Y"))

        self.datematch_up_button = QToolButton()
        self.datematch_up_button.setArrowType(Qt.ArrowType.UpArrow)

        self.datematch_down_button = QToolButton()
        self.datematch_down_button.setArrowType(Qt.ArrowType.DownArrow)

        self.start_matches_button = QPushButton()
        self.start_matches_button.setText("Start Wedestrijd")

        self.go_back_to_main_button = QPushButton()
        self.go_back_to_main_button.setText("Ga Terug")

        self.competition_table = QTableWidget()
        self.competition_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.competition_table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.competition_table.verticalHeader().setSectionsClickable(False)
        self.competition_table.horizontalHeader().setSectionsClickable(False)
        self.competition_table.setAlternatingRowColors(True)
        self.competition_table.setColumnCount(9)
        self.competition_table.setHorizontalHeaderLabels(["Ploeg", "P", "L", "D", "P", "F", "A", "GD", "pts"])
        

    def set_layout(self):
        self.master = QVBoxLayout()

        self.row1 = QHBoxLayout()
        self.row1.addWidget(self.competition_label)
        self.row1.addWidget(self.competition_name_label)
        self.row1.addWidget(self.match_dates())
        self.row1.addWidget(self.start_matches_button)
        self.row1.addWidget(self.go_back_to_main_button)

        self.master.addLayout(self.row1)
        self.master.addWidget(self.competition_table)

        self.setLayout(self.master)


    def match_dates(self) -> QWidget:
        widget = QWidget()
        master = QHBoxLayout()

        col2 = QVBoxLayout()
        col2.addWidget(self.datematch_up_button)
        col2.addWidget(self.datematch_down_button)

        master.addWidget(self.datematch_label)
        master.addLayout(col2)

        widget.setLayout(master)

        return widget

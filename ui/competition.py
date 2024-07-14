from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from ui.style import Style

class Competition(Style, QWidget):
    def __init__(self):
        super().__init__()
        self.competition_label = QLabel()
        self.competition_name_label = QLabel()
        self.datematch_label = QLabel()
        self.datematch_up_button = QToolButton()
        self.datematch_down_button = QToolButton()
        self.start_matches_button = QPushButton()
        self.go_back_to_main_button = QPushButton()
        self.competition_table = QTableWidget()

        self.create_window()

        row = 70
        col = 170

        for row1 in range(self.competition_table.columnCount()):
            row += self.competition_table.columnWidth(row1)

        for col1 in range(self.competition_table.rowCount()):
            col += self.competition_table.rowHeight(col1)
            print(col)


        self.resize(row, col)


    def create_window(self):
        self.set_layout()
        self.set_labels()
        self.set_tool_buttons()


    def set_tool_buttons(self):
        self.datematch_up_button.setArrowType(Qt.ArrowType.UpArrow)
        self.datematch_down_button.setArrowType(Qt.ArrowType.DownArrow)


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



    def set_labels(self):
        self.competition_label.setText("Competitie Naam")
        self.start_matches_button.setText("Start Wedestrijd")
        self.go_back_to_main_button.setText("Ga Terug")
        self.competition_table.setColumnCount(9)
        self.competition_table.setHorizontalHeaderLabels(["Ploeg", "P", "L", "D", "P", "F", "A", "GD", "pts"])
        self.competition_table.setRowCount(24)
        item = QTableWidgetItem("Anderlecht")
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.competition_table.setItem(0, 0, QTableWidgetItem(item))
        self.competition_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.competition_table.setAlternatingRowColors(True)
        self.competition_table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.competition_table.verticalHeader().setSectionsClickable(False)
        self.competition_table.horizontalHeader().setSectionsClickable(False)
        self.competition_table.resizeColumnsToContents()


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

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QHeaderView, QSizePolicy, QSpacerItem, QTableWidgetItem, QWidget, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton,
QTableWidget, QAbstractItemView, QFrame, QToolButton)
import modules.Data_Process as data


class Competition(QWidget):
    def __init__(self, league_name: str) -> None:
        super().__init__()
        self.league_name = league_name

        self.setWindowTitle(self.league_name)
        
        self.init_ui()
        self.set_layout()


    def init_ui(self) -> None:
        self.competition_tablewidget = QTableWidget()
        self.competition_tablewidget.setColumnCount(9)
        self.competition_tablewidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.competition_tablewidget.setFrameShape(QFrame.Shape.Box)
        self.competition_tablewidget.setFrameShadow(QFrame.Shadow.Plain)
        self.competition_tablewidget.setLineWidth(2)
        self.competition_tablewidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.competition_tablewidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.competition_tablewidget.setSizeAdjustPolicy(QAbstractItemView.SizeAdjustPolicy.AdjustToContents)
        self.competition_tablewidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.competition_tablewidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.competition_tablewidget.setAlternatingRowColors(True)


        self.frame1 = QFrame()
        self.frame1.setFrameShape(QFrame.Shape.Box)
        self.frame1.setFrameShadow(QFrame.Shadow.Plain)
        self.frame1.setLineWidth(4)

        self.date_label = QLabel(self.frame1)
        self.date_label.setText("Speeldag")
        self.date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.date_combobox = QComboBox(self.frame1)
        self.set_dates()
        self.date_combobox.currentTextChanged.connect(self.change_date)

        self.up_button = QToolButton(self.frame1)
        self.up_button.setArrowType(Qt.ArrowType.UpArrow)
        self.up_button.clicked.connect(self.down_index)

        self.down_button = QToolButton(self.frame1)
        self.down_button.setArrowType(Qt.ArrowType.DownArrow)
        self.down_button.clicked.connect(self.up_index)

        self.frame2 = QFrame()
        self.frame2.setFrameShape(QFrame.Shape.Box)
        self.frame2.setFrameShadow(QFrame.Shadow.Plain)
        self.frame2.setLineWidth(4)

        self.match_button = QPushButton(self.frame2)
        self.match_button.setText("Match")

        self.verticalspacer = QSpacerItem(20, 81, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.go_back_button = QPushButton(self.frame2)
        self.go_back_button.setText("Ga Terug")
        
        self.exit_putton = QPushButton(self.frame2)
        self.exit_putton.setText("Exit")
        self.exit_putton.clicked.connect(self.close)

        self.set_table()


    def set_layout(self) -> None:
        master_layout = QHBoxLayout()
        row2 = QVBoxLayout()
        row2_col1 = QVBoxLayout(self.frame1)
        row2_col1_row1 = QHBoxLayout()
        row2_col1_row2 = QVBoxLayout()
        row2_col2 = QVBoxLayout(self.frame2)

        row2_col1_row2.addWidget(self.up_button)
        row2_col1_row2.addWidget(self.down_button)

        row2_col1_row1.addWidget(self.date_combobox)
        row2_col1_row1.addLayout(row2_col1_row2)
        
        row2_col1.addWidget(self.date_label)
        row2_col1.addLayout(row2_col1_row1)

        row2_col2.addWidget(self.match_button)
        row2_col2.addItem(self.verticalspacer)
        row2_col2.addWidget(self.go_back_button)
        row2_col2.addWidget(self.exit_putton)

        row2.addWidget(self.frame1)
        row2.addWidget(self.frame2)

        master_layout.addWidget(self.competition_tablewidget)
        master_layout.addLayout(row2)

        self.setLayout(master_layout)


    def set_dates(self) -> None:
        dates: list[str] = data.return_dates(self.league_name)
        dates.sort(reverse=True)
        self.date_combobox.addItems(dates)


    def change_date(self) -> None:
        self.competition_tablewidget.clear()
        self.set_table()


    def set_table(self) -> None:
        date: str = self.date_combobox.currentText()
        matches: list[dict] = data.return_competition(self.league_name, date)
        self.competition_tablewidget.setRowCount(len(matches))
        row: int = 0
        while row < self.competition_tablewidget.rowCount():
            column: int = 0
            for item in matches[row].values():
                num: QTableWidgetItem = QTableWidgetItem()
                num.setData(Qt.ItemDataRole.DisplayRole, item)
                self.competition_tablewidget.setItem(row, column, num)
                column += 1
            row += 1
        self.competition_tablewidget.resizeColumnsToContents()
        self.check_buttons()
        self.competition_tablewidget.setHorizontalHeaderLabels(["Ploeg", "P", "W", "L", "D", "F", "A", "GD", "Pts"])
        row = 0
        for item in matches[row].values():
            self.competition_tablewidget.horizontalHeader().setSectionResizeMode(row, QHeaderView.ResizeMode.Stretch)
            row += 1


    def check_buttons(self) -> None:
        if self.date_combobox.currentIndex() == (len(self.date_combobox) - 1):
            self.down_button.setDisabled(True)
        if self.date_combobox.currentIndex() != (len(self.date_combobox) - 1):
            self.down_button.setDisabled(False)
        if self.date_combobox.currentIndex() == 0:
            self.up_button.setDisabled(True)
        if self.date_combobox.currentIndex() != 0:
            self.up_button.setDisabled(False)


    def up_index(self) -> None:
        self.competition_tablewidget.clear()
        index = self.date_combobox.currentIndex()
        index += 1
        self.date_combobox.setCurrentIndex(index)
        self.check_buttons()


    def down_index(self) -> None:
        self.competition_tablewidget.clear()
        index = self.date_combobox.currentIndex()
        index -= 1
        self.date_combobox.setCurrentIndex(index)
        self.check_buttons()

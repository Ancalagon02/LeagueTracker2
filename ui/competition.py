from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QHeaderView, QSizePolicy, QSpacerItem, QWidget, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton,
QTableWidget, QAbstractItemView, QFrame, QToolButton)


class Competition(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Competitie")
        
        self.init_ui()
        self.set_layout()


    def init_ui(self):
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
        self.competition_tablewidget.setHorizontalHeaderLabels(["Ploeg", "P", "W", "L", "D", "F", "A", "GD", "Pts"])

        self.label = QLabel()
        self.label.setText("Datum")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.date_combobox = QComboBox()

        self.up_button = QToolButton()
        self.up_button.setArrowType(Qt.ArrowType.UpArrow)

        self.down_button = QToolButton()
        self.down_button.setArrowType(Qt.ArrowType.UpArrow)

        self.match_button = QPushButton()
        self.match_button.setText("Match")

        self.verticalspacer = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.go_back_button = QPushButton()
        self.go_back_button.setText("Ga Terug")

        self.exit_button = QPushButton()
        self.exit_button.setText("Exit")



    def set_layout(self):
        self.master_layout = QHBoxLayout()
        self.col1 = QVBoxLayout()
        self.col2 = QHBoxLayout()
        self.col2_row1 = QVBoxLayout()
        self.col2_row2 = QVBoxLayout()

        self.col2_row1.addWidget(self.date_combobox)
        self.col2_row2.addWidget(self.up_button)
        self.col2_row2.addWidget(self.down_button)
        self.col2.addLayout(self.col2_row1)
        self.col2.addLayout(self.col2_row2)

        self.col1.addWidget(self.label)
        self.col1.addLayout(self.col2)
        self.col1.addWidget(self.match_button)
        self.col1.addItem(self.verticalspacer)
        self.col1.addWidget(self.go_back_button)
        self.col1.addWidget(self.exit_button)

        self.master_layout.addWidget(self.competition_tablewidget)
        self.master_layout.addLayout(self.col1)

        self.setLayout(self.master_layout)

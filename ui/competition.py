from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QSizePolicy, QSpacerItem, QTableWidgetItem, QWidget, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton,
QTableWidget, QAbstractItemView, QFrame, QToolButton)


class Competition(QWidget):
    def __init__(self, league_name: str) -> None:
        super().__init__()
        self.league_name = league_name
        
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
        self.competition_tablewidget.setHorizontalHeaderLabels(["Ploeg", "P", "W", "L", "D", "F", "A", "GD", "Pts"])


        self.frame1 = QFrame()
        self.frame1.setFrameShape(QFrame.Shape.Box)
        self.frame1.setFrameShadow(QFrame.Shadow.Plain)
        self.frame1.setLineWidth(4)

        self.date_label = QLabel(self.frame1)
        self.date_label.setText("Speeldag")
        self.date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.date_combobox = QComboBox(self.frame1)

        self.up_button = QToolButton(self.frame1)
        self.up_button.setArrowType(Qt.ArrowType.UpArrow)

        self.down_button = QToolButton(self.frame1)
        self.down_button.setArrowType(Qt.ArrowType.DownArrow)

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

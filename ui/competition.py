from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QSizePolicy, QSpacerItem, QWidget, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton,
QTableWidget, QAbstractItemView, QFrame, QToolButton)
from ui import matches, main_window


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
        self.down_button.setArrowType(Qt.ArrowType.UpArrow)

        self.frame2 = QFrame()
        self.frame2.setFrameShape(QFrame.Shape.Box)
        self.frame2.setFrameShadow(QFrame.Shadow.Plain)
        self.frame2.setLineWidth(4)

        self.match_button = QPushButton(self.frame2)
        self.match_button.setText("Match")
        self.match_button.clicked.connect(self.open_match)

        self.verticalspacer = QSpacerItem(20, 81, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.go_back_button = QPushButton(self.frame2)
        self.go_back_button.setText("Ga Terug")
        self.go_back_button.clicked.connect(self.open_main_window)
        
        self.exit_putton = QPushButton(self.frame2)
        self.exit_putton.setText("Exit")
        self.exit_putton.clicked.connect(self.close)

        self.second_window = None


    def set_layout(self):
        self.master_layout = QHBoxLayout()
        self.row2 = QVBoxLayout()
        self.row2_col1 = QVBoxLayout(self.frame1)
        self.row2_col1_row1 = QHBoxLayout()
        self.row2_col1_row2 = QVBoxLayout()
        self.row2_col2 = QVBoxLayout(self.frame2)

        self.row2_col1_row2.addWidget(self.up_button)
        self.row2_col1_row2.addWidget(self.down_button)

        self.row2_col1_row1.addWidget(self.date_combobox)
        self.row2_col1_row1.addLayout(self.row2_col1_row2)
        
        self.row2_col1.addWidget(self.date_label)
        self.row2_col1.addLayout(self.row2_col1_row1)

        self.row2_col2.addWidget(self.match_button)
        self.row2_col2.addItem(self.verticalspacer)
        self.row2_col2.addWidget(self.go_back_button)
        self.row2_col2.addWidget(self.exit_putton)

        self.row2.addWidget(self.frame1)
        self.row2.addWidget(self.frame2)

        self.master_layout.addWidget(self.competition_tablewidget)
        self.master_layout.addLayout(self.row2)

        self.setLayout(self.master_layout)


    def open_match(self):
        if self.second_window is not None:
            self.second_window = None

        if self.second_window is None:
            self.second_window = matches.Matches()
        self.second_window.show()


    def open_main_window(self):
        self.close()

        if self.second_window is not None:
            self.second_window = None

        if self.second_window is None:
            self.second_window = main_window.MainWindow()
        self.second_window.show()

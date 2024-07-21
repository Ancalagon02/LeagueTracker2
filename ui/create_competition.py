from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QLabel, QWidget, QPushButton, QFrame, QGridLayout, QVBoxLayout, QHBoxLayout,
QSizePolicy, QSpacerItem, QComboBox, QListWidget, QAbstractItemView)
from .create_dialog import CreateDialog
from ui import main_window


class CreateCompetition(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Maak Competitie")

        self.init_ui()
        self.set_layout()


    def init_ui(self):
        self.competition_label = QLabel()
        self.competition_label.setText("Competitie Naam:")

        self.competition_name_label = QLabel()
        self.competition_name_label.setText("Placeholder")

        self.line = QFrame()
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.competition_name_button = QPushButton()
        self.competition_name_button.setText("Competitie Naam")
        self.competition_name_button.clicked.connect(self.open_create_competition_name_dialog)

        self.verticalspacer1 = QSpacerItem(17, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.frame1 = QFrame()
        self.frame1.setFrameShape(QFrame.Shape.Box)
        self.frame1.setFrameShadow(QFrame.Shadow.Plain)
        self.frame1.setLineWidth(4)

        self.country_label = QLabel(self.frame1)
        self.country_label.setText("Selecteer Land")
        self.country_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.country_combobox = QComboBox(self.frame1)
        self.country_combobox.addItems(["Belgie", "England"])

        self.frame2 = QFrame()
        self.frame2.setFrameShape(QFrame.Shape.Box)
        self.frame2.setFrameShadow(QFrame.Shadow.Plain)
        self.frame2.setLineWidth(4)

        self.team_label = QLabel(self.frame2)
        self.team_label.setText("Selecteer Ploeg")
        self.team_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team_combobox = QComboBox(self.frame2)

        self.team_button = QPushButton(self.frame2)
        self.team_button.setText("OK")

        self.frame3 = QFrame()
        self.frame3.setFrameShape(QFrame.Shape.Box)
        self.frame3.setFrameShadow(QFrame.Shadow.Plain)
        self.frame3.setLineWidth(4)

        self.create_country_button = QPushButton(self.frame3)
        self.create_country_button.setText("Maak Land")
        self.create_country_button.clicked.connect(self.open_create_country_dialog)

        self.create_team_button = QPushButton(self.frame3)
        self.create_team_button.setText("Maak Ploeg")
        self.create_team_button.clicked.connect(self.open_create_team_dialog)

        self.verticalspacer2 = QSpacerItem(17, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.go_back_button = QPushButton()
        self.go_back_button.setText("Ga Terug")
        self.go_back_button.clicked.connect(self.open_main_window)

        self.create_competition_button = QPushButton()
        self.create_competition_button.setText("Maak Competitie")

        self.frame4 = QFrame()
        self.frame4.setFrameShape(QFrame.Shape.Box)
        self.frame4.setFrameShadow(QFrame.Shadow.Plain)
        self.frame4.setLineWidth(4)

        self.teams_label = QLabel(self.frame4)
        self.teams_label.setText("Ploegen")
        self.teams_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team_listwidget = QListWidget(self.frame4)
        self.team_listwidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.team_listwidget.setFrameShape(QFrame.Shape.NoFrame)
        self.team_listwidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.team_listwidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.team_listwidget.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.team_listwidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)

        self.second_window = None


    def set_layout(self):
        self.master_layout = QGridLayout()
        self.grid1 = QHBoxLayout()
        self.grid2 = QVBoxLayout()
        self.grid2_col1 = QVBoxLayout(self.frame1)
        self.grid2_col2 = QVBoxLayout(self.frame2)
        self.grid2_col2_row1 = QHBoxLayout()
        self.grid2_col3 = QHBoxLayout(self.frame3)
        self.grid2_col4 = QHBoxLayout()
        self.grid3 = QVBoxLayout(self.frame4)

        self.grid1.addWidget(self.competition_label)
        self.grid1.addWidget(self.competition_name_label)
        self.grid1.setStretch(1, 1)

        self.grid2_col1.addWidget(self.country_label)
        self.grid2_col1.addWidget(self.country_combobox)

        self.grid2_col2_row1.addWidget(self.team_combobox)
        self.grid2_col2_row1.addWidget(self.team_button)

        self.grid2_col2.addWidget(self.team_label)
        self.grid2_col2.addLayout(self.grid2_col2_row1)

        self.grid2_col3.addWidget(self.create_country_button)
        self.grid2_col3.addWidget(self.create_team_button)

        self.grid2_col4.addWidget(self.go_back_button)
        self.grid2_col4.addWidget(self.create_competition_button)

        self.grid2.addWidget(self.competition_name_button)
        self.grid2.addItem(self.verticalspacer1)
        self.grid2.addWidget(self.frame1)
        self.grid2.addWidget(self.frame2)
        self.grid2.addWidget(self.frame3)
        self.grid2.addItem(self.verticalspacer2)
        self.grid2.addLayout(self.grid2_col4)

        self.grid3.addWidget(self.teams_label)
        self.grid3.addWidget(self.team_listwidget)

        self.master_layout.addLayout(self.grid1,        0, 0, 1, 2)
        self.master_layout.addWidget(self.line,         1, 0, 1, 2)
        self.master_layout.addLayout(self.grid2,        2, 0, 2, 1)
        self.master_layout.addWidget(self.frame4,       3, 1, 1, 1)

        self.setLayout(self.master_layout)


    def open_main_window(self):
        self.close()

        if self.second_window is not None:
            self.second_window = None

        if self.second_window is None:
            self.second_window = main_window.MainWindow()
        self.second_window.show()


    def open_create_country_dialog(self):
        dialog = CreateDialog()
        dialog.setWindowTitle("Maak Land")

        dialog.label.setText("Land Naam")

        dialog.exec()


    def open_create_team_dialog(self):
        dialog = CreateDialog()
        dialog.setWindowTitle("Maak Team")

        dialog.label.setText("Team Naam")

        dialog.exec()


    def open_create_competition_name_dialog(self):
        dialog = CreateDialog()
        dialog.setWindowTitle("Create Competitie")

        dialog.label.setText("Competitie Naam")

        dialog.exec()

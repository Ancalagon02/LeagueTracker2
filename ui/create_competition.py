from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QLabel, QWidget, QPushButton, QFrame, QGridLayout, QVBoxLayout, QHBoxLayout,
QSizePolicy, QSpacerItem, QComboBox, QListWidget, QAbstractItemView)
import modules.mapping_data as data
from ui.create_dialog import CreateDialog
from ui.error_dialog import ErrorDialog


class CreateCompetition(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Maak Competitie")

        self.init_ui()
        self.set_layout()


    def init_ui(self) -> None:
        self.second_window = None

        self.competition_label = QLabel()
        self.competition_label.setText("Competitie Naam:")

        self.competition_name_label = QLabel()
        self.competition_name_label.setText("Placeholder")

        self.line = QFrame()
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.competition_name_button = QPushButton()
        self.competition_name_button.setText("Competitie Naam")
        self.competition_name_button.clicked.connect(self.init_name_label)

        self.verticalspacer1 = QSpacerItem(17, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.frame1 = QFrame()
        self.frame1.setFrameShape(QFrame.Shape.Box)
        self.frame1.setFrameShadow(QFrame.Shadow.Plain)
        self.frame1.setLineWidth(4)

        self.country_label = QLabel(self.frame1)
        self.country_label.setText("Selecteer Land")
        self.country_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.country_combobox = QComboBox(self.frame1)
        self.country_combobox.addItems(data.map_countries())
        self.country_combobox.currentTextChanged.connect(self.changed_country)

        self.frame2 = QFrame()
        self.frame2.setFrameShape(QFrame.Shape.Box)
        self.frame2.setFrameShadow(QFrame.Shadow.Plain)
        self.frame2.setLineWidth(4)

        self.team_label = QLabel(self.frame2)
        self.team_label.setText("Selecteer Ploeg")
        self.team_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team_combobox = QComboBox(self.frame2)
        self.team_combobox.addItems(data.map_teams(self.country_combobox.currentText()))

        self.team_button = QPushButton(self.frame2)
        self.team_button.setText("OK")
        self.team_button.clicked.connect(self.add_teams_to_list)
        if self.team_combobox.currentText() == "":
            self.team_button.setDisabled(True)

        self.frame3 = QFrame()
        self.frame3.setFrameShape(QFrame.Shape.Box)
        self.frame3.setFrameShadow(QFrame.Shadow.Plain)
        self.frame3.setLineWidth(4)

        self.create_country_button = QPushButton(self.frame3)
        self.create_country_button.setText("Maak Land")
        self.create_country_button.clicked.connect(self.init_create_country)

        self.create_team_button = QPushButton(self.frame3)
        self.create_team_button.setText("Maak Ploeg")
        self.create_team_button.clicked.connect(self.init_create_team)
        if self.country_combobox.currentText() == "":
            self.create_team_button.setDisabled(True)

        self.verticalspacer2 = QSpacerItem(17, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.go_back_button = QPushButton()
        self.go_back_button.setText("Ga Terug")

        self.create_competition_button = QPushButton()
        self.create_competition_button.setText("Maak Competitie")
        self.create_competition_button.setDisabled(True)
        self.create_competition_button.clicked.connect(self.create_competition)

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


    def set_layout(self) -> None:
        master_layout = QGridLayout()
        grid1 = QHBoxLayout()
        grid2 = QVBoxLayout()
        grid2_col1 = QVBoxLayout(self.frame1)
        grid2_col2 = QVBoxLayout(self.frame2)
        grid2_col2_row1 = QHBoxLayout()
        grid2_col3 = QHBoxLayout(self.frame3)
        grid2_col4 = QHBoxLayout()
        grid3 = QVBoxLayout(self.frame4)

        grid1.addWidget(self.competition_label)
        grid1.addWidget(self.competition_name_label)
        grid1.setStretch(1, 1)

        grid2_col1.addWidget(self.country_label)
        grid2_col1.addWidget(self.country_combobox)

        grid2_col2_row1.addWidget(self.team_combobox)
        grid2_col2_row1.addWidget(self.team_button)

        grid2_col2.addWidget(self.team_label)
        grid2_col2.addLayout(grid2_col2_row1)

        grid2_col3.addWidget(self.create_country_button)
        grid2_col3.addWidget(self.create_team_button)

        grid2_col4.addWidget(self.go_back_button)
        grid2_col4.addWidget(self.create_competition_button)

        grid2.addWidget(self.competition_name_button)
        grid2.addItem(self.verticalspacer1)
        grid2.addWidget(self.frame1)
        grid2.addWidget(self.frame2)
        grid2.addWidget(self.frame3)
        grid2.addItem(self.verticalspacer2)
        grid2.addLayout(grid2_col4)

        grid3.addWidget(self.teams_label)
        grid3.addWidget(self.team_listwidget)

        master_layout.addLayout(grid1,             0, 0, 1, 2)
        master_layout.addWidget(self.line,         1, 0, 1, 2)
        master_layout.addLayout(grid2,             2, 0, 2, 1)
        master_layout.addWidget(self.frame4,       3, 1, 1, 1)

        self.setLayout(master_layout)


    def error_message(self) -> str:
        error = ErrorDialog("verkeerde text ingevuld")
        error.exec()
        return ""


    def init_name_label(self) -> None:
        self.comp_dialog = CreateDialog("Competitie", "Competitie Naam")
        if self.comp_dialog.aproved is not None:
            self.comp_dialog.aproved.clicked.connect(self.set_competition_name)
        self.comp_dialog.exec()


    def set_competition_name(self) -> None:
        if data.validate_text(self.comp_dialog.line_edit.text()):
            self.competition_name_label.setText(self.comp_dialog.line_edit.text())
            self.comp_dialog.close()
            self.create_competition_button.setDisabled(data.validate_comp(self.competition_name_label.text(), self.team_listwidget.count()))
        else:
            self.comp_dialog.line_edit.setText(self.error_message())


    def init_create_country(self) -> None:
        self.country_dialog = CreateDialog("land", "Land Naam")
        if self.country_dialog.aproved is not None:
            self.country_dialog.aproved.clicked.connect(self.create_country)
        self.country_dialog.exec()


    def create_country(self) -> None:
        if data.validate_text(self.country_dialog.line_edit.text()):
            data.insert_country(self.country_dialog.line_edit.text())
            self.country_combobox.clear()
            self.country_combobox.addItems(data.map_countries())
            self.country_dialog.close()
            self.create_team_button.setDisabled(False)
        else:
            self.country_dialog.line_edit.setText(self.error_message())


    def init_create_team(self) -> None:
        self.team_dialog = CreateDialog("ploeg", "Ploeg Naam")
        if self.team_dialog.aproved is not None:
            self.team_dialog.aproved.clicked.connect(self.create_team)
        self.team_dialog.exec()


    def create_team(self) -> None:
        if data.validate_text(self.team_dialog.line_edit.text()):
            data.insert_team(self.country_combobox.currentText(), self.team_dialog.line_edit.text())
            self.team_combobox.clear()
            self.team_listwidget.addItem(self.team_dialog.line_edit.text())
            self.create_country_button.setDisabled(True)
            self.team_dialog.close()
            self.create_competition_button.setDisabled(data.validate_comp(self.competition_name_label.text(), self.team_listwidget.count()))
        else:
            self.team_dialog.line_edit.setText(self.error_message())


    def changed_country(self) -> None:
        self.team_combobox.clear()
        self.team_combobox.addItems(data.map_teams(self.country_combobox.currentText()))
        if self.team_combobox.currentText() == "":
            self.team_button.setDisabled(True)
        else:
            self.team_button.setDisabled(False)


    def add_teams_to_list(self) -> None:
        self.country_combobox.setDisabled(True)
        self.create_country_button.setDisabled(True)
        team: str = self.team_combobox.currentText()
        team_id: int = self.team_combobox.currentIndex()
        self.team_combobox.removeItem(team_id)
        self.team_listwidget.addItem(team)
        if self.team_combobox.currentText() == "":
            self.team_button.setDisabled(True)
        self.create_competition_button.setDisabled(data.validate_comp(self.competition_name_label.text(), self.team_listwidget.count()))


    def create_competition(self) -> None:
        data.insert_league(self.country_combobox.currentText(), self.competition_name_label.text())
        clubs: list[str] = []
        for club in range(self.team_listwidget.count()):
            item = self.team_listwidget.item(club) 
            if item is not None:
                clubs.append(item.text())
        data.insert_competition(self.competition_name_label.text(), clubs)

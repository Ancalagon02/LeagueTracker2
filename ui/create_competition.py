from datetime import date
from PyQt6.QtCore import QDate, Qt
from PyQt6.QtWidgets import (QDateEdit, QLabel, QWidget, QPushButton, QFrame, QGridLayout, QVBoxLayout, QHBoxLayout,
QSizePolicy, QSpacerItem, QComboBox, QListWidget, QAbstractItemView)
import modules.helpers as helper
import modules.Data_Process as data
from ui.create_dialog import CreateDialog
from ui.error_dialog import ErrorDialog


class CreateCompetition(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Maak Competitie")

        self.init_ui()
        self.set_layout()


    def init_ui(self) -> None:
        self.competition_label = QLabel()
        self.competition_label.setText("Competitie Naam:")

        self.competition_name_label = QLabel()
        self.competition_name_label.setText("Placeholder")

        self.line = QFrame()
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.competition_name_button = QPushButton()
        self.competition_name_button.setText("Competitie Naam")
        self.competition_name_button.clicked.connect(self.init_competition_name)

        self.verticalspacer1 = QSpacerItem(17, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.frame1 = QFrame()
        self.frame1.setFrameShape(QFrame.Shape.Box)
        self.frame1.setFrameShadow(QFrame.Shadow.Plain)
        self.frame1.setLineWidth(4)

        self.country_label = QLabel(self.frame1)
        self.country_label.setText("Selecteer Land")
        self.country_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.country_combobox = QComboBox(self.frame1)
        self.country_combobox.addItems(data.return_country_names())
        self.country_combobox.currentTextChanged.connect(self.changed_country)

        self.frame5 = QFrame()
        self.frame5.setFrameShape(QFrame.Shape.Box)
        self.frame5.setFrameShadow(QFrame.Shadow.Plain)
        self.frame5.setLineWidth(4)

        self.date_label = QLabel(self.frame5)
        self.date_label.setText("Selecteer Datum")
        self.date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.date_picker = QDateEdit(self.frame5)
        self.date_picker.setCalendarPopup(True)
        self.date_picker.setDate(QDate.currentDate())
        self.date_picker.setDisplayFormat("dddd dd MMMM yyyy")

        self.frame2 = QFrame()
        self.frame2.setFrameShape(QFrame.Shape.Box)
        self.frame2.setFrameShadow(QFrame.Shadow.Plain)
        self.frame2.setLineWidth(4)

        self.team_label = QLabel(self.frame2)
        self.team_label.setText("Selecteer Ploeg")
        self.team_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team_combobox = QComboBox(self.frame2)
        self.set_teams()

        self.team_button = QPushButton(self.frame2)
        self.team_button.setText("OK")
        self.team_button.clicked.connect(self.add_team_to_listwidget)
        if self.team_combobox.currentText() == "":
            self.team_button.setDisabled(True)

        self.frame3 = QFrame()
        self.frame3.setFrameShape(QFrame.Shape.Box)
        self.frame3.setFrameShadow(QFrame.Shadow.Plain)
        self.frame3.setLineWidth(4)

        self.create_country_button = QPushButton(self.frame3)
        self.create_country_button.setText("Maak Land")
        self.create_country_button.clicked.connect(self.init_country)

        self.create_team_button = QPushButton(self.frame3)
        self.create_team_button.setText("Maak Ploeg")
        self.create_team_button.clicked.connect(self.init_team)
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
        grid2_col1_2 = QVBoxLayout(self.frame5)
        grid2_col1 = QVBoxLayout(self.frame1)
        grid2_col2 = QVBoxLayout(self.frame2)
        grid2_col2_row1 = QHBoxLayout()
        grid2_col3 = QHBoxLayout(self.frame3)
        grid2_col4 = QHBoxLayout()
        grid3 = QVBoxLayout(self.frame4)

        grid1.addWidget(self.competition_label)
        grid1.addWidget(self.competition_name_label)
        grid1.setStretch(1, 1)

        grid2_col1_2.addWidget(self.date_label)
        grid2_col1_2.addWidget(self.date_picker)

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
        grid2.addWidget(self.frame5)
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

    
    def init_competition_name(self) -> None:
        self.comp_dialog = CreateDialog("Competitie", "Competitie Naam")
        if self.comp_dialog.aproved is not None:
            self.comp_dialog.aproved.clicked.connect(self.set_comp_name)
        self.comp_dialog.exec()


    def set_comp_name(self) -> None:
        comp_name: str = self.comp_dialog.line_edit.text()
        if helper.validate_text(comp_name):
            self.competition_name_label.setText(comp_name)
            self.comp_dialog.close()
            self.set_comp_button()
        else:
            self.comp_dialog.line_edit.setText(self.error_message())


    def init_country(self) -> None:
        self.country_dialog = CreateDialog("Land", "Land Naam")
        if self.country_dialog.aproved is not None:
            self.country_dialog.aproved.clicked.connect(self.create_country)
        self.country_dialog.exec()


    def create_country(self) -> None:
        country_name: str = self.country_dialog.line_edit.text()
        if helper.validate_text(country_name):
            data.create_country(country_name)
            self.country_combobox.clear()
            self.country_combobox.addItems(data.return_country_names())
            self.country_dialog.close()
            self.create_team_button.setDisabled(False)
        else:
            self.country_dialog.line_edit.setText(self.error_message())


    def init_team(self) -> None:
        self.team_dialog = CreateDialog("PLoeg", "Ploeg Naam")
        if self.team_dialog.aproved is not None:
            self.team_dialog.aproved.clicked.connect(self.create_team)
        self.team_dialog.exec()


    def create_team(self) -> None:
        country_name: str = self.country_combobox.currentText()
        team_name: str = self.team_dialog.line_edit.text()
        if helper.validate_text(team_name):
            data.create_team(country_name, team_name)
            self.team_listwidget.addItem(team_name)
            self.create_country_button.setDisabled(True)
            self.country_combobox.setDisabled(True)
            self.team_dialog.close()
            self.set_comp_button()
        else:
            self.team_dialog.line_edit.setText(self.error_message())


    def set_teams(self) -> None:
        country_name: str = self.country_combobox.currentText()
        self.team_combobox.addItems(data.return_team_names(country_name))


    def changed_country(self) -> None:
        self.team_combobox.clear()
        self.set_teams()
        if self.team_combobox.currentText() == "":
            self.team_button.setDisabled(True)
        else:
            self.team_button.setDisabled(False)


    def set_comp_button(self) -> None:
        label: str = self.competition_name_label.text()
        list_count: int = self.team_listwidget.count()
        self.create_competition_button.setDisabled(helper.validate_comp(label, list_count))


    def add_team_to_listwidget(self) -> None:
        self.country_combobox.setDisabled(True)
        self.create_country_button.setDisabled(True)
        team: str = self.team_combobox.currentText()
        team_id: int = self.team_combobox.currentIndex()
        self.team_combobox.removeItem(team_id)
        self.team_listwidget.addItem(team)
        if self.team_combobox.currentText() == "":
            self.team_button.setDisabled(True)
        self.set_comp_button()


    def create_league(self, league_name: str) -> None:
        country_name: str = self.country_combobox.currentText()
        data.create_league(country_name, league_name)


    def create_competition(self) -> None:
        league_name: str = self.competition_name_label.text()
        play_date: date = self.date_picker.date().toPyDate()
        self.create_league(league_name)
        teams: list[str] = []
        for club in range(self.team_listwidget.count()):
            team = self.team_listwidget.item(club)
            if team is not None:
                teams.append(team.text())
                data.create_match(team.text(), play_date)
        data.create_competition(teams, league_name)
        data.create_matches(teams, league_name)

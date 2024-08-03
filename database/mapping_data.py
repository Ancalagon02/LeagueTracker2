from PyQt6.QtWidgets import QComboBox
from database.data import Data
from models import Club, Country
from ui.create_dialog import CreateDialog
from ui.error_dialog import ErrorDialog


def map_country_combobox(combobox: QComboBox) -> None:
    data: list[Country] = Data().read_countries()
    for country in data:
        combobox.addItem(country.name)


def map_teams_combobox(country_combobox: QComboBox, team_combobox: QComboBox) -> None:
    country_id: int = Data().read_country_by_name(country_combobox.currentText())
    data: list[Club] = Data().read_teams_by_country_id(country_id)
    for team in data:
        team_combobox.addItem(team.name)


def map_team_insert(country_combobox: QComboBox, window: CreateDialog) -> None:
    country_id: int = Data().read_country_by_name(country_combobox.currentText())
    Data().create_team(country_id, window.line_edit.text())


def validate_text(window: CreateDialog) -> bool:
    output: bool = False
    if (window.line_edit.text().lower().isdigit() == True or
            window.line_edit.text().lower() == "" or 
            window.line_edit.text().lower().isspace() == True):
        error = ErrorDialog("Naam moet text bevatten")
        error.exec()
        output = False
    else:
        output = True
    if output == False:
        window.line_edit.setText("")
    return output

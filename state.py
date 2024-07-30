import database.data as data
from ui.create_dialog import CreateDialog
from ui.error_dialog import ErrorDialog


def load_countries() -> list:
    return data.read_countries()


def create_country(name: str):
    data.create_country(name)


def load_country_id(name: str) -> int:
    return data.read_country_by_name(name)


def create_team(country_id: int, club_name: str):
    data.create_team(country_id, club_name)


def load_team(country_id: int) -> list:
    return data.read_teams_by_country_id(country_id)


def checked_text(window: CreateDialog):
    error_dialog = ErrorDialog()
    if window.line_edit.text().isdigit() == True or window.line_edit.text().isspace() == True or window.line_edit.text() == "":
        error_dialog.label.setText("Verkeerde text ingevuld!")
        error_dialog.exec()
        window.line_edit.setText("")
        return False

    return True


def init_dialog(title: str, label: str) -> CreateDialog:
    window = CreateDialog()
    window.setWindowTitle(title)
    window.label.setText(label)
    return window

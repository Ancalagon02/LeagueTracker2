from database.data import Data
from ui.create_dialog import CreateDialog
from ui.main_window import MainWindow
from ui.create_competition import CreateCompetition


class State:
    def __init__(self) -> None:
        self.data = Data()


    def create_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.main_window.country_combobox.addItems(self.data.read_countries())
        self.main_window.create_competition_button.clicked.connect(self.show_comp)


    def show_comp(self) -> None:
        self.create_competition = CreateCompetition()
        self.create_competition.show()
        self.create_competition.country_combobox.addItems(self.data.read_countries())
        self.create_competition.go_back_button.clicked.connect(self.show_main)
        self.create_competition.competition_name_button.clicked.connect(self.set_comp_name)
        self.main_window.close()
        del self.main_window


    def show_main(self) -> None:
        self.create_window()
        self.create_competition.close()
        del self.create_competition


    def set_comp_name(self) -> None:
        window: CreateDialog = self.create_dialog("Competitie", "Competitie Naam")
        window.exec()


    def create_dialog(self, title: str, label: str) -> CreateDialog:
        window = CreateDialog()
        window.setWindowTitle(title)
        window.label.setText(label)
        return window

from ui.main_window import MainWindow
from ui.create_competition import CreateCompetition
from ui.competition import Competition
from ui.matches import Matches

class State:
    def __init__(self):
        self.league_name: str = ""


    def init_main_window(self) -> None:
        self.main_window = MainWindow()
        self.main_window.create_competition_button.clicked.connect(self.init_competition_window)
        self.main_window.start_competition_button.clicked.connect(self.init_comp_from_main)
        self.main_window.show()


    def init_competition_window(self) -> None:
        self.comp_window = CreateCompetition()
        self.comp_window.go_back_button.clicked.connect(self.return_main_window_from_comp)
        self.comp_window.create_competition_button.clicked.connect(self.init_comp_from_comp)
        self.comp_window.show()
        self.main_window.close()


    def return_main_window_from_comp(self) -> None:
        self.init_main_window()
        self.comp_window.close()


    def return_main_window_from_league(self) -> None:
        self.init_main_window()
        self.league_window.close()


    def init_competition(self) -> None:
        self.league_window = Competition(self.league_name)
        self.league_window.go_back_button.clicked.connect(self.return_main_window_from_league)
        self.league_window.exit_putton.clicked.connect(lambda: self.league_window.close())
        self.league_window.match_button.clicked.connect(self.init_match_window)
        self.league_window.show()


    def init_comp_from_main(self) -> None:
        self.league_name = self.main_window.competition_name_label.text()
        self.init_competition()
        self.main_window.close()

    
    def init_comp_from_comp(self) -> None:
        self.league_name = self.comp_window.competition_name_label.text()
        self.init_competition()
        self.comp_window.close()


    def init_match_window(self) -> None:
        self.match = Matches(self.league_window)
        self.match.go_back_button.clicked.connect(self.close_match)
        self.match.show()


    def close_match(self) -> None:
        del self.match

from ui.main_window import MainWindow
from ui.create_competition import CreateCompetition

class State:
    def init_main_window(self) -> None:
        self.main_window = MainWindow()
        self.main_window.create_competition_button.clicked.connect(self.init_competition_window)
        self.main_window.show()


    def init_competition_window(self) -> None:
        self.comp_window = CreateCompetition()
        self.comp_window.go_back_button.clicked.connect(self.return_main_window)
        self.comp_window.show()
        self.main_window.close()


    def return_main_window(self) -> None:
        self.init_main_window()
        self.comp_window.close()

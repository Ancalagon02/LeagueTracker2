from PyQt6.QtWidgets import QWidget


class MainWindow(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app

    def quit_app(self):
        self.app.quit()

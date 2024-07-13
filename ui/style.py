from pathlib import Path
from PyQt6.QtWidgets import QWidget

class Style(QWidget):
    def __init__(self):
        super().__init__()
        filepath = Path(__file__).parent / "style.css"
        with open(filepath, "r") as f:
            style = f.read()
            self.setStyleSheet(style)

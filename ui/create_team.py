from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QDialogButtonBox, QVBoxLayout

class CreateTeam(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Maak Ploeg")

        self.init_ui()
        self.set_layout()


    def init_ui(self):
        self.label = QLabel()
        self.label.setText("Ploeg Naam")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.team_lineedit = QLineEdit()

        self.buttonbox = QDialogButtonBox()
        self.buttonbox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonbox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)
        self.buttonbox.setCenterButtons(True)


    def set_layout(self):
        self.master_layout = QVBoxLayout()

        self.master_layout.addWidget(self.label)
        self.master_layout.addWidget(self.team_lineedit)
        self.master_layout.addWidget(self.buttonbox)

        self.setLayout(self.master_layout)

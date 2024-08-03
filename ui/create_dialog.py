from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QDialogButtonBox, QVBoxLayout

class CreateDialog(QDialog):
    def __init__(self, title: str, label: str):
        super().__init__()

        self.setWindowTitle(title)
        self.label_text = label

        self.init_ui()
        self.set_layout()


    def init_ui(self) -> None:
        self.label = QLabel()
        self.label.setText(self.label_text)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.line_edit = QLineEdit()

        self.buttonbox = QDialogButtonBox()
        self.buttonbox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonbox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)
        self.buttonbox.setCenterButtons(True)
        
        self.aproved = self.buttonbox.button(QDialogButtonBox.StandardButton.Ok)
        self.cancel = self.buttonbox.button(QDialogButtonBox.StandardButton.Cancel)

        if self.cancel is not None:
            self.cancel.clicked.connect(self.close)


    def set_layout(self) -> None:
        master_layout = QVBoxLayout()

        master_layout.addWidget(self.label)
        master_layout.addWidget(self.line_edit)
        master_layout.addWidget(self.buttonbox)

        self.setLayout(master_layout)

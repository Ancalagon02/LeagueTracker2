from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QLabel, QDialogButtonBox, QVBoxLayout

class ErrorDialog(QDialog):
    def __init__(self, label: str) -> None:
        super().__init__()

        self.setWindowTitle("Error")
        self.label_text = label

        self.init_ui()
        self.set_layout()


    def init_ui(self) -> None:
        self.label = QLabel()
        self.label.setText(self.label_text)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.buttonbox = QDialogButtonBox()
        self.buttonbox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonbox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
        self.buttonbox.setCenterButtons(True)
        
        self.aproved = self.buttonbox.button(QDialogButtonBox.StandardButton.Ok)

        if self.aproved is not None:
            self.aproved.clicked.connect(self.close)


    def set_layout(self) -> None:
        master_layout = QVBoxLayout()

        master_layout.addWidget(self.label)
        master_layout.addWidget(self.buttonbox)

        self.setLayout(master_layout)

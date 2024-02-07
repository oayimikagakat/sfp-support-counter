from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout

from app import ROOT_DIR
from src.button import IdolButton, CountButton
from src.settings import load_settings


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.count_buttons = list()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("SFP Support Counter")
        self.setWindowIcon(QIcon(str(ROOT_DIR / "icon.png")))
        self.resize(960, 84)
        self.setStyleSheet("background-color: black;")
        self.setup_buttons()
        self.show()

    def setup_buttons(self):
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.count_buttons = list()
        idols = load_settings()
        for idx in range(len(idols)):
            idol_button = IdolButton(idx + 1, idols[idx])
            layout.addWidget(idol_button)

            count_button = CountButton()
            self.count_buttons.append(count_button)
            layout.addWidget(count_button)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F4:
            for count_button in self.count_buttons:
                count_button.reset_count()
        else:
            super().keyPressEvent(event)

import sys

from PyQt5.QtWidgets import QApplication
from gui import MainWindow


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

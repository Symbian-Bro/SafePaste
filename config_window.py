import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QDialog, QFileDialog, QApplication
from configs import Ui_ApplicationSetup

class ConfigWindow(QDialog, Ui_ApplicationSetup):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connect_signals()

    def connect_signals(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConfigWindow()
    window.show()
    sys.exit(app.exec())
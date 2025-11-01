import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow

from ui_generated import Ui_CommandLineTool

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CommandLineTool()
        self.ui.setupUi(self)
        self.connect_signals()

    def connect_signals(self):
        self.ui.sendButton.clicked.connect(self.on_send_clicked)
        self.ui.fetchButton.clicked.connect(self.on_fetch_clicked)
    
    def on_send_clicked(self):
        print("Send button clicked")

    def on_fetch_clicked(self):
        print("Fetch button clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
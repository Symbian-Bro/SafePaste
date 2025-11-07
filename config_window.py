import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QDialog, QFileDialog, QApplication
from configs import Ui_ApplicationSetup

class ConfigWindow(QDialog, Ui_ApplicationSetup):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connect_signals()
        self.selected_file_path = ""

    def connect_signals(self):
        self.selectFileButton.clicked.connect(self.select_file)
        self.buttonBox.accepted.connect(self.accept)


    def select_file(self):
        file_path, not_needed = QFileDialog.getOpenFileName(
            self,
            "Select Firebase Admin Credentials",
            "",
            "JSON Files (*.json)"
        )
        if file_path:
            self.selected_file_path = file_path
            self.selectedFileLabel.setText(file_path)

    def accept(self):
        database_url = self.lineEdit_url.text().strip()
        if not database_url:
            print("Please enter a valid database URL.")
            return

        if not self.selected_file_path:
            print("Please select a valid Firebase Admin Credentials file.")
            return
        
        with open("config.txt", "w") as config_file:
            config_file.write(f"{database_url}\n")
            config_file.write(f"{self.selected_file_path}\n")
        super().accept()      
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConfigWindow()
    window.show()
    sys.exit(app.exec())
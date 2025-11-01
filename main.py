import sys
import random
import string
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow

from ui_generated import Ui_CommandLineTool
from cryptography.fernet import Fernet

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CommandLineTool()
        self.ui.setupUi(self)
        self.connect_signals()

    def connect_signals(self):
        self.ui.sendButton.clicked.connect(self.on_send_clicked)
        self.ui.fetchButton.clicked.connect(self.on_fetch_clicked)

    def encrypt_string(plain_text: str) -> tuple[bytes, bytes]:
        key = Fernet.generate_key()
        cipher = Fernet(key)
        plain_text_bytes = plain_text.encode('utf-8')
        encrypted_blob = cipher.encrypt(plain_text_bytes)
        return encrypted_blob, key

    def random_string(length: int =  7) -> str:
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))
    
    def on_send_clicked(self):
        print("Send button clicked")

    def on_fetch_clicked(self):
        print("Fetch button clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
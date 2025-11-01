import sys
import random
import string
import firebase_admin
import base64

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_generated import Ui_CommandLineTool
from cryptography.fernet import Fernet
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccountKey.json")

DATABASE_URL = 'https://safepaste-2e585-default-rtdb.firebaseio.com/'

try:
    firebase_admin.initialize_app(cred, {
        'databaseURL': DATABASE_URL
    })
    db_ref = db.reference('pastes')
except ValueError:
    print("Firebase already initialized...")
    db_ref = db.reference('pastes')

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CommandLineTool()
        self.ui.setupUi(self)
        self.connect_signals()

    def connect_signals(self):
        self.ui.sendButton.clicked.connect(self.on_send_clicked)
        self.ui.fetchButton.clicked.connect(self.on_fetch_clicked)
        self.ui.clipboardButton.clicked.connect(self.on_copy_clicked)

    @staticmethod
    def encrypt_string(plain_text: str) -> tuple[bytes, bytes]:
        key = Fernet.generate_key()
        cipher = Fernet(key)
        plain_text_bytes = plain_text.encode('utf-8')
        encrypted_blob = cipher.encrypt(plain_text_bytes)
        return encrypted_blob, key

    @staticmethod
    def decrypt_string(encrypted_blob: bytes, key: bytes) -> str:
        cipher = Fernet(key)
        decrypted_bytes = cipher.decrypt(encrypted_blob)
        return decrypted_bytes.decode('utf-8')

    @staticmethod
    def random_string(length: int =  10) -> str:
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))
    
    def on_send_clicked(self):
        plain_text = self.ui.sendTextEdit.toPlainText()
        if not plain_text:
            self.ui.idLabel.setText("ID - (Please enter text to send)")
            return
        encrypted_blob, key = self.encrypt_string(plain_text)
        rand_str = self.random_string()

        key_b64 = base64.b64encode(key)
        enc_blob_b64 = base64.b64encode(encrypted_blob)

        key_str = key_b64.decode('utf-8')
        encrypted_blob = enc_blob_b64.decode('utf-8')
        db_ref.child(rand_str).set(encrypted_blob)
        output_display = f"{key_str} : {rand_str}"
        self.ui.idLabel.setText(output_display)
        self.ui.sendTextEdit.clear()

    def on_fetch_clicked(self):
        print("Fetch button clicked")

    def on_copy_clicked(self):
        id_string = self.ui.idLabel.text()
        if "ID - " in id_string and ":" not in id_string:
            return
        clipboard = QApplication.clipboard()
        clipboard.setText(id_string.strip())
        self.ui.statusbar.showMessage("Copied to clipboard!", 2000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
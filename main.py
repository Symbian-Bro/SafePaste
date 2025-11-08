import sys
from PyQt6.QtWidgets import QApplication
from app_window import MainWindow
from config_window import ConfigWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConfigWindow()
    window.show()
    sys.exit(app.exec())
# SafePaste - A secure, cross-platform clipboard/text sharing tool.
# Copyright (C) 2025 SIDDHARTH K P
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import sys
from PyQt6.QtWidgets import QApplication,QDialog
from windowsnfunctions.config_window import ConfigWindow
from pathlib import Path

config_dir = Path.home() / ".safepaste"
config_file = config_dir / "config.txt"
key_file = config_dir / "serviceAccountKey.json"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if not(config_file.is_file() and key_file.is_file()):
        window = ConfigWindow()
        result = window.exec()
        if result == QDialog.DialogCode.Rejected:
            sys.exit(0)
    from windowsnfunctions.app_window import MainWindow
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
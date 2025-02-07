from os import name
import sys
from PyQt5.QtWidgets import QApplication
from registration import RegistrationWindow
from main_window import Main


if __name__ == '__main__':
    app = QApplication(sys.argv)
    registration = RegistrationWindow()
    registration.show()
    sys.exit(app.exec())

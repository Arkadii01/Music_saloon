import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class RegistrationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('windows/enter_window.ui', self)
        self.registration_part.hide()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    registration = RegistrationWindow()
    registration.show()
    sys.exit(app.exec())

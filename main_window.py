from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('windows/main.ui', self)
        # добавление настроек
        self.paused = True
        self.btn_start.setIcon(QIcon('img/start.png'))
        self.btn_next.setIcon(QIcon('img/next.png'))
        self.btn_previous.setIcon(QIcon('img/previous.png'))
        self.btn_menu.setIcon(QIcon('img/menu.png'))
        self.btn_start.clicked.connect(self.start)
        
    def start(self):
        if self.paused:
            self.btn_start.setIcon(QIcon('img/stop.png'))
            self.paused = False
        else:
            self.btn_start.setIcon(QIcon('img/start.png'))
            self.paused = True
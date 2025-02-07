from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_window import Main


class RegistrationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('windows/enter_window.ui', self)
        self.open_enter()
        self.main = Main()
        self.enter_btn_registration.clicked.connect(self.open_registration)
        self.registration_btn_back.clicked.connect(self.open_enter)
        self.enter_btn_enter.clicked.connect(self.open_main_window)
        
    def hide_everything(self):
        for i in range(self.enter_part.count()):
            widget = self.enter_part.itemAt(i).widget()
            if widget is not None: widget.hide()
        for i in range(self.registration_part.count()):
            widget = self.registration_part.itemAt(i).widget()
            if widget is not None: widget.hide()
            
        
    def open_enter(self):
        self.hide_everything()
        for i in range(self.enter_part.count()):
            widget = self.enter_part.itemAt(i).widget()
            if widget is not None: widget.show()
    
    def open_registration(self):
        self.hide_everything()
        for i in range(self.registration_part.count()):
            widget = self.registration_part.itemAt(i).widget()
            if widget is not None: widget.show()
            
    def open_main_window(self):
        # ÏÐÎÂÅÐÊÀ Â ÁÄ
        self.main.show()
        self.close()
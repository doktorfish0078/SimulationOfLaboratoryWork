import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from converted_forms_to_py import start_window
from py_code_labs import laba_2, laba_11, laba_14, laba_15


class Start_window(QMainWindow):
    """Класс стартового окна"""
    def __init__(self):
        super().__init__()
        self.ui = start_window.Ui_start_window()
        self.ui.setupUi(self)

        # constants
        self.laba_2 = laba_2.Laba2()
        self.laba_11 = laba_11.Laba11()
        self.laba_14 = laba_14.Laba14()
        self.laba_15 = laba_15.Laba15()

        # connects
        self.ui.button_laba2.clicked.connect(self.start_laba_2)
        self.ui.button_laba11.clicked.connect(self.start_laba_11)
        self.ui.button_laba14.clicked.connect(self.start_laba_14)
        self.ui.button_laba15.clicked.connect(self.start_laba_15)

    def start_laba_2(self):
        """Открывает форму 2ой лабы"""
        self.laba_2.show()
        # window.hide()

    def start_laba_11(self):
        """Открывает форму 11ой лабы"""
        self.laba_11.show()
        # window.hide()

    def start_laba_14(self):
        """Открывает форму 14ой лабы"""
        self.laba_14.show()
        # window.hide()

    def start_laba_15(self):
        """Открывает форму 15ой лабы"""
        self.laba_15.show()
        # window.hide()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Start_window()
    window.show()
    app.exec_()

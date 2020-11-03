import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from converted_forms_to_py import start_window
from py_code_labs import laba_2, laba_11, laba_14, laba_15


class Start_window(QMainWindow, start_window.Ui_start_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # constants
        self.laba_2 = laba_2.Laba2()
        self.laba_11 = laba_11.Laba11()
        self.laba_14 = laba_14.Laba14()
        self.laba_15 = laba_15.Laba15()

        # connects
        self.button_laba2.clicked.connect(self.start_laba_2)
        self.button_laba11.clicked.connect(self.start_laba_11)
        self.button_laba14.clicked.connect(self.start_laba_14)
        self.button_laba15.clicked.connect(self.start_laba_15)

    def start_laba_2(self):
        self.laba_2.show()
        # window.hide()

    def start_laba_11(self):
        self.laba_11.show()
        # window.hide()

    def start_laba_14(self):
        self.laba_14.show()
        # window.hide()

    def start_laba_15(self):
        self.laba_15.show()
        # window.hide()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Start_window()
    window.show()
    app.exec_()

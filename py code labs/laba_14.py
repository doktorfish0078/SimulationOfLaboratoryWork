import sys
from math import sqrt

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from converted_forms_to_py import laba14


class Laba14(QMainWindow, laba14.Ui_Laba14):
    amperage = 0.0

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.amperDial.valueChanged.connect(self.set_amperage)
        self.amperDial.valueChanged.connect(self.set_induction)
        self.shtok.valueChanged.connect(self.set_induction)

    def set_amperage(self):
        # print(float(self.amperDial.value())/10)
        self.amperage = self.amperDial.value() / 10
        self.amperOut.setText(str(self.amperage))

    def set_induction(self):
        # constants
        sl = 10 ** (-2) * self.shtok.value()
        self.shtokValue.move(480 + self.shtok.value() * 4.2, 460)
        self.shtokValue.setText(str(47 - self.shtok.value()))
        self.shtokRealValue.move(480 + self.shtok.value() * 4.2, 580)
        self.shtokRealValue.setText(str(self.shtok.value()))
        if sl < 0:
            self.mainOut.setText('0.0')
            return
        mu = 10 ** (-7) * 12.57
        n = 2000
        # shtok len:
        len = 0.38
        r = 0.0125
        # это пока нужно для того, чтобы заного не писать):
        # print(sl, '{:f}'.format(mu), n, self.amperage, len, r)
        # print("%.15f" % (mu * self.amperage * n / 2))
        # print("%.15f" % ((len - sl) / sqrt(r ** 2 + (len - sl) ** 2)))
        # print("%.15f" % (sl / sqrt(r ** 2 + sl ** 2)))
        self.mainOut.setText("%.15f" % (1000 * (mu * self.amperage * n / 2) *
                                           ((len - sl) / sqrt(r ** 2 + (len - sl) ** 2) + sl / sqrt(r ** 2 + sl ** 2))))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Laba14()
    window.show()
    app.exec_()
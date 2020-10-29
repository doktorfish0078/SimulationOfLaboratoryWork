import sys
from math import sqrt

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow

from converted_forms_to_py import laba14


class Laba14(QMainWindow, laba14.Ui_Laba14):
    # global const
    amperage = 0.0
    stok_x = 0
    stok_y = 0


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # const ini
        self.stok_x = self.label_stock.geometry().getCoords()[0]
        self.stok_y = self.label_stock.geometry().getCoords()[1]
        # set pixmaps
        self.label_instrumentation.setPixmap(QPixmap("..\\images\\laba_14\\pribori.png"))
        self.label_stock.setPixmap(QPixmap("..\\images\\laba_14\\stock.png"))
        self.label_solenoid.setPixmap(QPixmap("..\\images\\laba_14\\solenoid.png"))

        # connects
        self.amperDial.valueChanged.connect(self.set_amperage)
        self.amperDial.valueChanged.connect(self.set_induction)
        self.slider_stock.valueChanged.connect(self.set_induction)

    def set_amperage(self):
        # print(float(self.amperDial.value())/10)
        self.amperage = self.amperDial.value() / 10
        self.amperOut.setText(str(self.amperage))

    def set_induction(self):
        # constants
        shtk_dist = (float(self.slider_stock.value())/2.0);
        sl = 10 ** (-2) * shtk_dist
        self.shtokValue.setText(' ' + str(47 - shtk_dist))

        self.label_stock.move(
            # self.slider_stock.
            self.stok_x+(self.slider_stock.value()+6)*5-0.12*(self.slider_stock.value()+6),
            self.stok_y)

        self.label_stock_head.move(
            # self.slider_stock.
            self.label_stock.geometry().getCoords()[2],
            self.label_stock_head.geometry().getCoords()[1])

        if sl < 0:
            self.mainOut.setText(str("%.4f" % 0))
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
        self.mainOut.setText("%.4f" % (1000 * (mu * self.amperage * n / 2) *
                                           ((len - sl) / sqrt(r ** 2 + (len - sl) ** 2) + sl / sqrt(r ** 2 + sl ** 2))))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Laba14()
    window.show()
    app.exec_()
import sys
from math import sqrt

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget

from converted_forms_to_py import laba14
from converted_forms_to_py import info_laba

from svg_widgets import svg_widget_ammeter


class Info_laba(QWidget, info_laba.Ui_info_laba_11):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # set pixmaps
        self.label_info.setPixmap(QPixmap("..\\images\\laba_14\\info_laba_14.jpg"))


class Laba14(QMainWindow, laba14.Ui_Laba14):
    # global const
    amperage = 0.0
    stok_x = 0
    stok_y = 0


    def __init__(self):

        # constants
        self.info_laba_14 = Info_laba()

        super().__init__()
        self.setupUi(self)
        # const ini
        self.stok_x = self.label_stock.geometry().getCoords()[0]
        self.stok_y = self.label_stock.geometry().getCoords()[1]

        self.amperOut = svg_widget_ammeter.svg_widget_ammeter()
        self.verticalLayout.addWidget(self.amperOut.svg_widget)

        # set pixmaps
        self.label_instrumentation.setPixmap(QPixmap("..\\images\\laba_14\\pribori.png"))
        self.label_stock.setPixmap(QPixmap("..\\images\\laba_14\\stock.png"))
        self.label_solenoid.setPixmap(QPixmap("..\\images\\laba_14\\solenoid.png"))
        self.label_formula.setPixmap(QPixmap("..\\images\\laba_14\\formula.png"))
        self.label_lupa.setPixmap(QPixmap("..\\images\\laba_14\\lupa.png"))
        self.label_stock_head.setPixmap(QPixmap("..\\images\\laba_14\\stock_head.png"))
        self.button_info.setIcon(QIcon("..\\images\\laba_14\\info.png"))

        # connects
        self.amperDial.valueChanged.connect(self.set_amperage)
        self.amperDial.valueChanged.connect(self.set_induction)
        self.slider_stock.valueChanged.connect(self.set_induction)
        self.button_info.clicked.connect(self.show_info_about_laba)

    def show_info_about_laba(self):
        self.info_laba_14.show()

    def set_amperage(self):
        # print(float(self.amperDial.value())/10)
        self.amperage = self.amperDial.value() / 10
        self.amperOut.update_svg_ammeter(self.amperage)

    def set_induction(self):
        # constants
        shtk_dist = (float(self.slider_stock.value())/2.0);
        sl = 10 ** (-2) * shtk_dist
        self.shtokValue.setText('   ' + str(47 - shtk_dist))

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
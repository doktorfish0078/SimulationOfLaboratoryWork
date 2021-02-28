# -*- coding: utf-8 -*-
import sys
from math import sqrt

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow

from converted_forms_to_py import laba14
from py_code_labs.info_laba import Info_laba
from svg_widgets.svg_widget_ammeter import svg_widget_ammeter


class Laba14(QMainWindow):
    """Класс лабы 14, инициализирует форму и
    заполняет её элементами
    """

    def __init__(self):
        super().__init__()
        self.ui = laba14.Ui_Laba14()
        self.ui.setupUi(self)

        # set icon
        icon = QIcon()
        icon.addPixmap(QPixmap("../images/icon.png"),
                       QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        # constants
        self.info_laba_14 = Info_laba()

        self.amperage = 0.0

        self.cord_x_stock = self.ui.label_stock.geometry().getCoords()[0]
        self.cord_y_stock = self.ui.label_stock.geometry().getCoords()[1]

        # set widgets
        self.ui.ammeter = svg_widget_ammeter()
        self.ui.verticalLayout.addWidget(self.ui.ammeter.svg_widget)

        # set pixmaps
        self.ui.label_instrumentation.setPixmap(QPixmap("..\\images\\laba_14\\pribori.png"))
        self.ui.label_stock.setPixmap(QPixmap("..\\images\\laba_14\\stock.png"))
        self.ui.label_solenoid.setPixmap(QPixmap("..\\images\\laba_14\\solenoid.png"))
        self.ui.label_formula.setPixmap(QPixmap("..\\images\\laba_14\\formula.png"))
        self.ui.label_lupa.setPixmap(QPixmap("..\\images\\laba_14\\lupa.png"))
        self.ui.label_stock_head.setPixmap(QPixmap("..\\images\\laba_14\\stock_head.png"))
        self.ui.button_info.setIcon(QIcon("..\\images\\laba_14\\info.png"))

        # connects
        self.ui.amperDial.valueChanged.connect(self.set_amperage)
        self.ui.amperDial.valueChanged.connect(self.set_induction)
        self.ui.slider_stock.valueChanged.connect(self.set_induction)
        self.ui.button_info.clicked.connect(self.show_info_about_laba)

        # add info pictures about laba
        self.info_laba_14.add_picture_in_scroll_area_content("../images/laba_14/info_laba_14_1.jpg")
        self.info_laba_14.add_picture_in_scroll_area_content("../images/laba_14/info_laba_14_2.jpg")

    def show_info_about_laba(self):
        """Показывает окно с документацией по
        выполнению л.р.
        """
        self.info_laba_14.show()

    def set_amperage(self):
        """Коннектится к amperDial, когда изменяется
        значение пересчитывает ампераж и
        передаёт его амперметру,чтобы тот
        обновил показания
        """
        self.amperage = self.ui.amperDial.value() / 10
        self.ui.ammeter.update_svg_ammeter(self.amperage)

    def set_induction(self):
        """Коннектится к amperDial и slider_stock, когда
        изменяется значение одного из них,то
        Вычисляет индукцию магнитного поля
        соленоида(штока) в соответствии с
        формулой
        """
        # constants
        shtk_dist = (float(self.ui.slider_stock.value())/2.0)
        sl = 10 ** (-2) * shtk_dist
        self.ui.shtokValue.setText('   ' + str(47 - shtk_dist))

        self.ui.label_stock.move(
            int(self.cord_x_stock + (self.ui.slider_stock.value() + 6) * 5 - 0.12 * (self.ui.slider_stock.value() + 6)), self.cord_y_stock)

        self.ui.label_stock_head.move(
            self.ui.label_stock.geometry().getCoords()[2],
            self.ui.label_stock_head.geometry().getCoords()[1])

        if sl < 0:
            self.ui.mainOut.setText(str("%.4f" % 0))
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
        self.ui.mainOut.setText("%.4f" % (1000 * (mu * self.amperage * n / 2) *
                                           ((len - sl) / sqrt(r ** 2 + (len - sl) ** 2) + sl / sqrt(r ** 2 + sl ** 2))))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Laba14()
    window.show()
    app.exec_()
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'path/to/design.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QStyleFactory
from math import sqrt


class Laba14(QMainWindow):
    amperage = 0.0

    def __init__(self):
        super(Laba14, self).__init__()
        uic.loadUi('laba14.ui', self)
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
        self.mainOut.setText("%.4f" % (1000 * (mu * self.amperage * n / 2) *
                                       ((len - sl) / sqrt(r ** 2 + (len - sl) ** 2) + sl / sqrt(r ** 2 + sl ** 2))))


class Laba11(QMainWindow):
    def __init__(self):
        super(Laba11, self).__init__()
        uic.loadUi('laba11.ui', self)

        self.r1_value = 210
        self.r2_value = 405
        self.r3_value = 625
        self.resistence_on_store = 0

        # welcome to GavnoCode Empire, baby

        self.dial_1.valueChanged.connect(self.change_resistors_store_value)
        self.dial_2.valueChanged.connect(self.change_resistors_store_value)
        self.dial_3.valueChanged.connect(self.change_resistors_store_value)
        self.dial_4.valueChanged.connect(self.change_resistors_store_value)
        self.dial_5.valueChanged.connect(self.change_resistors_store_value)
        self.dial_6.valueChanged.connect(self.change_resistors_store_value)

        self.resetButton.clicked.connect(self.reset)

    def change_resistors_store_value(self):
        self.resistence_on_store = self.dial_1.value() * 10000 + self.dial_2.value() * 1000 + \
                                   self.dial_3.value() * 100 + self.dial_4.value() * 10 + \
                                   self.dial_5.value() * 1 + self.dial_6.value() * 0.1

        self.resistors_store.setText('Cопротивление в магазине сопротивлений: {}'.format(self.resistence_on_store))
        if self.PowerCheck.isChecked():
            self.browse_folder()

    def browse_folder(self):
        single = self.single.isChecked()
        parallel = self.parallel.isChecked()
        serial = self.serial.isChecked()

        resistors_used = [[self.check_r1.isChecked(), self.r1_value],
                          [self.check_r2.isChecked(), self.r2_value],
                          [self.check_r3.isChecked(), self.r3_value]]

        value_resistors = 0

        if single or serial or parallel:
            # пока так...
            if (single and serial) or (serial and parallel) or (single and parallel):
                QMessageBox.critical(self, "Нерабочая цепь", "Невозможно так соединить резисторы. Ку-ку?",
                                     QMessageBox.Ok)

            elif single:
                for resistor in resistors_used:
                    if resistor[0]:
                        value_resistors = resistor[1]

            elif serial:
                for resistor in resistors_used:
                    if resistor[0]:
                        value_resistors += resistor[1]

            elif parallel:
                resists = []
                for resistor in resistors_used:
                    if resistor[0]:
                        resists.append(resistor[1])
                value_resistors = (resists[0] * resists[1]) / (resists[0] + resists[1])
        self.voltmeter.setText(str(float("%.2f" % (self.resistence_on_store / 4 - value_resistors))))

    def reset(self):
        for dial in {self.dial_1, self.dial_2, self.dial_3,
                     self.dial_4, self.dial_5, self.dial_6}:
            dial.setValue(0)


class Laba15(QMainWindow):
    def __init__(self):
        super(Laba15, self).__init__()
        uic.loadUi('laba15.ui', self)

        self.total_resistance = 55.5
        self.voltage_regulator = 0
        self.resistance_c = 40
        self.resistance_r = 30
        self.resistance_kat = 54

        self.voltmeter.display(None)

        self.dial.setStyle(QStyleFactory.create('Windows'))
        # print(QStyleFactory.keys())

        self.measure_c_button.clicked.connect(self.measure_c)
        self.measure_3_button.clicked.connect(self.measure_3)
        self.measure_r_button.clicked.connect(self.measure_r)
        # всё так же как с кнопками и проч.
        # Коннектом можно даже соединять один объект с другим, типо два ползунка синхорнно ползут
        self.slider_voltage.valueChanged.connect(self.work)

        self.NetCheck.clicked.connect(self.zero_point_voltmeter)

        self.dial.sliderMoved.connect(self.zero_point)
        self.dial.sliderPressed.connect(self.zero_point)
        self.dial.sliderReleased.connect(self.zero_point)

    def zero_point(self):
        self.dial.setValue(self.voltage_regulator)

    def zero_point_voltmeter(self):
        if not self.NetCheck.isChecked():
            self.voltmeter.display(None)

    def work(self):
        # if self.checkPower.isChecked():
        self.voltage_regulator = self.slider_voltage.value()
        self.dial.setValue(self.voltage_regulator)
        print(self.voltage_regulator)

        self.ammeter.display(self.voltage_regulator / self.total_resistance)

    def measure_c(self):
        if self.NetCheck.isChecked():
            ammeter_value = float("%.3f" % (self.ammeter.value()))
            self.voltmeter.display("%.1f" % (ammeter_value * self.resistance_c))
        else:
            self.voltmeter.display(None)

    def measure_3(self):
        if self.NetCheck.isChecked():
            ammeter_value = float("%.3f" % (self.ammeter.value()))
            self.voltmeter.display("%.1f" % (ammeter_value * self.resistance_kat))
        else:
            self.voltmeter.display(None)

    def measure_r(self):
        if self.NetCheck.isChecked():
            ammeter_value = float("%.3f" % (self.ammeter.value()))
            self.voltmeter.display("%.1f" % (ammeter_value * self.resistance_r))
        else:
            self.voltmeter.display(None)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # window = Laba11()
    window = Laba15()
    # window = Laba14()
    window.show()
    app.exec_()
    input()

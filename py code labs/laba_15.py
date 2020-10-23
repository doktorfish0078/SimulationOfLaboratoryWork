import sys

from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from converted_forms_to_py import laba15


class Laba15(QMainWindow, laba15.Ui_Laba15):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # rearm display
        self.voltmeter.display(None)

        # constants
        self.total_resistance = 55.5
        self.voltage_regulator = 0
        self.resistance_c = 40
        self.resistance_r = 30
        self.resistance_kat = 54

        #set pixmaps
        self.label_resistor.setPixmap(QPixmap("..\\images\\laba_15\\resistor.png"))
        self.label_capacitor.setPixmap(QPixmap("..\\images\\laba_15\\capacitor.png"))
        self.label_coil.setPixmap(QPixmap("..\\images\\laba_15\\coil.png"))

        # connects
        self.measure_c_button.clicked.connect(self.measure_c)
        self.measure_3_button.clicked.connect(self.measure_3)
        self.measure_r_button.clicked.connect(self.measure_r)

        self.slider_voltage.valueChanged.connect(self.work)

        self.NetCheck.clicked.connect(self.zero_point_voltmeter)

    def zero_point_voltmeter(self):
        if not self.NetCheck.isChecked():
            self.voltmeter.display(None)

    def work(self):
        if self.NetCheck.isChecked():
            self.voltage_regulator = self.slider_voltage.value()
            self.ammeter.display(self.voltage_regulator / self.total_resistance)

    def measure_c(self):
        if self.NetCheck.isChecked():
            ammeter_value = float('{:.3f}'.format(self.ammeter.value()))
            self.voltmeter.display("{:.1f}".format(ammeter_value * self.resistance_c))
        else:
            self.voltmeter.display(None)

    def measure_3(self):
        if self.NetCheck.isChecked():
            ammeter_value = float('{:.3f}'.format(self.ammeter.value()))
            self.voltmeter.display("{:.1f}".format(ammeter_value * self.resistance_kat))
        else:
            self.voltmeter.display(None)

    def measure_r(self):
        if self.NetCheck.isChecked():
            ammeter_value = float('{:.3f}'.format(self.ammeter.value()))
            self.voltmeter.display("{:.1f}".format(ammeter_value * self.resistance_r))
        else:
            self.voltmeter.display(None)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Laba15()
    window.show()
    app.exec_()
    input()

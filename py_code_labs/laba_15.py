import sys

from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget

from converted_forms_to_py import laba15, info_laba

from py_code_labs import svg_widget_ammeter


class Laba15(QMainWindow, laba15.Ui_Laba15):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # rearm display
        self.voltmeter.display(None)

        # constants
        self.info_laba_15 = Info_laba()

        self.total_resistance = 55.5
        self.voltage_regulator = 0
        self.resistance_c = 40
        self.resistance_r = 30
        self.resistance_kat = 54

        self.ammeter = svg_widget_ammeter.svg_widget_ammeter()
        self.verticalLayout.addWidget(self.ammeter.svg_widget, 1)

        #set pixmaps
        self.label_resistor.setPixmap(QPixmap("..\\images\\laba_15\\resistor.png"))
        self.label_capacitor.setPixmap(QPixmap("..\\images\\laba_15\\capacitor.png"))
        self.label_coil.setPixmap(QPixmap("..\\images\\laba_15\\coil.png"))
        self.label_regulator.setPixmap(QPixmap("..\\images\\laba_15\\regulator_voltage.png"))

        # connects
        self.measure_c_button.clicked.connect(self.measure_c)
        self.measure_3_button.clicked.connect(self.measure_3)
        self.measure_r_button.clicked.connect(self.measure_r)

        self.slider_voltage.valueChanged.connect(self.update_ammeter)

        self.NetCheck.clicked.connect(self.zero_point_voltmeter)

        self.button_info.clicked.connect(self.show_info_about_laba)

    def zero_point_voltmeter(self):
        if not self.NetCheck.isChecked():
            self.voltmeter.display(None)

    def update_ammeter(self):
        if self.NetCheck.isChecked():
            self.voltage_regulator = self.slider_voltage.value()

            self.ammeter.update_svg_ammeter(self.voltage_regulator / self.total_resistance)

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

    def show_info_about_laba(self):
        self.info_laba_15.show()

class Info_laba(QWidget, info_laba.Ui_info_laba_11):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # set pixmaps
        self.label_info.setPixmap(QPixmap("..\\images\\laba_15\\info_laba_15_1.jpg"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Laba15()
    window.show()
    app.exec_()
    input()

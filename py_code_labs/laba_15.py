import sys

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget

from converted_forms_to_py import laba15, info_laba

from svg_widgets.svg_widget_ammeter import svg_widget_ammeter
from svg_widgets.svg_widget_milli_voltmeter import svg_widget_milli_voltmeter

class Laba15(QMainWindow, laba15.Ui_Laba15):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # constants
        self.info_laba_15 = Info_laba()

        self.resistance_c = 40
        self.resistance_r = 30
        self.resistance_kat = 54
        self.total_resistance = 55.5

        # values
        self.voltage_regulator = 0
        self.power_milli_voltmeter = False

        # set widgets
        self.ammeter = svg_widget_ammeter()
        self.verticalLayout.addWidget(self.ammeter.svg_widget, 1)

        self.milli_voltmeter = svg_widget_milli_voltmeter()
        self.verticalLayout_3.addWidget(self.milli_voltmeter.svg_widget)

        #set pixmaps
        self.label_resistor.setPixmap(QPixmap("..\\images\\laba_15\\resistor.png"))
        self.label_capacitor.setPixmap(QPixmap("..\\images\\laba_15\\capacitor.png"))
        self.label_coil.setPixmap(QPixmap("..\\images\\laba_15\\coil.png"))
        self.label_regulator.setPixmap(QPixmap("..\\images\\laba_15\\regulator_voltage.png"))
        self.button_info.setIcon(QIcon("..\\images\\laba_15\\info.png"))

        #для кликабельности лейблов
        self.label_power.installEventFilter(self)

        # connects
        self.measure_c_button.clicked.connect(self.measure_capacitor)
        self.measure_3_button.clicked.connect(self.measure_coil)
        self.measure_r_button.clicked.connect(self.measure_resistor)

        self.slider_voltage.valueChanged.connect(self.update_ammeter)

        self.button_info.clicked.connect(self.show_info_about_laba)

    def update_ammeter(self):
        self.voltage_regulator = self.slider_voltage.value()
        self.ammeter.update_svg_ammeter(self.voltage_regulator / self.total_resistance)

    def measure_capacitor(self):
        if self.power_milli_voltmeter:
            ammeter_value = float('{:.3f}'.format(self.ammeter.value()))
            self.milli_voltmeter.update_angle_svg_milli_voltmeter(float("{:.1f}".format(ammeter_value * self.resistance_c)))
        else:
            self.milli_voltmeter.update_angle_svg_milli_voltmeter(0)

    def measure_coil(self):
        if self.power_milli_voltmeter:
            ammeter_value = float('{:.3f}'.format(self.ammeter.value()))
            self.milli_voltmeter.update_angle_svg_milli_voltmeter(float("{:.1f}".format(ammeter_value * self.resistance_kat)))
        else:
            self.milli_voltmeter.update_angle_svg_milli_voltmeter(0)

    def measure_resistor(self):
        if self.power_milli_voltmeter:
            ammeter_value = float('{:.3f}'.format(self.ammeter.value()))
            self.milli_voltmeter.update_angle_svg_milli_voltmeter(float("{:.1f}".format(ammeter_value * self.resistance_r)))
        else:
            self.milli_voltmeter.update_angle_svg_milli_voltmeter(0)

    # Для кликабельности label
    def eventFilter(self, obj, e):
        if e.type() == 2:
            if obj == self.label_power:
                self.milli_voltmeter.change_power_svg()
                self.power_milli_voltmeter = not self.power_milli_voltmeter
        return super(QMainWindow, self).eventFilter(obj, e)

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

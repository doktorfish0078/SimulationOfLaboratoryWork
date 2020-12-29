import sys

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget

from converted_forms_to_py import laba15, info_laba

from svg_widgets.svg_widget_ammeter import svg_widget_ammeter
from svg_widgets.svg_widget_milli_voltmeter import svg_widget_milli_voltmeter


class Laba15(QMainWindow):
    """ Класс лабы 15, инициализирует форму и заполняет её элементами """

    def __init__(self):
        super().__init__()
        self.ui = laba15.Ui_Laba15()
        self.ui.setupUi(self)

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
        self.ui.ammeter = svg_widget_ammeter()
        self.ui.verticalLayout.addWidget(self.ui.ammeter.svg_widget, 1)

        self.ui.milli_voltmeter = svg_widget_milli_voltmeter()
        self.ui.verticalLayout_3.addWidget(self.ui.milli_voltmeter.svg_widget)

        # set pixmaps
        self.ui.label_resistor.setPixmap(QPixmap("..\\images\\laba_15\\resistor.png"))
        self.ui.label_capacitor.setPixmap(QPixmap("..\\images\\laba_15\\capacitor.png"))
        self.ui.label_coil.setPixmap(QPixmap("..\\images\\laba_15\\coil.png"))
        self.ui.label_regulator.setPixmap(QPixmap("..\\images\\laba_15\\regulator_voltage.png"))
        self.ui.button_info.setIcon(QIcon("..\\images\\laba_15\\info.png"))

        # для кликабельности лейблов
        self.ui.label_milli_voltmeter.installEventFilter(self)

        # connects
        self.ui.measure_c_button.clicked.connect(self.measure_capacitor)
        self.ui.measure_3_button.clicked.connect(self.measure_coil)
        self.ui.measure_r_button.clicked.connect(self.measure_resistor)

        self.ui.slider_voltage.valueChanged.connect(self.update_ammeter)

        self.ui.button_info.clicked.connect(self.show_info_about_laba)

    def update_ammeter(self):
        """ Коннектится к slider_voltage и при изменении значения
         обновняет value в поле класса voltage_regulator и обновляет картинку амперметра """
        self.voltage_regulator = self.ui.slider_voltage.value()
        self.ui.ammeter.update_svg_ammeter(self.voltage_regulator / self.total_resistance)

    def measure_capacitor(self):
        """ Изменяет напряжение конденсатора, если включён милливольтметр """
        if self.power_milli_voltmeter:
            ammeter_value = float('{:.3f}'.format(self.ui.ammeter.value()))
            self.ui.milli_voltmeter.update_angle_svg_milli_voltmeter(
                float("{:.1f}".format(ammeter_value * self.resistance_c)))
        else:
            self.ui.milli_voltmeter.update_angle_svg_milli_voltmeter(0)

    def measure_coil(self):
        """ Изменяет напряжение на катушке, если включён милливольтметр """
        if self.power_milli_voltmeter:
            ammeter_value = float('{:.3f}'.format(self.ui.ammeter.value()))
            self.ui.milli_voltmeter.update_angle_svg_milli_voltmeter(
                float("{:.1f}".format(ammeter_value * self.resistance_kat)))
        else:
            self.ui.milli_voltmeter.update_angle_svg_milli_voltmeter(0)

    def measure_resistor(self):
        """ Изменяет напряжение на резисторе, если включён милливольтметр """
        if self.power_milli_voltmeter:
            ammeter_value = float('{:.3f}'.format(self.ui.ammeter.value()))
            self.ui.milli_voltmeter.update_angle_svg_milli_voltmeter(
                float("{:.1f}".format(ammeter_value * self.resistance_r)))
        else:
            self.ui.milli_voltmeter.update_angle_svg_milli_voltmeter(0)

    # Для кликабельности label
    def eventFilter(self, obj, e):
        """
        Нужен для кликабельности лейблов
        :param obj: 
        :param e: 

        """
        if e.type() == 2:
            if obj == self.ui.label_milli_voltmeter:
                self.ui.milli_voltmeter.change_power_svg()
                self.power_milli_voltmeter = not self.power_milli_voltmeter
        return super(QMainWindow, self).eventFilter(obj, e)

    def show_info_about_laba(self):
        """ Показывает окно с документацией по выполнению л.р. """
        self.info_laba_15.show()


class Info_laba(QWidget):
    """ Форма с документацией по выполнению л.р. """

    def __init__(self):
        super().__init__()
        self.ui = info_laba.Ui_info_laba_11()
        self.ui.setupUi(self)

        # set pixmaps
        self.ui.label_info.setPixmap(QPixmap("..\\images\\laba_15\\info_laba_15_1.jpg"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Laba15()
    window.show()
    app.exec_()
    input()

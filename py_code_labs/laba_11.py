# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget

from converted_forms_to_py import laba11
from converted_forms_to_py import info_laba

from svg_widgets.svg_widget_galvanometer import svg_widget_galvanometer

class Laba11(QMainWindow, laba11.Ui_Laba11):
    """Класс лабы 11, инициализирует форму и
    заполняет её элементами
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # constants
        self.info_laba_11 = Info_laba()

        self.power_supply = False

        self.galvanometer = svg_widget_galvanometer()
        self.verticalLayout.addWidget(self.galvanometer.svg_widget)

        self.r1_value = 210
        self.r2_value = 405
        self.r3_value = 625
        self.resistance_on_store = 0

        # pixmaps
        self.map_res_default = QPixmap("..\\images\\laba_11\\default_resistors.png")

        self.map_r1_r2_serial = QPixmap("..\\images\\laba_11\\r1r2serial.png")
        self.map_r1_r3_serial = QPixmap("..\\images\\laba_11\\r1r3serial.png")
        self.map_r2_r3_serial = QPixmap("..\\images\\laba_11\\r2r3serial.png")

        self.map_r1_r2_parall = QPixmap("..\\images\\laba_11\\r1r2parall.png")
        self.map_r1_r3_parall = QPixmap("..\\images\\laba_11\\r1r3parall.png")
        self.map_r2_r3_parall = QPixmap("..\\images\\laba_11\\r2r3parall.png")

        self.map_r1_r2_r3_serial = QPixmap("..\\images\\laba_11\\r1r2r3serial.png")
        self.map_r1_r2_r3_parall = QPixmap("..\\images\\laba_11\\r1r2r3parall.png")

        self.map_power_supply_off = QPixmap("..\\images\\laba_11\\power_supply_off.png")
        self.map_power_supply_on = QPixmap("..\\images\\laba_11\\power_supply_on.png")

        self.map_voltage_divider = QPixmap("..\\images\\laba_11\\voltage_divider.png")

        # set pixmaps
        self.label_resistors.setPixmap(self.map_res_default)
        self.button_info.setIcon(QIcon("..\\images\\laba_11\\info.png"))
        self.label_resistors_shop.setPixmap(QPixmap("..\\images\\laba_11\\resistor_store.png"))
        self.label_voltage_divider.setPixmap(self.map_voltage_divider)

        # Для кликабельности лейблов
        self.label_power_supply.installEventFilter(self)

        # connects
        self.dial_1.valueChanged.connect(self.change_resistors_store_value)
        self.dial_2.valueChanged.connect(self.change_resistors_store_value)
        self.dial_3.valueChanged.connect(self.change_resistors_store_value)
        self.dial_4.valueChanged.connect(self.change_resistors_store_value)
        self.dial_5.valueChanged.connect(self.change_resistors_store_value)
        self.dial_6.valueChanged.connect(self.change_resistors_store_value)

        self.label_power_supply.setPixmap(self.map_power_supply_off)

        self.single.clicked.connect(self.change_map_resistors)
        self.serial.clicked.connect(self.change_map_resistors)
        self.parallel.clicked.connect(self.change_map_resistors)
        self.check_r1.clicked.connect(self.change_map_resistors)
        self.check_r2.clicked.connect(self.change_map_resistors)
        self.check_r3.clicked.connect(self.change_map_resistors)

        self.resetButton.clicked.connect(self.reset)
        self.button_info.clicked.connect(self.show_info_about_laba)

    def change_resistors_store_value(self):
        """Пересчитывает суммарное
        сопротивление на магазине
        сопротивлений. Метод подключается
        коннектом к каждому dial'y
        """
        self.resistance_on_store = self.dial_1.value() * 10000 + self.dial_2.value() * 1000 + \
                                   self.dial_3.value() * 100 + self.dial_4.value() * 10 + \
                                   self.dial_5.value() * 1 + self.dial_6.value() * 0.1

        self.resistors_store.setText('CРѕРїСЂРѕС‚РёРІР»РµРЅРёРµ РІ РјР°РіР°Р·РёРЅРµ СЃРѕРїСЂРѕС‚РёРІР»РµРЅРёР№: {}'.format(self.resistance_on_store))

        if self.power_supply:
            self.resistance_calculation()

    def resistance_calculation(self):
        """Считает и устанавливает текущее
        сопротивление в зависимости от
        выбранного типа подключения и
        выбранных резисторов
        """
        single = self.single.isChecked()
        parallel = self.parallel.isChecked()
        serial = self.serial.isChecked()

        resistors_used = [[self.check_r1.isChecked(), self.r1_value],
                          [self.check_r2.isChecked(), self.r2_value],
                          [self.check_r3.isChecked(), self.r3_value]]

        value_resistors = 0
        #
        if single or serial or parallel:
            # РїРѕРєР° С‚Р°Рє...
            if single:
                if self.check_only_one_checkbox_true():
                    for resistor in resistors_used:
                        if resistor[0]:
                            value_resistors = resistor[1]
                else:
                    QMessageBox.critical(self, "Ошибка", "Выбрано более одного резистора при одиночном подключении",
                                         QMessageBox.Ok)
                    self.check_r1.setChecked(False)
                    self.check_r2.setChecked(False)
                    self.check_r3.setChecked(False)

            if serial:
                for resistor in resistors_used:
                    if resistor[0]:
                        value_resistors += resistor[1]

            if parallel:
                if self.check_r1.isChecked() or self.check_r2.isChecked() or self.check_r3.isChecked():
                    if not self.check_only_one_checkbox_true():
                        summary_resist = 0
                        for resistor in resistors_used:
                            if resistor[0]:
                                summary_resist += 1 / resistor[1]
                        value_resistors = (1 / summary_resist)
                    else:
                        for resistor in resistors_used:
                            if resistor[0]:
                                value_resistors = resistor[1]

        self.galvanometer.update_svg_galvanometer(float("{:.2f}".format(self.resistance_on_store / 4 - value_resistors)))

    def reset(self):
        """Сбрасывает все dial'ы на позицию 0. тем
        самым обнуляя сопротивление в мазазине
        сопротивлений
        """
        for dial in [self.dial_1, self.dial_2, self.dial_3,
                     self.dial_4, self.dial_5, self.dial_6]:
            dial.setValue(0)

    def change_map_resistors(self):
        """Меняет картинку label_resistors в
        зависимости от выбранного типа
        подключения и выбранных резисторов тем
        самым отрисовывая вид текущего
        подключения
        """
        single = self.single.isChecked()
        parallel = self.parallel.isChecked()
        serial = self.serial.isChecked()

        r1 = self.check_r1.isChecked()
        r2 = self.check_r2.isChecked()
        r3 = self.check_r3.isChecked()
        if single or serial or parallel:
            if single:
                self.label_resistors.setPixmap(self.map_res_default)

            elif serial:
                if r1 and r2:
                    self.label_resistors.setPixmap(self.map_r1_r2_serial)
                elif r1 and r3:
                    self.label_resistors.setPixmap(self.map_r1_r3_serial)
                elif r2 and r3:
                    self.label_resistors.setPixmap(self.map_r2_r3_serial)
                else:
                    self.label_resistors.setPixmap(self.map_res_default)
                if r1 and r2 and r3:
                    self.label_resistors.setPixmap(self.map_r1_r2_r3_serial)


            elif parallel:
                if r1 and r2:
                    self.label_resistors.setPixmap(self.map_r1_r2_parall)
                elif r1 and r3:
                    self.label_resistors.setPixmap(self.map_r1_r3_parall)
                elif r2 and r3:
                    self.label_resistors.setPixmap(self.map_r2_r3_parall)
                else:
                    self.label_resistors.setPixmap(self.map_res_default)
                if r1 and r2 and r3:
                    self.label_resistors.setPixmap(self.map_r1_r2_r3_parall)

        self.change_resistors_store_value()

    def check_only_one_checkbox_true(self):
        """Проверяет подключено ли более 1
        резистора Если только 1 резистор
        включён,то возвращает true, в противном
        случае false
        """

        sum = 0
        for check_status in [self.check_r1, self.check_r2, self.check_r3]:
            sum += int(check_status.isChecked())
        if sum <= 1:
            return True
        return False

    def show_info_about_laba(self):
        """Показывает окно с документацией по
        выполнению л.р.
        """
        self.info_laba_11.show()

    # Для кликабельности лейблов
    def eventFilter(self, obj, e):
        """
        Нужен для кликабельности лейблов
        obj: :param e:
        """
        if e.type() == 2:
            if obj == self.label_power_supply:
                self.power_supply = not self.power_supply
                if self.power_supply:
                    self.label_power_supply.setPixmap(self.map_power_supply_on)
                else:
                    self.label_power_supply.setPixmap(self.map_power_supply_off)
                self.change_resistors_store_value()
        return super(QMainWindow, self).eventFilter(obj, e)


class Info_laba(QWidget, info_laba.Ui_info_laba_11):
    """Форма с документацией по выполнению
    л.р.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # set pixmaps
        self.label_info.setPixmap(QPixmap("..\\images\\laba_11\\info_laba_11.jpg"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Laba11()
    window.show()
    app.exec_()

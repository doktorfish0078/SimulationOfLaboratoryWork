# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget

from converted_forms_to_py import laba11

from svg_widgets.svg_widget_galvanometer import svg_widget_galvanometer

from py_code_labs.info_laba import Info_laba


class Laba11(QMainWindow):
    """Класс лабы 11, инициализирует форму и
    заполняет её элементами
    """

    def __init__(self):
        super().__init__()
        self.ui = laba11.Ui_Laba11()
        self.ui.setupUi(self)

        # set icon
        icon = QIcon()
        icon.addPixmap(QPixmap("../images/icon.png"),
                       QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        # constants
        self.info_laba_11 = Info_laba()

        self.power_supply = False

        self.ui.label_info.setText("Не включен источник питания!")

        self.r1_value = 210
        self.r2_value = 405
        self.r3_value = 625
        self.resistance_on_store = 0

        # set widgets
        self.ui.galvanometer = svg_widget_galvanometer()
        self.ui.verticalLayout.addWidget(self.ui.galvanometer.svg_widget)

        # pixmaps
        self.map_res_default = QPixmap("..\\images\\laba_11\\default_resistors.png")

        self.map_r1 = QPixmap("..\\images\\laba_11\\r1.png")
        self.map_r2 = QPixmap("..\\images\\laba_11\\r2.png")
        self.map_r3 = QPixmap("..\\images\\laba_11\\r3.png")

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
        self.ui.label_resistors.setPixmap(self.map_res_default)
        self.ui.button_info.setIcon(QIcon("..\\images\\laba_11\\info.png"))
        self.ui.label_resistors_shop.setPixmap(QPixmap("..\\images\\laba_11\\resistor_store.png"))
        self.ui.label_voltage_divider.setPixmap(self.map_voltage_divider)

        # Для кликабельности лейблов
        self.ui.label_power_supply.installEventFilter(self)

        # connects
        self.ui.dial_1.valueChanged.connect(self.change_resistors_store_value)
        self.ui.dial_2.valueChanged.connect(self.change_resistors_store_value)
        self.ui.dial_3.valueChanged.connect(self.change_resistors_store_value)
        self.ui.dial_4.valueChanged.connect(self.change_resistors_store_value)
        self.ui.dial_5.valueChanged.connect(self.change_resistors_store_value)
        self.ui.dial_6.valueChanged.connect(self.change_resistors_store_value)

        self.ui.label_power_supply.setPixmap(self.map_power_supply_off)

        self.ui.single.clicked.connect(self.change_map_resistors)
        self.ui.serial.clicked.connect(self.change_map_resistors)
        self.ui.parallel.clicked.connect(self.change_map_resistors)
        self.ui.check_r1.clicked.connect(self.change_map_resistors)
        self.ui.check_r2.clicked.connect(self.change_map_resistors)
        self.ui.check_r3.clicked.connect(self.change_map_resistors)

        self.ui.resetButton.clicked.connect(self.reset)
        self.ui.button_info.clicked.connect(self.show_info_about_laba)

        # add info pictures about laba
        self.info_laba_11.add_picture_in_scroll_area_content("../images/laba_11/info_laba_11.jpg")

    def change_resistors_store_value(self):
        """Пересчитывает суммарное
        сопротивление на магазине
        сопротивлений. Метод подключается
        коннектом к каждому dial'y
        """
        self.check_power_supply_for_label_info()

        self.resistance_on_store = self.ui.dial_1.value() * 10000 + self.ui.dial_2.value() * 1000 + \
                                   self.ui.dial_3.value() * 100 + self.ui.dial_4.value() * 10 + \
                                   self.ui.dial_5.value() * 1 + self.ui.dial_6.value() * 0.1

        self.ui.resistors_store.setText('Cопротивление в магазине сопротивлений: {}'.format(self.resistance_on_store))

        if self.power_supply:
            self.resistance_calculation()

    def resistance_calculation(self):
        """Считает и устанавливает текущее
        сопротивление в зависимости от
        выбранного типа подключения и
        выбранных резисторов
        """
        single = self.ui.single.isChecked()
        parallel = self.ui.parallel.isChecked()
        serial = self.ui.serial.isChecked()

        resistors_used = [[self.ui.check_r1.isChecked(), self.r1_value],
                          [self.ui.check_r2.isChecked(), self.r2_value],
                          [self.ui.check_r3.isChecked(), self.r3_value]]

        value_resistors = 0
        if single or serial or parallel:
            # Пока так
            if single:
                if self.check_only_one_checkbox_true():
                    for resistor in resistors_used:
                        if resistor[0]:
                            value_resistors = resistor[1]
                else:
                    QMessageBox.critical(self, "Ошибка", "Выбрано более одного резистора при одиночном подключении",
                                         QMessageBox.Ok)
                    self.ui.check_r1.setChecked(False)
                    self.ui.check_r2.setChecked(False)
                    self.ui.check_r3.setChecked(False)
                    self.change_map_resistors()

            if serial:
                for resistor in resistors_used:
                    if resistor[0]:
                        value_resistors += resistor[1]

            if parallel:
                if self.ui.check_r1.isChecked() or self.ui.check_r2.isChecked() or self.ui.check_r3.isChecked():
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

        self.ui.galvanometer.update_svg_galvanometer(float("{:.2f}".format(self.resistance_on_store / 4 - value_resistors)))

    def reset(self):
        """Сбрасывает все dial'ы на позицию 0. тем
        самым обнуляя сопротивление в мазазине
        сопротивлений
        """
        for dial in [self.ui.dial_1, self.ui.dial_2, self.ui.dial_3,
                     self.ui.dial_4, self.ui.dial_5, self.ui.dial_6]:
            dial.setValue(0)

    def change_map_resistors(self):
        """Меняет картинку label_resistors в
        зависимости от выбранного типа
        подключения и выбранных резисторов тем
        самым отрисовывая вид текущего
        подключения
        """
        self.check_power_supply_for_label_info()

        single = self.ui.single.isChecked()
        parallel = self.ui.parallel.isChecked()
        serial = self.ui.serial.isChecked()

        r1 = self.ui.check_r1.isChecked()
        r2 = self.ui.check_r2.isChecked()
        r3 = self.ui.check_r3.isChecked()
        if single or serial or parallel:
            if single:
                if r1:
                    self.ui.label_resistors.setPixmap(self.map_r1)
                elif r2:
                    self.ui.label_resistors.setPixmap(self.map_r2)
                elif r3:
                    self.ui.label_resistors.setPixmap(self.map_r3)
                else:
                    self.ui.label_resistors.setPixmap(self.map_res_default)

            elif serial:
                if r1 and r2 and r3:
                    self.ui.label_resistors.setPixmap(self.map_r1_r2_r3_serial)
                elif r1 and r2:
                    self.ui.label_resistors.setPixmap(self.map_r1_r2_serial)
                elif r1 and r3:
                    self.ui.label_resistors.setPixmap(self.map_r1_r3_serial)
                elif r2 and r3:
                    self.ui.label_resistors.setPixmap(self.map_r2_r3_serial)
                elif r1:
                    self.ui.label_resistors.setPixmap(self.map_r1)
                elif r2:
                    self.ui.label_resistors.setPixmap(self.map_r2)
                elif r3:
                    self.ui.label_resistors.setPixmap(self.map_r3)
                else:
                    self.ui.label_resistors.setPixmap(self.map_res_default)

            elif parallel:
                if r1 and r2 and r3:
                    self.ui.label_resistors.setPixmap(self.map_r1_r2_r3_parall)
                elif r1 and r2:
                    self.ui.label_resistors.setPixmap(self.map_r1_r2_parall)
                elif r1 and r3:
                    self.ui.label_resistors.setPixmap(self.map_r1_r3_parall)
                elif r2 and r3:
                    self.ui.label_resistors.setPixmap(self.map_r2_r3_parall)
                elif r1:
                    self.ui.label_resistors.setPixmap(self.map_r1)
                elif r2:
                    self.ui.label_resistors.setPixmap(self.map_r2)
                elif r3:
                    self.ui.label_resistors.setPixmap(self.map_r3)
                else:
                    self.ui.label_resistors.setPixmap(self.map_res_default)

        else:
            self.ui.label_resistors.setPixmap(self.map_res_default)

        self.change_resistors_store_value()

    def check_only_one_checkbox_true(self):
        """Проверяет подключено ли более 1
        резистора Если только 1 резистор
        включён,то возвращает true, в противном
        случае false
        """

        sum = 0
        for check_status in [self.ui.check_r1, self.ui.check_r2, self.ui.check_r3]:
            sum += int(check_status.isChecked())
        if sum <= 1:
            return True
        return False

    def check_power_supply_for_label_info(self):
        if self.power_supply:
            self.ui.label_info.setText("")
        else:
            self.ui.label_info.setText("Не включен источник питания!")

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
            if obj == self.ui.label_power_supply:
                self.power_supply = not self.power_supply
                if self.power_supply:
                    self.ui.label_power_supply.setPixmap(self.map_power_supply_on)
                else:
                    self.ui.label_power_supply.setPixmap(self.map_power_supply_off)
                    #  Т.к. питания нет, то переводим стрелку гальванометра в положение 0
                    self.ui.galvanometer.update_svg_galvanometer(0)

                self.change_resistors_store_value()
        return super(QMainWindow, self).eventFilter(obj, e)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Laba11()
    window.show()
    app.exec_()

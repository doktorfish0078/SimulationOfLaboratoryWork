import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from converted_forms_to_py import laba11


class Laba11(QMainWindow, laba11.Ui_Laba11):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # constants
        self.r1_value = 210
        self.r2_value = 405
        self.r3_value = 625
        self.resistance_on_store = 0

        # set pixmaps
        self.label_resistor_1.setPixmap(QPixmap("..\\images\\laba_11\\resistor.png"))
        self.label_resistor_2.setPixmap(QPixmap("..\\images\\laba_11\\resistor.png"))
        self.label_resistor_3.setPixmap(QPixmap("..\\images\\laba_11\\resistor.png"))
        self.label_info.setIcon(QIcon("..\\images\\laba_11\\info.jpg"))
        self.label_resistors_shop.setPixmap(QPixmap("..\\images\\laba_11\\resistor_store.png"))
        self.label_voltmeter.setPixmap(QPixmap("..\\images\\laba_11\\voltmeter.png"))

        # connects
        self.dial_1.valueChanged.connect(self.change_resistors_store_value)
        self.dial_2.valueChanged.connect(self.change_resistors_store_value)
        self.dial_3.valueChanged.connect(self.change_resistors_store_value)
        self.dial_4.valueChanged.connect(self.change_resistors_store_value)
        self.dial_5.valueChanged.connect(self.change_resistors_store_value)
        self.dial_6.valueChanged.connect(self.change_resistors_store_value)

        self.resetButton.clicked.connect(self.reset)

    def change_resistors_store_value(self):
        self.resistance_on_store = self.dial_1.value() * 10000 + self.dial_2.value() * 1000 + \
                                   self.dial_3.value() * 100 + self.dial_4.value() * 10 + \
                                   self.dial_5.value() * 1 + self.dial_6.value() * 0.1

        self.resistors_store.setText('Cопротивление в магазине сопротивлений: {}'.format(self.resistance_on_store))
        if self.PowerCheck.isChecked():
            self.resistance_calculation()

    def resistance_calculation(self):
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

        self.voltmeter.setText(str(self.resistance_on_store / 4 - value_resistors))

    def reset(self):
        for dial in [self.dial_1, self.dial_2, self.dial_3,
                     self.dial_4, self.dial_5, self.dial_6]:
            dial.setValue(0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Laba11()
    window.show()
    app.exec_()

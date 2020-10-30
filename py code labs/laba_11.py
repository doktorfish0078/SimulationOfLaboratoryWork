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

        # set pixmaps
        self.label_resistors.setPixmap(self.map_res_default)
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
        self.PowerCheck.clicked.connect(self.change_resistors_store_value)

        self.single.clicked.connect(self.change_map_resistors)
        self.serial.clicked.connect(self.change_map_resistors)
        self.parallel.clicked.connect(self.change_map_resistors)
        self.check_r1.clicked.connect(self.change_map_resistors)
        self.check_r2.clicked.connect(self.change_map_resistors)
        self.check_r3.clicked.connect(self.change_map_resistors)

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
        #
        if single or serial or parallel:
            # пока так...
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
                                summary_resist += 1/resistor[1]
                        value_resistors = (1 / summary_resist)
                    else:
                        for resistor in resistors_used:
                            if resistor[0]:
                                value_resistors = resistor[1]



        self.voltmeter.setText("{:.2f}".format(self.resistance_on_store / 4 - value_resistors))

    def reset(self):
        for dial in [self.dial_1, self.dial_2, self.dial_3,
                     self.dial_4, self.dial_5, self.dial_6]:
            dial.setValue(0)

    def change_map_resistors(self):
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
        sum = 0
        for check_status in [self.check_r1, self.check_r2, self.check_r3]:
            sum += int(check_status.isChecked())
        if sum <= 1:
            return True
        return False

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Laba11()
    window.show()
    app.exec_()

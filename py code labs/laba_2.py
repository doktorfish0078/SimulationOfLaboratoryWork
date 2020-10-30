import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from converted_forms_to_py import laba2


class Laba2(QMainWindow, laba2.Ui_Laba2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # rearm display
        self.galvanometer.display(None)

        # pixmaps
        self.map_left_pos_key = QPixmap("..\\images\\laba_2\\key_left.png")
        self.map_right_pos_key = QPixmap("..\\images\\laba_2\\key_right.png")
        self.map_middle_pos_key = QPixmap("..\\images\\laba_2\\key_middle.png")
        self.map_battery = QPixmap("..\\images\\laba_2\\battery1")
        self.map_full_slot_battery = QPixmap("..\\images\\laba_2\\battery_in_slot.png")
        self.map_empty_slot_battery = QPixmap("..\\images\\laba_2\\slot_battery.png")

        # для кликабельности лейблов
        self.label_battery1.installEventFilter(self)
        self.label_battery2.installEventFilter(self)
        self.slot_battery1.installEventFilter(self)
        self.slot_battery2.installEventFilter(self)

        # set pixmaps
        self.label_key.setPixmap(self.map_middle_pos_key)
        self.slot_battery1.setPixmap(self.map_empty_slot_battery)
        self.slot_battery2.setPixmap(self.map_empty_slot_battery)
        self.label_battery1.setPixmap(self.map_battery)
        self.label_battery2.setPixmap(self.map_battery)

        # connects
        self.key_slider.valueChanged.connect(self.change_picture_key)
        self.Reostat.valueChanged.connect(self.change_value_galvanometer)

        self.check_battery1.clicked.connect(self.change_slot_battery)
        self.check_battery2.clicked.connect(self.change_slot_battery)

    def change_picture_key(self):
        if self.key_slider.value() == 0:
            self.label_key.setPixmap(self.map_left_pos_key)
        elif self.key_slider.value() == 1:
            self.label_key.setPixmap(self.map_middle_pos_key)
        elif self.key_slider.value() == 2:
            self.label_key.setPixmap(self.map_right_pos_key)
        self.change_value_galvanometer()

    def change_value_galvanometer(self):
        value_reostat = self.Reostat.value() / 10  # значение реостата в сантиметрах,от 0 до 24 см с шагом в 0.1 см

        if self.key_slider.value() == 0:  # левая позиция ключа
            if value_reostat < 14.5:
                self.galvanometer.display(-(14.5 / 0.152 - value_reostat / 0.152))
            else:
                self.galvanometer.display(value_reostat / 0.152 - 14.5 / 0.152)

        elif self.key_slider.value() == 1:  # центральная позиция ключа(разомкнут)
            self.galvanometer.display(None)

        self.label_info.setText("")

        if self.key_slider.value() == 2:  # правая позиция ключа
            if self.check_battery1.isChecked() or self.check_battery2.isChecked():
                if value_reostat < 21.5:
                    self.galvanometer.display(-(21.5 / 0.165 - value_reostat / 0.165))
                else:
                    self.galvanometer.display(value_reostat / 0.165 - 21.5 / 0.165)
            else:
                self.label_info.setText("Ни одна из батареек не установлена")
                self.galvanometer.display(0)

    def change_slot_battery(self):
        if not(self.check_battery1.isChecked() and self.check_battery2.isChecked()):
            # проверка первого слота
            if self.check_battery1.isChecked():
                self.label_battery1.hide()
                self.slot_battery1.setPixmap(self.map_full_slot_battery)
            else:
                self.slot_battery1.setPixmap(self.map_empty_slot_battery)
                self.label_battery1.show()

            # проверка второго слота
            if self.check_battery2.isChecked():
                self.slot_battery2.setPixmap(self.map_full_slot_battery)
                self.label_battery2.hide()
            else:
                self.slot_battery2.setPixmap(self.map_empty_slot_battery)
                self.label_battery2.show()

            self.change_value_galvanometer()
        else:
            QMessageBox.critical(self, "Нельзя измерять более 1 батареи", "Нельзя измерять более 1 батареи,хорошо?",
                                 QMessageBox.Ok)
            self.check_battery1.setChecked(False)
            self.check_battery2.setChecked(False)
            self.change_slot_battery()
    # Для кликабельности label
    def eventFilter(self, obj, e):
        if e.type() == 2:
            if obj == self.label_battery1:
                self.check_battery1.setChecked(True)
                self.change_slot_battery()
            elif obj == self.label_battery2:
                self.check_battery2.setChecked(True)
                self.change_slot_battery()

            elif obj == self.slot_battery1:
                self.check_battery1.setChecked(False)
                self.change_slot_battery()
            elif obj == self.slot_battery2:
                self.check_battery2.setChecked(False)
                self.change_slot_battery()

        return super(QMainWindow, self).eventFilter(obj, e)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Laba2()
    window.show()
    app.exec_()
    input()

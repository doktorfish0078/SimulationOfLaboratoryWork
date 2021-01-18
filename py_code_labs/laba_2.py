# -*- coding: utf-8 -*-
import sys
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget

from converted_forms_to_py import laba2
from converted_forms_to_py import info_laba

from svg_widgets.svg_widget_galvanometer import svg_widget_galvanometer

class Laba2(QMainWindow):
    """Класс лабы 2, инициализирует форму и
        заполняет её элементами
    """
    def __init__(self):
        super().__init__()
        self.ui = laba2.Ui_Laba2()
        self.ui.setupUi(self)

        #set icon
        icon = QIcon()
        icon.addPixmap(QPixmap("../images/icon.png"),
                       QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        # constants
        self.info_laba_2 = Info_laba()

        # set widgets
        self.ui.galvanometer = svg_widget_galvanometer()
        self.ui.verticalLayout_3.addWidget(self.ui.galvanometer.svg_widget)

        # pixmaps
        self.map_left_pos_key = QPixmap("..\\images\\laba_2\\key_left.png")
        self.map_right_pos_key = QPixmap("..\\images\\laba_2\\key_right.png")
        self.map_middle_pos_key = QPixmap("..\\images\\laba_2\\key_middle.png")
        self.map_battery = QPixmap("..\\images\\laba_2\\battery1")
        self.map_full_slot_battery = QPixmap("..\\images\\laba_2\\battery_in_slot.png")
        self.map_empty_slot_battery = QPixmap("..\\images\\laba_2\\slot_battery.png")
        self.map_gc = QPixmap("..\\images\\laba_2\\Gc.png")
        self.map_g = QPixmap("..\\images\\laba_2\\G.png")

        # Для кликабельности лейблов
        self.ui.label_battery1.installEventFilter(self)
        self.ui.label_battery2.installEventFilter(self)
        self.ui.slot_battery1.installEventFilter(self)
        self.ui.slot_battery2.installEventFilter(self)

        # set pixmaps
        self.ui.label_key.setPixmap(self.map_middle_pos_key)
        self.ui.slot_battery1.setPixmap(self.map_empty_slot_battery)
        self.ui.slot_battery2.setPixmap(self.map_empty_slot_battery)
        self.ui.label_battery1.setPixmap(self.map_battery)
        self.ui.label_battery2.setPixmap(self.map_battery)
        self.ui.label_Gc.setPixmap(self.map_gc)
        self.ui.label_G.setPixmap(self.map_g)
        self.ui.button_info.setIcon(QIcon("..\\images\\laba_2\\info.png"))

        # connects
        self.ui.key_slider.valueChanged.connect(self.change_picture_key)
        self.ui.Reostat.valueChanged.connect(self.change_value_galvanometer)

        self.ui.check_battery1.clicked.connect(self.change_slot_battery)
        self.ui.check_battery2.clicked.connect(self.change_slot_battery)

        self.ui.button_info.clicked.connect(self.show_info_about_laba)

    def change_picture_key(self):
        """Коннектится к key_slider, при изменении
        его значения показывает в label_key другую
        картинку,соответствующую текущему
        положению ключа
        """
        if self.ui.key_slider.value() == 0:
            self.ui.label_key.setPixmap(self.map_left_pos_key)
        elif self.ui.key_slider.value() == 1:
            self.ui.label_key.setPixmap(self.map_middle_pos_key)
        elif self.ui.key_slider.value() == 2:
            self.ui.label_key.setPixmap(self.map_right_pos_key)
        self.change_value_galvanometer()

    def change_value_galvanometer(self):
        """Коннектится к Reostat'у, при изменении
        его значение, рассчитывает нужное
        показание гальванометра и обновляет
        изображение гальванометра
        """
        value_reostat = self.ui.Reostat.value() / 10  # значение реостата в сантиметрах,от 0 до 24 см с шагом в 0.1 см

        if self.ui.key_slider.value() == 0:  # левая позиция ключа
            if value_reostat < 14.5:
                self.ui.galvanometer.update_svg_galvanometer(-(14.5 / 0.152 - value_reostat / 0.152))
            else:
                self.ui.galvanometer.update_svg_galvanometer(value_reostat / 0.152 - 14.5 / 0.152)

        elif self.ui.key_slider.value() == 1:  # центральная позиция ключа(разомкнут)
            self.ui.galvanometer.update_svg_galvanometer(0)

        self.ui.label_info.setText("")

        if self.ui.key_slider.value() == 2:  # правая позиция ключа
            if self.ui.check_battery1.isChecked() or self.ui.check_battery2.isChecked():
                if value_reostat < 21.5:
                    self.ui.galvanometer.update_svg_galvanometer(-(21.5 / 0.165 - value_reostat / 0.165))
                else:
                    self.ui.galvanometer.update_svg_galvanometer(value_reostat / 0.165 - 21.5 / 0.165)
            else:
                self.ui.label_info.setText("Ни одна из батареек не установлена")
                self.ui.galvanometer.update_svg_galvanometer(0)

    def change_slot_battery(self):
        """Меняет положение батарейки на
        противоположное А так же отрисовывает
        положение батарейки(в слоте она или
        нет)
        """
        if not (self.ui.check_battery1.isChecked() and self.ui.check_battery2.isChecked()):
            # проверка первого слота
            if self.ui.check_battery1.isChecked():
                self.ui.label_battery1.hide()
                self.ui.slot_battery1.setPixmap(self.map_full_slot_battery)
            else:
                self.ui.slot_battery1.setPixmap(self.map_empty_slot_battery)
                self.ui.label_battery1.show()

            # проверка второго слота
            if self.ui.check_battery2.isChecked():
                self.ui.slot_battery2.setPixmap(self.map_full_slot_battery)
                self.ui.label_battery2.hide()
            else:
                self.ui.slot_battery2.setPixmap(self.map_empty_slot_battery)
                self.ui.label_battery2.show()

            self.change_value_galvanometer()
        else:
            QMessageBox.critical(self, "Нельзя измерять более 1 батареи", "Нельзя измерять более 1 батареи,хорошо?",
                                 QMessageBox.Ok)
            self.ui.check_battery1.setChecked(False)
            self.ui.check_battery2.setChecked(False)
            self.change_slot_battery()

    # Для кликабельности label
    def eventFilter(self, obj, e):
        """
        Для кликабельности лейблов
        Args:
            obj:
            e:
        """
        if e.type() == 2:
            if obj == self.ui.label_battery1:
                self.ui.check_battery1.setChecked(True)
                self.change_slot_battery()
            elif obj == self.ui.label_battery2:
                self.ui.check_battery2.setChecked(True)
                self.change_slot_battery()

            elif obj == self.ui.slot_battery1:
                self.ui.check_battery1.setChecked(False)
                self.change_slot_battery()
            elif obj == self.ui.slot_battery2:
                self.ui.check_battery2.setChecked(False)
                self.change_slot_battery()

        return super(QMainWindow, self).eventFilter(obj, e)

    def show_info_about_laba(self):
        """Показывает окно с документацией по
        выполнению л.р.
        """
        self.info_laba_2.show()


class Info_laba(QWidget):
    """Форма с документацией по выполнению л.р.
    """
    def __init__(self):
        super().__init__()
        self.ui = info_laba.Ui_info_laba_11()
        self.ui.setupUi(self)

        # set icon
        icon = QIcon()
        icon.addPixmap(QPixmap("../images/icon.png"),
                       QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        # set pixmaps
        self.ui.label_info.setPixmap(QPixmap("..\\images\\laba_2\\info_laba_2.jpg"))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Laba2()
    window.show()
    app.exec_()
    input()

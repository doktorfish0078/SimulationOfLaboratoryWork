# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Projects\SimulationOfLaboratoryWork\forms_ui\laba11.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Laba11(object):
    def setupUi(self, Laba11):
        Laba11.setObjectName("Laba11")
        Laba11.resize(1000, 700)
        Laba11.setMinimumSize(QtCore.QSize(1000, 700))
        Laba11.setMaximumSize(QtCore.QSize(1000, 700))
        Laba11.setStyleSheet("background-color: rgb(176,193,208);")
        self.centralwidget = QtWidgets.QWidget(Laba11)
        self.centralwidget.setObjectName("centralwidget")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(660, 254, 181, 25))
        self.label_8.setStyleSheet("font: 75 10pt \"Comic Sans MS\";")
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_resistors_shop = QtWidgets.QLabel(self.centralwidget)
        self.label_resistors_shop.setGeometry(QtCore.QRect(528, 278, 465, 325))
        self.label_resistors_shop.setText("")
        self.label_resistors_shop.setPixmap(QtGui.QPixmap("F:\\Projects\\SimulationOfLaboratoryWork\\forms_ui\\../images/laba_11/resistor_store.png"))
        self.label_resistors_shop.setScaledContents(True)
        self.label_resistors_shop.setObjectName("label_resistors_shop")
        self.resistors_store = QtWidgets.QLabel(self.centralwidget)
        self.resistors_store.setGeometry(QtCore.QRect(528, 604, 463, 21))
        self.resistors_store.setStyleSheet("font: 75 10pt \"Comic Sans MS\";")
        self.resistors_store.setText("")
        self.resistors_store.setAlignment(QtCore.Qt.AlignCenter)
        self.resistors_store.setObjectName("resistors_store")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(664, 628, 169, 49))
        self.resetButton.setStyleSheet("font: 11pt \"Comic Sans MS\";")
        self.resetButton.setObjectName("resetButton")
        self.button_info = QtWidgets.QPushButton(self.centralwidget)
        self.button_info.setGeometry(QtCore.QRect(958, 2, 41, 41))
        self.button_info.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:\\Projects\\SimulationOfLaboratoryWork\\forms_ui\\../images/laba_11/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_info.setIcon(icon)
        self.button_info.setIconSize(QtCore.QSize(32, 32))
        self.button_info.setObjectName("button_info")
        self.label_resistors = QtWidgets.QLabel(self.centralwidget)
        self.label_resistors.setGeometry(QtCore.QRect(26, 44, 201, 153))
        self.label_resistors.setText("")
        self.label_resistors.setPixmap(QtGui.QPixmap("F:\\Projects\\SimulationOfLaboratoryWork\\forms_ui\\../images/laba_11/default_resistors.png"))
        self.label_resistors.setScaledContents(True)
        self.label_resistors.setObjectName("label_resistors")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(232, 44, 293, 34))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.single = QtWidgets.QRadioButton(self.layoutWidget)
        self.single.setObjectName("single")
        self.horizontalLayout_2.addWidget(self.single)
        self.serial = QtWidgets.QRadioButton(self.layoutWidget)
        self.serial.setObjectName("serial")
        self.horizontalLayout_2.addWidget(self.serial)
        self.parallel = QtWidgets.QRadioButton(self.layoutWidget)
        self.parallel.setObjectName("parallel")
        self.horizontalLayout_2.addWidget(self.parallel)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(232, 84, 279, 89))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setContentsMargins(70, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.check_r1 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.check_r1.setTristate(False)
        self.check_r1.setObjectName("check_r1")
        self.verticalLayout_6.addWidget(self.check_r1)
        self.check_r2 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.check_r2.setEnabled(True)
        self.check_r2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.check_r2.setAutoFillBackground(False)
        self.check_r2.setChecked(False)
        self.check_r2.setAutoRepeat(False)
        self.check_r2.setObjectName("check_r2")
        self.verticalLayout_6.addWidget(self.check_r2)
        self.check_r3 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.check_r3.setObjectName("check_r3")
        self.verticalLayout_6.addWidget(self.check_r3)
        self.label_power_supply = QtWidgets.QLabel(self.centralwidget)
        self.label_power_supply.setGeometry(QtCore.QRect(84, 496, 331, 111))
        self.label_power_supply.setText("")
        self.label_power_supply.setPixmap(QtGui.QPixmap("F:\\Projects\\SimulationOfLaboratoryWork\\forms_ui\\../images/laba_11/power_supply_off.png"))
        self.label_power_supply.setScaledContents(True)
        self.label_power_supply.setObjectName("label_power_supply")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(584, 2, 335, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dial_1 = QtWidgets.QDial(self.centralwidget)
        self.dial_1.setGeometry(QtCore.QRect(578, 352, 75, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.dial_1.setPalette(palette)
        self.dial_1.setAutoFillBackground(False)
        self.dial_1.setStyleSheet("background-color: rgb(28, 30, 29);")
        self.dial_1.setInputMethodHints(QtCore.Qt.ImhNone)
        self.dial_1.setMaximum(9)
        self.dial_1.setPageStep(10)
        self.dial_1.setSliderPosition(0)
        self.dial_1.setInvertedAppearance(False)
        self.dial_1.setInvertedControls(False)
        self.dial_1.setWrapping(False)
        self.dial_1.setNotchTarget(10.0)
        self.dial_1.setNotchesVisible(False)
        self.dial_1.setObjectName("dial_1")
        self.label_voltage_divider = QtWidgets.QLabel(self.centralwidget)
        self.label_voltage_divider.setGeometry(QtCore.QRect(100, 292, 295, 111))
        self.label_voltage_divider.setText("")
        self.label_voltage_divider.setPixmap(QtGui.QPixmap("F:\\Projects\\SimulationOfLaboratoryWork\\forms_ui\\../images/laba_11/voltage_divider.png"))
        self.label_voltage_divider.setScaledContents(True)
        self.label_voltage_divider.setObjectName("label_voltage_divider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(88, 404, 315, 29))
        self.label.setStyleSheet("font: 75 15pt \"Comic Sans MS\";")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(86, 434, 315, 29))
        self.label_2.setStyleSheet("font: 75 15pt \"Comic Sans MS\";")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.dial_2 = QtWidgets.QDial(self.centralwidget)
        self.dial_2.setGeometry(QtCore.QRect(722, 352, 75, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.dial_2.setPalette(palette)
        self.dial_2.setAutoFillBackground(False)
        self.dial_2.setStyleSheet("background-color: rgb(28, 30, 29);")
        self.dial_2.setMaximum(9)
        self.dial_2.setPageStep(10)
        self.dial_2.setSliderPosition(0)
        self.dial_2.setInvertedAppearance(False)
        self.dial_2.setInvertedControls(False)
        self.dial_2.setWrapping(False)
        self.dial_2.setNotchTarget(10.0)
        self.dial_2.setNotchesVisible(False)
        self.dial_2.setObjectName("dial_2")
        self.dial_3 = QtWidgets.QDial(self.centralwidget)
        self.dial_3.setGeometry(QtCore.QRect(868, 352, 75, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.dial_3.setPalette(palette)
        self.dial_3.setAutoFillBackground(False)
        self.dial_3.setStyleSheet("background-color: rgb(28, 30, 29);")
        self.dial_3.setMaximum(9)
        self.dial_3.setPageStep(10)
        self.dial_3.setSliderPosition(0)
        self.dial_3.setInvertedAppearance(False)
        self.dial_3.setInvertedControls(False)
        self.dial_3.setWrapping(False)
        self.dial_3.setNotchTarget(10.0)
        self.dial_3.setNotchesVisible(False)
        self.dial_3.setObjectName("dial_3")
        self.dial_4 = QtWidgets.QDial(self.centralwidget)
        self.dial_4.setGeometry(QtCore.QRect(578, 492, 75, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.dial_4.setPalette(palette)
        self.dial_4.setAutoFillBackground(False)
        self.dial_4.setStyleSheet("background-color: rgb(28, 30, 29);")
        self.dial_4.setMaximum(9)
        self.dial_4.setPageStep(10)
        self.dial_4.setSliderPosition(0)
        self.dial_4.setInvertedAppearance(False)
        self.dial_4.setInvertedControls(False)
        self.dial_4.setWrapping(False)
        self.dial_4.setNotchTarget(10.0)
        self.dial_4.setNotchesVisible(False)
        self.dial_4.setObjectName("dial_4")
        self.dial_5 = QtWidgets.QDial(self.centralwidget)
        self.dial_5.setGeometry(QtCore.QRect(722, 492, 75, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.dial_5.setPalette(palette)
        self.dial_5.setAutoFillBackground(False)
        self.dial_5.setStyleSheet("background-color: rgb(28, 30, 29);")
        self.dial_5.setMaximum(9)
        self.dial_5.setPageStep(10)
        self.dial_5.setSliderPosition(0)
        self.dial_5.setInvertedAppearance(False)
        self.dial_5.setInvertedControls(False)
        self.dial_5.setWrapping(False)
        self.dial_5.setNotchTarget(10.0)
        self.dial_5.setNotchesVisible(False)
        self.dial_5.setObjectName("dial_5")
        self.dial_6 = QtWidgets.QDial(self.centralwidget)
        self.dial_6.setGeometry(QtCore.QRect(868, 492, 75, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 30, 29))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.dial_6.setPalette(palette)
        self.dial_6.setAutoFillBackground(False)
        self.dial_6.setStyleSheet("background-color: rgb(28, 30, 29);")
        self.dial_6.setMaximum(9)
        self.dial_6.setPageStep(10)
        self.dial_6.setSliderPosition(0)
        self.dial_6.setInvertedAppearance(False)
        self.dial_6.setInvertedControls(False)
        self.dial_6.setWrapping(False)
        self.dial_6.setNotchTarget(10.0)
        self.dial_6.setNotchesVisible(False)
        self.dial_6.setObjectName("dial_6")
        self.label_resistors_shop.raise_()
        self.label_8.raise_()
        self.resistors_store.raise_()
        self.resetButton.raise_()
        self.button_info.raise_()
        self.label_resistors.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.label_power_supply.raise_()
        self.verticalLayoutWidget.raise_()
        self.dial_1.raise_()
        self.label_voltage_divider.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.dial_2.raise_()
        self.dial_3.raise_()
        self.dial_4.raise_()
        self.dial_5.raise_()
        self.dial_6.raise_()
        Laba11.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Laba11)
        self.statusbar.setObjectName("statusbar")
        Laba11.setStatusBar(self.statusbar)

        self.retranslateUi(Laba11)
        QtCore.QMetaObject.connectSlotsByName(Laba11)

    def retranslateUi(self, Laba11):
        _translate = QtCore.QCoreApplication.translate
        Laba11.setWindowTitle(_translate("Laba11", "Лабораторная работа №11"))
        self.label_8.setText(_translate("Laba11", "Гальванометр"))
        self.resetButton.setText(_translate("Laba11", "Сбросить\n"
"сопротивления"))
        self.single.setText(_translate("Laba11", "Одиночно"))
        self.serial.setText(_translate("Laba11", "Последов."))
        self.parallel.setText(_translate("Laba11", "Параллельно"))
        self.check_r1.setText(_translate("Laba11", "R1"))
        self.check_r2.setText(_translate("Laba11", "R2"))
        self.check_r3.setText(_translate("Laba11", "R3"))
        self.label.setText(_translate("Laba11", "Делитель напряжения"))
        self.label_2.setText(_translate("Laba11", "l1/l2 = 0.25 ± 0.01"))

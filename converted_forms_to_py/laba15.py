# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Projects\SimulationOfLaboratoryWork\forms_ui\laba15.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Laba15(object):
    def setupUi(self, Laba15):
        Laba15.setObjectName("Laba15")
        Laba15.resize(1207, 904)
        Laba15.setMinimumSize(QtCore.QSize(0, 0))
        Laba15.setMaximumSize(QtCore.QSize(11111, 11111))
        Laba15.setStyleSheet("background-color: rgb(176,193,208);")
        self.centralwidget = QtWidgets.QWidget(Laba15)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(22, 352, 241, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(540, 768, 141, 63))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.measure_c_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.measure_c_button.setObjectName("measure_c_button")
        self.verticalLayout_2.addWidget(self.measure_c_button)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(827, 767, 235, 61))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.measure_3_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.measure_3_button.setObjectName("measure_3_button")
        self.verticalLayout_5.addWidget(self.measure_3_button)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(242, 726, 141, 103))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_resistor = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_resistor.setMaximumSize(QtCore.QSize(139, 30))
        self.label_resistor.setText("")
        self.label_resistor.setPixmap(QtGui.QPixmap("F:\\Projects\\SimulationOfLaboratoryWork\\forms_ui\\images/resistor.png"))
        self.label_resistor.setScaledContents(True)
        self.label_resistor.setObjectName("label_resistor")
        self.verticalLayout_6.addWidget(self.label_resistor)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.measure_r_button = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.measure_r_button.setObjectName("measure_r_button")
        self.verticalLayout_6.addWidget(self.measure_r_button)
        self.button_info = QtWidgets.QPushButton(self.centralwidget)
        self.button_info.setGeometry(QtCore.QRect(1172, 0, 41, 41))
        self.button_info.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:\\Projects\\SimulationOfLaboratoryWork\\forms_ui\\../images/laba_11/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_info.setIcon(icon)
        self.button_info.setIconSize(QtCore.QSize(32, 32))
        self.button_info.setObjectName("button_info")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(72, 260, 317, 35))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.slider_voltage = QtWidgets.QSlider(self.centralwidget)
        self.slider_voltage.setGeometry(QtCore.QRect(410, 44, 27, 171))
        self.slider_voltage.setStyleSheet("background-color: none;")
        self.slider_voltage.setMaximum(54)
        self.slider_voltage.setSliderPosition(0)
        self.slider_voltage.setTracking(True)
        self.slider_voltage.setOrientation(QtCore.Qt.Vertical)
        self.slider_voltage.setInvertedAppearance(False)
        self.slider_voltage.setInvertedControls(False)
        self.slider_voltage.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_voltage.setTickInterval(5)
        self.slider_voltage.setObjectName("slider_voltage")
        self.label_regulator = QtWidgets.QLabel(self.centralwidget)
        self.label_regulator.setGeometry(QtCore.QRect(18, 8, 431, 249))
        self.label_regulator.setText("")
        self.label_regulator.setPixmap(QtGui.QPixmap("F:\\Projects\\SimulationOfLaboratoryWork\\forms_ui\\../images/laba_15/Безымянный-2.png"))
        self.label_regulator.setScaledContents(True)
        self.label_regulator.setObjectName("label_regulator")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(24, 594, 239, 24))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_capacitor = QtWidgets.QLabel(self.centralwidget)
        self.label_capacitor.setGeometry(QtCore.QRect(540, 596, 139, 165))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_capacitor.sizePolicy().hasHeightForWidth())
        self.label_capacitor.setSizePolicy(sizePolicy)
        self.label_capacitor.setMaximumSize(QtCore.QSize(11111, 11111))
        self.label_capacitor.setText("")
        self.label_capacitor.setPixmap(QtGui.QPixmap("F:\\Projects\\SimulationOfLaboratoryWork\\forms_ui\\../images/laba_15/capacitor.png"))
        self.label_capacitor.setScaledContents(True)
        self.label_capacitor.setObjectName("label_capacitor")
        self.label_coil = QtWidgets.QLabel(self.centralwidget)
        self.label_coil.setGeometry(QtCore.QRect(830, 582, 235, 175))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_coil.sizePolicy().hasHeightForWidth())
        self.label_coil.setSizePolicy(sizePolicy)
        self.label_coil.setMaximumSize(QtCore.QSize(11111, 11111))
        self.label_coil.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_coil.setText("")
        self.label_coil.setPixmap(QtGui.QPixmap("F:\\Projects\\SimulationOfLaboratoryWork\\forms_ui\\../images/laba_15/coil.png"))
        self.label_coil.setScaledContents(True)
        self.label_coil.setAlignment(QtCore.Qt.AlignCenter)
        self.label_coil.setWordWrap(False)
        self.label_coil.setIndent(-1)
        self.label_coil.setOpenExternalLinks(False)
        self.label_coil.setObjectName("label_coil")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(686, 2, 483, 537))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_power = QtWidgets.QLabel(self.centralwidget)
        self.label_power.setGeometry(QtCore.QRect(1054, 410, 93, 99))
        self.label_power.setStyleSheet("background-color: none;")
        self.label_power.setText("")
        self.label_power.setObjectName("label_power")
        self.label_regulator.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.verticalLayoutWidget_4.raise_()
        self.button_info.raise_()
        self.label_10.raise_()
        self.slider_voltage.raise_()
        self.label.raise_()
        self.label_capacitor.raise_()
        self.label_coil.raise_()
        self.verticalLayoutWidget_5.raise_()
        self.label_power.raise_()
        Laba15.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Laba15)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1207, 21))
        self.menubar.setObjectName("menubar")
        Laba15.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Laba15)
        self.statusbar.setObjectName("statusbar")
        Laba15.setStatusBar(self.statusbar)

        self.retranslateUi(Laba15)
        QtCore.QMetaObject.connectSlotsByName(Laba15)
        Laba15.setTabOrder(self.measure_c_button, self.measure_3_button)
        Laba15.setTabOrder(self.measure_3_button, self.measure_r_button)

    def retranslateUi(self, Laba15):
        _translate = QtCore.QCoreApplication.translate
        Laba15.setWindowTitle(_translate("Laba15", "MainWindow"))
        self.label_3.setText(_translate("Laba15", "Конденсатор"))
        self.measure_c_button.setText(_translate("Laba15", "Измерить напряжение"))
        self.label_5.setText(_translate("Laba15", "Катушка индуктивности"))
        self.measure_3_button.setText(_translate("Laba15", "Измерить напряжение"))
        self.label_7.setText(_translate("Laba15", "Резистор"))
        self.measure_r_button.setText(_translate("Laba15", "Измерить напряжение"))
        self.label_10.setText(_translate("Laba15", "Регулятор напряжения"))
        self.label.setText(_translate("Laba15", "Амперметр"))

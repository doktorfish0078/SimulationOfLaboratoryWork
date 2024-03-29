# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Projects\Simulation_Of_Laboratory_Works\forms_ui\laba15.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Laba15(object):
    def setupUi(self, Laba15):
        Laba15.setObjectName("Laba15")
        Laba15.resize(1285, 630)
        Laba15.setMinimumSize(QtCore.QSize(1285, 630))
        Laba15.setMaximumSize(QtCore.QSize(1285, 630))
        Laba15.setStyleSheet("background-color: rgb(176,193,208);")
        self.centralwidget = QtWidgets.QWidget(Laba15)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(488, 10, 241, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_info = QtWidgets.QPushButton(self.centralwidget)
        self.button_info.setGeometry(QtCore.QRect(1242, 2, 41, 41))
        self.button_info.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:\\Projects\\Simulation_Of_Laboratory_Works\\forms_ui\\../images/laba_11/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_info.setIcon(icon)
        self.button_info.setIconSize(QtCore.QSize(32, 32))
        self.button_info.setObjectName("button_info")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(66, 252, 317, 35))
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
        self.slider_voltage.setGeometry(QtCore.QRect(386, 42, 23, 169))
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
        self.label_regulator.setGeometry(QtCore.QRect(18, 8, 401, 245))
        self.label_regulator.setText("")
        self.label_regulator.setPixmap(QtGui.QPixmap("F:\\Projects\\Simulation_Of_Laboratory_Works\\forms_ui\\../images/laba_15/regulator_voltage.png"))
        self.label_regulator.setScaledContents(True)
        self.label_regulator.setObjectName("label_regulator")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 252, 239, 28))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 28))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_coil = QtWidgets.QLabel(self.centralwidget)
        self.label_coil.setGeometry(QtCore.QRect(398, 338, 177, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_coil.sizePolicy().hasHeightForWidth())
        self.label_coil.setSizePolicy(sizePolicy)
        self.label_coil.setMinimumSize(QtCore.QSize(177, 141))
        self.label_coil.setMaximumSize(QtCore.QSize(177, 141))
        self.label_coil.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_coil.setText("")
        self.label_coil.setPixmap(QtGui.QPixmap("F:\\Projects\\Simulation_Of_Laboratory_Works\\forms_ui\\../images/laba_15/coil.png"))
        self.label_coil.setScaledContents(True)
        self.label_coil.setAlignment(QtCore.Qt.AlignCenter)
        self.label_coil.setWordWrap(False)
        self.label_coil.setIndent(-1)
        self.label_coil.setOpenExternalLinks(False)
        self.label_coil.setObjectName("label_coil")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(752, 2, 487, 573))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_resistor = QtWidgets.QLabel(self.centralwidget)
        self.label_resistor.setGeometry(QtCore.QRect(582, 454, 139, 23))
        self.label_resistor.setMinimumSize(QtCore.QSize(139, 23))
        self.label_resistor.setMaximumSize(QtCore.QSize(139, 23))
        self.label_resistor.setText("")
        self.label_resistor.setPixmap(QtGui.QPixmap("F:\\Projects\\Simulation_Of_Laboratory_Works\\forms_ui\\../images/laba_15/resistor.png"))
        self.label_resistor.setScaledContents(True)
        self.label_resistor.setObjectName("label_resistor")
        self.label_milli_voltmeter = QtWidgets.QLabel(self.centralwidget)
        self.label_milli_voltmeter.setGeometry(QtCore.QRect(754, 4, 483, 569))
        self.label_milli_voltmeter.setStyleSheet("background-color: None;")
        self.label_milli_voltmeter.setText("")
        self.label_milli_voltmeter.setObjectName("label_milli_voltmeter")
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(6, 578, 309, 27))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_info.setFont(font)
        self.label_info.setStyleSheet("font: 10pt \"Comic Sans MS\";")
        self.label_info.setText("")
        self.label_info.setObjectName("label_info")
        self.label_capacitor = QtWidgets.QLabel(self.centralwidget)
        self.label_capacitor.setGeometry(QtCore.QRect(232, 330, 111, 143))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_capacitor.sizePolicy().hasHeightForWidth())
        self.label_capacitor.setSizePolicy(sizePolicy)
        self.label_capacitor.setMinimumSize(QtCore.QSize(111, 143))
        self.label_capacitor.setMaximumSize(QtCore.QSize(111, 143))
        self.label_capacitor.setToolTip("")
        self.label_capacitor.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_capacitor.setAutoFillBackground(False)
        self.label_capacitor.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_capacitor.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_capacitor.setText("")
        self.label_capacitor.setPixmap(QtGui.QPixmap("F:\\Projects\\Simulation_Of_Laboratory_Works\\forms_ui\\../images/laba_15/capacitor.png"))
        self.label_capacitor.setScaledContents(True)
        self.label_capacitor.setAlignment(QtCore.Qt.AlignCenter)
        self.label_capacitor.setWordWrap(False)
        self.label_capacitor.setObjectName("label_capacitor")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(6, 480, 736, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(177, 53))
        self.label_4.setMaximumSize(QtCore.QSize(177, 53))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.measure_enter_voltage = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.measure_enter_voltage.setMinimumSize(QtCore.QSize(177, 28))
        self.measure_enter_voltage.setMaximumSize(QtCore.QSize(177, 28))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.measure_enter_voltage.setFont(font)
        self.measure_enter_voltage.setObjectName("measure_enter_voltage")
        self.verticalLayout_6.addWidget(self.measure_enter_voltage)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(177, 53))
        self.label_3.setMaximumSize(QtCore.QSize(177, 53))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.measure_c_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.measure_c_button.setMinimumSize(QtCore.QSize(177, 28))
        self.measure_c_button.setMaximumSize(QtCore.QSize(177, 28))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.measure_c_button.setFont(font)
        self.measure_c_button.setObjectName("measure_c_button")
        self.verticalLayout_2.addWidget(self.measure_c_button)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(177, 53))
        self.label_5.setMaximumSize(QtCore.QSize(177, 53))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.measure_3_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.measure_3_button.setMinimumSize(QtCore.QSize(177, 28))
        self.measure_3_button.setMaximumSize(QtCore.QSize(177, 28))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.measure_3_button.setFont(font)
        self.measure_3_button.setObjectName("measure_3_button")
        self.verticalLayout_5.addWidget(self.measure_3_button)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(177, 53))
        self.label_7.setMaximumSize(QtCore.QSize(177, 53))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.measure_r_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.measure_r_button.setMinimumSize(QtCore.QSize(177, 28))
        self.measure_r_button.setMaximumSize(QtCore.QSize(177, 28))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.measure_r_button.setFont(font)
        self.measure_r_button.setObjectName("measure_r_button")
        self.verticalLayout_4.addWidget(self.measure_r_button)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.label_regulator.raise_()
        self.verticalLayoutWidget.raise_()
        self.button_info.raise_()
        self.label_10.raise_()
        self.slider_voltage.raise_()
        self.label.raise_()
        self.label_coil.raise_()
        self.verticalLayoutWidget_5.raise_()
        self.label_resistor.raise_()
        self.label_milli_voltmeter.raise_()
        self.label_info.raise_()
        self.label_capacitor.raise_()
        self.horizontalLayoutWidget.raise_()
        Laba15.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Laba15)
        self.statusbar.setObjectName("statusbar")
        Laba15.setStatusBar(self.statusbar)

        self.retranslateUi(Laba15)
        QtCore.QMetaObject.connectSlotsByName(Laba15)

    def retranslateUi(self, Laba15):
        _translate = QtCore.QCoreApplication.translate
        Laba15.setWindowTitle(_translate("Laba15", "Лабораторная работа №15"))
        self.label_10.setText(_translate("Laba15", "Регулятор напряжения"))
        self.label.setText(_translate("Laba15", "Амперметр"))
        self.label_4.setText(_translate("Laba15", "Гнездо (1-1)"))
        self.measure_enter_voltage.setText(_translate("Laba15", "Измерить напряжение"))
        self.label_3.setText(_translate("Laba15", "Конденсатор (2-2)"))
        self.measure_c_button.setText(_translate("Laba15", "Измерить напряжение"))
        self.label_5.setText(_translate("Laba15", "Катушка индуктивности (3-3)"))
        self.measure_3_button.setText(_translate("Laba15", "Измерить напряжение"))
        self.label_7.setText(_translate("Laba15", "Резистор (4-4)"))
        self.measure_r_button.setText(_translate("Laba15", "Измерить напряжение"))

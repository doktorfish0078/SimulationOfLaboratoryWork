# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Projects\Simulation_Of_Laboratory_Works\forms_ui\laba2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Laba2(object):
    def setupUi(self, Laba2):
        Laba2.setObjectName("Laba2")
        Laba2.resize(1060, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Laba2.sizePolicy().hasHeightForWidth())
        Laba2.setSizePolicy(sizePolicy)
        Laba2.setMaximumSize(QtCore.QSize(1060, 850))
        Laba2.setStyleSheet("background-color: rgb(176,193,208);")
        self.centralwidget = QtWidgets.QWidget(Laba2)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(2, 44, 1057, 78))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Reostat = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.Reostat.setMaximum(240)
        self.Reostat.setSingleStep(1)
        self.Reostat.setSliderPosition(0)
        self.Reostat.setTracking(True)
        self.Reostat.setOrientation(QtCore.Qt.Horizontal)
        self.Reostat.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Reostat.setTickInterval(10)
        self.Reostat.setObjectName("Reostat")
        self.verticalLayout.addWidget(self.Reostat)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(4, -1, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout.addWidget(self.label_18)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout.addWidget(self.label_19)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.label_13)
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout.addWidget(self.label_23)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout.addWidget(self.label_22)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout.addWidget(self.label_21)
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout.addWidget(self.label_26)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 1)
        self.horizontalLayout.setStretch(5, 1)
        self.horizontalLayout.setStretch(6, 1)
        self.horizontalLayout.setStretch(7, 1)
        self.horizontalLayout.setStretch(8, 1)
        self.horizontalLayout.setStretch(9, 1)
        self.horizontalLayout.setStretch(10, 1)
        self.horizontalLayout.setStretch(11, 1)
        self.horizontalLayout.setStretch(12, 1)
        self.horizontalLayout.setStretch(13, 1)
        self.horizontalLayout.setStretch(14, 1)
        self.horizontalLayout.setStretch(15, 1)
        self.horizontalLayout.setStretch(16, 1)
        self.horizontalLayout.setStretch(17, 1)
        self.horizontalLayout.setStretch(18, 1)
        self.horizontalLayout.setStretch(19, 1)
        self.horizontalLayout.setStretch(20, 1)
        self.horizontalLayout.setStretch(21, 1)
        self.horizontalLayout.setStretch(22, 1)
        self.horizontalLayout.setStretch(23, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 8pt \"Comic Sans MS\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(362, 360, 371, 295))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_battery1 = QtWidgets.QLabel(self.centralwidget)
        self.label_battery1.setGeometry(QtCore.QRect(814, 168, 71, 110))
        self.label_battery1.setText("")
        self.label_battery1.setPixmap(QtGui.QPixmap("F:\\Projects\\Simulation_Of_Laboratory_Works\\forms_ui\\../images/laba_2/Battery1.png"))
        self.label_battery1.setScaledContents(True)
        self.label_battery1.setObjectName("label_battery1")
        self.label_battery2 = QtWidgets.QLabel(self.centralwidget)
        self.label_battery2.setGeometry(QtCore.QRect(898, 150, 71, 110))
        self.label_battery2.setText("")
        self.label_battery2.setPixmap(QtGui.QPixmap("F:\\Projects\\Simulation_Of_Laboratory_Works\\forms_ui\\../images/laba_2/Battery1.png"))
        self.label_battery2.setScaledContents(True)
        self.label_battery2.setObjectName("label_battery2")
        self.slot_battery2 = QtWidgets.QLabel(self.centralwidget)
        self.slot_battery2.setGeometry(QtCore.QRect(972, 528, 71, 110))
        self.slot_battery2.setText("")
        self.slot_battery2.setPixmap(QtGui.QPixmap("F:\\Projects\\Simulation_Of_Laboratory_Works\\forms_ui\\../images/laba_2/battery_in_slot.png"))
        self.slot_battery2.setScaledContents(True)
        self.slot_battery2.setObjectName("slot_battery2")
        self.slot_battery1 = QtWidgets.QLabel(self.centralwidget)
        self.slot_battery1.setGeometry(QtCore.QRect(972, 304, 71, 110))
        self.slot_battery1.setText("")
        self.slot_battery1.setPixmap(QtGui.QPixmap("F:\\Projects\\Simulation_Of_Laboratory_Works\\forms_ui\\../images/laba_2/battery_in_slot.png"))
        self.slot_battery1.setScaledContents(True)
        self.slot_battery1.setObjectName("slot_battery1")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(898, 356, 71, 41))
        self.label_28.setStyleSheet("font: 75 14pt \"Comic Sans MS\";")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(900, 578, 71, 41))
        self.label_29.setStyleSheet("font: 75 14pt \"Comic Sans MS\";")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.check_battery1 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_battery1.setGeometry(QtCore.QRect(838, 396, 131, 17))
        self.check_battery1.setChecked(False)
        self.check_battery1.setTristate(False)
        self.check_battery1.setObjectName("check_battery1")
        self.check_battery2 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_battery2.setGeometry(QtCore.QRect(840, 618, 131, 17))
        self.check_battery2.setTristate(False)
        self.check_battery2.setObjectName("check_battery2")
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(0, 652, 309, 27))
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
        self.key_slider = QtWidgets.QSlider(self.centralwidget)
        self.key_slider.setGeometry(QtCore.QRect(474, 330, 173, 22))
        self.key_slider.setMaximum(2)
        self.key_slider.setProperty("value", 1)
        self.key_slider.setOrientation(QtCore.Qt.Horizontal)
        self.key_slider.setObjectName("key_slider")
        self.label_key = QtWidgets.QLabel(self.centralwidget)
        self.label_key.setGeometry(QtCore.QRect(444, 226, 233, 103))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_key.sizePolicy().hasHeightForWidth())
        self.label_key.setSizePolicy(sizePolicy)
        self.label_key.setMaximumSize(QtCore.QSize(250, 175))
        self.label_key.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_key.setText("")
        self.label_key.setPixmap(QtGui.QPixmap("F:\\Projects\\Simulation_Of_Laboratory_Works\\forms_ui\\../images/laba_2/key_middle.png"))
        self.label_key.setScaledContents(True)
        self.label_key.setWordWrap(False)
        self.label_key.setOpenExternalLinks(False)
        self.label_key.setObjectName("label_key")
        self.button_info = QtWidgets.QPushButton(self.centralwidget)
        self.button_info.setGeometry(QtCore.QRect(1018, 0, 41, 41))
        self.button_info.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:\\Projects\\Simulation_Of_Laboratory_Works\\forms_ui\\../images/laba_11/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_info.setIcon(icon)
        self.button_info.setIconSize(QtCore.QSize(32, 32))
        self.button_info.setObjectName("button_info")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setEnabled(True)
        self.label_27.setGeometry(QtCore.QRect(486, 658, 129, 20))
        self.label_27.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_27.setStyleSheet("font: 8pt \"Comic Sans MS\";")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.label_Gc = QtWidgets.QLabel(self.centralwidget)
        self.label_Gc.setGeometry(QtCore.QRect(54, 154, 127, 221))
        self.label_Gc.setText("")
        self.label_Gc.setPixmap(QtGui.QPixmap("F:\\Projects\\Simulation_Of_Laboratory_Works\\forms_ui\\../images/laba_2/Gc.png"))
        self.label_Gc.setScaledContents(True)
        self.label_Gc.setObjectName("label_Gc")
        self.label_G = QtWidgets.QLabel(self.centralwidget)
        self.label_G.setGeometry(QtCore.QRect(66, 398, 101, 257))
        self.label_G.setText("")
        self.label_G.setPixmap(QtGui.QPixmap("F:\\Projects\\Simulation_Of_Laboratory_Works\\forms_ui\\../images/laba_2/G.png"))
        self.label_G.setScaledContents(True)
        self.label_G.setObjectName("label_G")
        Laba2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Laba2)
        self.statusbar.setObjectName("statusbar")
        Laba2.setStatusBar(self.statusbar)

        self.retranslateUi(Laba2)
        QtCore.QMetaObject.connectSlotsByName(Laba2)

    def retranslateUi(self, Laba2):
        _translate = QtCore.QCoreApplication.translate
        Laba2.setWindowTitle(_translate("Laba2", "Лабораторная работа №2"))
        self.label_6.setText(_translate("Laba2", "0"))
        self.label_5.setText(_translate("Laba2", "1"))
        self.label_4.setText(_translate("Laba2", "2"))
        self.label_3.setText(_translate("Laba2", "3"))
        self.label_7.setText(_translate("Laba2", "4"))
        self.label_2.setText(_translate("Laba2", "5"))
        self.label_9.setText(_translate("Laba2", "6"))
        self.label_10.setText(_translate("Laba2", "7"))
        self.label_12.setText(_translate("Laba2", "8"))
        self.label_11.setText(_translate("Laba2", "9"))
        self.label_8.setText(_translate("Laba2", "10"))
        self.label_16.setText(_translate("Laba2", "11"))
        self.label_17.setText(_translate("Laba2", "12"))
        self.label_18.setText(_translate("Laba2", "13"))
        self.label_14.setText(_translate("Laba2", "14"))
        self.label_15.setText(_translate("Laba2", "15"))
        self.label_19.setText(_translate("Laba2", "16"))
        self.label_13.setText(_translate("Laba2", "17"))
        self.label_23.setText(_translate("Laba2", "18"))
        self.label_22.setText(_translate("Laba2", "19"))
        self.label_20.setText(_translate("Laba2", "20"))
        self.label_21.setText(_translate("Laba2", "21"))
        self.label_24.setText(_translate("Laba2", "22"))
        self.label_25.setText(_translate("Laba2", "23"))
        self.label_26.setText(_translate("Laba2", "24"))
        self.label.setText(_translate("Laba2", "Реостат"))
        self.label_28.setText(_translate("Laba2", "GBx1"))
        self.label_29.setText(_translate("Laba2", "GBx2"))
        self.check_battery1.setText(_translate("Laba2", "Вставить батарейку"))
        self.check_battery2.setText(_translate("Laba2", "Вставить батарейку"))
        self.label_27.setText(_translate("Laba2", "Гальванометр"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Projects\SimulationOfLaboratoryWork\forms_ui\laba14.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Laba14(object):
    def setupUi(self, Laba14):
        Laba14.setObjectName("Laba14")
        Laba14.resize(1136, 706)
        Laba14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(Laba14)
        self.centralwidget.setObjectName("centralwidget")
        self.slider_stock = QtWidgets.QSlider(self.centralwidget)
        self.slider_stock.setGeometry(QtCore.QRect(590, 620, 221, 31))
        self.slider_stock.setMinimum(-3)
        self.slider_stock.setMaximum(47)
        self.slider_stock.setProperty("value", -3)
        self.slider_stock.setOrientation(QtCore.Qt.Horizontal)
        self.slider_stock.setObjectName("slider_stock")
        self.mainOut = QtWidgets.QLineEdit(self.centralwidget)
        self.mainOut.setGeometry(QtCore.QRect(720, 220, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mainOut.setFont(font)
        self.mainOut.setObjectName("mainOut")
        self.amperDial = QtWidgets.QDial(self.centralwidget)
        self.amperDial.setGeometry(QtCore.QRect(860, 10, 151, 101))
        self.amperDial.setMaximum(10)
        self.amperDial.setSingleStep(1)
        self.amperDial.setObjectName("amperDial")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(720, 10, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(750, 150, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.amperOut = QtWidgets.QLineEdit(self.centralwidget)
        self.amperOut.setGeometry(QtCore.QRect(710, 60, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.amperOut.setFont(font)
        self.amperOut.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.amperOut.setObjectName("amperOut")
        self.shtokValue = QtWidgets.QLabel(self.centralwidget)
        self.shtokValue.setGeometry(QtCore.QRect(590, 580, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.shtokValue.setFont(font)
        self.shtokValue.setObjectName("shtokValue")
        self.shtokRealValue = QtWidgets.QLabel(self.centralwidget)
        self.shtokRealValue.setGeometry(QtCore.QRect(390, 631, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.shtokRealValue.setFont(font)
        self.shtokRealValue.setObjectName("shtokRealValue")
        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(230, 630, 151, 31))
        self.info.setObjectName("info")
        self.label_solenoid = QtWidgets.QLabel(self.centralwidget)
        self.label_solenoid.setGeometry(QtCore.QRect(0, 500, 590, 70))
        self.label_solenoid.setText("")
        self.label_solenoid.setPixmap(QtGui.QPixmap("F:\\Projects\\SimulationOfLaboratoryWork\\forms_ui\\../images/laba_14/фывф.png"))
        self.label_solenoid.setScaledContents(True)
        self.label_solenoid.setObjectName("label_solenoid")
        self.label_stock = QtWidgets.QLabel(self.centralwidget)
        self.label_stock.setGeometry(QtCore.QRect(90, 500, 590, 70))
        self.label_stock.setText("")
        self.label_stock.setPixmap(QtGui.QPixmap("F:\\Projects\\SimulationOfLaboratoryWork\\forms_ui\\../images/laba_14/Без имени-4.png"))
        self.label_stock.setScaledContents(True)
        self.label_stock.setObjectName("label_stock")
        self.label_instrumentation = QtWidgets.QLabel(self.centralwidget)
        self.label_instrumentation.setGeometry(QtCore.QRect(0, 0, 691, 491))
        self.label_instrumentation.setText("")
        self.label_instrumentation.setPixmap(QtGui.QPixmap("F:\\Projects\\SimulationOfLaboratoryWork\\forms_ui\\../images/laba_14/pribori.png"))
        self.label_instrumentation.setScaledContents(True)
        self.label_instrumentation.setObjectName("label_instrumentation")
        self.slider_stock.raise_()
        self.mainOut.raise_()
        self.amperDial.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.amperOut.raise_()
        self.shtokValue.raise_()
        self.shtokRealValue.raise_()
        self.info.raise_()
        self.label_stock.raise_()
        self.label_instrumentation.raise_()
        self.label_solenoid.raise_()
        Laba14.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Laba14)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1136, 21))
        self.menubar.setObjectName("menubar")
        Laba14.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Laba14)
        self.statusbar.setObjectName("statusbar")
        Laba14.setStatusBar(self.statusbar)

        self.retranslateUi(Laba14)
        QtCore.QMetaObject.connectSlotsByName(Laba14)

    def retranslateUi(self, Laba14):
        _translate = QtCore.QCoreApplication.translate
        Laba14.setWindowTitle(_translate("Laba14", "MainWindow"))
        self.mainOut.setText(_translate("Laba14", "0.0"))
        self.label.setText(_translate("Laba14", "Амперметр"))
        self.label_2.setText(_translate("Laba14", "Индукция"))
        self.amperOut.setText(_translate("Laba14", "0.0"))
        self.shtokValue.setText(_translate("Laba14", "50"))
        self.shtokRealValue.setText(_translate("Laba14", "-3"))
        self.info.setText(_translate("Laba14", "(deBug info) lenOutside = "))

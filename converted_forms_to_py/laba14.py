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
        Laba14.resize(1315, 854)
        Laba14.setMinimumSize(QtCore.QSize(1315, 854))
        Laba14.setMaximumSize(QtCore.QSize(1315, 854))
        Laba14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(Laba14)
        self.centralwidget.setObjectName("centralwidget")
        self.slider_stock = QtWidgets.QSlider(self.centralwidget)
        self.slider_stock.setGeometry(QtCore.QRect(810, 720, 500, 31))
        self.slider_stock.setMaximumSize(QtCore.QSize(500, 16777215))
        self.slider_stock.setMinimum(-6)
        self.slider_stock.setMaximum(94)
        self.slider_stock.setProperty("value", -6)
        self.slider_stock.setSliderPosition(-6)
        self.slider_stock.setTracking(True)
        self.slider_stock.setOrientation(QtCore.Qt.Horizontal)
        self.slider_stock.setInvertedAppearance(False)
        self.slider_stock.setInvertedControls(False)
        self.slider_stock.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_stock.setObjectName("slider_stock")
        self.amperDial = QtWidgets.QDial(self.centralwidget)
        self.amperDial.setGeometry(QtCore.QRect(570, 380, 131, 81))
        self.amperDial.setMaximum(10)
        self.amperDial.setSingleStep(1)
        self.amperDial.setObjectName("amperDial")
        self.shtokValue = QtWidgets.QLabel(self.centralwidget)
        self.shtokValue.setGeometry(QtCore.QRect(970, 390, 121, 120))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.shtokValue.setFont(font)
        self.shtokValue.setAutoFillBackground(False)
        self.shtokValue.setStyleSheet("QLabel { border-radius: 60px;\n"
"        \n"
"    background-color:rgb(101, 100, 89); }")
        self.shtokValue.setObjectName("shtokValue")
        self.label_solenoid = QtWidgets.QLabel(self.centralwidget)
        self.label_solenoid.setGeometry(QtCore.QRect(0, 670, 703, 131))
        self.label_solenoid.setText("")
        self.label_solenoid.setPixmap(QtGui.QPixmap("F:\\Projects\\SimulationOfLaboratoryWork\\forms_ui\\../images/laba_14/solenoid.png"))
        self.label_solenoid.setScaledContents(True)
        self.label_solenoid.setObjectName("label_solenoid")
        self.label_stock = QtWidgets.QLabel(self.centralwidget)
        self.label_stock.setGeometry(QtCore.QRect(170, 690, 498, 91))
        self.label_stock.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_stock.setText("")
        self.label_stock.setPixmap(QtGui.QPixmap("F:\\Projects\\SimulationOfLaboratoryWork\\forms_ui\\../images/laba_14/stock.png"))
        self.label_stock.setScaledContents(True)
        self.label_stock.setObjectName("label_stock")
        self.label_instrumentation = QtWidgets.QLabel(self.centralwidget)
        self.label_instrumentation.setGeometry(QtCore.QRect(-10, 50, 881, 631))
        self.label_instrumentation.setText("")
        self.label_instrumentation.setPixmap(QtGui.QPixmap("F:\\Projects\\SimulationOfLaboratoryWork\\forms_ui\\../images/laba_14/pribori.png"))
        self.label_instrumentation.setScaledContents(True)
        self.label_instrumentation.setObjectName("label_instrumentation")
        self.label_stock_head = QtWidgets.QLabel(self.centralwidget)
        self.label_stock_head.setGeometry(QtCore.QRect(668, 700, 142, 71))
        self.label_stock_head.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_stock_head.setText("")
        self.label_stock_head.setPixmap(QtGui.QPixmap("F:\\Projects\\SimulationOfLaboratoryWork\\forms_ui\\../images/laba_14/stock_head.png"))
        self.label_stock_head.setScaledContents(True)
        self.label_stock_head.setObjectName("label_stock_head")
        self.label_lupa = QtWidgets.QLabel(self.centralwidget)
        self.label_lupa.setGeometry(QtCore.QRect(941, 380, 251, 251))
        self.label_lupa.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_lupa.setText("")
        self.label_lupa.setPixmap(QtGui.QPixmap("F:\\Projects\\SimulationOfLaboratoryWork\\forms_ui\\../images/laba_14/lupa.png"))
        self.label_lupa.setScaledContents(True)
        self.label_lupa.setObjectName("label_lupa")
        self.label_shtok_value_inf = QtWidgets.QLabel(self.centralwidget)
        self.label_shtok_value_inf.setGeometry(QtCore.QRect(910, 300, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_shtok_value_inf.setFont(font)
        self.label_shtok_value_inf.setObjectName("label_shtok_value_inf")
        self.mainOut = QtWidgets.QLineEdit(self.centralwidget)
        self.mainOut.setGeometry(QtCore.QRect(230, 120, 226, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.mainOut.setFont(font)
        self.mainOut.setStyleSheet("background-color: rgb(80, 113, 223);")
        self.mainOut.setReadOnly(True)
        self.mainOut.setObjectName("mainOut")
        self.label_formula_inf = QtWidgets.QLabel(self.centralwidget)
        self.label_formula_inf.setGeometry(QtCore.QRect(860, 40, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_formula_inf.setFont(font)
        self.label_formula_inf.setObjectName("label_formula_inf")
        self.label_formula = QtWidgets.QLabel(self.centralwidget)
        self.label_formula.setGeometry(QtCore.QRect(840, 100, 461, 181))
        self.label_formula.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_formula.setText("")
        self.label_formula.setPixmap(QtGui.QPixmap("F:\\Projects\\SimulationOfLaboratoryWork\\forms_ui\\../images/laba_14/formula.png"))
        self.label_formula.setScaledContents(True)
        self.label_formula.setObjectName("label_formula")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(286, 382, 155, 153))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_instrumentation.raise_()
        self.amperDial.raise_()
        self.slider_stock.raise_()
        self.label_stock.raise_()
        self.label_stock_head.raise_()
        self.shtokValue.raise_()
        self.label_shtok_value_inf.raise_()
        self.mainOut.raise_()
        self.label_solenoid.raise_()
        self.label_formula_inf.raise_()
        self.label_formula.raise_()
        self.label_lupa.raise_()
        self.verticalLayoutWidget.raise_()
        Laba14.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Laba14)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1315, 21))
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
        self.shtokValue.setText(_translate("Laba14", "   50.0"))
        self.label_shtok_value_inf.setText(_translate("Laba14", "Текущая отметка на штоке:"))
        self.label_formula_inf.setText(_translate("Laba14", "Формула поиска индукции соленоида:"))

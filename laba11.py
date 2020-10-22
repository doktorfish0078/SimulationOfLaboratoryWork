# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laba11.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(979, 739)
        MainWindow.setStyleSheet("background-color: rgb(201, 207, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 260, 130, 100))
        self.horizontalLayoutWidget.setMaximumSize(QtCore.QSize(130, 100))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setMaximumSize(QtCore.QSize(130, 100))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("images/resistor.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setWordWrap(False)
        self.label_9.setOpenExternalLinks(False)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_10.setMaximumSize(QtCore.QSize(130, 100))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("images/resistor.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setWordWrap(False)
        self.label_10.setOpenExternalLinks(False)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_11.setMaximumSize(QtCore.QSize(130, 100))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("images/resistor.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setWordWrap(False)
        self.label_11.setOpenExternalLinks(False)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(80, 400, 339, 107))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.single = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.single.setCheckable(True)
        self.single.setObjectName("single")
        self.horizontalLayout_2.addWidget(self.single)
        self.serial = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.serial.setObjectName("serial")
        self.horizontalLayout_2.addWidget(self.serial)
        self.parallel = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.parallel.setObjectName("parallel")
        self.horizontalLayout_2.addWidget(self.parallel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(70, -1, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.check_r1 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.check_r1.setTristate(False)
        self.check_r1.setObjectName("check_r1")
        self.verticalLayout_6.addWidget(self.check_r1)
        self.check_r2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.check_r2.setEnabled(True)
        self.check_r2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.check_r2.setAutoFillBackground(False)
        self.check_r2.setChecked(False)
        self.check_r2.setAutoRepeat(False)
        self.check_r2.setObjectName("check_r2")
        self.verticalLayout_6.addWidget(self.check_r2)
        self.check_r3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.check_r3.setObjectName("check_r3")
        self.verticalLayout_6.addWidget(self.check_r3)
        self.verticalLayout_2.addLayout(self.verticalLayout_6)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(430, 180, 100, 31))
        self.label_8.setStyleSheet("font: 75 10pt \"Comic Sans MS\";")
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(330, 30, 291, 151))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("images/voltmeter.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.voltmeter = QtWidgets.QLineEdit(self.centralwidget)
        self.voltmeter.setGeometry(QtCore.QRect(380, 60, 191, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.voltmeter.setFont(font)
        self.voltmeter.setStyleSheet("background-color: rgb(80, 113, 223);")
        self.voltmeter.setReadOnly(True)
        self.voltmeter.setObjectName("voltmeter")
        self.dial_1 = QtWidgets.QDial(self.centralwidget)
        self.dial_1.setGeometry(QtCore.QRect(580, 290, 101, 101))
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
        self.dial_1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(28, 30, 29);")
        self.dial_1.setMaximum(9)
        self.dial_1.setPageStep(10)
        self.dial_1.setSliderPosition(0)
        self.dial_1.setInvertedAppearance(False)
        self.dial_1.setInvertedControls(False)
        self.dial_1.setWrapping(False)
        self.dial_1.setNotchTarget(10.0)
        self.dial_1.setNotchesVisible(True)
        self.dial_1.setObjectName("dial_1")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(550, 260, 401, 251))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("images/resistor_store.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.dial_2 = QtWidgets.QDial(self.centralwidget)
        self.dial_2.setGeometry(QtCore.QRect(700, 290, 101, 101))
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
        self.dial_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(28, 30, 29);")
        self.dial_2.setMaximum(9)
        self.dial_2.setPageStep(10)
        self.dial_2.setSliderPosition(0)
        self.dial_2.setInvertedAppearance(False)
        self.dial_2.setInvertedControls(False)
        self.dial_2.setWrapping(False)
        self.dial_2.setNotchTarget(10.0)
        self.dial_2.setNotchesVisible(True)
        self.dial_2.setObjectName("dial_2")
        self.dial_3 = QtWidgets.QDial(self.centralwidget)
        self.dial_3.setGeometry(QtCore.QRect(820, 290, 101, 101))
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
        self.dial_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(28, 30, 29);")
        self.dial_3.setMaximum(9)
        self.dial_3.setPageStep(10)
        self.dial_3.setSliderPosition(0)
        self.dial_3.setInvertedAppearance(False)
        self.dial_3.setInvertedControls(False)
        self.dial_3.setWrapping(False)
        self.dial_3.setNotchTarget(10.0)
        self.dial_3.setNotchesVisible(True)
        self.dial_3.setObjectName("dial_3")
        self.dial_4 = QtWidgets.QDial(self.centralwidget)
        self.dial_4.setGeometry(QtCore.QRect(580, 400, 101, 101))
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
        self.dial_4.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(28, 30, 29);")
        self.dial_4.setMaximum(9)
        self.dial_4.setPageStep(10)
        self.dial_4.setSliderPosition(0)
        self.dial_4.setInvertedAppearance(False)
        self.dial_4.setInvertedControls(False)
        self.dial_4.setWrapping(False)
        self.dial_4.setNotchTarget(10.0)
        self.dial_4.setNotchesVisible(True)
        self.dial_4.setObjectName("dial_4")
        self.dial_5 = QtWidgets.QDial(self.centralwidget)
        self.dial_5.setGeometry(QtCore.QRect(700, 400, 101, 101))
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
        self.dial_5.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(28, 30, 29);")
        self.dial_5.setMaximum(9)
        self.dial_5.setPageStep(10)
        self.dial_5.setSliderPosition(0)
        self.dial_5.setInvertedAppearance(False)
        self.dial_5.setInvertedControls(False)
        self.dial_5.setWrapping(False)
        self.dial_5.setNotchTarget(10.0)
        self.dial_5.setNotchesVisible(True)
        self.dial_5.setObjectName("dial_5")
        self.dial_6 = QtWidgets.QDial(self.centralwidget)
        self.dial_6.setGeometry(QtCore.QRect(820, 400, 101, 101))
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
        self.dial_6.setStyleSheet("background-color: rgb(28, 30, 29);\n"
"")
        self.dial_6.setMaximum(9)
        self.dial_6.setPageStep(10)
        self.dial_6.setSliderPosition(0)
        self.dial_6.setInvertedAppearance(False)
        self.dial_6.setInvertedControls(False)
        self.dial_6.setWrapping(False)
        self.dial_6.setNotchTarget(10.0)
        self.dial_6.setNotchesVisible(True)
        self.dial_6.setObjectName("dial_6")
        self.resistors_store = QtWidgets.QLabel(self.centralwidget)
        self.resistors_store.setGeometry(QtCore.QRect(550, 520, 401, 21))
        self.resistors_store.setStyleSheet("font: 75 10pt \"Comic Sans MS\";")
        self.resistors_store.setText("")
        self.resistors_store.setAlignment(QtCore.Qt.AlignCenter)
        self.resistors_store.setObjectName("resistors_store")
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(690, 550, 151, 71))
        self.resetButton.setStyleSheet("font: 11pt \"Comic Sans MS\";")
        self.resetButton.setObjectName("resetButton")
        self.PowerCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.PowerCheck.setGeometry(QtCore.QRect(410, 610, 161, 61))
        self.PowerCheck.setStyleSheet("font: 75 16pt \"Comic Sans MS\";")
        self.PowerCheck.setObjectName("PowerCheck")
        self.info = QtWidgets.QPushButton(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(930, 10, 31, 31))
        self.info.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/info.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info.setIcon(icon)
        self.info.setIconSize(QtCore.QSize(32, 32))
        self.info.setObjectName("info")
        self.label_13.raise_()
        self.horizontalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.label_8.raise_()
        self.label_12.raise_()
        self.voltmeter.raise_()
        self.dial_1.raise_()
        self.dial_2.raise_()
        self.dial_3.raise_()
        self.dial_4.raise_()
        self.dial_5.raise_()
        self.dial_6.raise_()
        self.resistors_store.raise_()
        self.resetButton.raise_()
        self.PowerCheck.raise_()
        self.info.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 979, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.single.setText(_translate("MainWindow", "Одиночно"))
        self.serial.setText(_translate("MainWindow", "Последовательно"))
        self.parallel.setText(_translate("MainWindow", "Параллельно"))
        self.check_r1.setText(_translate("MainWindow", "R1"))
        self.check_r2.setText(_translate("MainWindow", "R2"))
        self.check_r3.setText(_translate("MainWindow", "R3"))
        self.label_8.setText(_translate("MainWindow", "Вольтметр"))
        self.resetButton.setText(_translate("MainWindow", "Сбросить\n"
"сопротивления"))
        self.PowerCheck.setText(_translate("MainWindow", "Замкнуть"))
import images_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Projects\SimulationOfLaboratoryWork\forms_ui\start_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_start_window(object):
    def setupUi(self, start_window):
        start_window.setObjectName("start_window")
        start_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(start_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 100, 321, 101))
        self.label.setStyleSheet("font: 75 14pt \"Comic Sans MS\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(230, 200, 371, 191))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_laba2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_laba2.sizePolicy().hasHeightForWidth())
        self.button_laba2.setSizePolicy(sizePolicy)
        self.button_laba2.setMinimumSize(QtCore.QSize(150, 50))
        self.button_laba2.setAutoDefault(True)
        self.button_laba2.setDefault(False)
        self.button_laba2.setObjectName("button_laba2")
        self.verticalLayout.addWidget(self.button_laba2)
        self.button_laba11 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_laba11.sizePolicy().hasHeightForWidth())
        self.button_laba11.setSizePolicy(sizePolicy)
        self.button_laba11.setMinimumSize(QtCore.QSize(150, 50))
        self.button_laba11.setAutoDefault(True)
        self.button_laba11.setDefault(False)
        self.button_laba11.setFlat(False)
        self.button_laba11.setObjectName("button_laba11")
        self.verticalLayout.addWidget(self.button_laba11)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.button_laba14 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_laba14.sizePolicy().hasHeightForWidth())
        self.button_laba14.setSizePolicy(sizePolicy)
        self.button_laba14.setMinimumSize(QtCore.QSize(150, 50))
        self.button_laba14.setAutoDefault(True)
        self.button_laba14.setDefault(False)
        self.button_laba14.setFlat(False)
        self.button_laba14.setObjectName("button_laba14")
        self.verticalLayout_3.addWidget(self.button_laba14)
        self.button_laba15 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_laba15.sizePolicy().hasHeightForWidth())
        self.button_laba15.setSizePolicy(sizePolicy)
        self.button_laba15.setMinimumSize(QtCore.QSize(150, 50))
        self.button_laba15.setAutoDefault(True)
        self.button_laba15.setDefault(False)
        self.button_laba15.setFlat(False)
        self.button_laba15.setObjectName("button_laba15")
        self.verticalLayout_3.addWidget(self.button_laba15)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        start_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(start_window)
        self.statusbar.setObjectName("statusbar")
        start_window.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(start_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        start_window.setMenuBar(self.menubar)

        self.retranslateUi(start_window)
        QtCore.QMetaObject.connectSlotsByName(start_window)

    def retranslateUi(self, start_window):
        _translate = QtCore.QCoreApplication.translate
        start_window.setWindowTitle(_translate("start_window", "MainWindow"))
        self.label.setText(_translate("start_window", "Выберите лабораторную работу, которую хотели бы выполнить"))
        self.button_laba2.setText(_translate("start_window", "Лабораторная №2"))
        self.button_laba11.setText(_translate("start_window", "Лабораторная №11"))
        self.button_laba14.setText(_translate("start_window", "Лабораторная №14"))
        self.button_laba15.setText(_translate("start_window", "Лабораторная №15"))
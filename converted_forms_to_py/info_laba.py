# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_info_laba_11(object):
    def setupUi(self, info_laba_11):
        info_laba_11.setObjectName("info_laba_11")
        info_laba_11.resize(696, 872)
        self.label_info = QtWidgets.QLabel(info_laba_11)
        self.label_info.setGeometry(QtCore.QRect(0, 0, 701, 871))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_info.sizePolicy().hasHeightForWidth())
        self.label_info.setSizePolicy(sizePolicy)
        self.label_info.setText("")
        self.label_info.setPixmap(QtGui.QPixmap("C:\\Users\\user\\PycharmProjects\\SimulationOfLaboratoryWork\\forms_ui\\../images/laba_11/info_laba_11.jpg"))
        self.label_info.setScaledContents(True)
        self.label_info.setObjectName("label_info")

        self.retranslateUi(info_laba_11)
        QtCore.QMetaObject.connectSlotsByName(info_laba_11)

    def retranslateUi(self, info_laba_11):
        _translate = QtCore.QCoreApplication.translate
        info_laba_11.setWindowTitle(_translate("info_laba_11", "Form"))

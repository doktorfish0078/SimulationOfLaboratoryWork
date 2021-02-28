import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5 import QtCore, QtGui

from converted_forms_to_py import info_laba


class Info_laba(QWidget):
    """Форма с документацией по выполнению
    л.р.
    """

    def __init__(self):
        super().__init__()
        self.ui = info_laba.Ui_info_laba()
        self.ui.setupUi(self)

        # set icon
        icon = QIcon()
        icon.addPixmap(QPixmap("../images/icon.png"),
                       QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

    def add_picture_in_scroll_area_content(self, path_to_picture):
        self.label_info = QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_info.sizePolicy().hasHeightForWidth())
        self.label_info.setSizePolicy(sizePolicy)
        self.label_info.setMinimumHeight(720)
        self.label_info.setText("")
        self.label_info.setPixmap(
            QtGui.QPixmap(path_to_picture))
        self.label_info.setScaledContents(True)
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setWordWrap(False)

        self.ui.verticalLayout_2.addWidget(self.label_info)


import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from converted_forms_to_py import authorization
from py_code_labs import start_window

import datetime


def creat_hash(a, p):
    s = 0
    k = 0
    z = 2 ** len(str(a))
    while a != 0:
        s += (a % 10) * p ** k
        s %= z
        k += 1
        a = a // 10
    buf = str(s)
    return 10 ** len(buf) * s + int(buf[::-1])


def get_hash():
    now = datetime.datetime.now()
    # x = int(input())
    x = now.year
    if now.month >= 9:
        x = x * 10 + 1
    else:
        x *= 10

    saved = x
    l = len(str(x))
    x = x * (10 ** (l * 2)) + int(str(x)[::-1]) * (10 ** l) + x
    x *= 1337

    hahs = creat_hash(x, 228)
    step = saved % 100 % 3
    ans = ""
    i = 0
    while hahs != 0:
        i += 1
        curr = hahs % 10
        if i == step:
            step += 1
            i = 0
            abc = hahs % 10
            hahs = hahs // 10
            ans += chr(ord('a') + (curr * 10 + abc) % 26)
        ans += str(curr)
        hahs = hahs // 10
    final = [item for item in ans]
    k = 1
    dist = saved % 100 // 10
    while k + dist < len(final):
        final[k], final[k + dist] = final[k + dist], final[k]
        k += 1
    ans = ''
    for item in final:
        ans += item
    return ans


class Authorization(QMainWindow):
    """Класс окна авторизации"""

    def __init__(self):
        super().__init__()
        self.ui = authorization.Ui_authorization_window()
        self.ui.setupUi(self)

        # connects
        self.ui.pushButton.clicked.connect(self.start_start_window)

        # constants
        self.start_window = start_window.Start_window()

    def start_start_window(self):
        text = str(self.ui.lineEdit.text())
        if text == get_hash():
            self.start_window.show()
            window.close()
            return
        self.ui.lineEdit.setText("")
        QMessageBox.warning(self, "Ошибка доступа", "Вы ввели неккоректный пароль.")

        # window.hide()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Authorization()
    window.show()
    app.exec_()

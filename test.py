# _*_ coding : utf-8 _*_
# @Time : 2022/8/5 20:20
# @Author : 浙工大曾友
# @File : test
# @Project : pythonProject

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from detectApp import Detect_App


class MyMainForm(QMainWindow, Detect_App):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.setWindowTitle("图像检索")
    myWin.setWindowIcon(QtGui.QIcon("./cache/title.jpeg"))
    myWin.show()
    sys.exit(app.exec_())

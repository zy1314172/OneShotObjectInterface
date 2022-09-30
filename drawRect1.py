# _*_ coding : utf-8 _*_
# @Time : 2022/8/10 19:27
# @Author : 浙工大曾友
# @File : drawRect
# @Project : pythonProject

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(30, 30, 600, 400)
        self.pos1 = [0, 0]
        self.pos2 = [0, 0]
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        # self.show()

    def paintEvent(self, event):
        width = self.pos2[0] - self.pos1[0]
        height = self.pos2[1] - self.pos1[1]
        qp = QtGui.QPainter(self)
        br = QtGui.QBrush(QtGui.QColor(100, 10, 10, 40))
        qp.setBrush(br)
        qp.drawRect(self.pos1[0], self.pos1[1], width, height)
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.pos1[0], self.pos1[1] = event.pos().x(), event.pos().y()
        self.update()

    def mouseMoveEvent(self, event):
        self.pos2[0], self.pos2[1] = event.pos().x(), event.pos().y()
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.pos2[0], self.pos2[1] = event.pos().x(), event.pos().y()
        self.begin = event.pos()
        self.end = event.pos()
        self.update()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())

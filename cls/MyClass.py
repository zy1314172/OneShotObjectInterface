# _*_ coding : utf-8 _*_
# @Time : 2022/9/26 14:16
# @Author : 浙工大曾友
# @File : MyClass
# @Project : pythonProject

from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPainter, QPen, QPixmap, QImage
from PyQt5.QtCore import Qt, QRect


class MyBigQLabel(QLabel):
    def __init__(self, parent=None):
        super(MyBigQLabel, self).__init__(parent)
        self.x0 = 0
        self.y0 = 0
        self.x1 = 0
        self.y1 = 0
        self.flag = False
        self.move = False  # 存在移动

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        # barHeight = self.bar.height()
        self.move = True
        if self.flag:
            self.x1 = event.pos().x()
            self.y1 = event.pos().y()
            if self.x1 > self.width():
                self.x1 = self.width()
            if self.y1 > self.height():
                self.y1 = self.height()
            self.update()

    # 鼠标释放事件
    def mouseReleaseEvent(self, event):
        # self.flag = False
        self.move = False
        # print(self.x0, self.y0, self.x1, self.y1)
        # self.x0, self.y0, self.x1, self.y1 = (0, 0, 0, 0)
        # print(self.x0, self.y0, self.x1, self.y1)

    # 绘制事件
    def paintEvent(self, event):
        super().paintEvent(event)
        if self.flag and self.move:  # 只有当鼠标按下并且移动状态
            rect = QRect(self.x0, self.y0, abs(self.x1 - self.x0), abs(self.y1 - self.y0))
            painter = QPainter(self)
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            painter.drawRect(rect)
        # print(self.x0, self.y0, self.x1, self.y1)

    # 单击鼠标触发事件
    def mousePressEvent(self, event):
        # barHeight = self.bar.height()
        if self.flag:
            self.x0 = event.pos().x()
            self.y0 = event.pos().y()

    def startDraw(self):
        self.flag = True
        self.setCursor(Qt.CrossCursor)

    def endDraw(self):
        self.flag = False
        self.setCursor(Qt.ArrowCursor)



class MyQLabel(QLabel):
    # 自定义信号, 注意信号必须为类属性
    button_clicked_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(MyQLabel, self).__init__(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        self.button_clicked_signal.emit()

    # 可在外部与槽函数连接
    def connect_customized_slot(self, func):
        self.button_clicked_signal.connect(func)

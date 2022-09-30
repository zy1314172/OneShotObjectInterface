# _*_ coding : utf-8 _*_
# @Time : 2022/8/9 19:49
# @Author : 浙工大曾友
# @File : photo_view
# @Project : pythonProject

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QPainter, QColor, QFont, QImage, QPen
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, \
    QDesktopWidget, QHBoxLayout, QLabel


class MyQGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(MyQGraphicsScene, self).__init__(parent)
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
            self.update()

    # 鼠标释放事件
    def mouseReleaseEvent(self, event):
        self.flag = False
        self.move = False
        print(self.x0, self.y0, self.x1, self.y1)
        self.x0, self.y0, self.x1, self.y1 = (0, 0, 0, 0)
        print(self.x0, self.y0, self.x1, self.y1)

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
        self.x0 = event.pos().x()
        self.y0 = event.pos().y()
        self.flag = True

class MyQLabel(QtWidgets.QLabel):
    # 自定义信号, 注意信号必须为类属性
    button_clicked_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(MyQLabel, self).__init__(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        self.button_clicked_signal.emit()

    # 可在外部与槽函数连接
    def connect_customized_slot(self, func):
        self.button_clicked_signal.connect(func)


class Ui_Detect_App(object):
    def setupUi(self, DetectApp):
        DetectApp.setObjectName("Detect_App")
        DetectApp.resize(890, 682)

        self.centralwidget = QtWidgets.QWidget(DetectApp)
        self.centralwidget.setObjectName("centralwidget")
        self.bigPic = QGraphicsView(self)
        self.bigPic.setCursor(Qt.CrossCursor)
        self.bigPic.setGeometry(0, 0, 750, 550)
        self.select_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_button.setGeometry(QtCore.QRect(760, 140, 75, 23))
        self.select_button.setCheckable(True)
        self.select_button.setObjectName("select_button")
        self.prev_img = QtWidgets.QPushButton(self.centralwidget)
        self.prev_img.setGeometry(QtCore.QRect(760, 180, 75, 23))
        self.prev_img.setCheckable(True)
        self.prev_img.setObjectName("prev_img")
        self.next_img = QtWidgets.QPushButton(self.centralwidget)
        self.next_img.setGeometry(QtCore.QRect(760, 220, 75, 23))
        self.next_img.setCheckable(True)
        self.next_img.setObjectName("next_img")
        self.amplification_button = QtWidgets.QPushButton(self.centralwidget)
        self.amplification_button.setGeometry(QtCore.QRect(760, 260, 75, 23))
        self.amplification_button.setCheckable(True)
        self.amplification_button.setObjectName("amplification_button")
        self.narrow_button = QtWidgets.QPushButton(self.centralwidget)
        self.narrow_button.setGeometry(QtCore.QRect(760, 300, 75, 23))
        self.narrow_button.setCheckable(True)
        self.narrow_button.setObjectName("narrow_button")
        self.rect_button = QtWidgets.QPushButton(self.centralwidget)
        self.rect_button.setGeometry(QtCore.QRect(760, 340, 75, 23))
        self.rect_button.setCheckable(True)
        self.rect_button.setObjectName("rect_button")
        self.confirm_button = QtWidgets.QPushButton(self.centralwidget)
        self.confirm_button.setGeometry(QtCore.QRect(760, 380, 75, 23))
        self.confirm_button.setCheckable(True)
        self.confirm_button.setObjectName("confirm_button")
        self.label_1 = MyQLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(0, 580, 70, 70))
        self.label_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.label_2 = MyQLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 580, 70, 70))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = MyQLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 580, 70, 70))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = MyQLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 580, 70, 70))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = MyQLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 580, 70, 70))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = MyQLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 580, 70, 70))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = MyQLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(540, 580, 70, 70))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = MyQLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(630, 580, 70, 70))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_5")
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(720, 580, 23, 23))
        self.next_button.setCheckable(True)
        self.next_button.setObjectName("next_button")
        self.prev_button = QtWidgets.QPushButton(self.centralwidget)
        self.prev_button.setGeometry(QtCore.QRect(720, 627, 23, 23))
        self.prev_button.setCheckable(True)
        self.prev_button.setObjectName("prev_button")

        DetectApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DetectApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 23))
        self.menubar.setObjectName("menubar")
        DetectApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DetectApp)
        self.statusbar.setObjectName("statusbar")
        DetectApp.setStatusBar(self.statusbar)

        # self.rect = False
        # self.pos1 = [0, 0]
        # self.pos2 = [0, 0]
        # self.begin = QtCore.QPoint()
        # self.end = QtCore.QPoint()
        # self.rect_button.clicked.connect(self.controlRect)
        # self.confirm_button.clicked.connect(self.confirmRect)

        self.zoomscale = 1
        self.next_button.setVisible(False)
        self.prev_button.setVisible(False)
        self.next_img.setEnabled(False)
        self.prev_img.setEnabled(False)
        self.amplification_button.setEnabled(False)
        self.narrow_button.setEnabled(False)
        self.select_button.clicked.connect(self.openFile)
        self.prev_img.clicked.connect(self.prevImg)
        self.next_img.clicked.connect(self.nextImg)
        self.next_button.clicked.connect(self.nextPage)
        self.prev_button.clicked.connect(self.prevPage)
        self.amplification_button.clicked.connect(self.amplification)
        self.narrow_button.clicked.connect(self.narrow)

        self.retranslateUi(DetectApp)
        QtCore.QMetaObject.connectSlotsByName(DetectApp)

    def retranslateUi(self, DetectApp):
        _translate = QtCore.QCoreApplication.translate
        DetectApp.setWindowTitle(_translate("DetectApp", "MainWindow"))
        self.select_button.setText(_translate("DetectApp", "选择文件"))
        self.prev_img.setText(_translate("DetectApp", "上一张"))
        self.next_img.setText(_translate("DetectApp", "下一张"))
        self.amplification_button.setText(_translate("DetectApp", "放大"))
        self.narrow_button.setText(_translate("DetectApp", "缩小"))
        self.rect_button.setText(_translate("DetectApp", "选框"))
        self.confirm_button.setText(_translate("DetectApp", "确定选框"))
        self.next_button.setText(_translate("DetectApp", "》"))
        self.prev_button.setText(_translate("DetectApp", "《"))

    # 打开文件
    def openFile(self):
        self.curIndex = 0
        self.curImg = 0
        self.picList = []
        picListInner = []
        i = 0
        cnt = 0

        paths, ok1 = QFileDialog.getOpenFileNames(self,
                                                  "选择需要的文件",
                                                  "./",
                                                  "Images (*.jpg *.png) *.jpeg")
        if not paths:
            QMessageBox.information(self, "提示", self.tr("没有选择图片文件！"))
            return 0
        picLength = len(paths)
        if picLength > 1:
            self.next_img.setEnabled(True)
        if picLength > 8:
            self.next_button.setVisible(True)
            self.prev_button.setVisible(True)
        if picLength % 8 == 0:
            self.maxGroup = picLength // 8 - 1
        else:
            self.maxGroup = picLength // 8

        for path in paths:
            picListInner.insert(cnt, path)
            cnt = cnt + 1
            if (cnt % 8 == 0):
                self.picList.insert(i, picListInner)
                picListInner = []
                cnt = 0
                i = i + 1
        self.picList.insert(i, picListInner)

        # 给图片标签添加单击切换图片事件
        self.label_1.connect_customized_slot(lambda: self.changePic(0))
        self.label_2.connect_customized_slot(lambda: self.changePic(1))
        self.label_3.connect_customized_slot(lambda: self.changePic(2))
        self.label_4.connect_customized_slot(lambda: self.changePic(3))
        self.label_5.connect_customized_slot(lambda: self.changePic(4))
        self.label_6.connect_customized_slot(lambda: self.changePic(5))
        self.label_7.connect_customized_slot(lambda: self.changePic(6))
        self.label_8.connect_customized_slot(lambda: self.changePic(7))

        self.controlAble()
        self.showSmallPic(self.curIndex)

    # 展示下面的小图片
    def showSmallPic(self, curIndex):
        jpg = QtGui.QPixmap('').scaled(60, 60)
        self.label_1.setPixmap(jpg)
        self.label_2.setPixmap(jpg)
        self.label_3.setPixmap(jpg)
        self.label_4.setPixmap(jpg)
        self.label_5.setPixmap(jpg)
        self.label_6.setPixmap(jpg)
        self.label_7.setPixmap(jpg)
        self.label_8.setPixmap(jpg)
        bigPicPath = self.picList[curIndex][self.curImg]
        self.showBigPic(bigPicPath)
        index = 1
        for path in self.picList[curIndex]:
            jpg = QtGui.QPixmap(path).scaled(70, 70)
            if index == 1:
                self.label_1.setPixmap(jpg)
            elif index == 2:
                self.label_2.setPixmap(jpg)
            elif index == 3:
                self.label_3.setPixmap(jpg)
            elif index == 4:
                self.label_4.setPixmap(jpg)
            elif index == 5:
                self.label_5.setPixmap(jpg)
            elif index == 6:
                self.label_6.setPixmap(jpg)
            elif index == 7:
                self.label_7.setPixmap(jpg)
            elif index == 8:
                self.label_8.setPixmap(jpg)
            index = index + 1

    # 展示大图
    def showBigPic(self, path):
        # imgs = cv2.imread(path)  # 读取图像
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
        # x = imgs.shape[1]  # 获取图像大小
        # y = imgs.shape[0]
        # self.zoomscale = 1  # 图片放缩尺度
        # frame = QImage(img, x, y, QImage.Format_RGB888)
        # pix = QPixmap.fromImage(frame)
        # img = QImage(path)
        # result = img.scaled(x, y, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        # pix = QPixmap(result)
        pix = QPixmap(path)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = MyQGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.bigPic.setScene(self.scene)
        self.bigPic.show()
        # self.bigPic.setPixmap(pix)

    # 跳转到下一页
    def nextPage(self):
        if (self.curIndex + 1) <= self.maxGroup:
            self.curIndex = self.curIndex + 1
            self.showSmallPic(self.curIndex)
        self.controlAble()

    # 跳转到上一页
    def prevPage(self):
        if (self.curIndex - 1) >= 0:
            self.curIndex = self.curIndex - 1
            self.showSmallPic(self.curIndex)
        self.controlAble()

    # 跳转到下一张
    def nextImg(self):
        self.curImg = self.curImg + 1
        self.controlChangePic()

        if 0 <= self.curImg <= 7:
            self.showBigPic(self.picList[self.curIndex][self.curImg])
        else:
            self.curImg = 0
            self.curIndex = self.curIndex + 1
            self.showBigPic(self.picList[self.curIndex][self.curImg])
            self.showSmallPic(self.curIndex)

    # 跳转到上一张
    def prevImg(self):
        self.curImg = self.curImg - 1
        self.controlChangePic()

        if 0 <= self.curImg <= 7:
            self.showBigPic(self.picList[self.curIndex][self.curImg])
        else:
            self.curImg = 7
            self.curIndex = self.curIndex - 1
            self.showBigPic(self.picList[self.curIndex][self.curImg])
            self.showSmallPic(self.curIndex)

    # 切换大图展示
    def changePic(self, idx):
        self.curImg = idx
        self.controlChangePic()

        bigPicPath = self.picList[self.curIndex]
        if bigPicPath[idx:]:
            self.showBigPic(bigPicPath[idx])

    # 控制图片切换过程中按钮是否可用
    def controlChangePic(self):
        if self.curImg == 0 and self.curIndex == 0:
            self.prev_img.setEnabled(False)
        else:
            self.prev_img.setEnabled(True)

        if self.curImg + 1 == len(self.picList[self.curIndex]) and self.curIndex == self.maxGroup:
            self.next_img.setEnabled(False)
        else:
            self.next_img.setEnabled(True)

        if self.curIndex == self.maxGroup:
            if self.curImg == len(self.picList[self.curIndex]):
                self.curImg = len(self.picList[self.curIndex]) - 1

        if self.curIndex == 0:
            if self.curImg < 0:
                self.curImg = 0

    # 放大图片
    def amplification(self):
        self.zoomscale = self.zoomscale + 0.05
        if self.zoomscale >= 1.2:
            self.zoomscale = 1.2
        self.item.setScale(self.zoomscale)

    # 缩小图片
    def narrow(self):
        self.zoomscale = self.zoomscale - 0.05
        if self.zoomscale <= 0.8:
            self.zoomscale = 0.8
        self.item.setScale(self.zoomscale)

    # 判断按钮是否可用
    def controlAble(self):
        self.next_button.setEnabled(True)
        self.prev_button.setEnabled(True)
        self.amplification_button.setEnabled(True)
        self.narrow_button.setEnabled(True)
        if self.curIndex == 0:
            self.prev_button.setEnabled(False)
        elif self.curIndex == self.maxGroup:
            self.next_button.setEnabled(False)

    # # 选框功能模块
    # def controlRect(self):
    #     self.rect = True
    #
    # def confirmRect(self):
    #     self.rect = False
    #
    # def paintEvent(self, event):
    #     width = self.pos2[0] - self.pos1[0]
    #     height = self.pos2[1] - self.pos1[1]
    #     qp = QtGui.QPainter(self)
    #     br = QtGui.QBrush(QtGui.QColor(100, 10, 10, 40))
    #     qp.setBrush(br)
    #     qp.drawRect(self.pos1[0], self.pos1[1], width, height)
    #     qp.drawRect(QtCore.QRect(self.begin, self.end))
    #
    # def mousePressEvent(self, event):
    #     if self.rect:
    #         self.begin = event.pos()
    #         self.end = event.pos()
    #         self.pos1[0], self.pos1[1] = event.pos().x(), event.pos().y()
    #         self.update()
    #
    # def mouseMoveEvent(self, event):
    #     if self.rect:
    #         self.pos2[0], self.pos2[1] = event.pos().x(), event.pos().y()
    #         self.end = event.pos()
    #         self.update()
    #
    # def mouseReleaseEvent(self, event):
    #     if self.rect:
    #         self.pos2[0], self.pos2[1] = event.pos().x(), event.pos().y()
    #         self.begin = event.pos()
    #         self.end = event.pos()
    #         self.update()

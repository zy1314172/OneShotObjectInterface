# _*_ coding : utf-8 _*_
# @Time : 2022/8/9 19:49
# @Author : 浙工大曾友
# @File : photo_view
# @Project : pythonProject

import os
from functools import partial
import time
from osgeo import gdal

from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from cls.MyClass import MyBigQLabel, MyQLabel


class Detect_App(object):
    def __init__(self):
        # 存放图片路径
        self.picList = []
        # 当前组的第几张
        self.curImg = 0
        # 第几组
        self.curIndex = 0
        # 每次展现多少张
        self.showNum = 5

    def setupUi(self, DetectApp):
        DetectApp.setObjectName("Detect_App")
        DetectApp.resize(900, 730)

        self.centralwidget = QtWidgets.QWidget(DetectApp)
        self.centralwidget.setObjectName("centralwidget")
        self.bigPic = MyBigQLabel(self)
        self.bigPic.setGeometry(0, 0, 800, 600)
        self.bigPic.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.select_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_button.setGeometry(QtCore.QRect(810, 140, 75, 23))
        self.select_button.setCheckable(True)
        self.select_button.setObjectName("select_button")
        self.prev_img = QtWidgets.QPushButton(self.centralwidget)
        self.prev_img.setGeometry(QtCore.QRect(810, 180, 75, 23))
        self.prev_img.setCheckable(True)
        self.prev_img.setObjectName("prev_img")
        self.next_img = QtWidgets.QPushButton(self.centralwidget)
        self.next_img.setGeometry(QtCore.QRect(810, 220, 75, 23))
        self.next_img.setCheckable(True)
        self.next_img.setObjectName("next_img")
        self.startDraw_button = QtWidgets.QPushButton(self.centralwidget)
        self.startDraw_button.setGeometry(QtCore.QRect(810, 260, 75, 23))
        self.startDraw_button.setCheckable(True)
        self.startDraw_button.setObjectName("startDraw_button")
        self.endDraw_button = QtWidgets.QPushButton(self.centralwidget)
        self.endDraw_button.setGeometry(QtCore.QRect(810, 300, 75, 23))
        self.endDraw_button.setCheckable(True)
        self.endDraw_button.setObjectName("narrow_button")
        self.startRecognize_button = QtWidgets.QPushButton(self.centralwidget)
        self.startRecognize_button.setGeometry(QtCore.QRect(810, 340, 75, 23))
        self.startRecognize_button.setCheckable(True)
        self.startRecognize_button.setObjectName("startRecognize_button")
        self.next_page = QtWidgets.QPushButton(self.centralwidget)
        self.next_page.setGeometry(QtCore.QRect(770, 620, 25, 25))
        self.next_page.setCheckable(True)
        self.next_page.setObjectName("next_page")
        self.prev_page = QtWidgets.QPushButton(self.centralwidget)
        self.prev_page.setGeometry(QtCore.QRect(770, 677, 25, 25))
        self.prev_page.setCheckable(True)
        self.prev_page.setObjectName("prev_page")
        self.label_1 = MyQLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(0, 620, 100, 100))
        self.label_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.label_2 = MyQLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 620, 100, 100))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = MyQLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 620, 100, 100))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = MyQLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 620, 100, 100))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = MyQLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(600, 620, 100, 100))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        DetectApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DetectApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 23))
        self.menubar.setObjectName("menubar")
        DetectApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DetectApp)
        self.statusbar.setObjectName("statusbar")
        DetectApp.setStatusBar(self.statusbar)

        self.resetButtonStyle()
        self.select_button.clicked.connect(self.openFile)
        self.startDraw_button.clicked.connect(self.startDraw)
        self.endDraw_button.clicked.connect(self.endDraw)
        self.startRecognize_button.clicked.connect(self.startRecognize)
        self.prev_img.clicked.connect(self.prevImg)
        self.next_img.clicked.connect(self.nextImg)
        self.next_page.clicked.connect(self.nextPage)
        self.prev_page.clicked.connect(self.prevPage)

        self.retranslateUi(DetectApp)
        QtCore.QMetaObject.connectSlotsByName(DetectApp)

    def retranslateUi(self, DetectApp):
        _translate = QtCore.QCoreApplication.translate
        DetectApp.setWindowTitle(_translate("DetectApp", "MainWindow"))
        self.select_button.setText(_translate("DetectApp", "选择文件"))
        self.prev_img.setText(_translate("DetectApp", "上一张"))
        self.next_img.setText(_translate("DetectApp", "下一张"))
        self.startDraw_button.setText(_translate("DetectApp", "开始选框"))
        self.endDraw_button.setText(_translate("DetectApp", "确定选框"))
        self.startRecognize_button.setText(_translate("DetectApp", "开始识别"))
        self.next_page.setText(_translate("DetectApp", "》"))
        self.prev_page.setText(_translate("DetectApp", "《"))

    # 打开文件
    def openFile(self):
        try:
            directory = QFileDialog.getExistingDirectory(self, "选取文件夹")  # 起始路径
            print(directory)
            paths = list(self.get_image_paths(directory))
            if not paths:
                return
        except Exception:
            QMessageBox.information(self, "提示", self.tr("没有选择图片文件！"))
            return
        picListInner = []
        i = 0
        cnt = 0
        self.resetButtonStyle()
        picLength = len(paths)
        self.controlButtonStyle(picLength)
        if picLength % 5 == 0:
            self.maxGroup = picLength // self.showNum - 1
        else:
            self.maxGroup = picLength // self.showNum

        for path in paths:
            picListInner.insert(cnt, path)
            cnt = cnt + 1
            if cnt % self.showNum == 0:
                self.picList.insert(i, picListInner)
                picListInner = []
                cnt = 0
                i = i + 1
        self.picList.insert(i, picListInner)

        # 给图片标签添加单击切换图片事件
        for i in range(self.showNum):
            label = eval("self.label_" + str(i+1))
            label.connect_customized_slot(partial(self.changePic, i))
        self.showSmallPic()

    # 获取图片的路径
    def get_image_paths(self, directory):
        img_prefix = ['png', 'jpg', 'jpeg', 'bmp', 'tif', 'gif', 'pcx', 'tga', 'exif', 'fpx', 'svg', 'psd', 'cdr',
                      'pcd', 'dxf', 'ufo', 'eps', 'ai', 'raw', 'wmf', 'webp', 'avif', 'apng']

        return (os.path.join(directory, f)
                for f in os.listdir(directory)
                if f.split('.')[-1].lower() in img_prefix)

    # 展示下面的小图片
    def showSmallPic(self):
        jpg = QtGui.QPixmap('').scaled(80, 80)
        for i in range(self.showNum):
            label = eval("self.label_" + str(i+1))
            label.setPixmap(jpg)
            label.setEnabled(True)

        bigPicPath = self.picList[self.curIndex][self.curImg]
        self.showBigPic(bigPicPath)

        index = 1
        for path in self.picList[self.curIndex]:
            t = time.time()
            jpg = QtGui.QPixmap(path).scaled(100, 100)
            data = gdal.Open(path)
            print(jpg)
            print(data)
            print(time.time() - t)
            if index <= len(self.picList[self.curIndex]):
                label = eval("self.label_" + str(index))
                label.setPixmap(jpg)
            index = index + 1
            for i in range(len(self.picList[self.curIndex]) + 1, self.showNum + 1):
                label = eval("self.label_" + str(i))
                label.setEnabled(False)

    # 展示大图
    def showBigPic(self, path):
        pix = QPixmap(path).scaled(800, 600, Qt.KeepAspectRatio)
        self.bigPic.setPixmap(pix)

    # 跳转到下一页
    def nextPage(self):
        if (self.curIndex + 1) <= self.maxGroup:
            self.curIndex = self.curIndex + 1
            self.curImg = 0
            self.showSmallPic()
        self.controlButtonStyle()

    # 跳转到上一页
    def prevPage(self):
        if (self.curIndex - 1) >= 0:
            self.curIndex = self.curIndex - 1
            self.curImg = 0
            self.showSmallPic()
        self.controlButtonStyle()

    # 跳转到下一张
    def nextImg(self):
        self.curImg = self.curImg + 1
        self.controlChangePic()

        if 0 <= self.curImg < self.showNum:
            self.showBigPic(self.picList[self.curIndex][self.curImg])
        else:
            self.curImg = 0
            self.curIndex = self.curIndex + 1
            self.showBigPic(self.picList[self.curIndex][self.curImg])
            self.showSmallPic()

    # 跳转到上一张
    def prevImg(self):
        self.curImg = self.curImg - 1
        self.controlChangePic()

        if 0 <= self.curImg < self.showNum:
            self.showBigPic(self.picList[self.curIndex][self.curImg])
        else:
            self.curImg = 4
            self.curIndex = self.curIndex - 1
            self.showBigPic(self.picList[self.curIndex][self.curImg])
            self.showSmallPic()

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

    # 重置按钮的状态
    def resetButtonStyle(self):
        self.next_page.setVisible(False)
        self.prev_page.setVisible(False)
        self.next_img.setEnabled(False)
        self.prev_img.setEnabled(False)
        self.startDraw_button.setEnabled(False)
        self.endDraw_button.setEnabled(False)
        self.startRecognize_button.setEnabled(False)

    # 判断按钮是否可用
    def controlButtonStyle(self, picLength=10):
        self.next_page.setEnabled(True)
        self.prev_page.setEnabled(True)
        self.startDraw_button.setEnabled(True)
        self.endDraw_button.setEnabled(True)
        self.startRecognize_button.setEnabled(True)
        if self.curIndex == 0:
            self.prev_page.setEnabled(False)
        elif self.curIndex == self.maxGroup:
            self.next_page.setEnabled(False)

        if picLength > 1:
            self.next_img.setEnabled(True)
        if picLength > self.showNum:
            self.next_page.setVisible(True)
            self.prev_page.setVisible(True)

    # 选框功能模块
    def startDraw(self):
        self.bigPic.startDraw()

    def endDraw(self):
        self.bigPic.endDraw()

    # 识别模块
    def startRecognize(self):
        try:
            pix = QPixmap(self.picList[self.curIndex][self.curImg]).scaled(800, 600, Qt.KeepAspectRatio)
            im = Image.open(self.picList[self.curIndex][self.curImg])
            if pix.width() == 800:
                beishu = im.width / 800
                widthOne = self.bigPic.x0 * beishu
                widthTwo = self.bigPic.x1 * beishu
                heightOne = (self.bigPic.y0 - (600-pix.height())/2) * beishu
                heightTwo = (self.bigPic.y1 - (600-pix.height())/2) * beishu
            else:
                beishu = im.height / 600
                widthOne = self.bigPic.x0 * beishu
                widthTwo = self.bigPic.x1 * beishu
                heightOne = self.bigPic.y0 * beishu
                heightTwo = self.bigPic.y1 * beishu
            print(int(widthOne), int(heightOne), int(widthTwo), int(heightTwo))
            region = im.crop((int(widthOne), int(heightOne), int(widthTwo), int(heightTwo)))
            region.save("./cache/cropDetect.jpg")
            print(self.bigPic.x0, self.bigPic.y0, self.bigPic.x1, self.bigPic.y1)

        except Exception:
            QMessageBox.information(self, "提示", self.tr("您还未框选任何的区域！"))
            return 0


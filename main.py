import os
import sys
import time

from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

from actions import ImageViewer
from cls.MyClass import MyBigQLabel
from PyQt5.QtGui import QMovie

# import test_custom

VALID_FORMAT = ('.BMP', '.GIF', '.JPG', '.JPEG', '.PNG', '.PBM', '.PGM', '.PPM', '.TIFF', '.XBM', 'TIF')


def getImages(folder):
    image_list = []
    if os.path.isdir(folder):
        for file in os.listdir(folder):
            if file.upper().endswith(VALID_FORMAT):
                im_path = os.path.join(folder, file)
                image_obj = {'name': file, 'path': im_path}
                image_list.append(image_obj)
    return image_list


def del_file(path_data):
    for i in os.listdir(path_data):
        file_data = path_data + "\\" + i
        if os.path.isfile(file_data) == True:
            os.remove(file_data)
        else:
            del_file(file_data)


class Iwindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.cntr, self.numImages = -1, -1
        self.flag = False

        self.image_viewer = ImageViewer(self.qlabel_image)
        self.__connectEvents()
        self.initConnect()
        self.showNormal()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/compute/.designer/backup/icons/Icon.ico"), QtGui.QIcon.Normal,QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toggle_rect = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggle_rect.sizePolicy().hasHeightForWidth())
        self.toggle_rect.setSizePolicy(sizePolicy)
        self.toggle_rect.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toggle_rect.setStyleSheet("border-radius:5px;border: 2px groove gray;border-style: outset;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/rectangle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toggle_rect.setIcon(icon1)
        self.toggle_rect.setIconSize(QtCore.QSize(20, 20))
        self.toggle_rect.setCheckable(False)
        self.toggle_rect.setObjectName("toggle_rect")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.toggle_rect)
        self.horizontalLayout_3.addWidget(self.toggle_rect)
        self.move_pic = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.move_pic.sizePolicy().hasHeightForWidth())
        self.move_pic.setSizePolicy(sizePolicy)
        self.move_pic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.move_pic.setStyleSheet("border-radius:5px;border: 2px groove gray;border-style: outset;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/move.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.move_pic.setIcon(icon2)
        self.move_pic.setIconSize(QtCore.QSize(20, 20))
        self.move_pic.setCheckable(False)
        self.move_pic.setObjectName("move_pic")
        self.buttonGroup.addButton(self.move_pic)
        self.horizontalLayout_3.addWidget(self.move_pic)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup.addButton(self.radioButton)
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
        self.radioButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup.addButton(self.radioButton_3)
        self.horizontalLayout_3.addWidget(self.radioButton_3)
        self.start_recognize = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_recognize.sizePolicy().hasHeightForWidth())
        self.start_recognize.setSizePolicy(sizePolicy)
        self.start_recognize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_recognize.setAutoFillBackground(False)
        self.start_recognize.setStyleSheet("border-radius:5px;border: 2px groove gray;border-style: outset;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/big.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_recognize.setIcon(icon3)
        self.start_recognize.setIconSize(QtCore.QSize(20, 20))
        self.start_recognize.setCheckable(False)
        self.start_recognize.setChecked(False)
        self.start_recognize.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.start_recognize.setAutoRaise(False)
        self.start_recognize.setObjectName("start_recognize")
        self.buttonGroup.addButton(self.start_recognize)
        self.horizontalLayout_3.addWidget(self.start_recognize)
        self.clear_all = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_all.sizePolicy().hasHeightForWidth())
        self.clear_all.setSizePolicy(sizePolicy)
        self.clear_all.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_all.setStyleSheet("border-radius:5px;border: 2px groove gray;border-style: outset;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/loop2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_all.setIcon(icon4)
        self.clear_all.setIconSize(QtCore.QSize(20, 20))
        self.clear_all.setObjectName("clear_all")
        self.horizontalLayout_3.addWidget(self.clear_all)
        self.prev_im = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev_im.sizePolicy().hasHeightForWidth())
        self.prev_im.setSizePolicy(sizePolicy)
        self.prev_im.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prev_im.setStyleSheet("border-radius:5px;border: 2px groove gray;border-style: outset;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/arrow-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prev_im.setIcon(icon5)
        self.prev_im.setIconSize(QtCore.QSize(20, 20))
        self.prev_im.setObjectName("prev_im")
        self.horizontalLayout_3.addWidget(self.prev_im)
        self.next_im = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_im.sizePolicy().hasHeightForWidth())
        self.next_im.setSizePolicy(sizePolicy)
        self.next_im.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next_im.setStyleSheet("border-radius:5px;border: 2px groove gray;border-style: outset;")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/arrow-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_im.setIcon(icon6)
        self.next_im.setIconSize(QtCore.QSize(20, 20))
        self.next_im.setObjectName("next_im")
        self.horizontalLayout_3.addWidget(self.next_im)
        self.zoom_plus = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoom_plus.sizePolicy().hasHeightForWidth())
        self.zoom_plus.setSizePolicy(sizePolicy)
        self.zoom_plus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zoom_plus.setStyleSheet("border-radius:5px;border: 2px groove gray;border-style: outset;")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/zoom_minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_plus.setIcon(icon7)
        self.zoom_plus.setIconSize(QtCore.QSize(20, 20))
        self.zoom_plus.setObjectName("zoom_plus")
        self.horizontalLayout_3.addWidget(self.zoom_plus)
        self.reset_zoom = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset_zoom.sizePolicy().hasHeightForWidth())
        self.reset_zoom.setSizePolicy(sizePolicy)
        self.reset_zoom.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset_zoom.setStyleSheet("border-radius:5px;border: 2px groove gray;border-style: outset;")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/enlarge2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_zoom.setIcon(icon8)
        self.reset_zoom.setIconSize(QtCore.QSize(20, 20))
        self.reset_zoom.setObjectName("reset_zoom")
        self.horizontalLayout_3.addWidget(self.reset_zoom)
        self.zoom_minus = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoom_minus.sizePolicy().hasHeightForWidth())
        self.zoom_minus.setSizePolicy(sizePolicy)
        self.zoom_minus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zoom_minus.setStyleSheet("border-radius:5px;border: 2px groove gray;border-style: outset;")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/zoom_plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_minus.setIcon(icon9)
        self.zoom_minus.setIconSize(QtCore.QSize(20, 20))
        self.zoom_minus.setObjectName("zoom_minus")
        self.horizontalLayout_3.addWidget(self.zoom_minus)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.qlabel_image = MyBigQLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qlabel_image.sizePolicy().hasHeightForWidth())
        self.qlabel_image.setSizePolicy(sizePolicy)
        self.qlabel_image.setStyleSheet("")
        self.qlabel_image.setFrameShape(QtWidgets.QFrame.Box)
        self.qlabel_image.setFrameShadow(QtWidgets.QFrame.Plain)
        self.qlabel_image.setLineWidth(1)
        self.qlabel_image.setMidLineWidth(0)
        self.qlabel_image.setText("")
        self.qlabel_image.setObjectName("qlabel_image")
        self.horizontalLayout_2.addWidget(self.qlabel_image)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(3, 12)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.open_folder = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.open_folder.setFont(font)
        self.open_folder.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.open_folder.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.open_folder.setAutoFillBackground(False)
        self.open_folder.setStyleSheet("background-color: black;padding:10px;color:white;")
        self.open_folder.setAutoDefault(False)
        self.open_folder.setDefault(False)
        self.open_folder.setFlat(False)
        self.open_folder.setObjectName("open_folder")
        self.verticalLayout_10.addWidget(self.open_folder)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.origin_pic = QtWidgets.QPushButton(self.centralwidget)
        self.origin_pic.setObjectName("origin_pic")
        self.horizontalLayout_4.addWidget(self.origin_pic)
        self.target_pic = QtWidgets.QPushButton(self.centralwidget)
        self.target_pic.setObjectName("target_pic")
        self.horizontalLayout_4.addWidget(self.target_pic)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("background-color:white")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setLineWidth(1)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setIndent(-1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_10.addWidget(self.label_4)
        self.qlist_images = QtWidgets.QListWidget(self.centralwidget)
        self.qlist_images.setStyleSheet("background-color:white")
        self.qlist_images.setFrameShape(QtWidgets.QFrame.Box)
        self.qlist_images.setFrameShadow(QtWidgets.QFrame.Plain)
        self.qlist_images.setLayoutMode(QtWidgets.QListView.Batched)
        self.qlist_images.setBatchSize(20)
        self.qlist_images.setObjectName("qlist_images")
        self.verticalLayout_10.addWidget(self.qlist_images)
        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(2, 3)
        self.verticalLayout_10.setStretch(3, 48)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.horizontalLayout.setStretch(0, 48)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 968, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图像检索"))
        self.toggle_rect.setToolTip(_translate("MainWindow", "Mark rectangular surface"))
        self.toggle_rect.setText(_translate("MainWindow", "选框"))
        self.move_pic.setToolTip(_translate("MainWindow", "Move Pic"))
        self.move_pic.setText(_translate("MainWindow", "移动"))
        self.start_recognize.setToolTip(_translate("MainWindow", "Start Recognize"))
        self.start_recognize.setText(_translate("MainWindow", "识别"))
        self.clear_all.setToolTip(_translate("MainWindow", "Clear All"))
        self.clear_all.setText(_translate("MainWindow", "清空"))
        self.prev_im.setToolTip(_translate("MainWindow", "Load Previous Image"))
        self.prev_im.setText(_translate("MainWindow", "上一张"))
        self.next_im.setToolTip(_translate("MainWindow", "Load Next Image"))
        self.next_im.setText(_translate("MainWindow", "下一张"))
        self.zoom_plus.setText(_translate("MainWindow", "+"))
        self.zoom_plus.setToolTip(_translate("MainWindow", "zoom plus"))
        self.reset_zoom.setToolTip(_translate("MainWindow", "Fit Image to Canvas"))
        self.reset_zoom.setText(_translate("MainWindow", "重置"))
        self.zoom_minus.setText(_translate("MainWindow", "-"))
        self.zoom_minus.setToolTip(_translate("MainWindow", "zoom minus"))
        self.open_folder.setText(_translate("MainWindow", "Open Folder"))
        self.origin_pic.setText(_translate("MainWindow", "Origin Pic"))
        self.target_pic.setText(_translate("MainWindow", "Target Pic"))
        self.label_4.setText(_translate("MainWindow", "List of Images"))
        self.radioButton.setText(_translate("MainWindow", "model1"))
        self.radioButton_2.setText(_translate("MainWindow", "model2"))
        self.radioButton_3.setText(_translate("MainWindow", "model3"))

    def __connectEvents(self):
        self.open_folder.clicked.connect(self.openFile)
        self.next_im.clicked.connect(self.nextImg)
        self.prev_im.clicked.connect(self.prevImg)
        self.clear_all.clicked.connect(self.clearAll)
        self.qlist_images.itemClicked.connect(self.item_click)

        self.zoom_plus.clicked.connect(self.zoomPlus)
        self.reset_zoom.clicked.connect(self.resetZoom)
        self.zoom_minus.clicked.connect(self.zoomMinus)

        self.toggle_rect.clicked.connect(self.markRect)
        self.move_pic.clicked.connect(self.movePic)
        self.start_recognize.clicked.connect(self.startRecognize)

        self.origin_pic.clicked.connect(self.originPic)
        self.target_pic.clicked.connect(self.targetPic)

    def openFile(self):
        self.folder = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.originFolder = self.folder
        if not self.folder:
            QtWidgets.QMessageBox.warning(self, 'No Folder Selected', 'Please select a valid Folder')
            return
        self.flag = False
        self.selectDir()

    def selectDir(self):
        self.logs = getImages(self.folder)
        if not self.logs:
            QtWidgets.QMessageBox.warning(self, 'No Folder Selected', 'Please select a valid Folder')
            return
        self.numImages = len(self.logs)

        self.qlist_images.clear()
        self.items = [QtWidgets.QListWidgetItem(log['name']) for log in self.logs]
        for item in self.items:
            self.qlist_images.addItem(item)

        self.cntr = 0
        self.image_viewer.enablePan(True)
        self.image_viewer.loadImage(self.logs[self.cntr]['path'])
        self.items[self.cntr].setSelected(True)
        # self.qlist_images.setItemSelected(self.items[self.cntr], True)

        if self.numImages > 1:
            self.next_im.setEnabled(True)

    def resizeEvent(self, evt):
        if self.cntr >= 0:
            self.image_viewer.onResize()

    def nextImg(self):
        if self.cntr < self.numImages - 1:
            self.cntr += 1
            self.image_viewer.loadImage(self.logs[self.cntr]['path'])
            self.items[self.cntr].setSelected(True)
            # self.qlist_images.setItemSelected(self.items[self.cntr], True)
        else:
            QtWidgets.QMessageBox.warning(self, 'Sorry', 'No more Images!')

    def prevImg(self):
        if self.cntr > 0:
            self.cntr -= 1
            self.image_viewer.loadImage(self.logs[self.cntr]['path'])
            self.items[self.cntr].setSelected(True)
            # self.qlist_images.setItemSelected(self.items[self.cntr], True)
        else:
            QtWidgets.QMessageBox.warning(self, 'Sorry', 'No previous Image!')

    def item_click(self, item):
        self.cntr = self.items.index(item)
        self.image_viewer.loadImage(self.logs[self.cntr]['path'])

    def markRect(self):
        self.image_viewer.enablePan(False)
        self.qlabel_image.startDraw()
        self.initConnect()

    def movePic(self):
        self.qlabel_image.endDraw()
        self.qlabel_image.setCursor(QtCore.Qt.OpenHandCursor)
        self.image_viewer.enablePan(True)
        self.initConnect()

    def startRecognize(self):
        self.qlabel_image.endDraw()
        # if self.radioButton.isChecked():
        #     model = 1
        # elif self.radioButton_2.isChecked():
        #     model = 2
        # elif self.radioButton_3.isChecked():
        #     model = 3
        # else:
        #     QMessageBox.information(self, "提示", self.tr("请选择模型！"))
        try:
            im = Image.open(self.logs[self.cntr]['path'])
            scale = im.width / im.height - self.qlabel_image.width() / self.qlabel_image.height()
            if scale > 0:
                beishu = im.width / (self.qlabel_image.width() * self.image_viewer.zoomX)
            else:
                beishu = im.height / (self.qlabel_image.height() * self.image_viewer.zoomX)

            x, y = self.image_viewer.position
            widthOne = (self.qlabel_image.x0 + x) * beishu
            widthTwo = (self.qlabel_image.x1 + x) * beishu
            heightOne = (self.qlabel_image.y0 + y) * beishu
            heightTwo = (self.qlabel_image.y1 + y) * beishu
            region = im.crop((int(widthOne), int(heightOne), int(widthTwo), int(heightTwo)))
            region.save("./cache/cropDetect.jpg")
            self.flag = True
            self.qlabel_image.setAlignment(Qt.AlignCenter)
            gif = QMovie(r"icons/load.gif")
            self.qlabel_image.setMovie(gif)
            gif.start()


            # 跑模型
            # query_img_path = 'cache/cropDetect.jpg'
            # image_dir = self.folder
            # path_data = r"images_out"
            # del_file(path_data)
            # test_custom.main(query_img_path, image_dir)

            # self.targetPic()
        except Exception:
            QMessageBox.information(self, "提示", self.tr("您还未框选任何的区域！"))
            return 0

    def clearAll(self):
        self.cntr, self.numImages = -1, -1
        self.logs = []
        self.qlist_images.clear()
        self.qlabel_image.setPixmap(QPixmap(""))

    def initConnect(self):
        self.qlabel_image.mousePressEvent = self.image_viewer.mousePressAction
        self.qlabel_image.mouseMoveEvent = self.image_viewer.mouseMoveAction
        self.qlabel_image.mouseReleaseEvent = self.image_viewer.mouseReleaseAction
        self.qlabel_image.wheelEvent = self.image_viewer.wheel

    def zoomPlus(self):
        self.image_viewer.zoomPlus()
        self.movePic()

    def resetZoom(self):
        self.image_viewer.resetZoom()

    def zoomMinus(self):
        self.image_viewer.zoomMinus()

    def originPic(self):
        try:
            self.folder = self.originFolder
            self.selectDir()
        except Exception:
            return

    def targetPic(self):
        if self.flag:
            self.folder = r"images_out"
            self.selectDir()


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create("Cleanlooks"))
    app.setPalette(QtWidgets.QApplication.style().standardPalette())
    parentWindow = Iwindow(None)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

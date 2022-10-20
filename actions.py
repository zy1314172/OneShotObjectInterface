from PyQt5.QtGui import QImage, QPixmap, QPainter
from PyQt5 import QtCore, QtWidgets

class ImageViewer:
    def __init__(self, qlabel):
        self.qlabel_image = qlabel                            # widget/window name where image is displayed (I'm usiing qlabel)
        self.qimage_scaled = QImage()                         # scaled image to fit to the size of qlabel_image
        self.qpixmap = QPixmap()                              # qpixmap to fill the qlabel_image

        self.zoomX = 1              # zoom factor w.r.t size of qlabel_image
        self.position = [0, 0]      # position of top left corner of qimage_label w.r.t. qimage_scaled
        self.panFlag = False        # to enable or disable pan

        self.qlabel_image.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)

    def wheel(self, event):  # 鼠标滚轮事件
        try:
            if event.angleDelta().y() > 0:
                self.zoomPlus()
            else:
                self.zoomMinus()
        except Exception:
            return

    def mousePressAction(self, QMouseEvent):
        if self.panFlag:
            self.pressed = QMouseEvent.pos()  # starting point of drag vector
            self.anchor = self.position  # save the pan position when panning starts
        if self.qlabel_image.flag:
            self.qlabel_image.x0 = QMouseEvent.pos().x()
            self.qlabel_image.y0 = QMouseEvent.pos().y()
            self.qlabel_image.mousePressEvent = self.qlabel_image.mousePress

    def mouseMoveAction(self, QMouseEvent):
        if self.panFlag:
            if self.pressed:
                x, y = QMouseEvent.pos().x(), QMouseEvent.pos().y()
                dx, dy = x - self.pressed.x(), y - self.pressed.y()  # calculate the drag vector
                self.position = self.anchor[0] - dx, self.anchor[1] - dy  # update pan position using drag vector
                self.update()  # show the image with udated pan position
        if self.qlabel_image.flag:
            self.qlabel_image.mouseMoveEvent = self.qlabel_image.mouseMove

    def mouseReleaseAction(self, QMouseEvent):
        if self.panFlag:
            self.pressed = None
        if self.qlabel_image.flag:
            self.qlabel_image.mouseReleaseEvent = self.qlabel_image.mouseRelease


    def onResize(self):
        self.qpixmap = QPixmap(self.qlabel_image.size())
        self.qpixmap.fill(QtCore.Qt.gray)
        self.qimage_scaled = self.qimage.scaled(self.qlabel_image.width() * self.zoomX, self.qlabel_image.height() * self.zoomX, QtCore.Qt.KeepAspectRatio)
        self.update()

    def loadImage(self, imagePath):
        self.qimage = QImage(imagePath)
        self.qpixmap = QPixmap(self.qlabel_image.size())
        if not self.qimage.isNull():
            # reset Zoom factor and Pan position
            self.zoomX = 1
            self.position = [0, 0]
            self.qimage_scaled = self.qimage.scaled(self.qlabel_image.width(), self.qlabel_image.height(), QtCore.Qt.KeepAspectRatio)
            self.update()
        else:
            self.statusbar.showMessage('Cannot open this image! Try another one.', 5000)

    def update(self):
        if not self.qimage_scaled.isNull():
            # check if position is within limits to prevent unbounded panning.
            px, py = self.position
            px = px if (px <= self.qimage_scaled.width() - self.qlabel_image.width()) else (self.qimage_scaled.width() - self.qlabel_image.width())
            py = py if (py <= self.qimage_scaled.height() - self.qlabel_image.height()) else (self.qimage_scaled.height() - self.qlabel_image.height())
            px = px if (px >= 0) else 0
            py = py if (py >= 0) else 0
            self.position = (px, py)

            if self.zoomX == 1:
                self.qpixmap.fill(QtCore.Qt.white)

            # the act of painting the qpixamp
            painter = QPainter()
            painter.begin(self.qpixmap)
            painter.drawImage(QtCore.QPoint(0, 0), self.qimage_scaled,
                    QtCore.QRect(self.position[0], self.position[1], self.qlabel_image.width(), self.qlabel_image.height()) )
            painter.end()

            self.qlabel_image.setPixmap(self.qpixmap)
        else:
            pass                                          # clear the starting point of drag vector


    def zoomPlus(self):
        self.zoomX = self.zoomX + 1
        px, py = self.position
        px = px + int(self.qlabel_image.width()/2)
        py = py + int(self.qlabel_image.height()/2)
        self.position = (px, py)
        self.qimage_scaled = self.qimage.scaled(self.qlabel_image.width() * self.zoomX, self.qlabel_image.height() * self.zoomX, QtCore.Qt.KeepAspectRatio)
        self.update()

    def zoomMinus(self):
        if self.zoomX > 1:
            self.zoomX = self.zoomX - 1
            px, py = self.position
            px -= int(self.qlabel_image.width()/2)
            py -= int(self.qlabel_image.height()/2)
            self.position = (px, py)
            self.qimage_scaled = self.qimage.scaled(self.qlabel_image.width() * self.zoomX, self.qlabel_image.height() * self.zoomX, QtCore.Qt.KeepAspectRatio)
            self.update()

    def resetZoom(self):
        self.zoomX = 1
        self.position = [0, 0]
        self.qimage_scaled = self.qimage.scaled(self.qlabel_image.width() * self.zoomX, self.qlabel_image.height() * self.zoomX, QtCore.Qt.KeepAspectRatio)
        self.update()

    def enablePan(self, value):
        self.panFlag = value

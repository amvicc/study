import sys
import cv2
import numpy as np

import MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Window(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)

        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        self.actionOpen.triggered.connect(self.openPicture)
        self.actionSave.triggered.connect(self.savePicture)
        self.actionExit.triggered.connect(self.exit)

        # self.actionResize.triggered.connect(self.resize)
        self.actionRotate.triggered.connect(self.rotate)

    def openPicture(self):

        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open picture')
        img = cv2.imread(filename[0])
        # cv2.imshow("Image", img)
        self.addPictureToScene(img)

    def addPictureToScene(self, cvImage):
        self.scene.clear()

        height, width, channel = cvImage.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(cvImage.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        pixMap = QtGui.QPixmap.fromImage(qImg)
        self.scene.addPixmap(pixMap)
        self.graphicsView.fitInView(QtCore.QRectF(0, 0, width, height), QtCore.Qt.KeepAspectRatio)
        self.scene.update()

    def savePicture(self):
        image = self.graphicsView.grab().toImage()
        filepath = QtWidgets.QFileDialog.getSaveFileName(self, "Save path")
        image.save(filepath[0], "PNG")

    def exit(self):
        self.close()

    def rotate(self):
        img = self.graphicsView.grab().toImage()
        cvImg = self.convertQImageToMat(img)
        rotated = self.rotate_bound(cvImg, 90)
        self.addPictureToScene(rotated)

    def rotate_bound(self, image, angle):
        (h, w) = image.shape[:2]
        (cX, cY) = (w // 2, h // 2)

        M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1])

        nW = int((h * sin) + (w * cos))
        nH = int((h * cos) + (w * sin))

        M[0, 2] += (nW / 2) - cX
        M[1, 2] += (nH / 2) - cY

        return cv2.warpAffine(image, M, (nW, nH))

    def convertQImageToMat(self, image):
        '''  Converts a QImage into an opencv MAT format  '''

        cvImage = np.array(image.height, image.width, image.bits, image.byteCount)

        return cvImage
        # ptr = image.bits()
        # ptr.setsize(image.byteCount())
        # arr = np.asarray(ptr).reshape(image.height(), image.width(), 4)
        # return arr


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Window()
    mainWindow.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

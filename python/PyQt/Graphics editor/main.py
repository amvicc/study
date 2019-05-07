import sys
import cv2
import numpy as np
import MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Window(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)

        self.image = None

        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        self.actionOpen.triggered.connect(self.open_picture)
        self.actionSave.triggered.connect(self.save_picture)
        self.actionExit.triggered.connect(self.exit)

        self.actionRotate.triggered.connect(self.rotate)

        self.actionBlur.triggered.connect(self.blurFilter)
        self.actionLighter.triggered.connect(self.lighterFilter)
        self.actionDarker.triggered.connect(self.darkerFilter)
        self.actionSobel_operator.triggered.connect(self.sobel)

    def open_picture(self):

        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open picture')
        self.image = cv2.imread(filename[0])
        self.update_scene()

    def update_scene(self):
        self.scene.clear()
        height, width, channel = self.image.shape
        bytesPerLine = 3 * width
        qImg = QtGui.QImage(self.image.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        pixMap = QtGui.QPixmap.fromImage(qImg)
        self.scene.addPixmap(pixMap)
        self.graphicsView.fitInView(QtCore.QRectF(0, 0, width, height), QtCore.Qt.KeepAspectRatio)
        self.scene.update()

    def save_picture(self):
        image = self.graphicsView.grab().toImage()
        filepath = QtWidgets.QFileDialog.getSaveFileName(self, "Save path")
        image.save(filepath[0], "PNG")

    def exit(self):
        self.close()

    def rotate(self):
        angle, ok = QtWidgets.QInputDialog.getDouble(self, 'Input Dialog', 'Enter angle:')
        if ok:
            (h, w) = self.image.shape[:2]
            (cX, cY) = (w // 2, h // 2)

            # grab the rotation matrix (applying the negative of the
            # angle to rotate clockwise), then grab the sine and cosine
            # (i.e., the rotation components of the matrix)
            M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
            cos = np.abs(M[0, 0])
            sin = np.abs(M[0, 1])

            # compute the new bounding dimensions of the image
            nW = int((h * sin) + (w * cos))
            nH = int((h * cos) + (w * sin))

            # adjust the rotation matrix to take into account translation
            M[0, 2] += (nW / 2) - cX
            M[1, 2] += (nH / 2) - cY

            # perform the actual rotation and return the image
            rotated = cv2.warpAffine(self.image, M, (nW, nH))
            self.image = rotated
            self.update_scene()

    def blurFilter(self):
        blur = cv2.blur(self.image, (5, 5))
        self.image = blur
        self.update_scene()

    def lighterFilter(self):
        kernel_lighten = [[-0.1, 0.2, -0.1], [0.2, 3, 0.2], [-0.1, 0.2, -0.1]]
        kernel = np.zeros((3, 3))
        kernel[:] = kernel_lighten

        dst = np.zeros((self.image.shape[0], self.image.shape[1], 3), np.uint8)
        cv2.filter2D(src=self.image, dst=dst, ddepth=-1, kernel=kernel)
        self.image = dst
        self.update_scene()

    def darkerFilter(self):
        kernel_darken = [[-0.1, 0.1, -0.1], [0.1, 0.5, 0.1], [-0.1, 0.1, -0.1]]
        kernel = np.zeros((3, 3))
        kernel[:] = kernel_darken

        dst = np.zeros((self.image.shape[0], self.image.shape[1], 3), np.uint8)
        cv2.filter2D(src=self.image, dst=dst, ddepth=-1, kernel=kernel)
        self.image = dst
        self.update_scene()

    def sobel(self):
        img_16 = self.image * 256

        img_sobel_8 = self.image.copy()
        img_sobel_16 = img_16.copy()

        cv2.Sobel(src=img_16, ddepth=-1, dst=img_sobel_16, dx=1, dy=1, ksize=3)
        cv2.convertScaleAbs(src=img_sobel_16, dst=img_sobel_8)
        self.image = img_sobel_8

        self.update_scene()


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Window()
    mainWindow.showMaximized()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

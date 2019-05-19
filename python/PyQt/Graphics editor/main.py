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

        self.actionResize.triggered.connect(self.resize_picture)
        self.actionRotate.triggered.connect(self.rotate)
        self.actionCrop.triggered.connect(self.crop_image)

        self.actionBlur.triggered.connect(self.blurFilter)
        self.actionLighter.triggered.connect(self.lighterFilter)
        self.actionDarker.triggered.connect(self.darkerFilter)
        self.actionSobel_operator.triggered.connect(self.sobel)

        self.actionKenny_Detector.triggered.connect(self.canny)

    def update_scene(self):
        self.scene.clear()
        height, width, bytesPerLine = self.image.shape
        qImg = QtGui.QImage(self.image.data, width, height, bytesPerLine * width, QtGui.QImage.Format_RGB888)
        pixMap = QtGui.QPixmap.fromImage(qImg)
        self.scene.addPixmap(pixMap)
        self.graphicsView.fitInView(QtCore.QRectF(0, 0, width, height), QtCore.Qt.KeepAspectRatio)
        self.scene.update()

    def open_picture(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open picture')
        self.image = cv2.imread(filename[0])
        self.update_scene()

    def save_picture(self):
        image = self.graphicsView.grab().toImage()
        filepath = QtWidgets.QFileDialog.getSaveFileName(self, "Save path")
        image.save(filepath[0], "PNG")

    def exit(self):
        self.close()

    def resize_picture(self):
        x, ok = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter X:')
        if ok:
            y, okk = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Enter Y:')
            if okk:
                dim = (y, x)
                resized = cv2.resize(self.image, dim)
                self.image = resized
                self.update_scene()

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

    def crop_image(self):
        x1, ok = QtWidgets.QInputDialog.getInt(self, 'Input dialog', 'x1: ', min=0)
        if not ok:
            return

        x2, ok = QtWidgets.QInputDialog.getInt(self, 'Input dialog', 'x2: ', min=0)
        if not ok:
            return

        y1, ok = QtWidgets.QInputDialog.getInt(self, 'Input dialog', 'y1: ', min=0)
        if not ok:
            return

        y2, ok = QtWidgets.QInputDialog.getInt(self, 'Input dialog', 'y2: ', min=0)
        if not ok:
            return

        rows, cols, _ = self.image.shape

        bad_args = y1 < 0 or x1 < 0 or y2 > rows or x2 > cols or y1 >= y2 or x1 >= x2
        if bad_args:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('Wrong input')
            msg.exec()
            return

        croped = self.image[y1:y2, x1:x2]
        self.image = croped
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

    def canny(self):
        ratio = 3
        kernel_size = 3
        low_threshold = 50

        src_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.blur(src_gray, (3, 3))
        detected_edges = cv2.Canny(img_blur, low_threshold, low_threshold * ratio, kernel_size)
        mask = detected_edges != 0
        self.image = self.image * (mask[:, :, None].astype(self.image.dtype))
        self.update_scene()



def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Window()
    mainWindow.showMaximized()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

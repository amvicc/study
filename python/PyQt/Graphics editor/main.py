import sys
import cv2
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

    def openPicture(self):
        self.scene.clear()

        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open picture')
        img = cv2.imread(filename[0])
        height, width, byteValue = img.shape
        byteValue = byteValue * width

        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)

        qImg = QtGui.QImage(img, width, height, byteValue, QtGui.QImage.Format_RGB888)
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

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Window()
    mainWindow.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

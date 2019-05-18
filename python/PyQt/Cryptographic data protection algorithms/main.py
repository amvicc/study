import sys
import MainWindow
from Task1 import Task1
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.task1_window = Task1()

        self.pbTask1.clicked.connect(self.task1)

    def task1(self):
        self.task1_window.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

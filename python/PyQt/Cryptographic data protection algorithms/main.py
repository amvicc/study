import sys
import MainWindow
from Task1 import Task1
from Task2 import Task2
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.task1_window = Task1()
        self.task2_window = Task2()

        self.pbTask1.clicked.connect(self.task1)
        self.pbTask2.clicked.connect(self.task2)

    def task1(self):
        self.task1_window.show()

    def task2(self):
        self.task2_window.show()



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

import sys
import MainWindow
from task1 import Task1
from task2 import Task2
from task11 import Task11
from PyQt5 import QtWidgets


class MyWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.task1_window = Task1()
        self.task2_window = Task2()
        self.task11_window = Task11()

        self.pbTask1.clicked.connect(self.task1)
        self.pbTask2.clicked.connect(self.task2)
        self.pbTask11.clicked.connect(self.task11)

    def task1(self):
        self.task1_window.show()

    def task2(self):
        self.task2_window.show()

    def task11(self):
        self.task11_window.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

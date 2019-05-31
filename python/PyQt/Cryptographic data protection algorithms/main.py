import sys
import MainWindow
from task1 import Task1
from task2 import Task2
from task9 import Task9
from task10 import Task10
from task11 import Task11
from task12 import Task12
from PyQt5 import QtWidgets


class MyWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.task1_window = Task1()
        self.task2_window = Task2()
        self.task9_window = Task9()
        self.task10_window = Task10()
        self.task11_window = Task11()
        self.task12_window = Task12()

        self.pbTask1.clicked.connect(self.task1)
        self.pbTask2.clicked.connect(self.task2)
        self.pbTask9.clicked.connect(self.task9)
        self.pbTask10.clicked.connect(self.task10)
        self.pbTask11.clicked.connect(self.task11)
        self.pbTask12.clicked.connect(self.task12)

    def task1(self):
        self.task1_window.show()

    def task2(self):
        self.task2_window.show()

    def task9(self):
        self.task9_window.show()

    def task10(self):
        self.task10_window.show()

    def task11(self):
        self.task11_window.show()

    def task12(self):
        self.task12_window.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

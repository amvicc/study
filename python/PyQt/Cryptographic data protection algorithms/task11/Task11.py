from task11 import Task11Window
import BitOperations
from PyQt5 import QtWidgets


class Task11(QtWidgets.QWidget, Task11Window.Ui_Form):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
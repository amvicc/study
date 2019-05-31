from task10 import Task10Window
import BitOperations
from PyQt5 import QtWidgets


class Task10(QtWidgets.QWidget, Task10Window.Ui_Form):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

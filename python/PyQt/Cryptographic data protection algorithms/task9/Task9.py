from task9 import Task9Window
import BitOperations
from PyQt5 import QtWidgets


class Task9(QtWidgets.QWidget, Task9Window.Ui_Form):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

from task12 import Task12Window
import BitOperations
from PyQt5 import QtWidgets


class Task12(QtWidgets.QWidget, Task12Window.Ui_Form):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

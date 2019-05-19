import Task2Window
import BitOperations
from PyQt5 import QtCore, QtGui, QtWidgets


class Task2(QtWidgets.QWidget, Task2Window.Ui_Form):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.flag_number_valid = False
        self.flag_i_valid = False

        self.pb_A.setEnabled(False)
        self.pb_B.setEnabled(False)

        self.le_number.textChanged.connect(self.enter_number)
        self.le_i.textChanged.connect(self.enter_i)

        self.pb_A.clicked.connect(self.task_a)
        self.pb_B.clicked.connect(self.task_b)

    def enter_number(self):
        if self.le_number.text() == "":
            self.le_number.setStyleSheet("QLineEdit { background-color: white }")
            self.flag_number_valid = False
            self.pb_A.setEnabled(False)
            self.pb_B.setEnabled(False)
            self.binary_number.setText("")
            return

        try:
            number = self.le_number.text()
            if not number.isdigit():
                raise ValueError('Value Error!')
        except ValueError:
            self.le_number.setStyleSheet("QLineEdit { background-color: red }")
            self.flag_number_valid = False
            self.pb_A.setEnabled(False)
            self.pb_B.setEnabled(False)
            self.binary_number.setText("")
            return

        self.le_number.setStyleSheet("QLineEdit { background-color: white }")
        self.flag_number_valid = True
        number = self.le_number.text()
        result = str(bin(int(number)))
        result = result[2:]
        self.binary_number.setText(result)

        if self.flag_i_valid:
            self.pb_A.setEnabled(True)
            self.pb_B.setEnabled(True)

    def enter_i(self):
        if self.le_i.text() == "":
            self.le_i.setStyleSheet("QLineEdit { background-color: white }")
            self.flag_i_valid = False
            self.pb_A.setEnabled(False)
            self.pb_B.setEnabled(False)
            return

        try:
            number = self.le_i.text()
            if not number.isdigit():
                raise ValueError('Value Error!')
            num = int(number)
            if num < 1 or num > len(self.binary_number.text()):
                raise ValueError('Value Error!')
        except ValueError:
            self.le_i.setStyleSheet("QLineEdit { background-color: red }")
            self.flag_i_valid = False
            self.pb_A.setEnabled(False)
            self.pb_B.setEnabled(False)
            return

        self.le_i.setStyleSheet("QLineEdit { background-color: white }")
        self.flag_i_valid = True

        if self.flag_number_valid:
            self.pb_A.setEnabled(True)
            self.pb_B.setEnabled(True)

    def task_a(self):
        number = int(self.le_number.text())
        i = int(self.le_i.text())

        result = str(bin(BitOperations.concat_bits(number, i)))
        result = result[2:]
        self.answer_A.setText("Ответ:" + result)

    def task_b(self):
        number = int(self.le_number.text())
        i = int(self.le_i.text())

        result = str(bin(BitOperations.cut_bits(number, i)))
        result = result[2:]
        self.answer_B.setText("Ответ:" + result)
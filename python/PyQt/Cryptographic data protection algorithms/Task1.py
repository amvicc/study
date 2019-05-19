import Task1Window
import BitOperations
from PyQt5 import QtCore, QtGui, QtWidgets


class Task1(QtWidgets.QWidget, Task1Window.Ui_Form):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.flag_i = False
        self.flag_j = False

        self.input_k.setEnabled(False)
        self.input_k_2.setEnabled(False)
        self.input_i.setEnabled(False)
        self.input_j.setEnabled(False)
        self.input_m.setEnabled(False)

        self.pbStartTask.setEnabled(False)
        self.pbStartTask_2.setEnabled(False)
        self.pbStartTask_3.setEnabled(False)
        self.pbStartTask_4.setEnabled(False)

        self.leNumber.textChanged.connect(self.enter_number)

        self.input_k.textChanged.connect(self.enter_k_1)
        self.pbStartTask.clicked.connect(self.task_1)

        self.input_k_2.textChanged.connect(self.enter_k_2)
        self.pbStartTask_2.clicked.connect(self.task_2)

        self.input_i.textChanged.connect(self.enter_i)
        self.input_j.textChanged.connect(self.enter_j)
        self.pbStartTask_3.clicked.connect(self.task_3)

        self.input_m.textChanged.connect(self.enter_m)
        self.pbStartTask_4.clicked.connect(self.task_4)

    def enter_number(self):
        if self.leNumber.text() == "":
            self.leNumber.setStyleSheet("QLineEdit { background-color: white }")

            self.input_k.setEnabled(False)
            self.input_k_2.setEnabled(False)
            self.input_i.setEnabled(False)
            self.input_j.setEnabled(False)
            self.input_m.setEnabled(False)

            self.pbStartTask.setEnabled(False)
            self.pbStartTask_2.setEnabled(False)
            self.pbStartTask_3.setEnabled(False)
            self.pbStartTask_4.setEnabled(False)
            return

        try:
            number = self.leNumber.text()
            if len(number) != 32:
                raise ValueError('Value Error!')
            if not number.isdigit():
                raise ValueError('Value Error!')
            if not BitOperations.is_binary(number):
                raise ValueError('Value Error!')
        except ValueError:
            self.leNumber.setStyleSheet("QLineEdit { background-color: red }")

            self.input_k.setEnabled(False)
            self.input_k_2.setEnabled(False)
            self.input_i.setEnabled(False)
            self.input_j.setEnabled(False)
            self.input_m.setEnabled(False)

            self.pbStartTask.setEnabled(False)
            self.pbStartTask_2.setEnabled(False)
            self.pbStartTask_3.setEnabled(False)
            self.pbStartTask_4.setEnabled(False)
            return

        self.leNumber.setStyleSheet("QLineEdit { background-color: white }")
        self.input_k.setEnabled(True)
        self.input_k_2.setEnabled(True)
        self.input_i.setEnabled(True)
        self.input_j.setEnabled(True)
        self.input_m.setEnabled(True)

    def enter_k_1(self):
        if self.input_k.text() == "":
            self.input_k.setStyleSheet("QLineEdit { background-color: white }")
            self.pbStartTask.setEnabled(False)
            return

        try:
            k = self.input_k.text()
            if not k.isdigit():
                raise ValueError('Value Error!')
            check = int(k)
            if check < 0 or check > 31:
                raise ValueError('Value Error!')

        except ValueError:
            self.input_k.setStyleSheet("QLineEdit { background-color: red }")
            self.pbStartTask.setEnabled(False)
            return

        self.input_k.setStyleSheet("QLineEdit { background-color: white }")
        self.pbStartTask.setEnabled(True)

    def task_1(self):
        number = int(self.leNumber.text(), 2)
        k = int(self.input_k.text())
        result = BitOperations.get_bit(number, k)

        if result:
            self.labelResult1.setText("K-ый бит числа - 1")
        else:
            self.labelResult1.setText("K-ый бит числа - 0")

    def enter_k_2(self):
        if self.input_k_2.text() == "":
            self.input_k_2.setStyleSheet("QLineEdit { background-color: white }")
            self.pbStartTask_2.setEnabled(False)
            return

        try:
            k = self.input_k_2.text()
            if not k.isdigit():
                raise ValueError('Value Error!')
            check = int(k)
            if check < 0 or check > 31:
                raise ValueError('Value Error!')

        except ValueError:
            self.input_k_2.setStyleSheet("QLineEdit { background-color: red }")
            self.pbStartTask_2.setEnabled(False)
            return

        self.input_k_2.setStyleSheet("QLineEdit { background-color: white }")
        self.pbStartTask_2.setEnabled(True)

    def task_2(self):
        number = int(self.leNumber.text(), 2)
        k = int(self.input_k_2.text())
        res = BitOperations.get_bit(number, k)
        if res:
            result = str(bin(BitOperations.clear_bit(number, k)))
            result = result[2:]
            self.leNumber.setText(result)
        else:
            result = str(bin(BitOperations.set_bit(number, k)))
            result = result[2:]
            self.leNumber.setText(result)

    def enter_i(self):
        if self.input_i.text() == "":
            self.input_i.setStyleSheet("QLineEdit { background-color: white }")
            self.flag_i = False
            self.pbStartTask_3.setEnabled(False)
            return

        try:
            i = self.input_i.text()
            if not i.isdigit():
                raise ValueError('Value Error!')
            check = int(i)
            if check < 0 or check > 31:
                raise ValueError('Value Error!')

        except ValueError:
            self.input_i.setStyleSheet("QLineEdit { background-color: red }")
            self.flag_i = False
            self.pbStartTask_3.setEnabled(False)
            return

        self.input_i.setStyleSheet("QLineEdit { background-color: white }")
        self.flag_i = True

        if self.flag_j:
            self.pbStartTask_3.setEnabled(True)

    def enter_j(self):
        if self.input_j.text() == "":
            self.input_j.setStyleSheet("QLineEdit { background-color: white }")
            self.flag_j = False
            self.pbStartTask_3.setEnabled(False)
            return

        try:
            j = self.input_j.text()
            if not j.isdigit():
                raise ValueError('Value Error!')
            check = int(j)
            if check < 0 or check > 31:
                raise ValueError('Value Error!')

        except ValueError:
            self.input_j.setStyleSheet("QLineEdit { background-color: red }")
            self.flag_j = False
            self.pbStartTask_3.setEnabled(False)
            return

        self.input_j.setStyleSheet("QLineEdit { background-color: white }")
        self.flag_j = True

        if self.flag_i:
            self.pbStartTask_3.setEnabled(True)

    def task_3(self):
        i = int(self.input_i.text())
        j = int(self.input_j.text())
        number = int(self.leNumber.text(), 2)
        result = str(bin(BitOperations.swap_bits(number, i, j)))
        result = result[2:]
        self.leNumber.setText(result)

    def enter_m(self):
        if self.input_m.text() == "":
            self.input_m.setStyleSheet("QLineEdit { background-color: white }")
            self.pbStartTask_4.setEnabled(False)
            return

        try:
            m = self.input_m.text()
            if not m.isdigit():
                raise ValueError('Value Error!')
            check = int(m)
            if check < 1 or check > 32:
                raise ValueError('Value Error!')

        except ValueError:
            self.input_m.setStyleSheet("QLineEdit { background-color: red }")
            self.pbStartTask_4.setEnabled(False)
            return

        self.input_m.setStyleSheet("QLineEdit { background-color: white }")
        self.pbStartTask_4.setEnabled(True)

    def task_4(self):
        value = int(self.leNumber.text(), 2)
        m = int(self.input_m.text())
        result = str(bin(BitOperations.clear_junior_bits(value, m)))
        result = result[2:]
        self.leNumber.setText(result)

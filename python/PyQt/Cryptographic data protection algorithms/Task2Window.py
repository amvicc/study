# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task2Window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(991, 498)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.le_number = QtWidgets.QLineEdit(Form)
        self.le_number.setObjectName("le_number")
        self.verticalLayout.addWidget(self.le_number)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.binary_number = QtWidgets.QLabel(Form)
        self.binary_number.setText("")
        self.binary_number.setObjectName("binary_number")
        self.verticalLayout.addWidget(self.binary_number)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.le_i = QtWidgets.QLineEdit(Form)
        self.le_i.setObjectName("le_i")
        self.verticalLayout.addWidget(self.le_i)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.pb_A = QtWidgets.QPushButton(Form)
        self.pb_A.setObjectName("pb_A")
        self.verticalLayout_3.addWidget(self.pb_A)
        self.answer_A = QtWidgets.QLabel(Form)
        self.answer_A.setObjectName("answer_A")
        self.verticalLayout_3.addWidget(self.answer_A)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.pb_B = QtWidgets.QPushButton(Form)
        self.pb_B.setObjectName("pb_B")
        self.verticalLayout_4.addWidget(self.pb_B)
        self.answer_B = QtWidgets.QLabel(Form)
        self.answer_B.setObjectName("answer_B")
        self.verticalLayout_4.addWidget(self.answer_B)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Введите число:"))
        self.label_3.setText(_translate("Form", "Число в двоичной СС:"))
        self.label_2.setText(_translate("Form", "Введите i:"))
        self.label_5.setText(_translate("Form", "«Склеить» первые i битов с последними i битами из целого числа."))
        self.pb_A.setText(_translate("Form", "Склеить биты"))
        self.answer_A.setText(_translate("Form", "Ответ:"))
        self.label_4.setText(_translate("Form", "Получить биты из целого числа, находящиеся между первыми i битами и последними i битами."))
        self.pb_B.setText(_translate("Form", "Получить биты"))
        self.answer_B.setText(_translate("Form", "Ответ:"))



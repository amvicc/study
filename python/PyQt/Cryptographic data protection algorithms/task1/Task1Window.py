# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task1Window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(935, 464)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_5 = QtWidgets.QGroupBox(Form)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.leNumber = QtWidgets.QLineEdit(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.leNumber.setFont(font)
        self.leNumber.setObjectName("leNumber")
        self.verticalLayout_2.addWidget(self.leNumber)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.input_k = QtWidgets.QLineEdit(self.groupBox)
        self.input_k.setObjectName("input_k")
        self.verticalLayout.addWidget(self.input_k)
        self.pbStartTask = QtWidgets.QPushButton(self.groupBox)
        self.pbStartTask.setObjectName("pbStartTask")
        self.verticalLayout.addWidget(self.pbStartTask)
        self.labelResult1 = QtWidgets.QLabel(self.groupBox)
        self.labelResult1.setObjectName("labelResult1")
        self.verticalLayout.addWidget(self.labelResult1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.input_k_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.input_k_2.setObjectName("input_k_2")
        self.verticalLayout_4.addWidget(self.input_k_2)
        self.pbStartTask_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pbStartTask_2.setObjectName("pbStartTask_2")
        self.verticalLayout_4.addWidget(self.pbStartTask_2)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.input_i = QtWidgets.QLineEdit(self.groupBox_3)
        self.input_i.setObjectName("input_i")
        self.verticalLayout_6.addWidget(self.input_i)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.input_j = QtWidgets.QLineEdit(self.groupBox_3)
        self.input_j.setObjectName("input_j")
        self.verticalLayout_6.addWidget(self.input_j)
        self.pbStartTask_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pbStartTask_3.setObjectName("pbStartTask_3")
        self.verticalLayout_6.addWidget(self.pbStartTask_3)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.input_m = QtWidgets.QLineEdit(self.groupBox_4)
        self.input_m.setObjectName("input_m")
        self.verticalLayout_5.addWidget(self.input_m)
        self.pbStartTask_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pbStartTask_4.setObjectName("pbStartTask_4")
        self.verticalLayout_5.addWidget(self.pbStartTask_4)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_5.setTitle(_translate("Form", "32-х разрядное целое число в двоичной системе счисления"))
        self.groupBox.setTitle(_translate("Form", "Вывод K-ого бита числа :"))
        self.label_2.setText(_translate("Form", "Введите K:"))
        self.pbStartTask.setText(_translate("Form", "Отобразить бит"))
        self.labelResult1.setText(_translate("Form", "K-ый бит числа:"))
        self.groupBox_2.setTitle(_translate("Form", "Установить/снять K−ый бит числа :"))
        self.label.setText(_translate("Form", "Введите K:"))
        self.pbStartTask_2.setText(_translate("Form", "Установить/снять бит"))
        self.groupBox_3.setTitle(_translate("Form", "Поменять местами i−ый и j−ый биты в числе :"))
        self.label_4.setText(_translate("Form", "Введите i:"))
        self.label_5.setText(_translate("Form", "Введите j:"))
        self.pbStartTask_3.setText(_translate("Form", "Поменять местами"))
        self.groupBox_4.setTitle(_translate("Form", "Обнулить младшие m бит :"))
        self.label_3.setText(_translate("Form", "Введите m:"))
        self.pbStartTask_4.setText(_translate("Form", "Обнулить младшие биты"))



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.lab1 = QtWidgets.QWidget()
        self.lab1.setObjectName("lab1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.lab1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.part1 = QtWidgets.QGroupBox(self.lab1)
        self.part1.setObjectName("part1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.part1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pbTask1 = QtWidgets.QPushButton(self.part1)
        self.pbTask1.setObjectName("pbTask1")
        self.verticalLayout_2.addWidget(self.pbTask1)
        self.pbTask2 = QtWidgets.QPushButton(self.part1)
        self.pbTask2.setObjectName("pbTask2")
        self.verticalLayout_2.addWidget(self.pbTask2)
        self.pbTask3 = QtWidgets.QPushButton(self.part1)
        self.pbTask3.setObjectName("pbTask3")
        self.verticalLayout_2.addWidget(self.pbTask3)
        self.verticalLayout_5.addWidget(self.part1)
        self.part2 = QtWidgets.QGroupBox(self.lab1)
        self.part2.setObjectName("part2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.part2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pbTask4 = QtWidgets.QPushButton(self.part2)
        self.pbTask4.setObjectName("pbTask4")
        self.verticalLayout_3.addWidget(self.pbTask4)
        self.pbTask5 = QtWidgets.QPushButton(self.part2)
        self.pbTask5.setObjectName("pbTask5")
        self.verticalLayout_3.addWidget(self.pbTask5)
        self.pbTask6 = QtWidgets.QPushButton(self.part2)
        self.pbTask6.setObjectName("pbTask6")
        self.verticalLayout_3.addWidget(self.pbTask6)
        self.pbTask7 = QtWidgets.QPushButton(self.part2)
        self.pbTask7.setObjectName("pbTask7")
        self.verticalLayout_3.addWidget(self.pbTask7)
        self.pbTask8 = QtWidgets.QPushButton(self.part2)
        self.pbTask8.setObjectName("pbTask8")
        self.verticalLayout_3.addWidget(self.pbTask8)
        self.verticalLayout_5.addWidget(self.part2)
        self.part3 = QtWidgets.QGroupBox(self.lab1)
        self.part3.setObjectName("part3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.part3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pbTask9 = QtWidgets.QPushButton(self.part3)
        self.pbTask9.setObjectName("pbTask9")
        self.verticalLayout_4.addWidget(self.pbTask9)
        self.pbTask10 = QtWidgets.QPushButton(self.part3)
        self.pbTask10.setObjectName("pbTask10")
        self.verticalLayout_4.addWidget(self.pbTask10)
        self.pbTask11 = QtWidgets.QPushButton(self.part3)
        self.pbTask11.setObjectName("pbTask11")
        self.verticalLayout_4.addWidget(self.pbTask11)
        self.pbTask12 = QtWidgets.QPushButton(self.part3)
        self.pbTask12.setObjectName("pbTask12")
        self.verticalLayout_4.addWidget(self.pbTask12)
        self.verticalLayout_5.addWidget(self.part3)
        self.tabWidget.addTab(self.lab1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавить заголовок"))
        self.part1.setTitle(_translate("MainWindow", "Часть 1"))
        self.pbTask1.setText(_translate("MainWindow", "Задание 1"))
        self.pbTask2.setText(_translate("MainWindow", "Задание 2"))
        self.pbTask3.setText(_translate("MainWindow", "Задание 3"))
        self.part2.setTitle(_translate("MainWindow", "Часть 2"))
        self.pbTask4.setText(_translate("MainWindow", "Задание 4"))
        self.pbTask5.setText(_translate("MainWindow", "Задание 5"))
        self.pbTask6.setText(_translate("MainWindow", "Задание 6"))
        self.pbTask7.setText(_translate("MainWindow", "Задание 7"))
        self.pbTask8.setText(_translate("MainWindow", "Задание 8"))
        self.part3.setTitle(_translate("MainWindow", "Часть 3"))
        self.pbTask9.setText(_translate("MainWindow", "Задание 9"))
        self.pbTask10.setText(_translate("MainWindow", "Задание 10"))
        self.pbTask11.setText(_translate("MainWindow", "Задание 11"))
        self.pbTask12.setText(_translate("MainWindow", "Задание 12"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.lab1), _translate("MainWindow", "Лабораторная работа №1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task9Window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(668, 390)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.inputFile = QtWidgets.QLineEdit(Form)
        self.inputFile.setObjectName("inputFile")
        self.horizontalLayout.addWidget(self.inputFile)
        self.pbSelectInputFile = QtWidgets.QPushButton(Form)
        self.pbSelectInputFile.setObjectName("pbSelectInputFile")
        self.horizontalLayout.addWidget(self.pbSelectInputFile)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.outputFile = QtWidgets.QLineEdit(Form)
        self.outputFile.setObjectName("outputFile")
        self.horizontalLayout_2.addWidget(self.outputFile)
        self.pbSelectOutputFile = QtWidgets.QPushButton(Form)
        self.pbSelectOutputFile.setObjectName("pbSelectOutputFile")
        self.horizontalLayout_2.addWidget(self.pbSelectOutputFile)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.bitSeTable = QtWidgets.QLineEdit(Form)
        self.bitSeTable.setObjectName("bitSeTable")
        self.horizontalLayout_3.addWidget(self.bitSeTable)
        self.pbShowBitSeTable = QtWidgets.QPushButton(Form)
        self.pbShowBitSeTable.setObjectName("pbShowBitSeTable")
        self.horizontalLayout_3.addWidget(self.pbShowBitSeTable)
        self.pbRandomBitSeTable = QtWidgets.QPushButton(Form)
        self.pbRandomBitSeTable.setObjectName("pbRandomBitSeTable")
        self.horizontalLayout_3.addWidget(self.pbRandomBitSeTable)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pbEncrypt = QtWidgets.QPushButton(Form)
        self.pbEncrypt.setObjectName("pbEncrypt")
        self.horizontalLayout_8.addWidget(self.pbEncrypt)
        self.pbDecrypt = QtWidgets.QPushButton(Form)
        self.pbDecrypt.setObjectName("pbDecrypt")
        self.horizontalLayout_8.addWidget(self.pbDecrypt)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Bit-Se"))
        self.label.setText(_translate("Form", "Input file"))
        self.pbSelectInputFile.setText(_translate("Form", "Select"))
        self.label_2.setText(_translate("Form", "Output file"))
        self.pbSelectOutputFile.setText(_translate("Form", "Select"))
        self.label_3.setText(_translate("Form", "Table"))
        self.pbShowBitSeTable.setText(_translate("Form", "Show"))
        self.pbRandomBitSeTable.setText(_translate("Form", "Random"))
        self.pbEncrypt.setText(_translate("Form", "Encrypt"))
        self.pbDecrypt.setText(_translate("Form", "Decrypt"))



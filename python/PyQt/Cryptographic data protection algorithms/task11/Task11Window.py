# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task11Window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 390)
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
        self.key = QtWidgets.QLineEdit(Form)
        self.key.setObjectName("key")
        self.horizontalLayout_3.addWidget(self.key)
        self.pbShowKey = QtWidgets.QPushButton(Form)
        self.pbShowKey.setObjectName("pbShowKey")
        self.horizontalLayout_3.addWidget(self.pbShowKey)
        self.pbRandomKey = QtWidgets.QPushButton(Form)
        self.pbRandomKey.setObjectName("pbRandomKey")
        self.horizontalLayout_3.addWidget(self.pbRandomKey)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.IV = QtWidgets.QLineEdit(Form)
        self.IV.setObjectName("IV")
        self.horizontalLayout_4.addWidget(self.IV)
        self.pbRandomIV = QtWidgets.QPushButton(Form)
        self.pbRandomIV.setObjectName("pbRandomIV")
        self.horizontalLayout_4.addWidget(self.pbRandomIV)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Padding_mode = QtWidgets.QGroupBox(Form)
        self.Padding_mode.setObjectName("Padding_mode")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Padding_mode)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.rbPaddingModeANSIX923 = QtWidgets.QRadioButton(self.Padding_mode)
        self.rbPaddingModeANSIX923.setObjectName("rbPaddingModeANSIX923")
        self.horizontalLayout_6.addWidget(self.rbPaddingModeANSIX923)
        self.horizontalLayout_5.addWidget(self.Padding_mode)
        self.Cipher_mode = QtWidgets.QGroupBox(Form)
        self.Cipher_mode.setObjectName("Cipher_mode")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Cipher_mode)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.rbModeECB = QtWidgets.QRadioButton(self.Cipher_mode)
        self.rbModeECB.setObjectName("rbModeECB")
        self.horizontalLayout_7.addWidget(self.rbModeECB)
        self.rbModeOFB = QtWidgets.QRadioButton(self.Cipher_mode)
        self.rbModeOFB.setObjectName("rbModeOFB")
        self.horizontalLayout_7.addWidget(self.rbModeOFB)
        self.rbModeCBC = QtWidgets.QRadioButton(self.Cipher_mode)
        self.rbModeCBC.setObjectName("rbModeCBC")
        self.horizontalLayout_7.addWidget(self.rbModeCBC)
        self.rbModeCFB = QtWidgets.QRadioButton(self.Cipher_mode)
        self.rbModeCFB.setObjectName("rbModeCFB")
        self.horizontalLayout_7.addWidget(self.rbModeCFB)
        self.horizontalLayout_5.addWidget(self.Cipher_mode)
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
        Form.setWindowTitle(_translate("Form", "DES"))
        self.label.setText(_translate("Form", "Input file"))
        self.pbSelectInputFile.setText(_translate("Form", "Select"))
        self.label_2.setText(_translate("Form", "Output file"))
        self.pbSelectOutputFile.setText(_translate("Form", "Select"))
        self.label_3.setText(_translate("Form", "Key (hex)"))
        self.pbShowKey.setText(_translate("Form", "Show"))
        self.pbRandomKey.setText(_translate("Form", "Random"))
        self.label_4.setText(_translate("Form", "IV (hex)"))
        self.pbRandomIV.setText(_translate("Form", "Random"))
        self.Padding_mode.setTitle(_translate("Form", "Padding mode    "))
        self.rbPaddingModeANSIX923.setText(_translate("Form", "ANSI X 923"))
        self.Cipher_mode.setTitle(_translate("Form", "Cipher mode   "))
        self.rbModeECB.setText(_translate("Form", "ECB"))
        self.rbModeOFB.setText(_translate("Form", "OFB"))
        self.rbModeCBC.setText(_translate("Form", "CBC"))
        self.rbModeCFB.setText(_translate("Form", "CFB"))
        self.pbEncrypt.setText(_translate("Form", "Encrypt"))
        self.pbDecrypt.setText(_translate("Form", "Decrypt"))



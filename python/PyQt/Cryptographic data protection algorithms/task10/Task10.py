import os
import threading

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import pyqtSignal

from task10 import Task10Window
from PyQt5 import QtWidgets


class Task10(QtWidgets.QWidget, Task10Window.Ui_Form):
    encrypt_finished = pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.key.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pbSelectInputFile.clicked.connect(self.open_file)
        self.pbSelectOutputFile.clicked.connect(self.save_file)
        self.pbShowKey.clicked.connect(self.show_or_hide_password)
        self.pbRandomKey.clicked.connect(self.random_password)
        self.pbEncrypt.clicked.connect(self.processFile)
        self.pbDecrypt.clicked.connect(self.processFile)

        self.encrypt_finished.connect(self.info_message)

    def show_error(self, message: str):
        QtWidgets.QMessageBox.information(self, 'Error', message)

    def info_message(self):
        self.progressBar.setValue(0)
        QtWidgets.QMessageBox.information(self, 'Info', "Encrypt/Decrypt finished")

    def open_file(self):
        filename, ok = QtWidgets.QFileDialog.getOpenFileName(self, "Open File")
        if not ok:
            return

        self.inputFile.setText(filename)

    def save_file(self):
        filename, ok = QtWidgets.QFileDialog.getSaveFileName(self, "Save File")
        if not ok:
            return

        self.outputFile.setText(filename)

    def show_or_hide_password(self):
        if self.key.echoMode() == QLineEdit.Password:
            self.key.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.pbShowKey.setText("Hide")
        else:
            self.key.setEchoMode(QtWidgets.QLineEdit.Password)
            self.pbShowKey.setText("Show")

    def random_password(self):
        self.key.setText("!+#passwd-pass943939PaSsS")

    def processFile(self):
        if not os.path.exists(self.inputFile.text()):
            self.show_error("Can't open input file")
            return
        if not os.path.exists(self.outputFile.text()):
            self.show_error("Can't open output file")
            return
        threading.Thread(target=self.VernamCipherFunction()).start()

    def VernamCipherFunction(self):
        fin = open(self.inputFile.text())
        text = fin.read()
        fin.close()
        key = self.key.text()

        result = ""
        text_size = len(text)
        part_of_text = text_size / 100
        readed = 0
        ptr = 0
        for char in text:
            readed = readed + 1

            if readed >= part_of_text:
                readed = 0
                self.progressBar.setValue(self.progressBar.value() + 1)

            result = result + chr(ord(char) ^ ord(key[ptr]))
            ptr = ptr + 1
            if ptr == len(key):
                ptr = 0

        fout = open(self.outputFile.text(), "w")
        fout.write(result)
        fout.close()

        self.encrypt_finished.emit()

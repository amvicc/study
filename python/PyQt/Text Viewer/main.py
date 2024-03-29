import sys
import MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.rbUTF.setChecked(True)

        path = "/home/amvicc/"
        self.dirModel = QtWidgets.QFileSystemModel(self.window())
        self.dirModel.setRootPath(path)
        self.dirModel.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.AllDirs)
        self.treeView.setModel(self.dirModel)
        self.treeView.setRootIndex(self.dirModel.index(path))
        self.treeView.clicked.connect(self.on_clicked_dir)

        self.fileModel = QtWidgets.QFileSystemModel(self.window())
        self.fileModel.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Files)
        self.listView.setModel(self.fileModel)
        self.listView.setRootIndex(self.fileModel.index(path))
        self.listView.clicked.connect(self.onFileClick)

        self.pbReset.clicked.connect(self.setDefault)
        self.actionExit.triggered.connect(self.exit)
        self.actionAbout.triggered.connect(self.about)
        self.actionHelp.triggered.connect(self.help)

        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave.setStatusTip('Save File')
        self.actionSave.triggered.connect(self.save)

        self.comboBox.currentTextChanged.connect(self.onComboBoxChanged)

        self.cbBold.stateChanged.connect(self.onBoldClick)
        self.cbItalic.stateChanged.connect(self.onItalicClick)
        self.cbUnderlined.stateChanged.connect(self.onUnderlinedClick)

        self.rbUTF.clicked.connect(self.decodeUTF)
        self.rbCp.clicked.connect(self.decodeCP1551)

    def setDefault(self):
        self.rbUTF.setChecked(True)
        self.decodeUTF()
        self.comboBox.setCurrentIndex(0)
        self.cbBold.setChecked(False)
        self.cbItalic.setChecked(False)
        self.cbUnderlined.setChecked(False)

    def decodeUTF(self):
        self.onFileClick(self.listView.currentIndex())

    def decodeCP1551(self):
        self.onFileClick(self.listView.currentIndex())

    def save(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
        try:
            file = open(name[0], 'w')
            text = self.textEdit.toPlainText()
            file.write(text)
            file.close()
        except:
            print('Error in saving file')

    def exit(self):
        self.close()

    def help(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('Help')
        msg.setText('This programm for view text of the file')
        msg.exec()

    def about(self):
        msg=QtWidgets.QMessageBox()
        msg.setWindowTitle('About')
        msg.setText('Anton Osipov 8-T30-302b-16')
        msg.exec()

    def on_clicked_dir(self, index):
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        self.listView.setRootIndex(self.fileModel.setRootPath(path))

    def onFileClick(self, index):
        path = self.fileModel.fileInfo(index).absoluteFilePath()
        file = QtCore.QFile(path)
        if not file.open(QtCore.QIODevice.ReadOnly):
            QtWidgets.QMessageBox.information(None, 'info', file.errorString())
        stream = QtCore.QTextStream(file)
        stream.setAutoDetectUnicode(False)

        if self.rbUTF.isChecked():
            stream.setCodec('UTF-8')
        else:
            stream.setCodec('cp1251')

        self.textEdit.setText(stream.readAll())
        file.close()

    def onComboBoxChanged(self, value):
        text = self.textEdit.toPlainText()
        self.textEdit.clear()
        self.textEdit.setTextColor(QtGui.QColor(value.lower()))
        self.textEdit.setText(text)

    def onBoldClick(self):
        if self.cbBold.isChecked():
            text = self.textEdit.toPlainText()
            self.textEdit.clear()
            self.textEdit.setFontWeight(QtGui.QFont.Bold)
            self.textEdit.setText(text)
        else:
            text = self.textEdit.toPlainText()
            self.textEdit.clear()
            self.textEdit.setFontWeight(QtGui.QFont.Normal)
            self.textEdit.setText(text)

    def onItalicClick(self):
        if self.cbItalic.isChecked():
            text = self.textEdit.toPlainText()
            self.textEdit.clear()
            self.textEdit.setFontItalic(True)
            self.textEdit.setText(text)
        else:
            text = self.textEdit.toPlainText()
            self.textEdit.clear()
            self.textEdit.setFontItalic(False)
            self.textEdit.setText(text)

    def onUnderlinedClick(self):
        if self.cbUnderlined.isChecked():
            text = self.textEdit.toPlainText()
            self.textEdit.clear()
            self.textEdit.setFontUnderline(True)
            self.textEdit.setText(text)
        else:
            text = self.textEdit.toPlainText()
            self.textEdit.clear()
            self.textEdit.setFontUnderline(False)
            self.textEdit.setText(text)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.showMaximized()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()


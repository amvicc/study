import sys
import MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        self.setDefault()

        path = QtCore.QDir.rootPath()
        self.dirModel = QtWidgets.QFileSystemModel()
        self.dirModel.setRootPath(path)
        self.dirModel.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.AllDirs)
        self.treeView.setModel(self.dirModel)
        self.treeView.setRootIndex(self.dirModel.index(path))
        self.treeView.clicked.connect(self.on_clicked_dir)

        self.fileModel = QtWidgets.QFileSystemModel()
        self.fileModel.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Files)
        self.listView.setModel(self.fileModel)
        self.listView.setRootIndex(self.fileModel.index(path))
        self.listView.clicked.connect(self.onFileClick)

        self.pbReset.clicked.connect(self.setDefault)
        self.actionExit.triggered.connect(self.exit)
        self.actionAbout.triggered.connect(self.about)

        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave.setStatusTip('Save File')
        self.actionSave.triggered.connect(self.save)

    def setDefault(self):
        self.rbUTF.setChecked(True)
        self.comboBox.setCurrentIndex(0)
        self.cbBold.setChecked(False)
        self.cbItalic.setChecked(False)
        self.cbUnderlined.setChecked(False)

    def save(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
        try:
            file = open(name, 'w')
            text = self.textBrowser.toPlainText()
            file.write(text)
            file.close()
        except:
            print('Error in saving file')

    def exit(self):
        self.close()

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
        self.textBrowser.setText(stream.readAll())
        file.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()


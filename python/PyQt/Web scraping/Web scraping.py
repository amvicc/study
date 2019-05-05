import sys
import requests
import MainWindow
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets


class Window(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)

        model = QtGui.QStandardItemModel(20, 5)
        columnNames = ['Title', 'Author', 'Link', 'Number of comments', 'Number of likes']
        model.setHorizontalHeaderLabels(columnNames)
        self.tableView.setModel(model)

        self.actionSearch_information.triggered.connect(self.search)
        self.actionExit.triggered.connect(self.exit)
        self.actionAbout.triggered.connect(self.about)

    def search(self):
        url = "https://habr.com/ru/news/"

        try:
            r = requests.get(url)
        except:
            msg = QtWidgets.QErrorMessage()
            msg.setText('No internet connection')
            msg.exec()

        soup = BeautifulSoup(r.content, "html.parser")

        model = QtGui.QStandardItemModel(20, 5)
        columnNames = ['Title', 'Author', 'Link', 'Number of comments', 'Number of likes']
        model.setHorizontalHeaderLabels(columnNames)

        # Adding titles
        counter = 0
        links = soup.find_all("a", {"class": "post__title_link"})
        for link in links:
            item = QtGui.QStandardItem(link.contents[0])
            model.setItem(counter, 0, item)
            counter = counter + 1

        # Adding links
        counter = 0
        for link in links:
            item = QtGui.QStandardItem(link.get("href"))
            model.setItem(counter, 2, item)
            counter = counter + 1

        # Adding authors
        counter = 0
        authors = soup.find_all("span", {"class": "user-info__nickname"})
        for author in authors:
            item = QtGui.QStandardItem(author.contents[0])
            model.setItem(counter, 1, item)
            counter = counter + 1

        # Adding likes count
        counter = 0
        likes = soup.find_all("span", {"class": "voting-wjt__counter"})
        for like in likes:
            item = QtGui.QStandardItem(like.contents[0])
            model.setItem(counter, 4, item)
            counter = counter + 1

        # Adding columns count
        counter = 0

        comments = soup.find_all("span", {"class": "post-stats__comments-count"})
        for comment in comments:
            item = QtGui.QStandardItem(comment.contents[0])
            model.setItem(counter, 3, item)
            counter = counter + 1

        self.tableView.setModel(model)

    def exit(self):
        self.close()

    def about(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('About')
        msg.setText('Anton Osipov 8-T30-302b-16')
        msg.exec()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.showMaximized()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

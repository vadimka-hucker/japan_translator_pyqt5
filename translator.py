from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import PyQt5.uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pronunciationBox = QCheckBox()
        self.statusBar = QStatusBar()
        self.initUI()

    def initUI(self):
        PyQt5.uic.loadUi('translator.ui', self)
        self.setGeometry(300, 300, 300, 300)
        self.setFixedSize(550, 450)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

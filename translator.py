import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import PyQt5.uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Подключаем атрибуты: кнопки, лейблы и т.п.
        self.pronunciationBox = QCheckBox()
        self.translated_text_edit = QPlainTextEdit()
        self.japan_text_edit = QPlainTextEdit()
        self.translate_btn = QPushButton()
        self.choose_file_btn = QPushButton()
        self.initUI()

        # Атрибут для пути к файлу
        self.fname = ''

        # Подключаем кнопки
        self.choose_file_btn.clicked.connect(self.on_choose_file_btn)

    def initUI(self):
        PyQt5.uic.loadUi('translator.ui', self)
        self.setGeometry(300, 300, 300, 300)
        self.setFixedSize(550, 450)

    def on_choose_file_btn(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать файл', '')[0]
        self.fname = fname
        # if str(fname).strip() == '':
        #    self.errors_label.setText('Файл не был выбран')
        # else:
        #    self.errors_label.setText(f'Выбран файл: {str(fname)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())

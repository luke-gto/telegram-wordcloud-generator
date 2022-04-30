from ui.main_window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
from src.wordcloud import tokenize_chat

import sys


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.choose_json()
        self.choose_stopwords()
    #     self.select_option()

    # def select_option(self):
    #     self.buttonGroup.IdChecked()

    def choose_json(self):
        self.pushButton_json.clicked.connect(self.browse_file_json)

    def choose_stopwords(self):
        self.pushButton_stopwords.clicked.connect(self.browse_file_stopwords)

    def browse_file_stopwords(self):
        stopwords_path = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open File", "", "*.txt"
        )
        self.label_stopwords.setText("Selected file: " + stopwords_path[0])
        return stopwords_path

    def browse_file_json(self):
        json_path = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open File", "", "*.json"
        )
        self.label_json.setText("Selected file: " + json_path[0])
        return json_path


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

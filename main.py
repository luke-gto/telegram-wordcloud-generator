from lib2to3.pgen2.tokenize import tokenize
from ui.main_window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
import src.wordcloud as wc
import os
from pathlib import Path

import sys

script_directory = os.path.dirname(os.path.realpath(__file__))
file_save_directory = str(Path(__file__).resolve().parents[1])


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.choose_json()
        self.choose_stopwords()
        self.start_creation()

    def start_creation(self):
        self.pushButton_start.clicked.connect(self.chosen_option)

    def choose_json(self):
        self.pushButton_json.clicked.connect(self.browse_file_json)

    def choose_stopwords(self):
        self.pushButton_stopwords.clicked.connect(self.browse_file_stopwords)

    def browse_file_stopwords(self):
        global stopwords_path
        stopwords_path = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open File", "", "*.txt"
        )
        self.label_stopwords.setText("Selected file: " + stopwords_path[0])

    def browse_file_json(self):

        global json_path

        json_path = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open File", "", "*.json"
        )
        self.label_json.setText("Selected file: " + json_path[0])

    def output_jdata(self, json_path):
        jdata = wc.load_json(json_path)

        return jdata

    def chosen_option(self):
        if self.buttonGroup.checkedId() == -2:
            tokenized_chat = wc.tokenize_chat(
                self.output_jdata(json_path[0]), stopwords_path[0]
            )
            chat_as_text = " ".join(tokenized_chat)
            msg = QMessageBox()
            msg.setWindowTitle("Yeees!")
            msg.setText("Choose where you want to save the chat file")
            msg.setIcon(msg.Information)
            msg.exec()

            save_path = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Open Save Directory", ""
            )

            with open(save_path + "/telegram_chat.txt", "w") as f:
                f.write(chat_as_text)
                msg = QMessageBox()
                msg.setWindowTitle("Yeees!")
                msg.setText(
                    "Tokenized chat text saved in {}/telegram_chat.txt".format(
                        save_path
                    )
                )
                msg.setIcon(msg.Information)
                msg.exec()
                return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

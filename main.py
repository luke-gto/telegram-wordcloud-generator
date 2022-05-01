from ui.main_window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QColorDialog,
)
import os
from pathlib import Path
import sys
from PIL import Image
import webbrowser

import src.wordcloud as wc
import src.image_processing as ip


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.buttons_listener()
        self.progressBar.hide()
        self.back_color_code = None
        self.cont_color_code = None
        self.mask_ready = None
        self.font_path = None

    def buttons_listener(self):

        self.pushButton_start.clicked.connect(self.chosen_option)
        self.pushButton_json.clicked.connect(self.browse_file_json)
        self.pushButton_stopwords.clicked.connect(self.browse_file_stopwords)
        self.pushButton_font.clicked.connect(self.browse_file_font)
        self.pushButton_back_color.clicked.connect(self.back_color_picker)
        self.pushButton_cont_color.clicked.connect(self.cont_color_picker)
        self.pushButton_mask.clicked.connect(self.choose_mask)
        # self.actionExit.triggered.connect(self.exit_app)
        # self.actionGuide.triggered.connect(self.open_guide)

    def exit_app(self):
        sys.exit()

    def open_guide(self):
        webbrowser.open(
            "https://github.com/luke-gto/telegram-wordcloud-generator/blob/main/README.md"
        )

    def adapt_canvas_size(self, image_mask):
        mask_img = Image.open(image_mask[0])
        width = mask_img.size[0]
        height = mask_img.size[1]
        self.spinBox_width.setValue(width)
        self.spinBox_height.setValue(height)

    def choose_mask(self):
        buttonReply = QMessageBox.question(
            self,
            "Mask image",
            'Do you a b/w PNG file <a href="https://github.com/luke-gto/telegram-wordcloud-generator#tips">ready to be used as a mask</a> for your word cloud?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if buttonReply == QMessageBox.Yes:
            png_ready_path = QtWidgets.QFileDialog.getOpenFileName(
                self, "Open a PNG image", "", "*.png"
            )
            self.adapt_canvas_size(png_ready_path)

            self.mask_ready = ip.make_mask(png_ready_path[0])
        else:
            buttonReply = QMessageBox.question(
                self,
                "Mask image",
                "Ok, do you have a PNG image you want me to try to convert to a mask?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )
            if buttonReply == QMessageBox.Yes:
                png_raw_path = QtWidgets.QFileDialog.getOpenFileName(
                    self, "Open a PNG image", "", "*.png"
                )

                self.adapt_canvas_size(png_raw_path)
                self.mask_ready = ip.black_and_white(png_raw_path[0])
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Noooo")
                msg.setText(
                    "Okay, you can still make a standard rectangular boring word cloud. Select the appropriate option on the top right of the main window"
                )
                msg.setIcon(msg.Information)
                msg.exec()

    def back_color_picker(self):

        color = QColorDialog.getColor()
        if color.isValid():
            self.back_color_code = color.name()
            self.pushButton_back_color.setStyleSheet(
                "background-color : {}".format(self.back_color_code)
            )

    def cont_color_picker(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.cont_color_code = color.name()
            self.pushButton_cont_color.setStyleSheet(
                "background-color : {}".format(self.back_color_code)
            )

    def browse_file_font(self):

        self.font_path = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open File", "", "*.ttf, *otf"
        )[0]

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

    def read_wordcloud_options(self):

        height = self.spinBox_height.value()
        width = self.spinBox_width.value()
        repeat_words = self.checkBox_repeat.isChecked()
        numbers = self.checkBox_num.isChecked()
        font = self.font_path
        min_font_size = self.spinBox_min_font.value()
        font_step = self.spinBox_font_step.value()

        if self.spinBox_max_font.value() == 0:
            max_font = None
        else:
            max_font = self.spinBox_max_font.value()

        if self.spinBox_max_words.value() == 0:
            max_words = None
        else:
            max_words = self.spinBox_max_words.value()

        min_word_lenght = self.spinBox_min_word_length.value()

        scale = self.doubleSpinBox_scale.value()

        background_color = self.back_color_code

        mask = self.mask_ready

        color_mode = self.lineEdit_color_mode.text()
        prefer_horizontal = self.doubleSpinBox_horizontal.value()
        collocation_threshold = self.spinBox_collocation.value()
        relative_scaling = self.doubleSpinBox_relative_scale.value()

        mask_contour_color = self.cont_color_code

        contour_width = self.spinBox_contour.value()

        return (
            height,
            width,
            repeat_words,
            numbers,
            font,
            min_font_size,
            font_step,
            max_font,
            max_words,
            min_word_lenght,
            scale,
            background_color,
            color_mode,
            prefer_horizontal,
            collocation_threshold,
            relative_scaling,
            mask_contour_color,
            contour_width,
            mask,
        )

    def chosen_option(self):

        options = self.read_wordcloud_options()
        print(options)
        self.progressBar.show()
        self.pushButton_start.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))

        tokenized_chat_output = wc.tokenize_chat(
            self.output_jdata(json_path[0]), stopwords_path[0]
        )

        chat_as_text = " ".join(tokenized_chat_output[0])
        save_path = tokenized_chat_output[1]
        if self.buttonGroup.checkedId() == -2:  ### text only no wordcloud

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
                self.progressBar.hide()
                self.pushButton_start.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

                return

        if self.buttonGroup.checkedId() == -4:
            wc.generate_wordcloud(
                save_path=save_path,
                tokenized_chat=chat_as_text,
                font_path=options[4],
                width=options[1],
                height=options[0],
                prefer_horizontal=options[13],
                scale=options[10],
                max_words=options[8],
                min_font_size=options[5],
                background_color=options[11],
                max_font_size=options[7],
                font_step=options[6],
                mode=options[12],
                relative_scaling=options[15],
                repeat=options[2],
                include_numbers=options[4],
                min_word_length=options[9],
                collocation_threshold=options[14],
                mask_contour_color=options[16],
                contour_width=options[17],
                mask=options[18],
            )
            self.progressBar.hide()
            self.pushButton_start.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        if self.buttonGroup.checkedId() == -3:
            options = self.read_wordcloud_options()
            wc.generate_wordcloud(
                save_path=save_path,
                tokenized_chat=chat_as_text,
                font_path=options[4],
                width=options[1],
                height=options[0],
                prefer_horizontal=options[13],
                scale=options[10],
                max_words=options[8],
                min_font_size=options[5],
                background_color=options[11],
                max_font_size=options[7],
                font_step=options[6],
                mode=options[12],
                relative_scaling=options[15],
                repeat=options[2],
                include_numbers=options[4],
                min_word_length=options[9],
                collocation_threshold=options[14],
                mask_contour_color=options[16],
                contour_width=options[17],
                mask=options[18],
            )
            self.progressBar.hide()
            self.pushButton_start.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

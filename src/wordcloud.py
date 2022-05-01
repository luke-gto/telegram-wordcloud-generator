import json
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

import os.path
from pathlib import Path
import sys
from wordcloud import WordCloud
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets


# from .image_processing import make_mask, black_and_white

script_directory = os.path.dirname(os.path.realpath(__file__))
file_save_directory = str(Path(__file__).resolve().parents[1])


def load_json(json_file_path):
    with open(json_file_path, "r") as fcc_file:
        contents = fcc_file.read()
        jdata = json.loads(contents)
        return jdata


def tokenize_chat(jdata, stopwords_path):
    messages = []
    for item in jdata["messages"]:

        if type(item["text"]) == list:
                continue

        message = item["text"] + "\n"
        messages.append(message)

    text = "".join(messages)

    stopword_file = stopwords_path

    if os.path.exists(stopword_file):

        with open(stopword_file, "r") as stopword:
            stopword_list = stopword.read()

            tokenized_chat = [
            i for i in word_tokenize(text.lower()) if i not in stopword_list
                ]

        msg = QMessageBox()
        msg.setWindowTitle("Yeees!")
        msg.setText("Choose where you want to save the file")
        msg.setIcon(msg.Information)
        msg.exec()

        save_path = QtWidgets.QFileDialog.getExistingDirectory(
            None, "Open Save Directory"
        )

        return tokenized_chat, save_path


def save_img(wc, save_path):  # function to save img

    plt.figure(figsize=(20, 10))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(
        save_path + "/wordcloud.png", bbox_inches="tight"
    )

def standard_wordcloud(save_path, font_path,
                width,
                height,
                prefer_horizontal,
                scale,
                max_words,
                min_font_size,
                background_color,
                max_font_size,
                font_step,
                mode,
                relative_scaling,
                repeat,
                include_numbers,
                min_word_length,
                collocation_threshold,tokenized_chat):

    wc = WordCloud(
                font_path=font_path,
                width=width,
                height=height,
                prefer_horizontal=prefer_horizontal,
                scale=scale,
                max_words=max_words,
                min_font_size=min_font_size,
                background_color=background_color,
                max_font_size=max_font_size,
                font_step=font_step,
                mode=mode,
                relative_scaling=relative_scaling,
                repeat=repeat,
                include_numbers=include_numbers,
                min_word_length=min_word_length,
                collocation_threshold=collocation_threshold).generate_from_text(tokenized_chat)


    save_img(wc, save_path)


# def map_wordcloud(tokenized_chat):

#     color = input(
#         "\n\nType the background color name. E.g.: black, white, green, grey...\n\n"
#     )

#     contour_color_input = input("\nType the colour name of the contour:\n\n")

#     contour_size_input = input(
#         "\nEnter the thickness of the contour. E.g.: 1, 2, 10...\n\n"
#     )

#     mask_choice = input(
#         "Please read the documentation to know what charateristics the mask should have.\nDo you have a mask ready to be used? Y/N\n"
#     ).lower()

#     if mask_choice == "y":

#         easygui.msgbox(
#             "Choose the mask image for your wordcloud",
#             "Telegram chat wordcloud generator",
#         )
#         mask_ready = easygui.fileopenbox(
#             msg="Select the mask image", default=script_directory, filetypes="*.png"
#         )

#         mask_img = Image.open(mask_ready)
#         wc = WordCloud(
#             background_color=color,
#             width=mask_img.size[0],
#             height=mask_img.size[1],
#             mask=make_mask(mask_ready),
#             contour_width=contour_size_input,
#             contour_color_input=contour_color_input,
#         ).generate_from_text(tokenized_chat)

#         save_img(wc)

#     if mask_choice == "n":

#         easygui.msgbox(
#             "I can try to convert a PNG image to a mask for you. The result quality may vary. Choose the image you want to use",
#             "Telegram chat wordcloud generator",
#         )
#         mask_img_path = easygui.fileopenbox(
#             msg="Select the mask image", default=script_directory, filetypes="*.png"
#         )
#         mask_img = Image.open(mask_img_path)
#         mask_img_width = mask_img.size[0]
#         mask_img_length = mask_img.size[1]
#         mask_ready = black_and_white(
#             mask_img_path
#         )  # the function already outputs a np array that can be used as a mask, no more operations are needed

#         wc = WordCloud(
#             background_color=color,
#             width=mask_img_width,
#             height=mask_img_length,
#             mask=mask_ready,
#             contour_width=contour_size_input,
#             contour_color_input=contour_color_input,
#         ).generate_from_text(tokenized_chat)

#         save_img(wc)

import json
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
import os.path
from pathlib import Path
from wordcloud import WordCloud
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets


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
    plt.savefig(save_path + "/wordcloud.png", bbox_inches="tight")
    msg = QMessageBox()
    msg.setWindowTitle("Yeees!")
    msg.setText(
        "Word cloud saved! You can find at: {}".format(save_path + "/wordcloud.png")
    )
    msg.setIcon(msg.Information)
    msg.exec()


def standard_wordcloud(
    save_path,
    font_path,
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
    collocation_threshold,
    tokenized_chat,
):

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
        collocation_threshold=collocation_threshold,
    ).generate_from_text(tokenized_chat)

    save_img(wc, save_path)

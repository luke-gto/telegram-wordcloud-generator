
import json
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
import os.path
from pathlib import Path
from PIL import Image
import sys
from wordcloud import WordCloud

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
            return tokenized_chat

    else:

        print("\n\nStopwords file not found, try again.")
        sys.exit()


# def save_img(wc):  # function to save img

#     plt.figure(figsize=(20, 10))
#     plt.imshow(wc, interpolation="bilinear")
#     plt.axis("off")
#     plt.tight_layout(pad=0)
#     wordcloud_file_name = input(
#         "\n\nEnter the filename of the generated wordcloud:\n\n"
#     )
#     plt.savefig(
#         file_save_directory + "/{}.png".format(wordcloud_file_name), bbox_inches="tight"
#     )
#     print("\n\nWordCloud saved in {}".format(file_save_directory))


def standard_wordcloud(tokenized_chat):

    wc = WordCloud().generate_from_text(
        tokenized_chat
    )

    # save_img(wc)


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

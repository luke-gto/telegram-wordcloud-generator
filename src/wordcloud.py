import json
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
import os.path
import sys
from wordcloud import WordCloud
from .image_processing import make_mask
from pathlib import Path
from PIL import Image
import easygui
script_directory = os.path.dirname(os.path.realpath(__file__))
file_save_directory = str(Path(__file__).resolve().parents[1])


def load_json():
    easygui.msgbox('Select the JSON file you got from the Telegram application', 'Telegram chat wordcloud generator')
    json_file_path = easygui.fileopenbox(msg="Select the JSON file", default=script_directory, filetypes="*.json")

    file_exists = os.path.exists(json_file_path)

    if file_exists:

        with open(json_file_path, 'r') as fcc_file:
                contents = fcc_file.read()
                jdata = json.loads(contents)

                return jdata

    else:
        print('JSON file not found, try again.')

        sys.exit()


def tokenize_chat(jdata):

    messages = []

    for item in jdata['messages']:

        if type(item['text']) == list:
            continue

        message = item['text'] + "\n"

        messages.append(message)

    text = ''.join(messages)

    easygui.msgbox("Select the stopwords file. If you don't know what that is, please red the documentation", 'Telegram chat wordcloud generator')
    stopword_file = easygui.fileopenbox(msg="Select the stopwords file", default=script_directory, filetypes="*.txt")

    file_exists = os.path.exists(stopword_file)

    if file_exists:

        with open(stopword_file, "r") as stopword:
            stopword_list = stopword.read()

            tokenized_chat = ([i for i in word_tokenize(text.lower()) if i not in stopword_list])

            return tokenized_chat

    else:

        print('Stopwords file not found, try again.')
        sys.exit()


def save_img(wc): # function to save img

    plt.figure(figsize=(20,10))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    wordcloud_file_name = input("Enter the filename of the generated wordcloud: ")
    plt.savefig(file_save_directory + '/{}.png'.format(wordcloud_file_name), bbox_inches='tight')
    print("WordCloud saved in {}".format(file_save_directory))

def standard_wordcloud(tokenized_chat):

    color = input("Type the background color name. E.g.: black, white, green, grey...\n")

    wc = WordCloud(background_color=color, width=1600, height=800).generate_from_text(tokenized_chat)

    save_img(wc)

def map_wordcloud(tokenized_chat):

    color = input("Type the background color name. E.g.: black, white, green, grey...\n")

    contour_input = input("Type the colour name of the contour:\n")

    mask_choice = input("Please read the documentation to know what charateristics the mask should have.\nDo you have a mask ready to be used? Y/N\n").lower()

    if mask_choice == "y":

        easygui.msgbox('Choose the mask image for your wordcloud', 'Telegram chat wordcloud generator')
        mask_ready = easygui.fileopenbox(msg="Select the mask image", default=script_directory, filetypes="*.png")

        mask_img = Image.open(mask_ready)
        wc = WordCloud(background_color=color, width=mask_img.size[0], height=mask_img.size[1], mask=make_mask(mask_ready), contour_color=contour_input).generate_from_text(tokenized_chat)

        save_img(wc)

    if mask_choice == "n":

        easygui.msgbox('I can try convert a PNG image to a mask for you. The result quality may vary. Choose the image you want to use:', 'Telegram chat wordcloud generator')
        mask_image = easygui.fileopenbox(msg="Select the mask image", default=script_directory, filetypes="*.png")
        mask_ready = make_mask(mask_image)

        wc = WordCloud(background_color=color, width=1600, height=800, mask=make_mask(mask_ready), contour_color=contour_input).generate_from_text(tokenized_chat)

        save_img(wc)
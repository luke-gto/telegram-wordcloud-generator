from src.wordcloud import load_json, tokenize_chat, map_wordcloud, standard_wordcloud
import os
import sys
import easygui

script_directory = os.path.dirname(os.path.realpath(__file__))

def main():

    choice = input("What type of wordcloud do you want to generate?\n1. Standard\n2. wordcloud with image map\n3. I want only the chat messages without stopwords ready for some text mining, you incompetent!\n")

    chat = tokenize_chat(load_json()) # input chat json file

    chat_as_text = ' '.join(chat) # from list to string --> needed by wordcloud library 

    if choice == "1":
        standard_wordcloud(chat_as_text)
        sys.exit()

    if choice == "2":
        map_wordcloud(chat_as_text)
        sys.exit()
    
    if choice == "3":
        print("Loading...")
        easygui.msgbox('Select the folder where you want to save the chat messages ready for some text mining with third party tools', 'Telegram chat wordcloud generator')
        save_directory = easygui.diropenbox(msg="Select the folder", default=script_directory)

        with open(save_directory + '/telegram_chat.txt', 'w') as f:
            f.write(chat_as_text)
        print("Saving the exported chat in " + script_directory)
        sys.exit()

    else:
        print("Please choose a valid option: 1, 2 or 3")
        sys.exit()

if __name__ == '__main__':

    main()
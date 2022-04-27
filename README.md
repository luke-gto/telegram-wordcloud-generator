## Welcome to the Telegram word cloud generator

You can use this tool to create a [word cloud](https://bfy.tw/SigJ)  of your Telegram chats.

1. Open Telegram Desktop installed on your computer, then click Settings > Export Telegram data.

2. Select the [JSON format](docs/img/export.png) option or the whole program simply won't work. 

3. Save the file in a directory and don't forget its name

4. You need a [stopwords](https://en.wikipedia.org/wiki/Stop_word) list for your language in order to clean the chat from useless words. You can find [here](https://github.com/stopwords-iso/) a collection of stopwords for multiple languages. Download the one you need.

5. Install the required libraries
		 ```pip install -r requirements.txt```
		 
6. Launch the script and follow the instructions
		```python main.py``` 

7. Enjoy(?)

### Tips

**1. Use python virtual environments**

I suggest you to use a Python virtual environment ^[1](https://docs.python.org/3/library/venv.html)  ^[2](https://realpython.com/python-virtual-environments-a-primer/)  to not mess around with the Python installation that's part of your OS.

**2. Masked wordcloud**

The script supports [masked word clouds](https://amueller.github.io/word_cloud/auto_examples/masked.html#sphx-glr-auto-examples-masked-py) implemented by the [WordCloud Python library](WordCloud)  but their quality depends on the mask that the user chooses.

You get the best results with a black and white PNG image [like this one](https://amueller.github.io/word_cloud/_images/sphx_glr_masked_002.png).

The text would be placed inside the black image portion.

**3. From PNG to mask**

You can select the option to use a non b/w PNG and the script will try to make a good mask out of it. You can get the best result with images that have clear contours and plain colours without fancy textures.

 
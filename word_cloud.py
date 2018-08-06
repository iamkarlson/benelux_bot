import os

import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from pymystem3 import Mystem
from telethon import TelegramClient
from wordcloud import WordCloud


def get_messages(chat, messages_number):
    client = TelegramClient(os.environ['TELEGRAM_CLIENT_FOR_WORDCLOUD'], os.environ['API_ID'], os.environ['API_KEY'])
    client.start()
    messages = client.get_messages(chat, limit=messages_number)
    text = ''
    for i in messages:
        if i.text is not None:
            text = text + ' ' + i.text
    return text


def word_cloud(chat, messages_number):
    messages_array = get_messages(chat, messages_number)
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(messages_array)
    filtered_words = [w for w in tokens if not w in stopwords.words('russian')]
    m = Mystem()
    lemmas = m.lemmatize(filtered_words)
    wordcloud_array = WordCloud(max_font_size=40).generate(lemmas)
    plt.figure()
    plt.axis("off")
    return plt.imshow(wordcloud_array, interpolation="bilinear")

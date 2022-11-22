import requests
import operator
from bs4 import BeautifulSoup
from collections import Counter

#instalar bibliotecas pip install bs4. pip install requests

###################
def Start(url):
    wordlist = []
    source_code = requests.get(url).text

    # Baixar o html do site:
    soup = BeautifulSoup(source_code, 'html.parser')

    # Text in given web-page is stored under
    # the <div> tags with class <entry-content>
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)


###################
# Remover caracteres especiais de wordlist, criando uma clean_list:
def clean_wordlist(wordlist):
    clean_list = []
    symbols = '!@#$%&*()+-+=[]{}|\"/,.;:?<> '
    symbols += '–…'

    for word in wordlist:
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)


###################
def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(f'{key} : {value}')

    print('#' * 40)
    c = Counter(word_count)
    top = c.most_common(10)
    print(top)
    print('#' * 40)
    print(word_count)


###################
if __name__ == '__main__':
    print('#' * 40)
    # url='https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar'
    url = 'https://www.geeksforgeeks.org/machine-learning/'
    Start(url)

###################



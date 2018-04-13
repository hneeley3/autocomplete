import nltk
nltk.corpus.abc.words()
import random

def other():
    length = len(nltk.corpus.abc.words())
    print(length)
    print('')

    twenty = nltk.corpus.abc.words()[:20]
    print(twenty)
    print('')

    def num():
        word = input('pick a word ')
        number = 0
        for i in nltk.corpus.abc.words():
            if i == word:
                number = number + 1
        print(number)
        print('')


    def look():
        word2 = input('pick a word ')
        place1 = 0
        for i,f in enumerate(nltk.corpus.abc.words()):
            if f == word2:
                place1 = nltk.corpus.abc.words()[i+1]
        print(word2)
        print(place1)
        print('')

    AllThCounts = {}
    number = 0
    name = ''
    for i in nltk.corpus.abc.words():
        if i in AllThCounts.keys():
            AllThCounts[i] = AllThCounts[i] + 1
        else:
            AllThCounts[i] = 0
        if AllThCounts[i] > number:
            name = i
            number = AllThCounts[i]
    print(name)
    print(number)

start_word = input("pick a word ")
def sentence(start_word):
    next_words = []
    for i, f in enumerate(nltk.corpus.abc.words()):
        if f == start_word:
            nect = nltk.corpus.abc.words()[i + 1]
            next_words.append(nect)
    nextstart = random.choice(next_words)
    return nextstart
nextstart = start_word
x = 0
while x <= 5:
    nextstart = sentence(nextstart)
    print(nextstart)
    x = x + 1
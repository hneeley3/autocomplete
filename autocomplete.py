import nltk
nltk.corpus.abc.words()

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
look()

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
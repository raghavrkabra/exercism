import re

def count_words(sentence):
    pattern = re.compile("[a-z]+'[a-z]+|[a-z0-9]+")
    word_list = re.findall(pattern, sentence.lower())

    counter = {}
    for w in word_list:
        if w in counter:
            counter[w] += 1
        else:
            counter[w] = 1

    return counter

"""Solution to Word Count exercise in python track."""

import re


def count_words(sentence):
    """Count the number of words in given sentence."""
    pattern = re.compile("[a-z]+'[a-z]+|[a-z]+|[0-9]+")
    word_list = re.findall(pattern, sentence.lower())

    counter = {}
    for w in word_list:
        if w in counter:
            counter[w] += 1
        else:
            counter[w] = 1

    return counter

from string import ascii_lowercase

def is_pangram(sentence):
    for element in ascii_lowercase:
        if element not in sentence.lower():
            return False

    return True

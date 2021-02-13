"""Solution to Scrabble Score exercise in python Track on Exercism."""


def score(word):
    """Calculate Scrabble score of given word."""
    letter_values = {
                     **dict.fromkeys((letter for letter in "AEIOULNRST"), 1),
                     **dict.fromkeys((letter for letter in "DG"), 2),
                     **dict.fromkeys((letter for letter in "BCMP"), 3),
                     **dict.fromkeys((letter for letter in "FHVWY"), 4),
                     **dict.fromkeys((letter for letter in "K"), 5),
                     **dict.fromkeys((letter for letter in "JX"), 8),
                     **dict.fromkeys((letter for letter in "QZ"), 10),
                    }
    score_ = 0
    for letter in word.upper():
        score_ += letter_values.get(letter)

    return score_

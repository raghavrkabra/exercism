"""Solution to Scrabble Score exercise in python Track on Exercism."""


def score(word):
    """Calculate Scrabble score of given word."""
    letter_values = {
                     **dict.fromkeys(iter("AEIOULNRST"), 1),
                     **dict.fromkeys(iter("DG"), 2),
                     **dict.fromkeys(iter("BCMP"), 3),
                     **dict.fromkeys(iter("FHVWY"), 4),
                     **dict.fromkeys(iter("K"), 5),
                     **dict.fromkeys(iter("JX"), 8),
                     **dict.fromkeys(iter("QZ"), 10),
                    }

    return sum(letter_values.get(letter) for letter in word.upper())

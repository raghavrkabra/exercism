"""Solution to Scrabble Score exercise in python Track on Exercism."""


def score(word):
    """Calculate Scrabble score of given word."""
    letter_values = {
                     **dict.fromkeys("AEIOULNRST", 1),
                     **dict.fromkeys("DG", 2),
                     **dict.fromkeys("BCMP", 3),
                     **dict.fromkeys("FHVWY", 4),
                     **dict.fromkeys("K", 5),
                     **dict.fromkeys("JX", 8),
                     **dict.fromkeys("QZ", 10),
    }

    return sum(letter_values[letter] for letter in word.upper())

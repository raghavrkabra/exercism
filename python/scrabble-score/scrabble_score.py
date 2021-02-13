"""Solution to Scrabble Score exercise in python Track on Exercism."""


def score(word):
    """Calculate Scrabble score of given word."""
    latter_values = {
                     **dict.fromkeys((latter for latter in "AEIOULNRST"), 1),
                     **dict.fromkeys((latter for latter in "DG"), 2),
                     **dict.fromkeys((latter for latter in "BCMP"), 3),
                     **dict.fromkeys((latter for latter in "FHVWY"), 4),
                     **dict.fromkeys((latter for latter in "K"), 5),
                     **dict.fromkeys((latter for latter in "JX"), 8),
                     **dict.fromkeys((latter for latter in "QZ"), 10),
                    }
    score_ = 0
    for latter in word.upper():
        score_ += latter_values.get(latter)

    return score_

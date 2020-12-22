def classify(number):
    """Class given number as Perfect, Deficient or Abundant

    The Greek mathematician Nicomachus devised a classification scheme for
    natural numbers, identifying each as belonging uniquely to the categories
    of perfect, abundant, or deficient based on their aliquot sum. The aliquot
    sum is defined as the sum of the factors of a number not including the
    number itself. For example, the aliquot sum of 15 is (1 + 3 + 5) = 9"""
    factor_list = factors(number)
    sum_ = sum(n for n in factor_list)
    if number == sum_:
        return "perfect"
    elif number > sum_:
        return "deficient"
    else:
        return "abundant"


def factors(number):
    """Give a list of all the facotrs of given natural number."""
    if number > 1:
        return [i for i in range(1, number) if number % i == 0]
    elif number == 1:
        return []
    else:
        raise ValueError("Requires a Natural number")

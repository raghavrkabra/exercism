from math import ceil

def triplets_with_sum(number):
    triplets = []

    for a in range(1, ceil(number/3)):
        for b in range(a, ceil( (number - a)/2 )):
            c = number - (a + b)
            if is_triplet( (a, b, c) ):
                triplets.append([a, b, c])

    return triplets


def triplets_in_range(start, end):
    pass


def is_triplet(triplet):
    a, b, c = triplet
    return a**2 + b**2 == c**2

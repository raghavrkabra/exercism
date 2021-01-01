from math import sqrt, floor

def factors(value):
    prime_factors = []

    while value % 2 == 0:
        prime_factors.append(2)
        value /= 2

    for d in range(3, floor(sqrt(value)) + 1, 2):
        while value % d == 0:
            prime_factors.append(d)
            value /= d

    if value > 1:
        prime_factors.append(value)

    return prime_factors

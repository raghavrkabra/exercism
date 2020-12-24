def largest(min_factor, max_factor: int) -> tuple:
    """Return the largest palindrome number and its factors in given range"""
    if min_factor > max_factor:
        raise ValueError("'min_factor' is grater than 'max_factor'")

    factors = []
    result = None

    # We are going from higher number to lower number as it will be closer to
    # the result.
    for i in range(max_factor, min_factor-1, -1):
        for j in range(max_factor, i-1, -1):
            _n = i*j

            if (result is None or _n > result) and is_palindrome(_n):
                result = _n
                factors.clear()
                factors.append([i, j])
                break

            if _n == result:
                factors.append([i, j])

            if (result is not None and _n < result):
                break

    return (result, factors)


def smallest(min_factor, max_factor: int) -> tuple:
    """Return the smallest palindrome number and its factors in given range"""
    if min_factor > max_factor:
        raise ValueError("'min_factor' is grater than 'max_factor'")

    factors = []
    result = None

    for i in range(min_factor, max_factor+1):
        for j in range(i, max_factor+1):
            _n = i*j

            if (result is None or _n < result) and is_palindrome(_n):
                result = _n
                factors.clear()
                factors.append([i, j])
                break

            if _n == result:
                factors.append([i, j])

            if (result is not None and _n > result):
                break

    return (result, factors)


def is_palindrome(number: int) -> bool:
    """Return True if given number is a Palindrome Number"""
    copy = number
    reverse = 0

    while copy > 0:
        reverse *= 10
        reverse += copy % 10
        copy //= 10

    return number == reverse

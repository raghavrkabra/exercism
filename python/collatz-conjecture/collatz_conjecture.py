def steps(number: int) -> int:
    """Return the number of steps to reach 1 for Collatz Conjecture"""
    if number < 1:
        raise ValueError(f"{number} is not a natural number")

    _n = number
    count = 0

    while _n != 1:
        count += 1
        if _n % 2 == 0:
            _n /= 2
        elif _n != 1:
            _n = _n*3 + 1

    return count

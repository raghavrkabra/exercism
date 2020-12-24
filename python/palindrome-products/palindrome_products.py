def largest(min_factor, max_factor: int) -> tuple:
    pass


def smallest(min_factor, max_factor: int) -> tuple:
    pass


def is_palindrome(number: int) -> bool:
    """Return True if given number is a Palindrome Number"""
    n = number
    reverse = 0

    while n > 0:
        reverse *= 10
        reverse += n % 10
        n //= 10

    return number == reverse


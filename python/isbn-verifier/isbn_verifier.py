def is_valid(isbn):
    """Varify if given number is a valid ISBN 10 number"""

    # Setup for validity check
    digits = [int(n) for n in isbn if n.isnumeric()]
    if len(digits) == 9 and isbn[-1].upper() == "X":
        digits.append(10)

    # length check to weed out obvious wrong answers
    if len(digits) != 10:
        return False

    # Validity check
    sum_ = sum((len(digits)-i)*v for i, v in enumerate(digits))
    return sum_ % 11 == 0


def generate_isbn13(isbn10: str) -> str:
    """Generate ISBN 13 number for given ISBN 10 number"""

    if is_valid(isbn10):
        number = "978" + isbn10[:-1]
        number.replace("-", "")
    else:
        raise ValueError("Invalid ISBN 10 number")

    # calculate check digit of ISBN 13
    sum_ = 0
    check = 1
    for n in number:
        sum_ += int(n)*check
        check = 4 - check
    check_digit = (10 - (sum_ % 10))

    # Return ISBN 13
    return number + str(check_digit)

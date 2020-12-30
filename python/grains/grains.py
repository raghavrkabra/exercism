def square(number):
    """Returns the number of grains on given square on chess board."""
    if number not in range(1, 64+1):
        raise ValueError(f"{number} is not a square in a chess board.")

    return 2**(number - 1)


def total():
    """Returns the total number of grains on the chessboard."""
    return 2**64 - 1

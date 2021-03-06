"""Solution to Leap exercise in python track."""


def leap_year(year):
    """Check whether given year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

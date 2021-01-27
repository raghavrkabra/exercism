"""Solution to Gigasecond exercise on exercism."""
from datetime import timedelta


def add(moment):
    """Return the moment that is a gigasecond after given moment."""
    gigaseconds = timedelta(seconds=1E9)  # 1E9 == 1_000_000_000
    return moment + gigaseconds

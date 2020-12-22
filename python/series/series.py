def slices(series, length):
    """Return substrings of given length of a string."""
    is_valid(series, length)

    limit = len(series) - length + 1

    return [series[i:i+length] for i in range(limit)]

def is_valid(series, length):
    """Raise ValueError on invalid series or length."""
    if length < 1:
        raise ValueError("Invalid length")
    if len(series) == 0:
        raise ValueError("Empty series")
    if len(series) < length:
        raise ValueError("Invalid length for the series")

def is_isogram(string: str) -> bool:
    # Remove whitespace and punctuations from the string
    cleaned = list(l for l in string.lower() if l.isalpha())

    return len(set(cleaned)) == len(cleaned)

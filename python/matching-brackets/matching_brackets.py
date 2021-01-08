"""Solution to matching bracket exercise in python track"""


def is_paired(input_string: str) -> bool:
    """Validate if brackets are matching in given string"""
    brackests = {"(": ")", "[": "]", "{": "}"}
    stack = []

    for char in input_string:
        if char in brackests:
            stack.append(brackests[char])
        elif char in brackests.values():
            if stack == [] or char != stack.pop():
                return False

    return stack == []

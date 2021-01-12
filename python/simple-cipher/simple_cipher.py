"""Solution for Simple Cipher exercise in python track."""

from itertools import cycle
import secrets
from string import ascii_lowercase as letters


class Cipher:
    """An Implamention of Subsitution Cipher."""

    def __init__(self, key=None):
        if key is None:
            key = "".join(secrets.choice(letters) for _ in range(100))

        self.key = key

    def encode(self, text):
        """Encode plaintext massage to cipher."""
        encoded = []
        for char, k in zip(text, cycle(self.key)):
            letter = ((ord(char) + ord(k) - 2*ord(letters[0])) % len(letters) +
                      ord(letters[0]))
            encoded.append(chr(letter))

        return "".join(encoded)

    def decode(self, text):
        """Decode Cipher to plaintext massage."""
        decoded = []
        for char, k in zip(text, cycle(self.key)):
            # python ensure that moduler division always return a positive
            # number, so no need to worry about it.
            letter = ((ord(char) - ord(k)) % len(letters) +
                      ord(letters[0]))
            decoded.append(chr(letter))

        return "".join(decoded)

Ceaser = Cipher("d")

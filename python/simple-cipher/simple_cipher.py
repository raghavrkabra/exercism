"""Solution for Simple Cipher exercise in python track."""

from itertools import cycle
import secrets
from string import ascii_lowercase as letters


class Cipher:
    """An Implamention of Subsitution Cipher."""

    def __init__(self, key=None):
        if key is None:
            key = "".join(secrets.choice(letters) for i in range(100))

        self.key = key

    def encode(self, text):
        """Encode plaintext massage to cipher."""
        msg = []
        for c, k in zip(text, cycle(self.key)):
            letter = ((ord(c) + ord(k) - 2*ord(letters[0])) % len(letters) +
                       ord(letters[0]))
            msg.append(chr(letter))

        return "".join(msg)

    def decode(self, text):
        """Decode Cipher to plaintext massage."""
        msg = []
        for c, k in zip(text, cycle(self.key)):
            # python ensure that moduler division always return a positive
            # number, so no need to worry about it.
            letter = ((ord(c) - ord(k)) % len(letters) +
                       ord(letters[0]))
            msg.append(chr(letter))

        return "".join(msg)

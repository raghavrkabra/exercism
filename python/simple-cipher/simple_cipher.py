"""Solution for Simple Cipher exercise in python track."""

from itertools import cycle
import secrets
from string import (ascii_lowercase as lowercase,
                    ascii_uppercase as uppercase)


class Cipher:
    """An Implamention of Subsitution Cipher."""

    def __init__(self, key=None):
        if key is None:
            key = "".join(secrets.choice(lowercase) for i in range(100))

        self.key = key

    def encode(self, text):
        """Encode plaintext massage to cipher."""
        msg = []
        for c, k in zip(text, cycle(self.key)):
            if c.islower():
                letter = ((ord(c) + ord(k) - 2*ord(lowercase[0])) % 26 +
                           ord(lowercase[0]))
            if c.isupper():
                # This is bad and should not be done in actual code
                # I am only doing this because I Want to encode and decode
                # uppercase letters too but don't want to spend too much time
                # on this exercise
                k.upper()
                letter = ((ord(c) + ord(k) - 2*ord(uppercase[0])) % 26 +
                           ord(uppercase[0]))
            msg.append(chr(letter))

        return "".join(msg)

    def decode(self, text):
        """Decode Cipher to plaintext massage."""
        msg = []
        for c, k in zip(text, cycle(self.key)):
            if c.islower():
                # python ensure that moduler division always return a positive
                # number, so no need to worry about it.
                letter = ((ord(c) - ord(k)) % 26 +
                           ord(lowercase[0]))
            if c.isupper():
                # This is bad and should not be done in actual code
                # I am only doing this because I Want to encode and decode
                # uppercase letters too but don't want to spend too much time
                # on this exercise
                k.upper()
                letter = ((ord(c) - ord(k)) % 26 +
                           ord(uppercase[0]))
            msg.append(chr(letter))

        return "".join(msg)

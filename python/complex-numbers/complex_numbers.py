"""Solutin to Complex Number exercise in python track."""

from math import cos, exp, sin, sqrt


class ComplexNumber:
    """Complex number object."""

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        """Return self == other."""
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        """Return self + other."""
        r = self.real + other.real
        i = self.imaginary + other.imaginary
        return ComplexNumber(r, i)

    def __mul__(self, other):
        """Return self * other."""
        r = (self.real * other.real) - (self.imaginary * other.imaginary)
        i = (self.real * other.imaginary) + (self.imaginary * other.real)
        return ComplexNumber(r, i)

    def __sub__(self, other):
        """Return self - other."""
        r = self.real - other.real
        i = self.imaginary - other.imaginary
        return ComplexNumber(r, i)

    def __truediv__(self, other):
        """Return self / other."""
        d = float(pow(other.real, 2) + pow(other.imaginary, 2))
        r = ((self.real * other.real + self.imaginary *
             other.imaginary) / d)
        i = ((self.imaginary * other.real - self.real *
             other.imaginary) / d)
        return ComplexNumber(r, i)

    def __abs__(self):
        """Return absolute value."""
        return sqrt(pow(self.real, 2) + pow(self.imaginary, 2))

    def conjugate(self):
        """Return conjugate of the complex number."""
        return ComplexNumber(self.real, (- self.imaginary))

    def exp(self):
        """Raise e to the complex number."""
        r = exp(self.real) * cos(self.imaginary)
        i = exp(self.real) * sin(self.imaginary)
        return ComplexNumber(r, i)

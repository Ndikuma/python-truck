import math


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    # --- helper ---
    def _coerce(self, other):
        if isinstance(other, ComplexNumber):
            return other
        return ComplexNumber(other, 0)

    # --- addition ---
    def __add__(self, other):
        other = self._coerce(other)
        return ComplexNumber(
            self.real + other.real,
            self.imaginary + other.imaginary
        )

    def __radd__(self, other):
        return self.__add__(other)

    # --- subtraction ---
    def __sub__(self, other):
        other = self._coerce(other)
        return ComplexNumber(
            self.real - other.real,
            self.imaginary - other.imaginary
        )

    def __rsub__(self, other):
        other = self._coerce(other)
        return ComplexNumber(
            other.real - self.real,
            other.imaginary - self.imaginary
        )

    # --- multiplication ---
    def __mul__(self, other):
        other = self._coerce(other)
        return ComplexNumber(
            self.real * other.real - self.imaginary * other.imaginary,
            self.real * other.imaginary + self.imaginary * other.real
        )

    def __rmul__(self, other):
        return self.__mul__(other)

    # --- division ---
    def __truediv__(self, other):
        other = self._coerce(other)
        denom = other.real**2 + other.imaginary**2

        return ComplexNumber(
            (self.real * other.real + self.imaginary * other.imaginary) / denom,
            (self.imaginary * other.real - self.real * other.imaginary) / denom
        )

    def __rtruediv__(self, other):
        other = self._coerce(other)
        denom = self.real**2 + self.imaginary**2

        return ComplexNumber(
            (other.real * self.real + other.imaginary * self.imaginary) / denom,
            (other.imaginary * self.real - other.real * self.imaginary) / denom
        )

    # --- equality ---
    def __eq__(self, other):
        other = self._coerce(other)
        return self.real == other.real and self.imaginary == other.imaginary

    # --- absolute value ---
    def __abs__(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

    # --- conjugate ---
    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    # --- exponential ---
    def exp(self):
        exp_real = math.exp(self.real)
        return ComplexNumber(
            exp_real * math.cos(self.imaginary),
            exp_real * math.sin(self.imaginary)
        )
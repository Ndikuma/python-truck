import math

class Rational:
    def __init__(self, numer, denom):
        if denom == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
            
        # Determine the greatest common divisor to reduce the fraction
        gcd = math.gcd(numer, denom)
        
        # Simplify the numerator and denominator
        self.numer = numer // gcd
        self.denom = denom // gcd
        
        # Enforce standard form: denominator must always be positive
        if self.denom < 0:
            self.numer = -self.numer
            self.denom = -self.denom

    def __eq__(self, other):
        if not isinstance(other, Rational):
            return False
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        # r1 + r2 = (a1 * b2 + a2 * b1) / (b1 * b2)
        new_numer = self.numer * other.denom + other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __sub__(self, other):
        # r1 - r2 = (a1 * b2 - a2 * b1) / (b1 * b2)
        new_numer = self.numer * other.denom - other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __mul__(self, other):
        # r1 * r2 = (a1 * a2) / (b1 * b2)
        new_numer = self.numer * other.numer
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)

    def __truediv__(self, other):
        if other.numer == 0:
            raise ZeroDivisionError("Cannot divide by a rational number with a zero numerator.")
        # r1 / r2 = (a1 * b2) / (a2 * b1)
        new_numer = self.numer * other.denom
        new_denom = self.denom * other.numer
        return Rational(new_numer, new_denom)

    def __abs__(self):
        # |a/b| = |a| / |b|
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        # Handle a real/floating-point exponent
        if isinstance(power, float):
            return (self.numer ** power) / (self.denom ** power)
            
        # Handle an integer exponent
        if isinstance(power, int):
            if power >= 0:
                return Rational(self.numer ** power, self.denom ** power)
            else:
                m = abs(power)
                return Rational(self.denom ** m, self.numer ** m)
                
        raise TypeError("Power must be an int or float.")

    def __rpow__(self, base):
        # Exponentiation of a real number 'base' to a rational number self (base ** self)
        # x ** (a/b) = root(x ** a, b) which is equivalent to (base ** a) ** (1 / b)
        return (base ** self.numer) ** (1 / self.denom)
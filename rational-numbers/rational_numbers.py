import math


class Rational:
    def __init__(self, numer, denom):
        if numer == 0:
            self.numer = 0
            self.denom = 1

        div = math.gcd(numer, denom)
        self.numer = numer // div
        self.denom = denom // div

        if self.denom < 0:
            self.numer *= -1
            self.denom *= -1

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f"{self.numer}/{self.denom}"

    def __add__(self, other):
        numer = self.numer * other.denom + self.denom * other.numer
        return Rational(
            numer,
            self.denom * other.denom,
        )

    def __sub__(self, other):
        numer = self.numer * other.denom - self.denom * other.numer
        return Rational(
            numer,
            self.denom * other.denom,
        )

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power < 0:
            return Rational(self.denom ** (-power), self.numer ** (-power))

        return Rational(self.numer**power, self.denom**power)

    # Exponentiation of a real number x to a rational number r = a/b
    # is x^(a/b) = root(x^a, b), where root(p, q) is the qth root of p.
    def __rpow__(self, base):
        return root(base**self.numer, self.denom)


def root(p, q):
    return p ** (1 / q)

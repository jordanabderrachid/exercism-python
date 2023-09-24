import math


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imaginary == other.imaginary
        else:
            return self.real == other and self.imaginary == 0

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real + other.real
            imaginary = self.imaginary + other.imaginary
            return ComplexNumber(real, imaginary)
        else:
            return ComplexNumber(self.real + other, self.imaginary)

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real = (self.real * other.real) - (self.imaginary * other.imaginary)
            imaginary = (self.imaginary * other.real) + (self.real * other.imaginary)
            return ComplexNumber(real, imaginary)
        else:
            return ComplexNumber(self.real * other, self.imaginary * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real - other.real
            imaginary = self.imaginary - other.imaginary
            return ComplexNumber(real, imaginary)
        else:
            return ComplexNumber(self.real - other, self.imaginary)

    def __rsub__(self, other):
        return ComplexNumber(-self.real, -self.imaginary).__add__(other)

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            real = (self.real * other.real + self.imaginary * other.imaginary) / (
                other.real * other.real + other.imaginary * other.imaginary
            )
            imaginary = (self.imaginary * other.real - self.real * other.imaginary) / (
                other.real * other.real + other.imaginary * other.imaginary
            )
            return ComplexNumber(real, imaginary)
        else:
            return ComplexNumber(self.real / other, self.imaginary / other)

    def __rtruediv__(self, other):
        return ComplexNumber(other, 0) / self

    def __abs__(self):
        return math.sqrt(self.real * self.real + self.imaginary * self.imaginary)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        exp = math.exp(self.real)
        return ComplexNumber(
            exp * math.cos(self.imaginary), exp * math.sin(self.imaginary)
        )

def valid(sides):
    a, b, c = sides
    if a == 0 or b == 0 or c == 0:
        return False
    
    return (a + b) >= c and (b + c) >= a and (a + c) >= b

def equilateral(sides):
    a, b, c = sides
    return valid(sides) and a == b and b == c


def isosceles(sides):
    a, b, c = sides
    return valid(sides) and ((a == b) or (a == c) or (b == c))


def scalene(sides):
    a, b, c = sides
    return valid(sides) and a != b and a != c and b != c

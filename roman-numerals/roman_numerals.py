numerals = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
]

def roman(number):
    res = ""
    while number > 0:
        for s, v in numerals:
            if number >= v:
                res += s
                number -= v
                break

    return res

def label(colors):
    return to_text(value(colors))

def to_text(value):
    prefix = ""
    if value < 10 ** 3:
        prefix = ""
    elif value < 10 ** 6:
        prefix = "kilo"
        value /= 10 ** 3
    elif value < 10 ** 9:
        prefix = "mega"
        value /= 10 ** 6
    else:
        prefix = "giga"
        value /= 10 ** 9

    return f"{int(value)} {prefix}ohms"

def value(colors):
    return (10 * to_digit(colors[0]) + to_digit(colors[1])) * (10 ** to_digit(colors[2]))

map = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

def to_digit(color):
    return map[color]

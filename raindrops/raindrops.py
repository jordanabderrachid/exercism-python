def convert(number):
    has_3 = number % 3 == 0
    has_5 = number % 5 == 0
    has_7 = number % 7 == 0

    if not(has_3 or has_5 or has_7):
        return str(number)

    res = ""
    if has_3:
        res += "Pling"

    if has_5:
        res += "Plang"

    if has_7:
        res += "Plong"

    return res

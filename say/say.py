mapping = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eigth",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

mapping_tenth = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    
    if number == 0:
        return "zero"

    splitted = split(number)

    res = list()
    b = to_text(splitted[0], "billion")
    if b != "":
        res.append(b)

    m = to_text(splitted[1], "million")
    if m != "":
        res.append(m)
    
    t = to_text(splitted[2], "thousand")
    if t != "":
        res.append(t)

    u = to_text(splitted[3], None)
    if u != "":
        res.append(u)

    return " ".join(res)

def to_text(number, unit):
    if number > 999:
        raise ValueError("greater than 999")
    
    if number == 0:
        return ""

    res = list()
    if number >= 100:
        c = number // 100
        res.append(f"{mapping[c]} hundred")
        number -= c * 100

    if number >= 20:
        d = number // 10
        u = number % 10
        tmp = mapping_tenth[d]
        if u != 0:
            tmp += f"-{mapping[u]}"
        
        res.append(tmp)
    elif number > 0:
        res.append(mapping[number])

    if unit != None:
        res.append(unit)

    return " ".join(res)

def split(number):
    billions = number // 1_000_000_000
    number -= billions * 1_000_000_000 
    millions = number // 1_000_000
    number -= millions * 1_000_000
    thousands = number // 1000
    number -= thousands * 1_000

    return [billions, millions, thousands, number]
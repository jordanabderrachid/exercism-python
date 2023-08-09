def is_digit(l):
    o = ord(l)
    return o >= 48 and o <= 57

def decode(string):
    rle = list()
    digit = ""
    for l in string:
        if is_digit(l):
            digit += l
        else:
            if digit != "":
                digit = int(digit)
            else:
                digit = 1
            rle.append((l, digit))
            digit = ""

    res = ""
    for l, c in rle:
        for _ in range(c):
            res += l

    return res

def encode(string):
    rle = list()
    for c in string:
        if len(rle) == 0:
            rle.append((c, 1))
        else:
            prev = rle[-1]
            if prev[0] == c:
                rle[-1] = (c, prev[1]+1)
            else:
                rle.append((c, 1))

    res = ""
    for r in rle:
        res += enc(r[0], r[1])
    
    return res

def enc(current, count):
    if count == 1:
        return current
    
    return f"{str(count)}{current}"
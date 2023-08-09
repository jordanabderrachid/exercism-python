def score(word):
    s = 0
    for l in word:
        s += point(l.lower())

    return s

one_point = set("aeioulnrst")
two_points = set("dg")
three_points = set("bcmp")
four_points = set("fhvwy")
five_points = set("k")
eight_points = set("jx")
ten_points = set("qz")

def point(letter):
    if letter in one_point:
        return 1
    elif letter in two_points:
        return 2
    elif letter in three_points:
        return 3
    elif letter in four_points:
        return 4
    elif letter in five_points:
        return 5
    elif letter in eight_points:
        return 8
    elif letter in ten_points:
        return 10
    
    raise ValueError("letter has no points #{letter}")
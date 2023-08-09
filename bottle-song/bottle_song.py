wall = "hanging on the wall"

def recite(start, take=1):
    sentences = list()
    current = start
    while current > start-take:
        sentences += [
            f"{green_bottle(current).capitalize()} {wall},",
            f"{green_bottle(current).capitalize()} {wall},",
            f"And if {green_bottle(1)} should accidentally fall,",
            f"There'll be {green_bottle(current-1)} {wall}."
        ]
        current -= 1
        if current > start-take:
            sentences.append("")

    return sentences

digit = {
    10: "ten",
    9: "nine",
    8: "eight",
    7: "seven",
    6: "six",
    5: "five",
    4: "four",
    3: "three",
    2: "two",
    1: "one",
    0: "no",
}
def green_bottle(n):
    return f"{digit[n]} green {bottle(n)}"

def bottle(n):
    res = "bottle"
    if n != 1:
        res += "s"
    return res

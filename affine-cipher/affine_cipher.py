from math import gcd

M = 26


def atoi(a: str) -> int:
    return ord(a.lower()) - 97


def itoa(i: int) -> str:
    return chr(i + 97)


def assert_coprime(a: int):
    if gcd(a, M) != 1:
        raise ValueError("a and m must be coprime.")


def encode(plain_text, a, b):
    assert_coprime(a)

    res = ""
    for letter in plain_text:
        if letter.isdigit():
            res += letter

        if letter.isalpha():
            v = (a * atoi(letter) + b) % M
            res += itoa(v)

    return group(res)


def group(input: str) -> str:
    res = ""
    for i in range(len(input)):
        if i > 0 and i % 5 == 0:
            res += " "

        res += input[i]
    return res


def mmi(a: int) -> int:
    for i in range(1, M):
        if (a * i) % M == 1:
            return i

    return 0


def decode(ciphered_text, a, b):
    assert_coprime(a)

    res = ""
    for letter in ciphered_text:
        if letter.isdigit():
            res += letter

        if letter.isalpha():
            y = atoi(letter)
            x = (mmi(a) * (y - b)) % M
            res += itoa(int(x))

    return res

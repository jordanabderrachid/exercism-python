from functools import reduce


def largest_product(input, size):
    if size < 0:
        raise ValueError("span must not be negative")

    if size > len(input):
        raise ValueError("span must be smaller than string length")

    product = 0
    for i in range(0, len(input) - size + 1):
        serie = input[i : i + size]
        product = max(
            reduce(lambda l, r: l * r, map(convert_to_int, list(serie)), 1), product
        )

    return product


def convert_to_int(x: str) -> int:
    if not x.isdigit():
        raise ValueError("digits input must only contain digits")

    return int(x)

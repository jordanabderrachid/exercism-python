def encode(numbers):
    bytes = []
    for n in reversed(numbers):
        bits = binary(n)

        first = True
        while len(bits) > 0:
            padding = 0 if first else 1
            first = False

            if len(bits) < 7:
                chunk = bits[0:7] + [0] * (7 - len(bits)) + [padding]
            else:
                chunk = bits[0:7] + [padding]
            bits = bits[7:]
            bytes.append(number(chunk))

    return list(reversed(bytes))


def binary(number):
    if number == 0:
        return [0]

    res = []
    while number > 0:
        res.append(number % 2)
        number = number >> 1

    return res


def number(bits):
    n = 0
    for i, b in enumerate(bits):
        n += b * (2**i)
    return n


def decode(bytes_):
    numbers = []
    bits = []
    for byte in reversed(bytes_):
        chunk = pad(binary(byte))
        if chunk[7] == 0:
            # start new sequence
            if len(bits) > 0:
                numbers.append(bits)

            bits = chunk[0:7]
        else:
            # continue current sequence
            if len(bits) == 0:
                raise ValueError("incomplete sequence")

            bits += chunk[0:7]

    if len(bits) > 0:
        numbers.append(bits)

    res = []
    for bits in numbers:
        res.append(number(bits[0:32]))

    return list(reversed(res))


def pad(chunk):
    if len(chunk) < 8:
        chunk += [0] * (8 - len(chunk))

    return chunk

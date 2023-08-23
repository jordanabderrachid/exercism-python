def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    v = 0
    for i, d in enumerate(reversed(digits)):
        if 0 <= d and d < input_base:
            v += d * (input_base**i)
        else:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    res = []
    if v == 0:
        res.append(0)

    i = 1
    while v > 0:
        d = (v % (output_base**i)) // (output_base ** (i - 1))
        v -= d * (output_base ** (i - 1))
        res.append(d)
        i += 1

    return list(reversed(res))

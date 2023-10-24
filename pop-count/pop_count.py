from typing import List
import math


def egg_count(display_value):
    return sum(decimal_to_binary(display_value))


def decimal_to_binary(v: int) -> List[int]:
    if v == 0:
        return [0]

    res = []
    n = math.ceil(math.log2(v))
    for i in range(n, -1, -1):
        t = 2**i
        if v >= t:
            v -= t
            res.append(1)
        else:
            res.append(0)

    return res

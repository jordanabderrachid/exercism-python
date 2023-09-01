# import itertools

digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def combinations(target, size, exclude):
    allowed_digits = digits.difference(exclude)
    possible_combinations = make_combination(size, allowed_digits)
    possible_combinations = [
        list(tupl) for tupl in {tuple(item) for item in possible_combinations}
    ]
    filtered = list(filter(lambda c: sum(c) == target, possible_combinations))

    filtered.sort(key=lambda l: l[0])
    return filtered


def make_combination(size, roaster):
    if size == 0:
        return []

    if len(roaster) == 0:
        raise ValueError("got an empty roaster")

    res = []
    for e in roaster:
        sub_combinations = make_combination(size - 1, roaster.difference({e}))
        if len(sub_combinations) == 0:
            res.append([e])
        else:
            for sub_combination in sub_combinations:
                res.append(sorted([e] + sub_combination))

    return res

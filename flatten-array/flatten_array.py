def flatten(iterable):
    res = list()
    for e in iterable:
        if e == None:
            continue

        if isinstance(e, list):
            res += flatten(e)
        else:
            res.append(e)

    return res

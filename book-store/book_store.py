def total(basket: list[int]):
    groups: list[set[int]] = [set()]
    for item in basket:
        added = False
        for group in groups:
            if item not in group:
                group.add(item)
                added = True
                break

        if not added:
            groups.append(set([item]))

    trios, quintet = [], []
    for group in groups:
        if len(group) == 3:
            trios.append(group)

        if len(group) == 5:
            quintet.append(group)

    for trio, quintet in zip(trios, quintet):
        elem = (quintet - trio).pop()
        quintet.remove(elem)
        trio.add(elem)

    return cost(groups)


def cost(groups: list[set[int]]) -> int:
    res = 0
    for group in groups:
        if len(group) == 0:
            continue

        res += 800 * len(group) * (1 - unique_book_discount(len(group)))
    return res


def unique_book_discount(unique_book_count):
    map = {0: 0, 1: 0, 2: 0.05, 3: 0.10, 4: 0.20, 5: 0.25}
    return map[unique_book_count]

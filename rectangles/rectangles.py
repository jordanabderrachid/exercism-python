from typing import List, Callable

Coord = (int, int)
Pred = Callable[[Coord], bool]


def rectangles(input: List[str]):
    corners: List[Coord] = list()
    horizontal_borders: List[Coord] = list()
    vertical_borders: List[Coord] = list()
    for i, row in enumerate(input):
        for j, c in enumerate(list(row)):
            if c == "+":
                corners.append((i, j))

            if c == "-" or c == "+":
                horizontal_borders.append((i, j))

            if c == "|" or c == "+":
                vertical_borders.append((i, j))

    rectangle_count = 0
    for tl in corners:
        top_right_candidates = find(corners, lambda x: x[0] == tl[0] and x[1] > tl[1])
        top_right_corners = list()
        for trc in top_right_candidates:
            if has_horizontal_line(tl, trc, horizontal_borders):
                top_right_corners.append(trc)

        bottom_right_corners = list()
        for tr in top_right_corners:
            bottom_right_candidates = list()
            bottom_right_candidates += find(
                corners, lambda x: x[0] > tr[0] and x[1] == tr[1]
            )
            for brc in bottom_right_candidates:
                if has_vertical_line(tr, brc, vertical_borders):
                    bottom_right_corners.append(brc)

        bottom_left_corners = list()
        for br in bottom_right_corners:
            bottom_left_candidates = list()
            bottom_left_candidates += find(
                corners, lambda x: x[0] == br[0] and x[1] < br[1]
            )
            for blc in bottom_left_candidates:
                if has_horizontal_line(blc, br, horizontal_borders):
                    bottom_left_corners.append(blc)

        for bl in bottom_left_corners:
            if bl[0] > tl[0] and bl[1] == tl[1]:
                if has_vertical_line(tl, bl, vertical_borders):
                    rectangle_count += 1
                    print(tl)

    return rectangle_count


def find(coords: List, pred: Pred) -> List:
    res: List[Coord] = []
    for c in coords:
        if pred(c):
            res.append(c)

    return res


def contains(search_in: List, target) -> bool:
    try:
        search_in.index(target)
        return True
    except ValueError:
        return False


def has_horizontal_line(left: Coord, right: Coord, horizontal_borders) -> bool:
    if left[0] != right[0]:
        raise ValueError(f"not on the same line left:{left}, right:{right}")

    if left[1] >= right[1]:
        raise ValueError(f"left and right inverted left:{left}, right:{right}")

    if left[1] + 1 == right[1]:
        return True

    for i in range(left[1] + 1, right[1]):
        if not contains(horizontal_borders, (left[0], i)):
            return False

    return True


def has_vertical_line(top: Coord, bottom: Coord, vertical_borders) -> bool:
    if top[1] != bottom[1]:
        raise ValueError(f"not on the same bolumn top:{top}, bottom:{bottom}")

    if top[0] >= bottom[0]:
        raise ValueError(f"top and bottom inverted top:{top}, bottom:{bottom}")

    if top[0] + 1 == bottom[0]:
        return True

    for i in range(top[0] + 1, bottom[0]):
        if not contains(vertical_borders, (i, top[1])):
            return False

    return True

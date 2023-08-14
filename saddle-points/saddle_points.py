from typing import List


def saddle_points(matrix):
    rows_max = list()
    row_length = None
    for row in matrix:
        if row_length is not None and row_length != len(row):
            raise ValueError("irregular matrix")

        if row_length is None:
            row_length = len(row)

        rows_max.append(max(row))

    cols_min = [min(i) for i in zip(*matrix)]

    res = list()
    for s in set(rows_max).intersection(set(cols_min)):
        rows_indexes = find_all(s, rows_max)
        cols_indexes = find_all(s, cols_min)

        for i in rows_indexes:
            for j in cols_indexes:
                res.append({"row": i + 1, "column": j + 1})

    return res


def find_all(target: int, arr: List[int], offset=0):
    if len(arr) == 0:
        return []

    try:
        i = arr.index(target)
        return [i + offset] + find_all(target, arr[i + 1 :], offset + i + 1)
    except ValueError:
        return []

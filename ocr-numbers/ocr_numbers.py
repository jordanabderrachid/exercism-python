from typing import List

DIGITS = {
    "0": [[" ", "_", " "], ["|", " ", "|"], ["|", "_", "|"], [" ", " ", " "]],
    "1": [[" ", " ", " "], [" ", " ", "|"], [" ", " ", "|"], [" ", " ", " "]],
    "2": [[" ", "_", " "], [" ", "_", "|"], ["|", "_", " "], [" ", " ", " "]],
    "3": [[" ", "_", " "], [" ", "_", "|"], [" ", "_", "|"], [" ", " ", " "]],
    "4": [[" ", " ", " "], ["|", "_", "|"], [" ", " ", "|"], [" ", " ", " "]],
    "5": [[" ", "_", " "], ["|", "_", " "], [" ", "_", "|"], [" ", " ", " "]],
    "6": [[" ", "_", " "], ["|", "_", " "], ["|", "_", "|"], [" ", " ", " "]],
    "7": [[" ", "_", " "], [" ", " ", "|"], [" ", " ", "|"], [" ", " ", " "]],
    "8": [[" ", "_", " "], ["|", "_", "|"], ["|", "_", "|"], [" ", " ", " "]],
    "9": [[" ", "_", " "], ["|", "_", "|"], [" ", "_", "|"], [" ", " ", " "]],
}


def convert(input_grid: List[str]):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    line_count = len(input_grid) // 4

    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")
    column_count = len(input_grid[0]) // 3

    res = list()
    for i in range(0, line_count):
        for j in range(0, column_count):
            res.append(
                parse_chunk(
                    [
                        list(input_grid[i * 4][j * 3 : j * 3 + 3]),
                        list(input_grid[i * 4 + 1][j * 3 : j * 3 + 3]),
                        list(input_grid[i * 4 + 2][j * 3 : j * 3 + 3]),
                        list(input_grid[i * 4 + 3][j * 3 : j * 3 + 3]),
                    ]
                )
            )
        if i + 1 != line_count:
            res.append(",")

    return "".join(res)


def parse_chunk(chunk: List[List[str]]) -> str:
    assert_chunk_size(chunk)

    for digit, repr in DIGITS.items():
        if chunk == repr:
            return digit

    return "?"


def assert_chunk_size(chunk: List[List[str]]):
    lines = len(chunk)
    if lines != 4:
        raise ValueError(f"chunk has invalid lines count: {lines}")

    for line in chunk:
        col_len = len(line)
        if col_len != 3:
            raise ValueError(f"chunk has invalid columns count: {col_len}")

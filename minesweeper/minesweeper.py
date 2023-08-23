VALID_CHARS = {" ", "*", "1", "2", "3", "4", "5", "6", "7", "8", "9"}


def annotate(minefield):
    height = len(minefield)
    if height == 0:
        return []
    width = len(minefield[0])
    grid = []
    for line in minefield:
        if len(line) != width:
            raise ValueError("The board is invalid with current input.")
        grid.append(list(line))

    for i in range(0, height):
        for j in range(0, width):
            if grid[i][j] == "*":
                continue

            if len(VALID_CHARS.intersection(set(grid[i][j]))) == 0:
                raise ValueError("The board is invalid with current input.")

            count = 0
            for c in adjacent(i, j, width, height):
                if grid[c[0]][c[1]] == "*":
                    count += 1

            if count > 0:
                grid[i][j] = str(count)

    return ["".join(line) for line in grid]


def adjacent(i, j, width, height):
    return filter(
        lambda c: c[0] >= 0 and c[1] >= 0 and c[0] < height and c[1] < width,
        [
            (i - 1, j - 1),
            (i - 1, j),
            (i - 1, j + 1),
            (i, j - 1),
            (i, j + 1),
            (i + 1, j - 1),
            (i + 1, j),
            (i + 1, j + 1),
        ],
    )

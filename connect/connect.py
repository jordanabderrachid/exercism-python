from typing import List, Tuple, Set

Coord = Tuple[int, int]
Path = Set[Coord]


class ConnectGame:
    def __init__(self, board: str):
        self.tiles = []
        for row in board.splitlines():
            self.tiles.append(list(row.replace(" ", "")))
        self.width = len(self.tiles[0])
        self.height = len(self.tiles)

    def get_winner(self):
        if self.has_left_to_right_path():
            return "X"

        if self.has_top_to_bottom_path():
            return "O"

        return ""

    def has_left_to_right_path(self):
        starting_points = []
        for i in range(0, self.height):
            if self.tiles[i][0] == "X":
                starting_points.append((i, 0))

        for start in starting_points:
            path = self.traverse_path(start, "X")
            if self.wins(path, lambda c: c[1] == self.width - 1):
                return True

        return False

    def has_top_to_bottom_path(self):
        starting_points = []
        for j in range(0, self.width):
            if self.tiles[0][j] == "O":
                starting_points.append((0, j))

        for start in starting_points:
            path = self.traverse_path(start, "O")
            if self.wins(path, lambda c: c[0] == self.height - 1):
                return True

        return False

    def traverse_path(self, starting_point: Coord, target: str) -> Path:
        path = set()
        path.add(starting_point)
        next_coords = [starting_point]
        while len(next_coords) > 0:
            found = set()
            for next_coord in next_coords:
                for t in self.adjacent_tiles(next_coord[0], next_coord[1]):
                    if self.tiles[t[0]][t[1]] == target:
                        found.add(t)

            already_present = path.intersection(found)
            found -= already_present
            path = path.union(found)
            next_coords = list(found)

        return path

    def wins(self, path: Path, test) -> bool:
        for c in path:
            if test(c):
                return True

        return False

    def adjacent_tiles(self, i: int, j: int) -> List[Coord]:
        return list(
            filter(
                lambda c: c[0] >= 0
                and c[0] < self.height
                and c[1] >= 0
                and c[1] < self.width,
                [
                    (i - 1, j),
                    (i - 1, j + 1),
                    (i, j - 1),
                    (i, j + 1),
                    (i + 1, j - 1),
                    (i + 1, j),
                ],
            )
        )

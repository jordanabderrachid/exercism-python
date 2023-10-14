from typing import Set, Tuple
import random


class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.width = len(board[0])
        self.height = len(board)
        self.board = [list(line) for line in board]

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        pos = self._get(x, y)
        if pos is None:
            raise ValueError("Invalid coordinate")

        if pos[0] != " ":
            return (NONE, set())

        coords = set()
        coords.add(pos[1])
        coords = coords.union(self._adjacent(x, y, set()))

        owners = list(map(lambda c: self._owner(c[0], c[1]), list(coords)))

        if len(owners) == 1 and owners[0] == UNDEFINED:
            return (NONE, coords)

        if all(map(lambda o: o == WHITE or o == UNDEFINED, owners)):
            return (WHITE, coords)

        if all(map(lambda o: o == BLACK or o == UNDEFINED, owners)):
            return (BLACK, coords)

        return (NONE, coords)

    def _adjacent(
        self, x: int, y: int, visited: Set[Tuple[int, int]] = set()
    ) -> Set[Tuple[int, int]]:
        if self._is_out_of_bound(x, y):
            return visited

        res = visited
        for x, y in [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]:
            if (x, y) in res:
                continue

            pos = self._get(x, y)
            if pos is not None and pos[0] == NONE:
                res.add(pos[1])
                res = res.union(self._adjacent(x, y, res))

        return res

    def _get(self, x, y):
        if self._is_out_of_bound(x, y):
            return None

        match self.board[y][x]:
            case "B":
                stone = BLACK
            case "W":
                stone = WHITE
            case _:
                stone = NONE

        return (stone, (x, y))

    def _is_out_of_bound(self, i, j):
        return i < 0 or i >= self.width or j < 0 or j >= self.height

    def _owner(self, x, y):
        stones = list(
            map(
                lambda c: self.board[c[1]][c[0]],
                filter(
                    lambda c: (not self._is_out_of_bound(c[0], c[1])),
                    [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)],
                ),
            )
        )

        if all(map(lambda s: s == " ", stones)):
            return UNDEFINED

        if all(map(lambda s: s == "W" or s == " ", stones)):
            return WHITE

        if all(map(lambda s: s == "B" or s == " ", stones)):
            return BLACK

        return NONE

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        res = {WHITE: set(), BLACK: set(), NONE: set()}
        coords = set()
        for x in range(self.width):
            for y in range(self.height):
                coords.add((x, y))

        while coords is not None and len(coords) > 0:
            coord = random.choice(list(coords))
            stone, territory = self.territory(coord[0], coord[1])
            if stone == WHITE:
                res[WHITE] = res[WHITE].union(territory)
                coords = coords.difference(territory)

            if stone == BLACK:
                res[BLACK] = res[BLACK].union(territory)
                coords = coords.difference(territory)

            if stone == NONE:
                if len(territory) == 0:
                    coords.remove(coord)
                else:
                    res[NONE] = res[NONE].union(territory)
                    coords = coords.difference(territory)

        return res

    def __repr__(self) -> str:
        return "\n".join(map(lambda r: "".join(r), self.board))


WHITE = "W"
BLACK = "B"
NONE = " "
UNDEFINED = "U"

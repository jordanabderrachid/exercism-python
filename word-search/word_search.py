class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def next(self, direction):
        if direction == LEFT:
            return Point(self.x + 1, self.y)

        if direction == RIGHT:
            return Point(self.x - 1, self.y)

        if direction == DOWN:
            return Point(self.x, self.y + 1)

        if direction == UP:
            return Point(self.x, self.y - 1)

        if direction == RIGHT_DOWN:
            return Point(self.x + 1, self.y + 1)

        if direction == LEFT_UP:
            return Point(self.x - 1, self.y - 1)

        if direction == RIGHT_UP:
            return Point(self.x + 1, self.y - 1)

        if direction == LEFT_DOWN:
            return Point(self.x - 1, self.y + 1)


LEFT = 1
RIGHT = 2
DOWN = 3
UP = 4
RIGHT_DOWN = 5
LEFT_UP = 6
RIGHT_UP = 7
LEFT_DOWN = 8
DIRECTIONS = [LEFT, RIGHT, DOWN, UP, RIGHT_DOWN, LEFT_UP, RIGHT_UP, LEFT_DOWN]


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):
        candidates = []
        first_letter = word[0]
        for y, row in enumerate(self.puzzle):
            for x, e in enumerate(row):
                if e == first_letter:
                    for d in DIRECTIONS:
                        candidates.append((d, [Point(x, y)]))

        if len(candidates) == 0:
            return None

        for letter in word[1:]:
            valid_candidates = []
            for c in candidates:
                d, points = c
                point = points[-1].next(d)
                if letter == self.get_letter(point):
                    valid_candidates.append((d, points + [point]))
            candidates = valid_candidates

        if len(candidates) == 1:
            return (candidates[0][1][0], candidates[0][1][-1])

        return None

    def get_letter(self, p):
        if p.x < 0 or p.y < 0 or p.x >= len(self.puzzle[0]) or p.y >= len(self.puzzle):
            return None

        return self.puzzle[p.y][p.x]

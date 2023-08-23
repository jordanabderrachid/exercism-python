"""
      x_min                           x_max
y_min      








y_max

"""


class CoordGenerator:
    def __init__(self, limit):
        self.x_min = 0
        self.x_max = limit - 1
        self.y_min = 0
        self.y_max = limit - 1
        self.current = (0, 0)
        self.direction = "right"

    def next(self):
        ret = self.current

        if self.direction == "right":
            next_y = self.current[0]
            next_x = self.current[1] + 1
            self.current = (next_y, next_x)

            if next_x == self.x_max:
                self.direction = "down"
                self.y_min += 1
        elif self.direction == "down":
            next_y = self.current[0] + 1
            next_x = self.current[1]
            self.current = (next_y, next_x)

            if next_y == self.y_max:
                self.direction = "left"
                self.x_max -= 1
        elif self.direction == "left":
            next_y = self.current[0]
            next_x = self.current[1] - 1
            self.current = (next_y, next_x)

            if next_x == self.x_min:
                self.direction = "up"
                self.y_max -= 1
        elif self.direction == "up":
            next_y = self.current[0] - 1
            next_x = self.current[1]
            self.current = (next_y, next_x)

            if next_y == self.y_min:
                self.direction = "right"
                self.x_min += 1

        return ret


def spiral_matrix(size):
    if size == 0:
        return []

    limit = size * size
    res = [[None] * size for _ in range(0, size)]
    coord_generator = CoordGenerator(size)
    current = 0
    while current < limit:
        current += 1
        coord = coord_generator.next()
        res[coord[0]][coord[1]] = current

    return res

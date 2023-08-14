# Globals for the directions
# Change the values as you see fit
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, instructions: str):
        for i in list(instructions):
            if i == "R":
                self.direction = (self.direction + 1) % 4

            if i == "L":
                d = self.direction - 1
                if d < 0:
                    d = 3
                self.direction = d

            if i == "A":
                if self.direction == NORTH:
                    self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)

                if self.direction == SOUTH:
                    self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)

                if self.direction == EAST:
                    self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])

                if self.direction == WEST:
                    self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])

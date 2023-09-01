class CoordIterator:
    def __init__(self, rails, message_length):
        self.rails = rails
        self.message_length = message_length
        self.i = 0
        self.j = 0
        self.direction = "down"

    def next(self):
        res = (self.i, self.j)

        self.j += 1
        if self.direction == "down":
            self.i += 1
        else:
            self.i -= 1

        if self.i == 0:
            self.direction = "down"

        if self.i == self.rails - 1:
            self.direction = "up"

        return res


def encode(message, rails):
    message_length = len(message)
    coord_iterator = CoordIterator(rails, message_length)

    chars = []
    for _ in range(rails):
        chars.append([""] * message_length)

    for c in message:
        i, j = coord_iterator.next()
        chars[i][j] = c

    chars = ["".join(line) for line in chars]
    return "".join(chars)


def decode(encoded_message, rails):
    message_length = len(encoded_message)
    coord_iterator = CoordIterator(rails, message_length)

    chars = []
    for _ in range(rails):
        chars.append([""] * message_length)

    coords = []
    for _ in range(message_length):
        coords.append(coord_iterator.next())

    row_coords = []
    for i in range(rails):
        row = []
        for c in coords:
            if c[0] == i:
                row.append(c)

        row_coords += row

    for i, char in enumerate(encoded_message):
        c = row_coords[i]
        chars[c[0]][c[1]] = char

    res = ""
    for c in coords:
        res += chars[c[0]][c[1]]

    return res

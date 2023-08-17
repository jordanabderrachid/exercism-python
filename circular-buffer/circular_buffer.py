class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message
        pass


class CircularBuffer:
    def __init__(self, capacity):
        self.buf = [None] * capacity
        self.capacity = capacity
        self.write_index = 0
        self.read_index = 0
        self.items_count = 0

    def read(self):
        if self.items_count == 0:
            raise BufferEmptyException("Circular buffer is empty")

        data = self.buf[self.read_index]
        next_index = (self.read_index + 1) % self.capacity
        self.read_index = next_index
        self.items_count -= 1
        return data

    def write(self, data):
        if self.capacity == self.items_count:
            raise BufferFullException("Circular buffer is full")

        self.buf[self.write_index] = data
        next_index = (self.write_index + 1) % self.capacity
        self.write_index = next_index
        self.items_count += 1

    def overwrite(self, data):
        if self.capacity != self.items_count:
            self.write(data)
        else:
            self.buf[self.read_index] = data
            next_read_index = (self.read_index + 1) % self.capacity
            self.read_index = next_read_index
            next_write_index = (self.write_index + 1) % self.capacity
            self.write_index = next_write_index
            self.items_count = min(self.items_count + 1, self.capacity)

    def clear(self):
        self.items_count = 0

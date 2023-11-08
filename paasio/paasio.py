import io
from os import strerror
import errno


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        self.__in_context = False
        self.__read_ops = 0
        self.__read_bytes = 0
        self.__write_ops = 0
        self.__write_bytes = 0
        super().__init__(super, args, kwargs)

    def __enter__(self):
        self.__in_context = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__in_context = False
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self):
        return self

    def __next__(self):
        line = super().readline()
        self.__read_ops += 1
        self.__read_bytes += len(line)

        if line == b"":
            raise StopIteration
        else:
            return line

    def read(self, size=-1):
        if not self.__in_context:
            raise ValueError("I/O operation on closed file.")

        data = super().read(size)
        self.__read_ops += 1
        self.__read_bytes += len(data)
        return data

    @property
    def read_bytes(self):
        return self.__read_bytes

    @property
    def read_ops(self):
        return self.__read_ops

    def write(self, b):
        if not self.__in_context:
            raise ValueError("I/O operation on closed file.")

        size = super().write(b)
        self.__write_ops += 1
        self.__write_bytes += size
        return size

    @property
    def write_bytes(self):
        return self.__write_bytes

    @property
    def write_ops(self):
        return self.__write_ops


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        self.socket = socket
        self.in_context = False
        self.__recv_ops = 0
        self.__recv_bytes = 0
        self.__send_ops = 0
        self.__send_bytes = 0

    def __enter__(self):
        self.in_context = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.in_context = False
        return self.socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags=0):
        if not self.in_context:
            raise OSError(strerror(errno.EBADF))

        bytes = self.socket.recv(bufsize, flags)
        self.__recv_ops += 1
        self.__recv_bytes += len(bytes)
        return bytes

    @property
    def recv_bytes(self):
        return self.__recv_bytes

    @property
    def recv_ops(self):
        return self.__recv_ops

    def send(self, data, flags=0):
        if not self.in_context:
            raise OSError(strerror(errno.EBADF))

        send_len = self.socket.send(data, flags)
        self.__send_ops += 1
        self.__send_bytes += send_len
        return send_len

    @property
    def send_bytes(self):
        return self.__send_bytes

    @property
    def send_ops(self):
        return self.__send_ops

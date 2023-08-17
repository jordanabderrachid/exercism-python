from __future__ import annotations


class Node:
    def __init__(self, value: int, next: Node = None):
        self._value = value
        self._next = next

    def value(self) -> int:
        return self._value

    def next(self) -> Node:
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self._len = 0
        self._head = None
        for v in values:
            self.push(v)

    def __len__(self):
        return self._len

    def __iter__(self):
        return self

    def __next__(self):
        if len(self) == 0:
            raise StopIteration

        return self.pop()

    def head(self):
        if len(self) == 0:
            raise EmptyListException("The list is empty.")

        return self._head

    def push(self, value):
        self._len += 1
        self._head = Node(value, self._head)

    def pop(self):
        if len(self) == 0:
            raise EmptyListException("The list is empty.")

        self._len -= 1
        v = self._head.value()
        self._head = self._head.next()
        return v

    def reversed(self):
        reversed_linked_list = LinkedList()
        while len(self) > 0:
            reversed_linked_list.push(self.pop())

        return reversed_linked_list


class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message

class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedListIterator:
    def __init__(self, linked_list):
        self.linked_list = linked_list
        self.head = linked_list.head

    def __next__(self):
        v = self.head
        if v is None:
            raise StopIteration()

        self.head = v.succeeding
        return v


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.succeeding

        return count

    def __iter__(self):
        return LinkedListIterator(self)

    def __repr__(self) -> str:
        res = "HEAD -> "
        for n in self:
            res += f"{n.value} -> "

        res += "TAIL"
        return res

    def push(self, value):
        if self.head is None:
            node = Node(value)
            self.head = node
            self.tail = node
        else:
            node = Node(value, previous=self.tail)
            self.tail.succeeding = node
            self.tail = node

    def pop(self):
        if self.tail is None:
            raise IndexError("List is empty")

        v = self.tail.value
        self.tail = self.tail.previous
        if self.tail is None:
            self.head = None
        else:
            self.tail.succeeding = None

        return v

    def shift(self):
        if self.head is None:
            raise IndexError("List is empty")

        v = self.head.value
        new_head = self.head.succeeding
        if new_head is None:
            self.head = None
            self.tail = None
        else:
            new_head.previous = None
            self.head = new_head

        return v

    def unshift(self, value):
        if self.head is None:
            self.push(value)
        else:
            new_head = Node(value, succeeding=self.head)
            self.head.previous = new_head
            self.head = new_head

    def delete(self, value):
        if len(self) == 0:
            raise ValueError("Value not found")

        for node in self:
            if node.value == value:
                previous = node.previous
                next = node.succeeding
                if previous is None:  # node is head
                    self.shift()
                    return
                elif next is None:  # node is tail
                    self.pop()
                    return
                else:  # node is in the middle
                    previous.succeeding = next
                    next.previous = previous
                    return

        raise ValueError("Value not found")

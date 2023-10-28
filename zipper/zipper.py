from typing import Self


class Node:
    def __init__(
        self, value: int, left: Self | None = None, right: Self | None = None
    ) -> None:
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def from_tree(tree: dict) -> Self:
        value = tree["value"]
        left = None if tree["left"] is None else Node.from_tree(tree["left"])
        right = None if tree["right"] is None else Node.from_tree(tree["right"])
        return Node(value, left, right)

    def to_tree(self) -> dict:
        res = {}
        res["value"] = self.value
        res["right"] = None if self.right is None else self.right.to_tree()
        res["left"] = None if self.left is None else self.left.to_tree()
        return res

    def set_value(self, value: int) -> None:
        self.value = value

    def set_left(self, left: Self | None) -> None:
        self.left = left

    def set_right(self, right: Self | None) -> None:
        self.right = right


class Zipper:
    @staticmethod
    def from_tree(tree) -> Self:
        return Zipper(Node.from_tree(tree))

    def __init__(self, root: Node, path: list[Node] = []) -> None:
        self.root = root
        self.path = path

    def _current(self) -> Node:
        return self.root if len(self.path) == 0 else self.path[-1]

    def value(self) -> int:
        return self._current().value

    def set_value(self, value: int) -> Self:
        self._current().set_value(value)
        return self

    def left(self) -> None | Self:
        left = self._current().left
        return None if left is None else Zipper(self.root, self.path + [left])

    def set_left(self, tree: dict | None) -> Self:
        self._current().set_left(None if tree is None else Node.from_tree(tree))
        return self

    def right(self) -> None | Self:
        right = self._current().right
        return None if right is None else Zipper(self.root, self.path + [right])

    def set_right(self, tree: dict | None) -> Self:
        self._current().set_right(None if tree is None else Node.from_tree(tree))
        return self

    def up(self) -> None | Self:
        return None if len(self.path) == 0 else Zipper(self.root, self.path[:-1])

    def to_tree(self) -> dict:
        return self.root.to_tree()

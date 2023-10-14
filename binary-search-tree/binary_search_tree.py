class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def append(self, data):
        if data <= self.data:
            self._append_left(data)
        else:
            self._append_right(data)

    def _append_left(self, data):
        if self.left is None:
            self.left = TreeNode(data)
        else:
            self.left.append(data)

    def _append_right(self, data):
        if self.right is None:
            self.right = TreeNode(data)
        else:
            self.right.append(data)

    def sorted(self):
        res = []
        if self.left is not None:
            res += self.left.sorted()

        res.append(self.data)

        if self.right is not None:
            res += self.right.sorted()

        return res

    def __str__(self):
        return f"TreeNode(data={self.data}, left={self.left}, right={self.right})"


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = None
        for data in tree_data:
            self.append(data)

    def append(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self.root.append(data)

    def data(self):
        return self.root

    def sorted_data(self):
        return self.root.sorted()

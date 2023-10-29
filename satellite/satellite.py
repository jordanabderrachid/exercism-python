class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def to_tree(self):
        tree = {"v": self.value}
        tree["l"] = {} if self.left is None else self.left.to_tree()
        tree["r"] = {} if self.right is None else self.right.to_tree()
        return tree


def tree_from_traversals(preorder, inorder):
    if len(preorder) == 0:
        return {}

    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")

    if len(preorder) != len(set(preorder)):
        raise ValueError("traversals must contain unique items")

    return build_node(preorder, inorder).to_tree()


def build_node(preorder: list[str], inorder: list[str]) -> Node:
    if len(preorder) == 0:
        return None

    root = preorder[0]
    root_index = inorder.index(root)
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1 :]
    left_preorder = preorder[1 : 1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder) :]

    return Node(
        root,
        build_node(left_preorder, left_inorder),
        build_node(right_preorder, right_inorder),
    )

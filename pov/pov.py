from json import dumps


class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def remove(self, label):
        children = []
        for c in self.children:
            if c.label != label:
                children.append(c)
        return Tree(self.label, children)

    def from_pov(self, from_node):
        if from_node == self.label:
            return self

        parent = self.parent(from_node)
        n = self.find(from_node)
        if parent is None or n is None:
            raise ValueError("Tree could not be reoriented")

        if self.children == []:
            return self

        return Tree(
            from_node, n.children + [self.from_pov(parent.label).remove(from_node)]
        )

    def path_to(self, from_node, to_node):
        rebased = self.from_pov(from_node)
        res = []
        res.append(to_node)
        next = to_node
        while True:
            parent = rebased.parent(next)
            if parent is None:
                raise ValueError("No path found")

            next = parent.label
            res.append(next)
            if next == from_node:
                break

        return list(reversed(res))

    def parent(self, label):
        if len(self.children) == 0:
            return None

        for c in self.children:
            parent = c.parent(label)
            if parent is not None:
                return parent

            if c.label == label:
                return self

    def find(self, label):
        if self.label == label:
            return self

        for c in self.children:
            n = c.find(label)
            if n is not None:
                return n

        return None

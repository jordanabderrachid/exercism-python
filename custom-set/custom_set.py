class CustomSet:
    def __init__(self, elements=[]):
        self.elements = set(elements)

    def isempty(self):
        return len(self.elements) == 0

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        for e in self.elements:
            if e not in other:
                return False

        return len(self.elements) <= len(other)

    def isdisjoint(self, other):
        if len(self) == 0 or len(other) == 0:
            return True

        for e in self.elements:
            if e in other:
                return False

        return True

    def __eq__(self, other):
        return self.issubset(other) and len(self) == len(other)

    def add(self, element):
        self.elements.add(element)

    def intersection(self, other):
        res = CustomSet()
        for e in self.elements:
            if e in other:
                res.add(e)

        return res

    def __sub__(self, other):
        res = CustomSet()
        for e in self.elements:
            if e not in other:
                res.add(e)

        return res

    def __add__(self, other):
        for e in self.elements:
            other.add(e)

        return other

    def __len__(self):
        return len(self.elements)

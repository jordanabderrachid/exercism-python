NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (
            self.src == other.src
            and self.dst == other.dst
            and self.attrs == other.attrs
        )


class Graph:
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}

        self._assert_data(data)
        if data is not None:
            for d in data:
                self._add_data(d)

    def _assert_data(self, data):
        if data is None:
            return

        if not isinstance(data, list):
            raise TypeError("Graph data malformed")

    def _add_data(self, d):
        if len(d) < 1:
            raise TypeError("Graph item incomplete")

        if d[0] == NODE:
            self._add_node(d)
        elif d[0] == EDGE:
            self._add_edge(d)
        elif d[0] == ATTR:
            self._add_attr(d)
        else:
            raise ValueError("Unknown item")

    def _add_node(self, d):
        if len(d) != 3:
            raise ValueError("Node is malformed")

        self.nodes.append(Node(d[1], d[2]))

    def _add_edge(self, d):
        if len(d) != 4:
            raise ValueError("Edge is malformed")

        self.edges.append(Edge(d[1], d[2], d[3]))

    def _add_attr(self, d):
        if len(d) == 1:
            raise TypeError("Graph item incomplete")

        if len(d) != 3:
            raise ValueError("Attribute is malformed")

        self.attrs[d[1]] = d[2]

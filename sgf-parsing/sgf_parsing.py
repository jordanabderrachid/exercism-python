class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other):
        return not self == other


class Token:
    def __init__(self, value: str):
        self.value = value

    def __eq__(self, __other: object) -> bool:
        return isinstance(__other, Token) and __other.value == self.value


class StringLiteral:
    def __init__(self, value: str):
        self.value = value

    def add(self, c: str):
        self.value += c
        self.value = self.value.replace("\t", " ")


def parse(input_string: str):
    tokens = tokenize(input_string)
    tree, _ = parse_tree(tokens)
    return tree


def tokenize(input: str) -> list[Token | StringLiteral]:
    tokens = []
    for c in input:
        if c in ["(", ")", "[", "]", "\\", ";"] and (
            len(tokens) == 0 or tokens[-1] != Token("\\")
        ):
            tokens.append(Token(c))
        else:
            if len(tokens) == 0 or not isinstance(tokens[-1], StringLiteral):
                tokens.append(StringLiteral(c))
            else:
                tokens[-1].add(c)
    return merge_symbols_in_property_value(tokens)


def merge_symbols_in_property_value(
    tokens: list[Token | StringLiteral],
) -> list[Token | StringLiteral]:
    res = []
    in_property_value = False
    for t in tokens:
        if isinstance(t, StringLiteral):
            if len(res) == 0 or not isinstance(res[-1], StringLiteral):
                res.append(t)
            else:
                res[-1].add(t.value)

        if isinstance(t, Token):
            if t.value == "[":
                if in_property_value:
                    if len(res) == 0 or not isinstance(res[-1], StringLiteral):
                        res.append(StringLiteral(t.value))
                    else:
                        res[-1].add(t.value)
                else:
                    in_property_value = True
                    res.append(t)
            elif t.value == "]":
                in_property_value = False
                res.append(t)
            elif t.value == "\\":
                res.append(t)
            else:
                if in_property_value:
                    res[-1].add(t.value)
                else:
                    res.append(t)
    return res


def parse_tree(tokens: list[Token | StringLiteral]) -> tuple[SgfTree, int]:
    if len(tokens) == 0:
        raise ValueError("tree missing")

    if tokens[0] != Token("("):
        raise ValueError("tree missing")

    i = 0
    tree = None
    while i < len(tokens):
        t = tokens[i]
        if t == Token("("):
            i += 1

        if t == Token(";"):
            tree, read = parse_node(tokens[i:])
            i += read

        if t == Token(")"):
            i += 1
            break

    if tree is None:
        raise ValueError("tree with no nodes")

    return (tree, i)


def parse_node(tokens: list[Token | StringLiteral]) -> tuple[SgfTree, int]:
    properties = {}
    children = []
    i = 0
    properties_read = False
    while i < len(tokens):
        t = tokens[i]
        if t == Token(";"):
            if not properties_read:
                properties_read = True
                i += 1
                properties, read = parse_properties(tokens[i:])
                i += read
            else:
                node, read = parse_node(tokens[i:])
                children = [node]
                i += read

        if t == Token("("):
            node, read = parse_tree(tokens[i:])
            children.append(node)
            i += read

        if t == Token(")"):
            break

    return SgfTree(properties, children), i


def parse_properties(tokens: list[Token | StringLiteral]) -> tuple[map, int]:
    # STOP at ; - ) - or end of input
    res = {}
    i = 0
    property_name = ""
    while i < len(tokens):
        t = tokens[i]
        if isinstance(t, StringLiteral):
            i += 1
            property_name = t.value

        if t == Token("["):
            values, read = parse_values(tokens[i:])
            res[assert_uppercase(property_name)] = values
            property_name = ""
            i += read

        if t == Token(";") or t == Token(")") or t == Token("("):
            if property_name != "":
                raise ValueError("properties without delimiter")
            return res, i

    if property_name != "":
        raise ValueError("properties without delimiter")
    return res, i


def parse_values(tokens: list[Token | StringLiteral]) -> tuple[list[str], int]:
    res = []
    curr = ""
    i = 0
    reading_value = False
    while i < len(tokens):
        t = tokens[i]
        if t == Token("["):
            curr = ""
            reading_value = True
            i += 1
        elif t == Token("]"):
            i += 1
            res.append(curr)
            reading_value = False
        elif t == Token("\\"):
            i += 1
        else:
            if reading_value:
                if tokens[i - 1].value == "\\" and t.value.startswith("\n"):
                    curr += t.value[1:]
                else:
                    curr += t.value
                i += 1
            else:
                break

    return res, i


def assert_uppercase(value: str) -> str:
    for v in value:
        if v.isalpha() and not v.isupper():
            raise ValueError("property must be in uppercase")

    return value


def convert_tabs(input: str) -> str:
    return input.replace("\t", " ")

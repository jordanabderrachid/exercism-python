class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message = message


def evaluate(input_data):
    stack = list()
    user_defined = {}
    for input in input_data:
        if input[0] == ":":
            tokens = input[2:-2].split()
            assert_custom_is_legal(tokens[0])
            user_defined[tokens[0].lower()] = interpret(
                " ".join(tokens[1:]), user_defined.copy()
            )
        else:
            tokens = input_data[-1].split()
            for token in tokens:
                eval(token, user_defined)(stack)

    return stack


def interpret(tokens, user_defined):
    def run(stack):
        for token in tokens.split():
            eval(token, user_defined)(stack)

    return run


def eval(token, user_defined):
    token = token.lower()

    def run(stack):
        if is_digit(token):
            stack.append(int(token))
        elif token in user_defined:
            user_defined[token](stack)
        else:
            built_ins(token, stack)

    return run


def is_digit(token):
    try:
        int(token)
        return True
    except ValueError:
        return False


def add(stack):
    assert_stack(stack, 2)
    stack.append(stack.pop() + stack.pop())


def sub(stack):
    assert_stack(stack, 2)
    right = stack.pop()
    left = stack.pop()
    stack.append(left - right)


def mul(stack):
    assert_stack(stack, 2)
    stack.append(stack.pop() * stack.pop())


def div(stack):
    assert_stack(stack, 2)
    right = stack.pop()

    if right == 0:
        raise ZeroDivisionError("divide by zero")

    left = stack.pop()
    stack.append(left // right)


def dup(stack):
    assert_stack(stack, 1)
    stack.append(stack[-1])


def drop(stack):
    assert_stack(stack, 1)
    stack.pop()


def swap(stack):
    assert_stack(stack, 2)
    last = stack.pop()
    before_last = stack.pop()
    stack.append(last)
    stack.append(before_last)


def over(stack):
    assert_stack(stack, 2)
    stack.append(stack[-2])


def built_ins(token, stack):
    builtins = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
        "dup": dup,
        "drop": drop,
        "swap": swap,
        "over": over,
    }

    if token not in builtins:
        raise ValueError("undefined operation")

    builtins[token](stack)


def assert_stack(stack, size):
    if len(stack) < size:
        raise StackUnderflowError("Insufficient number of items in stack")


def assert_custom_is_legal(token):
    if is_digit(token):
        raise ValueError("illegal operation")

def solve(puzzle):
    tokens = operands(puzzle) + [result(puzzle)]
    leading_letters = make_leading_letters(tokens)
    solution_space = make_solution_space(letters(tokens), leading_letters)
    for solution in solution_space:
        if valid(solution, puzzle):
            return solution

    return None


def operands(puzzle: str) -> list[str]:
    lhs = puzzle.split("==")[0]
    tokens = lhs.split("+")
    return [token.strip() for token in tokens]


def result(puzzle: str) -> str:
    return puzzle.split("==")[1].strip()


def letters(tokens: list[str]) -> set[str]:
    res = set()
    for token in tokens:
        for letter in token:
            res.add(letter)
    return res


def make_solution_space(
    letters: set[str], leading_letters: set[str]
) -> list[dict[str, int]]:
    return make_solution_space_iter(
        letters, set([d for d in range(10)]), {}, leading_letters
    )


def make_solution_space_iter(
    letters: set[str], digits: set[int], prev: dict[str, int], leading_letters: set[str]
) -> list[dict[str, int]]:
    if len(letters) == 0:
        return [prev]

    next_letters = letters.copy()
    letter = next_letters.pop()
    res = []
    for d in digits:
        if letter in leading_letters and d == 0:
            continue

        next = prev.copy()
        next[letter] = d
        next_digits = digits.copy()
        next_digits.remove(d)
        res += make_solution_space_iter(
            next_letters, next_digits, next, leading_letters
        )
    return res


def valid(solution: dict[str, int], puzzle: str) -> bool:
    actual = sum(transform(token, solution) for token in operands(puzzle))
    expected = transform(result(puzzle), solution)
    return actual == expected


def transform(token: str, solution: dict[str, int]) -> int:
    v = 0
    for i in range(len(token)):
        letter = token[-1 - i]
        d = solution[letter]
        v += d * 10**i
    return v


def make_leading_letters(tokens: list[str]) -> set[str]:
    res = set()
    for token in tokens:
        if len(token) > 1:
            res.add(token[0])
    return res


def solution_constains_leading_zero(
    solution: dict[str, int], leading_letters: set[str]
) -> bool:
    for letter in leading_letters:
        if solution[letter] == 0:
            return True
    return False

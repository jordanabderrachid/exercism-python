def recite(start_verse, end_verse):
    res = []
    for i in range(start_verse, end_verse + 1):
        res += verse(i)
        if start_verse != end_verse and i != end_verse:
            res.append("")
    return res


def animal(n):
    return ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"][n - 1]


def first_repetition(n):
    map = {
        3: "How absurd to swallow",
        4: "Imagine that, to swallow",
        5: "What a hog, to swallow",
        6: "Just opened her throat and swallowed",
        7: "I don't know how she swallowed",
    }
    return map[n]


def before_last_repetition(n):
    if n == 2:
        return " that wriggled and jiggled and tickled inside her."

    return "."


def verse(verse_number):
    res = []
    n = verse_number
    animal_count = verse_number
    res.append(f"I know an old lady who swallowed a {animal(animal_count)}.")
    if verse_number == 8:
        res.append("She's dead, of course!")
        return res

    while n > 0:
        if n == verse_number:
            if verse_number == 2:
                res.append("It wriggled and jiggled and tickled inside her.")
            elif verse_number > 2:
                res.append(f"{first_repetition(n)} a {animal(n)}!")
        else:
            if verse_number != 1:
                res.append(
                    f"She swallowed the {animal(animal_count)} to catch the {animal(animal_count-1)}{before_last_repetition(n)}"
                )
                animal_count -= 1
        n -= 1
    res.append(
        f"I don't know why she swallowed the {animal(animal_count)}. Perhaps she'll die."
    )

    return res

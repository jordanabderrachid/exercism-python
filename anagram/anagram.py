def to_letters(word):
    return "".join(sorted(list(word.lower())))

def find_anagrams(word, candidates):
    letters = to_letters(word)
    return [c for c in candidates if letters == to_letters(c) and not word.lower() == c.lower()]

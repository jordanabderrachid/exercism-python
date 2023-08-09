alphabet = set(list("abcdefghijklmnopqrstuvwxyz"))

def is_isogram(string):
    seen = set()
    for l in list(string.lower()):
        if l in alphabet:
            if l in seen:
                return False

            seen.add(l)

    return True

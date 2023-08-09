all_letters = set(list("abcdefghijklmnopqrstuvwxyz"))

def is_pangram(sentence):
    return all_letters <= set(list(sentence.lower()))

vowels = ["yt", "xr", "a", "e", "i", "o", "u"]
consonant = ["thr", "sch", "squ", "p", "k", "x", "qu", "ch", "th","rh", "q", "m", "y", "f", "r"]

def starts_with_vowel(text):
    for v in vowels:
        if text.startswith(v):
            return True

    return False

def starts_with_consonant(text):
    for c in consonant:
        if text.startswith(c):
            return c
        
    return None

def translate(text):
    words = list()
    for w in text.split(" "):
        words.append(translate_word(w))
    
    return " ".join(words)

def translate_word(word):
    if starts_with_vowel(word):
        word += "ay"
    elif starts_with_consonant(word) != None:
        c = starts_with_consonant(word)
        word = word[len(c):] + word[0:len(c)]
        word += "ay"

    return word
import re

def count_words(sentence):
    count = {}
    sentence = re.sub(r'^(\'|\")', "", sentence)
    sentence = re.sub(r'(\'|\")$', "", sentence)
    replaced = sentence.replace("_", " ").replace("\t", " ").replace("\n", " ").replace(",", " ")
    for word in replaced.split(" "):
        if word == "":
            continue

        word = clean(word)
        occurence = count.get(word)
        if occurence == None:
            count[word] = 1
        else:
            count[word] = occurence + 1
        
    return count

def clean(word):
    word = re.sub(r'^\'', "", word)
    word = re.sub(r'\'$', "", word)
    return re.sub(r'[^a-zA-Z1-9\']+', "", word).lower()
def abbreviate(words):
    res = ""
    for word in words.replace("_", "").replace("-", " ").split(" "):
        if word != "":
            res += word[0].upper()

    return res

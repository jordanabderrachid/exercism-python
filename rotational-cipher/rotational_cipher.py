def rotate(text, key):
    res = ""
    for t in text:
        code = ord(t)
        if code >= 97 and code <= 122: # [a-z]
            code = 97 + (code - 97 + key) % 26

        if code >= 65 and code <= 90: # [A-Z]
            code = 65 + (code - 65 + key) % 26

        res += chr(code)

    return res

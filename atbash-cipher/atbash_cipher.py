# a = 97
# m = 109
# n = 110
# z = 122

def encode(plain_text):
    cipher = ""
    for l in plain_text:
        cipher += encode_letter(l.lower())
    
    return group(cipher)

def group(cipher):
    groupped = ""
    for i, l in enumerate(cipher):
        if i % 5 == 0 and i != 0:
            groupped += " "
        groupped += l
    return groupped

def encode_letter(l):
    if l == " " or l == "," or l == ".":
        return ""

    if l >= '0' and l <= '9':
        return l

    if ord(l) <= ord('m'):
        return chr(ord('m') - ord(l) + ord('n'))
    else:
        return chr(ord('m') - (ord(l) - ord('n')))

def decode(ciphered_text):
    ciphered_text = ciphered_text.replace(" ", "")

    text = ""
    for l in ciphered_text:
        text += decode_letter(l)

    return text

def decode_letter(l):
    return encode_letter(l)
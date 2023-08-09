import re
import math

def cipher_text(plain_text):
    normalized = normalize(plain_text)
    r, c = find_dimensions(len(normalized))

    chunks = list()
    for j in range(c):
        chunk = ""
        for i in range(r):
            idx = i*c + j
            if idx >= len(normalized):
                chunk += " "
            else:
                chunk += normalized[idx]
        chunks.append(chunk)
    
    return " ".join(chunks)

def normalize(text):
    return re.sub(r'[^a-zA-Z0-9]', "", text).lower()



def find_dimensions(l):
    sqrt = math.sqrt(l)
    r, c = (int(math.floor(sqrt)),int(math.ceil(sqrt)))
    if r * c < l:
        r += 1
    return (r, c)
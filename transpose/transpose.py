PAD = -2

def transpose(lines):
    lines = lines.split("\n")
    
    input = []
    max_col = -1
    for l in lines:
        line = list()
        for c in l:
            line.append(c)
        col_len = len(line)
        if col_len > max_col:
            max_col = col_len
        input.append(line)
    
    res = list()
    for j in range(max_col):
        new_line = list()
        for i in range(len(lines)):
            e = None
            try:
                e = input[i][j]
            except IndexError:
                e = PAD
            new_line.append(e)
        res.append(convert(new_line))
    
    return "\n".join(res)

def convert(elems):
    return "".join(replace_padding(trim_pad_right(elems)))

def trim_pad_right(elems):
    l = len(elems)
    if l == 0:
        return elems
    
    if elems[l-1] != PAD:
        return elems
    
    return trim_pad_right(elems[:l-1])

def replace_padding(elems):
    for i, e in enumerate(elems):
        if e == PAD:
            elems[i] = " "
    
    return elems
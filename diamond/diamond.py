def abs(n):
    if n < 0:
        return -n
    
    return n

def rows(letter):
    diff = ord(letter) - ord("A")
    rows = list()
    for i in range(2*diff+1):
        col = list()
        for j in range(2*diff+1):
            if i <= diff:
                if (i+j) == diff or (j-i)==diff:
                    col.append(chr(ord("A") + i))
                else:
                    col.append(" ")
            else:
                i = (2*diff)-i
                if (i+j) == diff or (j-i)==diff:
                    col.append("X")
                else:
                    col.append(" ")
        rows.append("".join(col))
    
    return rows

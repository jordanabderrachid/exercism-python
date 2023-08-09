def slices(series, length):
    if series == "":
        raise ValueError("series cannot be empty")
    
    if length == 0:
        raise ValueError("slice length cannot be zero")

    if length < 0:
        raise ValueError("slice length cannot be negative")

    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    res = list()
    for i in range(0, len(series)+1-length):
        res.append(slice(series, i, length))

    return res

def slice(series, start, length):
    return "".join(series[start:start+length])
import math

def find(search_list, value):
    s = len(search_list)
    if s == 0:
        raise ValueError("value not in array")

    low, high = 0, s - 1
    
    while True:
        i = math.floor(((high - low) / 2)) + low
        e = search_list[i]
        if e == value:
            return i
    
        if low == high:
            raise ValueError("value not in array")

        if e > value:
            high = i
        else:
            low = i + 1
    
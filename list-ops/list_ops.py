def append(list1, list2):
    return list1 + list2

def concat(lists):
    out_list = []
    for list in lists:
        out_list += list
    return out_list

def filter(function, elems):
    res = list()
    for e in elems:
        if function(e):
            res.append(e)
    
    return res


def length(list):
    return len(list)


def map(function, elems):
    for i, e in enumerate(elems):
        elems[i] = function(e)
    
    return elems


def foldl(function, list, initial):
    acc = initial
    for e in list:
        acc = function(acc, e)
    
    return acc


def foldr(function, list, initial):
    for element in list[::-1]:
        initial = function(element, initial)
    return initial


def reverse(elems):
    res = list()
    i = len(elems) - 1
    while i >= 0:
        res.append(elems[i])
        i -= 1

    return res

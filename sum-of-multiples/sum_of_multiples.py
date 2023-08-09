def sum_of_multiples(limit, multiples):
    res = set()
    for multiple in multiples:
        if multiple == 0:
            continue

        i = 0
        while True:
            i += 1
            n = multiple * i
            if n >= limit:
                break
            else:
                res.add(n)

    sum = 0
    for n in res:
        sum += n
    
    return sum

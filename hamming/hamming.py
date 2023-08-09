def distance(strand_a, strand_b):
    len_a, len_b = len(strand_a), len(strand_b)
    if len_a != len_b:
        raise ValueError("Strands must be of equal length.")

    res = 0
    for i in range(len_a):
        if strand_a[i] != strand_b[i]:
            res += 1
    
    return res

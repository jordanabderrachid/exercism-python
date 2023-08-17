# def fibo(n):
#     if n == 0:
#         return 0

#     if n == 1:
#         return 1

#     return fibo(n - 1) + fibo(n - 2)


def triplets_with_sum(N):
    res = []
    for a in range(1, N):
        D = N - a
        c = (D * D - a * a) / (2 * D)
        b = D - c

        if c.is_integer() and c > 0:
            triplet = sorted([a, int(b), int(c)])
            try:
                res.index(triplet)
            except ValueError:
                res.append(triplet)

    return res
    # iter = True
    # n = 1
    # while iter:
    #     a = fibo(n) * fibo(n + 3)
    #     b = 2 * fibo(n + 1) * fibo(n + 2)
    #     c = fibo(n + 1) * fibo(n + 1) + fibo(n + 2) * fibo(n + 2)

    #     n += 1
    #     if a + b + c == number:
    #         res.append(sorted([a, b, c]))

    #     if a > number:
    #         iter = False

    # triplets = [[], [], [], [4, 3, 5]]
    # res = []
    # n = 3
    # iterate = True
    # while iterate:
    #     [a, b, c] = triplets[n]
    #     if a + b + c == number:
    #         res.append(sorted([a, b, c]))

    #     if a + b + c > number:
    #         iterate = False
    #     n += 1
    #     triplets.append([a + b + c, fibo(2 * n - 1) - b, fibo(2 * n)])

    return res

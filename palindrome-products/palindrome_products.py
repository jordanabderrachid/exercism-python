def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    # return find_palindromes(
    #     min_factor, max_factor, lambda value, current: value > current
    # )
    max_palindrome = find_max_palindrome(min_factor, max_factor)
    return (max_palindrome, find_factors(max_palindrome, min_factor, max_factor))


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    min_palindrome = find_min_palindrome(min_factor, max_factor)
    return (min_palindrome, find_factors(min_palindrome, min_factor, max_factor))
    # return find_palindromes(
    #     min_factor, max_factor, lambda value, current: value < current
    # )


def find_min_palindrome(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor, max_factor + 1):
            pal = i * j

            if is_palindrome(str(pal)):
                next_min_factor = min(i, j)
                next_max_factor = max(i, j)
                if next_min_factor == next_max_factor:
                    return pal
                else:
                    next_pal = find_min_palindrome(next_min_factor + 1, next_max_factor)
                    if next_pal is None:
                        return pal

                    return min(pal, next_pal)

    return None


def find_max_palindrome(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    amp = max_factor - min_factor
    for i in range(0, amp + 1):
        for j in range(0, amp + 1):
            left = max_factor - i
            right = max_factor - j
            pal = left * right
            if is_palindrome(str(pal)):
                next_min_factor = min(left, right)
                next_max_factor = max(left, right)
                if next_min_factor == next_max_factor:
                    return pal

                next_pal = find_max_palindrome(next_min_factor + 1, next_max_factor)
                if next_pal is None:
                    return pal

                return max(pal, next_pal)

    return None


# def find_min_palindrome(factor, max_factor):
#     left = factor
#     right = factor
#     while left <= max_factor:
#         v = left * right
#         if is_palindrome(str(v)):
#             return v

#         right += 1
#         v = left * right
#         if is_palindrome(str(v)):
#             return v

#         left += 1

#     return None


def find_factors(target, min_factor, max_factor):
    if target is None:
        return []

    factors = []
    for left in range(min_factor, max_factor + 1):
        if target % left == 0:
            right = target // left
            if right >= min_factor and right <= max_factor:
                factors.append([left, right])

    return factors


def is_palindrome(value):
    if len(value) <= 1:
        return True

    if value[0] != value[len(value) - 1]:
        return False

    return is_palindrome(value[1 : len(value) - 1])


# 10..99
# 10*10 = 100
# 10*11 = 110
# 11*11 = 121

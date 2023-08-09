def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    factor_list = factors(number)
    sum = 0
    for f in factor_list:
        sum += f

    if sum == number:
        return "perfect"

    if sum > number:
        return "abundant"
    
    return "deficient"

def factors(n):
    res = list()
    for i in range(n-1):
        d = i + 1
        if n % d == 0:
            res.append(d)

    return res

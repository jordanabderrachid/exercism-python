def square_of_sum(n):
    sum = 0
    for i in range(n+1):
        sum += i
    
    return sum * sum


def sum_of_squares(n):
    squares = list()
    for i in range(n+1):
        squares.append(i*i)

    sum = 0
    for o in squares:
        sum += o
    
    return sum


def difference_of_squares(n):
    return square_of_sum(n) - sum_of_squares(n)

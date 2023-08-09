def is_armstrong_number(number):
    armstrong = 0
    stringified = str(number)
    number_length = len(stringified)
    for d in stringified:
        armstrong += int(d) ** number_length

    return armstrong == number

import re

regex_no_dash = re.compile(r'^(\d{9})(\d|X)$')
regex_dashes = re.compile(r'^(\d)-(\d{3})-(\d{5})-(\d|X)$')

def is_valid(isbn):
    numbers = list()
    match = regex_no_dash.search(isbn)
    if match:
        numbers += list(match.group(1))
        numbers.append(match.group(2))

    match = regex_dashes.search(isbn)
    if match:
        numbers.append(match.group(1))
        numbers += list(match.group(2))
        numbers += list(match.group(3))
        numbers.append(match.group(4))

    if len(numbers) == 0:
        return False

    numbers = map(lambda n: 10 if n == "X" else int(n), numbers)
    sum = 0
    for i, n in enumerate(numbers):
        sum += (10 - i) * n
    
    return sum % 11 == 0

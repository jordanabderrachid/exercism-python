import math

def square_root(number):
    guess = math.floor(number / 2) + 1

    while guess * guess != number:
        guess = math.floor((guess + (number/guess))/2)
    
    return guess

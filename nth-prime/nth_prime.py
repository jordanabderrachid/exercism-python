def is_prime(n, primes):
    for i in primes:
        if n % i == 0:
            return False
        
    return True

def is_even(n):
    return n % 2 == 0

def next_prime(f, primes):
    print(f"next prime {f}\n")
    if is_even(f):
        next = f + 1
    else:
        next = f + 2
    
    while True:
        if is_prime(next, primes):
            return next
        next += 2

def prime(number):
    if number == 0:
        raise ValueError("there is no zeroth prime")

    primes = [2]
    curr = 2
    while len(primes) != number:
        next = next_prime(curr, primes)
        primes.append(next)
        print(f"found {len(primes)} primes")
        curr = next
    
    return primes.pop()

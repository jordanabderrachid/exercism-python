import math

def factors(value):
    factors = list()
    
    prime_list = [2]
    current_prime = 2
    while value > 1:
        print(f"testing {current_prime}")
        if value % current_prime == 0:
            factors.append(current_prime)
            value /= current_prime
        else:
            prime_list.append(current_prime)
            current_prime = next_prime(prime_list)

    return factors

def is_even(n):
    return n % 2 == 0

def next_prime(prime_list):
    def is_prime(n):
        sq_n = math.sqrt(n)
        for p in prime_list:
            if n % p == 0:
                return False
            
            if p > sq_n:
                return True

        return True
    
    prev = prime_list[-1]
    next = prev + 1 if is_even(prev) else prev + 2
    while True:
        if is_prime(next):
            return next
        next += 2

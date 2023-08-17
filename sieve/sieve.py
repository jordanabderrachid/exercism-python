def primes(limit):
    candidates = [i for i in range(2, limit + 1)]
    primes = []
    while len(candidates) > 0:
        prime = candidates[0]
        primes.append(prime)

        to_remove = prime
        below_limit = True
        while below_limit:
            try:
                candidates.remove(to_remove)
            except ValueError:
                pass

            to_remove += prime
            if to_remove >= limit + 1:
                below_limit = False

    return primes

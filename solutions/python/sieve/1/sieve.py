def primes(limit):
    if limit < 2:
        return []

    # start with all numbers marked as potential primes
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= limit:
        if is_prime[p]:
            # mark multiples of p as not prime
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
        p += 1

    # collect primes
    return [i for i, prime in enumerate(is_prime) if prime]
def prime(n):
    if n < 1:
        raise ValueError("there is no zeroth prime")

    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    count = 0
    num = 1

    while True:
        num += 1
        if is_prime(num):
            count += 1
            if count == n:
                return num
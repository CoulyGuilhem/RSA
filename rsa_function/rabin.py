import random


def rabin_miller_test(n, d):
    a = random.randint(2, n - 2)
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False


def is_prime_rabin_miller(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    d = n - 1
    while d % 2 == 0:
        d //= 2
    for _ in range(k):
        if not rabin_miller_test(n, d):
            return False
    return True


def generate_prime(size=10, k=5):
    lower_bound = 10 ** (size - 1)
    upper_bound = (10 ** size) - 1
    while True:
        candidate = random.randint(lower_bound, upper_bound)
        if candidate % 2 == 0:
            candidate += 1
        if is_prime_rabin_miller(candidate, k):
            return candidate

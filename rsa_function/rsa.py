from rsa_function.encrypt import encrypt_message
from rsa_function.decrypt import decrypt_message
from rsa_function.rabin import generate_prime
import random
from math import gcd


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def find_d(e, phi_n):
    gcd, d, _ = extended_gcd(e, phi_n)
    if gcd != 1:
        raise ValueError("Pas de valeur pour d trouvée")
    return d % phi_n


def find_e(phi_n):
    while True:
        e = random.randint(2, phi_n - 1)
        if gcd(e, phi_n) == 1:
            return e


def key_gen(size=10):
    p = generate_prime(size=size)
    q = generate_prime(size=size)
    while p == q:
        q = generate_prime(size=size)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = find_e(phi_n)
    d = find_d(e, phi_n)
    return (n, e), (n, d)


def encrypt(message, e, n):
    return encrypt_message(message, e, n)


def decrypt(encrypted_message, d, n):
    return decrypt_message(encrypted_message, d, n)

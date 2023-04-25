import random


def fast_pow(x, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return x * (fast_pow(x, (n - 1) / 2))**2
    return fast_pow(x, n/2)**2


def mod_fast_pow(base, exponent, mod):
    if mod == 1:
        return 0

    result = 1
    base = base % mod

    while exponent > 0:
        if exponent % 2:
            result = (result * base) % mod
            exponent -= 1
        else:
            base = (base**2) % mod
            exponent //= 2

    return result % mod


def fermat_primality_test(n, k):
    for i in range(k):
        a = random.randint(1, n)

        if mod_fast_pow(a, n - 1, n) != 1:
            return False

    return True


def miller_rabin_alg(d, n):
    a = 2 + random.randint(1, n - 4)

    x = mod_fast_pow(a, d, n)

    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = (x**2) % n
        d *= 2

        if x == 1:
            return False
        if x == n - 1:
            return True

    return False


def m_r_primality_test(n, k):
    d = n - 1

    while d % 2 == 0:
        d //= 2

    for i in range(k):
        if not miller_rabin_alg(d, n):
            return False

    return True


print(fermat_primality_test(100, 10))
# print(m_r_primality_test(100, 10))

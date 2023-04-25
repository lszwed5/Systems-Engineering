from Lista06zad01 import prime_factorization
from timeit import timeit
import matplotlib.pyplot as plt


def RNWD(a, b):
    result = 1
    result_factors = []
    a_factors = prime_factorization(a)
    b_factors = prime_factorization(b)

    a_factors.sort(reverse=True)
    b_factors.sort(reverse=True)

    if len(a_factors) >= len(b_factors):
        iterator, validator = a_factors, b_factors
    else:
        iterator, validator = b_factors, a_factors

    for i in iterator:
        if i in validator:
            result_factors.append(i)
            validator.remove(i)

    for i in result_factors:
        result *= i

    return result


def ENWD(a, b):
    if a == 0:
        return b

    return ENWD(b % a, a)


def compare_time(n, m, iterations=10):
    RNWD_times, ENWD_times = [], []
    q = 1

    while q < m:
        RNWD_times.append(timeit(lambda: RNWD(n, q),
                                 number=iterations) / iterations)

        ENWD_times.append(timeit(lambda: ENWD(n, q),
                                 number=iterations) / iterations)

        q += 1

    x = range(1, q)

    plt.figure()
    plt.plot(x, RNWD_times, label='RNWD')
    plt.plot(x, ENWD_times, label='ENWD')
    plt.title(f'Comparison of gcd algorithms for {n}')
    plt.xlabel('q')
    plt.ylabel('Time [s]')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(RNWD(a, b))
    print(ENWD(a, b))

    compare_time(10000, 500)

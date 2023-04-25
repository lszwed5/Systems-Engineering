def prime_factorization(number, factor=2):
    if number < factor:
        return []
    if number % factor == 0:
        return [factor] + prime_factorization(number / factor, 2)
    return prime_factorization(number, factor + 1)


if __name__ == '__main__':
    n = int(input("Enter the desired number n: "))
    print(prime_factorization(n))

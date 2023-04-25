def eratosthenes_sieve(p):
    x = [True for _ in range(p + 1)]

    for n in range(2, int(p**(1/2) + 1)):
        if x[n]:
            for j in range(2, int(p/n) + 1):
                i = n*j
                x[i] = False

    return x


if __name__ == '__main__':
    p = int(input("Enter the value of p: "))
    if p < 1:
        raise ValueError('The value of p must be more than 1.')


    x = eratosthenes_sieve(p)
    for i in range(2, p + 1):
        if x[i]:
            print(i)

    # print(eratosthenes_sieve(p))

import math
from sympy import fft, ifft


def FFT(P):
    n = len(P)
    if n == 1:
        return P
    w = math.e ** ((2 * math.pi * complex(0, 1)) / n)
    Pe, Po = P[::2], P[1::2]
    ye, yo = FFT(Pe), FFT(Po)
    y = [0] * n
    for j in range(n//2):
        y[j] = ye[j] + w**j * yo[j]
        y[j + int(n/2)] = ye[j] - w**j * yo[j]

    return y


def IFFT(P):
    n = len(P)
    if n == 1:
        return P
    w = (1/n) * (math.e ** ((-2 * math.pi * complex(0, 1)) / n))
    Pe, Po = P[::2], P[1::2]
    ye, yo = IFFT(Pe), IFFT(Po)
    y = [0] * n
    for j in range(n//2):
        y[j] = abs(ye[j] + w**j * yo[j])
        y[j + int(n/2)] = abs(ye[j] - w**j * yo[j])

    return y


if __name__ == '__main__':
    signal = [1, 2, 3, 4]

    print(FFT(signal))
    # print(ifft(fft(signal)))

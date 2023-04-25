import matplotlib.pyplot as plt
from timeit import timeit
from random import randint
from Lista07zad01 import naive_polynomial_multiplication
from Lista07zad03 import fft_polynomial_multiplication


def calc_execution_times(pol_1, pol_2, iterations=3):
    naive_time = timeit(lambda: naive_polynomial_multiplication(pol_1, pol_2),
                        number=iterations) / iterations

    fft_time = timeit(lambda: fft_polynomial_multiplication(pol_1, pol_2),
                      number=iterations) / iterations

    return naive_time, fft_time


span = [2 ** i for i in range(1, 10)]

naive_times, fft_times = [], []
for coef_num in span:
    first_pol = [randint(0, 10) for _ in range(int(coef_num))]
    second_pol = [randint(0, 10) for _ in range(int(coef_num))]

    naive, fft = calc_execution_times(first_pol, second_pol)
    naive_times.append(naive)
    fft_times.append(fft)

plt.figure()
plt.plot(span, naive_times, label='naive')
plt.plot(span, fft_times, label='fft')
plt.title(f'Comparison of polynomial multiplication algorithms performance')
plt.xlabel('Number of coefficients')
plt.ylabel('Time [s]')
plt.legend()
plt.show()

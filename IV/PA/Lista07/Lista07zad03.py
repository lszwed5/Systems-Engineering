from Lista07zad01 import naive_polynomial_multiplication, print_result
from Lista07zad02 import FFT
from sympy import ifft


def fft_polynomial_multiplication(pol_1, pol_2):
    pol_1 += [0] * len(pol_1)
    pol_2 += [0] * len(pol_2)
    trans_pol_1 = FFT(pol_1)
    trans_pol_2 = FFT(pol_2)
    fourier_result = []
    for i in range(len(trans_pol_1)):
        fourier_result.append(trans_pol_1[i] * trans_pol_2[i])

    return fourier_result


if __name__ == '__main__':
    first_pol = [2, 3]
    second_pol = [3, 2]

    naive_result = naive_polynomial_multiplication(first_pol, second_pol)
    print_result(naive_result)

    fft_result = ifft(fft_polynomial_multiplication(first_pol, second_pol))
    fft_result = [float(round(
        (complex(number).real**2 + complex(number).imag**2)**(1/2), 2))
        for number in fft_result]
    print_result(fft_result)

def naive_polynomial_multiplication(pol_1, pol_2):
    result = [0] * (len(pol_1) + len(pol_2) - 1)
    for i in range(len(pol_1)):
        for j in range(len(pol_2)):
            result[i + j] += pol_1[i] * pol_2[j]

    return result


def print_result(polynomial):
    print()
    for i in range(len(polynomial)):
        print(polynomial[i], end="")
        if i != 0 and i != 1:
            print(f"x^{i}", end="")
        if i == 1:
            print("x", end="")
        if i != len(polynomial) - 1:
            print(" + ", end="")
    print()


if __name__ == '__main__':
    first_pol = [1, 3, 6, 9]
    second_pol = [3, 2, 2]

    print_result(naive_polynomial_multiplication(first_pol, second_pol))

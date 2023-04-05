import math


"-------------------------------- Sequence 1 --------------------------------"


def recursive_alg_1(n):
    if n == 0:
        return 1
    else:
        return 3**n + recursive_alg_1(n-1)


#                               n
# Analytic solution: X(n) = 1 + Σ (3^i)
#                              i=1


def analytic_alg_1(n):
    n_val = 1
    for i in range(1, n + 1):
        n_val += 3**i

    return n_val


"-------------------------------- Sequence 2 --------------------------------"


def recursive_alg_2(n):
    if n == -1 or n == 0:
        return 0
    else:
        return n + recursive_alg_2(n - 2)


# Analytic solution: X(n) = ((n + 1) // 2) * (((n + 1) // 2) + ((n + 1) % 2))


def analytic_alg_2(n):
    return ((n + 1) // 2) * (((n + 1) // 2) + ((n + 1) % 2))


"-------------------------------- Sequence 3 --------------------------------"


def recursive_alg_3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_alg_3(n - 1) + recursive_alg_3(n - 2)


# Analytic solution: round( (1 + sqrt(5))**n / 2**n * sqrt(5) )


def analytic_alg_3(n):
    return round(((1 + math.sqrt(5))**n) / (2**n * math.sqrt(5)))


"------------------------------- Verification -------------------------------"


def verify(recursive_alg, analytic_form, n_first_values):
    rec, form = [], []
    for i in range(n_first_values):
        rec.append(recursive_alg(i))
        form.append(analytic_form(i))
        print(f'\nn = {i}')
        print(f"Recursive function output: {rec[i]}")
        print(f"Analytic function output: {form[i]}")
        print()

    if rec == form:
        print(f"The results for {n_first_values} first values are correct")
    else:
        print(f"The results for {n_first_values} first values are not correct")


print("\n" + 60*"-")
print("\nFirst algorithm validation")
verify(recursive_alg_1, analytic_alg_1, 10)

print("\n" + 60*"-")
print("\nSecond algorithm validation")
verify(recursive_alg_2, analytic_alg_2, 10)

print("\n" + 60*"-")
print("\nThird algorithm validation")
verify(recursive_alg_3, analytic_alg_3, 10)

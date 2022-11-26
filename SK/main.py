import math
import numpy as np
from scipy import stats
from numpy.random import normal, uniform
import matplotlib.pyplot as plt


# Generate the normal distribution sample
normal_data = normal(loc=0, scale=1, size=100)

# Generate the uniform distribution
uniform_data = uniform(low=0.0, high=100, size=100)

for index_ in range(len(uniform_data)):
    uniform_data[index_] = math.floor(uniform_data[index_])


def save_to_txt(data, filename):
    with open(filename, "w") as f:
        for item in data:
            f.write(str(item) + "\n")


def load_from_txt(filename):
    with open(filename, "r") as f:
        data = f.read().splitlines()
        data = np.array([float(i) for i in data])
        return data


def info(data):
    mean = np.mean(data)
    median = np.median(data)
    print(f"The mean of this dataset is {mean}")
    print(f"The median of this dataset is {median}")
    skewness = 3 * (mean - median) / np.std(data)
    print(f"The skewness of this dataset is {skewness}")
    # print(scipy.stats.skew(data))
    h1 = (len(data) * (len(data) + 1)) / ((len(data) - 1) * (len(data) - 2) * (len(data) - 3))
    h2 = sum([((i - mean) / np.std(data)) ** 4 for i in data])
    h3 = (3 * (len(data) - 1) ** 2) / ((len(data) - 2) * (len(data) - 3))
    kurtosis = h1 * h2 - h3
    print(f"The kurtosis of this dataset is {kurtosis}")
    # print(scipy.stats.kurtosis(data))


def chi_square_normal_test(data):
    expected = np.median(data)
    value = sum([((i - expected) ** 2) / expected for i in data])
    # print(f"Value of the chi-square statistic: {value}")
    if value < 124.342:
        print("Data most likely come from a normal distribution \n(statistical significance 0.05)")
    else:
        print("Data most likely do not come from a normal distribution \n(statistical significance 0.05)")
    # print(stats.chisquare(data))


def chi_square_uniform_test(data):
    expected = 10
    data_bins = [0] * 10

    bin_width = math.ceil((max(data) - min(data)) / 10)
    for record in data:
        data_bins[int(record) // bin_width] += 1

    value = sum([((bin_ - expected) ** 2) / expected for bin_ in data_bins])
    # print(data_bins)
    # print(f"Value of the chi-square statistic: {value}")
    if value < 18.307:
        print("Data most likely come from a uniform distribution \n(statistical significance 0.05)")
    else:
        print("Data most likely do not come from a uniform distribution \n(statistical significance 0.05)")


def lcg_uniform_generator(seed, size, top=2**32):
    result = []
    multiplier = 22695477
    increment = 1
    modulus = top
    for i in range(size):
        result.append(((multiplier * seed) + increment) % modulus)
        seed += 1
    result = np.array(result)
    return result


def box_muller_generator():
    uniform1 = np.random.uniform(0, 1, 100)
    uniform2 = np.random.uniform(0, 1, 100)
    dataset = np.zeros(100)
    for i in range(1, 100):
        dataset[i-1] = ((-2*np.log(uniform1[i-1]))**0.5)*math.cos(2*3.14*uniform2[i-1])
    return dataset


def wilcoxon_test(dataset1, dataset2):
    pvalue = stats.wilcoxon(dataset1, dataset2)[1]
    print(pvalue)
    if pvalue > 0.05:
        print("Datasets most likely come from the same distribution")
    else:
        print("Datasets most likely do not come from the same distribution")


def student_t_test(dataset1, dataset2):
    pvalue = stats.ttest_ind(dataset1, dataset2)[1]
    print(pvalue)
    if pvalue > 0.05:
        print("Datasets most likely come from the same distribution")
    else:
        print("Datasets most likely do not come from the same distribution")


def scatter_plot(dataset):
    index = np.linspace(0, 100, 100)
    plt.scatter(index, dataset)
    plt.show()

# For 22.11.2022


def function_x(x):
    return x**5


def monte_carlo_integral(start, stop, function):
    sign = 1
    if start > stop:
        start, stop = stop, start
        sign = -1
    number_of_points = 10000
    counter = 0
    x_coordinates = uniform(low=start, high=stop, size=number_of_points)
    y_abs_max = function(x_coordinates[0])

    for arg in x_coordinates:
        y = function(arg)
        if abs(y) > abs(y_abs_max):
            y_abs_max = y

    y_coordinates = uniform(low=0, high=abs(y_abs_max), size=number_of_points)

    plt.scatter(x_coordinates, y_coordinates)
    plt.scatter(x_coordinates, function(x_coordinates))
    plt.show()

    for i in range(number_of_points):
        if y_coordinates[i] <= abs(function(x_coordinates[i])):
            if function(x_coordinates[i]) >= 0:
                counter += 1
            else:
                counter -= 1

    ans = sign * counter/number_of_points * ((stop - start) * abs(y_abs_max))
    print(f"Approximated value of the integral is {ans}")


def riemann_integral(start, stop, function):
    number_of_fields = 10000
    sign = 1
    if start > stop:
        start, stop = stop, start
        sign = -1

    integration_step = (stop - start) / number_of_fields
    x = start
    ans = 0

    for _ in range(number_of_fields):
        ans += integration_step * function(x)
        x += integration_step

    print(f"Approximated value of the integral is {sign*ans}")


def monte_carlo_area_approximation(figure):
    """Calculates the approximate area value of a 2D Figure.
    FORMAT: Figure should be described by an array of FUNCTIONS and their ranges - [[start, stop, function]]
        example:
        [[3, 9, lambda x: 1/3 * x + 10],
        [5, 9, lambda x: 2*x - 5],
        [5, 6, lambda x: 5*x - 20],
        [3, 6, lambda x: -1/3*x + 12]]"""
    figure = np.array(figure)
    number_of_points = 10000
    counter = 0
    x_min = min(figure.T[0])
    x_max = max(figure.T[1])
    y_min = figure[0][2](figure[0][0])
    y_max = figure[0][2](figure[0][0])
    for i in range(len(figure)):
        y1 = figure.T[2][i](figure.T[0][i])
        y2 = figure.T[2][i](figure.T[1][i])
        if y1 < y_min:
            y_min = y1
        if y1 > y_max:
            y_max = y1
        if y2 < y_min:
            y_min = y2
        if y2 > y_max:
            y_max = y2

    x_coordinates = uniform(low=x_min, high=x_max, size=number_of_points)
    y_coordinates = uniform(low=y_min, high=y_max, size=number_of_points)

    plt.scatter(x_coordinates, y_coordinates)
    for side in figure:
        x_coord = np.linspace(side[0], side[1], 100)
        plt.scatter(x_coord, side[2](x_coord))
    plt.show()

    for i in range(number_of_points):
        crosses = 0
        for j in range(len(figure.T[2])):
            if figure.T[0][j] < x_coordinates[i] < figure.T[1][j]:
                if y_coordinates[i] > figure.T[2][j](x_coordinates[i]):
                    crosses += 1
        if crosses % 2 == 1:
            counter += 1

    ans = counter/number_of_points * ((x_max-x_min)*(y_max-y_min))
    print(f"Approximated area of this figure is {ans}")


"""------------------------------------------------------------------------------------------------------------------"""
# save_to_txt(normal_data, "normal.txt")
# save_to_txt(uniform_data, "uniform.txt")
#
# normal_dataset = load_from_txt("normal.txt")
# uniform_dataset = load_from_txt("uniform.txt")
#
# info(normal_dataset)
# print()
# info(uniform_dataset)
# print()
#
#
# # scatter_plot(normal_dataset)
# # scatter_plot(uniform_dataset)
#
# chi_square_normal_test(normal_dataset)
# print()
# chi_square_uniform_test(uniform_dataset)
#
#
# lcg_dataset = lcg_uniform_generator(seed=5, size=100, top=100)
# box_muller_dataset = box_muller_generator()
#
# wilcoxon_test(uniform_dataset, lcg_dataset)
# student_t_test(box_muller_dataset, normal_dataset)

"""------------------------------------------------------------------------------------------------------------------"""

monte_carlo_integral(0, 100, lambda x: x**5)
riemann_integral(0, 100, function_x)

fig1 = [[3, 9, lambda x: 1/3 * x + 10],
        [5, 9, lambda x: 2*x - 5],
        [5, 6, lambda x: 5*x - 20],
        [3, 6, lambda x: -1/3*x + 12]]

monte_carlo_area_approximation(fig1)

"""------------------------------------------------------------------------------------------------------------------"""


"""
Do 21.11 do 7 rano ma być na Teams

Metoda Monte Carlo:
1. Obliczyć całkę oznaczoną metodą Monte Carlo z funkcji:
    f(początek przedziału, koniec przedziału, funkcja całkowana)
    
2. Obliczyć tę samą całkę metodą Riemanna (trzeba zaimplementować)

3. Porównać te dwa wyniki

2> METODA MONTE CARLO DO LICZENIA POLA FIGURY NIESYMETRYCZNEJ
Sugestia:
1. Nałożyć na to siatkę symetryczną
2. Z każdego kawałka siatki wyliczać pole i zsumować

------------------------------------------------------------------------------------------------------------------------

Na 22.11 trzeba mieć pomysł na projekt, wiedzieć co się chce robić
29.11 - ostateczna decyzja

1) Wybór tematu
2) Określenie zmiennych i parametrów
    Określenie zmiennych decyzyjnych
3) Wyznaczenie kryteriów oceny systemu (max 2)

Czas na to do świąt

Musi być możliwość parametryzowania modelu (okienko z możliwością wyboru parametrów)

Końcowo: Sprawozdanie (ok. 2 strony)

NIE MODELOWAĆ FIZYCZNYCH ZJAWISK
"""

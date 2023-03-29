import math
import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew
import nolds
from sklearn import preprocessing


"----------------------------------- Data -----------------------------------"

N = 505
t = np.arange(N)
time_range = pd.date_range(start='2020-01-01', end='2020-01-22', freq='H')
y = np.random.normal(loc=1, scale=0.03, size=N)

plt.figure(figsize=(10, 3))
plt.plot(time_range, y, label='x')
plt.legend()
plt.show()

"---------------------------------- Zad 01 ----------------------------------"


def get_stats(arr):
    mean = float(sum(arr) / len(arr))
    variance = float(abs(sum([(v - mean) ** 2 for v in arr]) / mean))
    std_deviation = float(math.sqrt(variance))
    max_value = float(max(arr))
    min_value = float(min(arr))
    median = float(statistics.median(arr))
    kurt = float(kurtosis(arr))
    skewness = float(3 * (mean - median) / std_deviation)

    print(f"The mean of given data is {mean}")
    print(f"The variance of given data is {variance}")
    print(f"The standard deviation of given data is {std_deviation}")
    print(f"The max value of given data is {max_value}")
    print(f"The min value of given data is {min_value}")
    print(f"The median of given data is {median}")
    print(f"The kurtosis of given data is {kurt}")
    print(f"The skewness of given data is {skewness}")


print("\n" + 26 * "-" + " Zad 1 " + 26 * "-" + "\n")
get_stats(y)

"---------------------------------- Zad 02 ----------------------------------"


def get_fancy_stats(arr):
    entropy = nolds.sampen(arr)
    fractal_dim = nolds.corr_dim(arr, emb_dim=2)
    hurts_exponent = nolds.hurst_rs(arr)

    print(f"The entropy of y is {entropy}")
    print(f"The fractal dimension of y is {fractal_dim}")
    print(f"The Hurst exponent of y is {hurts_exponent}")


print("\n" + 26 * "-" + " Zad 2 " + 26 * "-" + "\n")
get_fancy_stats(y)

"---------------------------------- Zad 03 ----------------------------------"

start = 100
stop = 228

plt.figure(figsize=(10, 3))
plt.plot(time_range, y, label='x')
plt.axvline(x=time_range[start], color='red')
plt.axvline(x=time_range[stop], color='red')
plt.legend()
plt.show()

window_y = y[start:stop]

print("\n" + 26 * "-" + " Zad 3 " + 26 * "-" + "\n")
get_stats(window_y)
print()
get_fancy_stats(window_y)

"---------------------------------- Zad 04 ----------------------------------"

start = 100
stop = 228

window_y = y[start:stop]
y_norm = np.array(preprocessing.MinMaxScaler().fit_transform(y.reshape(-1, 1)))

plt.figure(figsize=(10, 3))
plt.plot(time_range, y_norm, label='x')
plt.legend()
plt.show()

print("\n" + 20 * "-" + " Zad 4 - Normalised " + 20 * "-" + "\n")
get_stats(y_norm)
print()
get_fancy_stats(y_norm)


y_stand = np.array(preprocessing.StandardScaler().fit_transform(
    y.reshape(-1, 1)))

print("\n" + 18 * "-" + " Zad 4 - Standardised " + 18 * "-" + "\n")
get_stats(y_stand)
print()
get_fancy_stats(y_stand)
print("\n" + 60*"-")

"-----------------------------------------------------------------------------"

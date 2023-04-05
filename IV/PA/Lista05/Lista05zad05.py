import numpy as np
from numpy.random import randint
from timeit import timeit
from Lista05zad02 import recursive_max_val, recursive_second_max_val, \
    recursive_average
from Lista05zad03 import merge_sort
from matplotlib import pyplot as plt

start = int(input("Enter the start of the range: "))
stop = int(input("Enter the stop of the range: "))
iterations = int(input("Enter the number of iterations to time: "))
interval = (stop - start + 1) // 100
span = np.linspace(start=start, stop=stop, num=interval)

merge_sort_times = []
recursive_max_times, recursive_second_max_times = [], []
recursive_average_times = []

for n in span:
    n = int(n)
    if n == 0:
        continue

    input_list = [randint(0, 10000) for _ in range(n)]
    recursive_max_times.append(timeit(lambda: recursive_max_val(input_list),
                                      number=iterations) / iterations)
    recursive_second_max_times.append(timeit(
        lambda: recursive_second_max_val(input_list),
        number=iterations) / iterations)
    recursive_average_times.append(timeit(
        lambda: recursive_average(input_list), number=iterations) / iterations)
    merge_sort_times.append(timeit(lambda: merge_sort(input_list),
                                   number=iterations) / iterations)


fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(span, recursive_max_times)
ax1.set_title('Recursive max number')
ax1.set_xlabel('n')
ax1.set_ylabel('Time [s]')

ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(span, recursive_second_max_times)
ax2.set_title('Recursive second max number')
ax2.set_xlabel('n')
ax2.set_ylabel('Time [s]')

ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(span, recursive_average_times)
ax3.set_title('Recursive average')
ax3.set_xlabel('n')
ax3.set_ylabel('Time [s]')

ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(span, merge_sort_times)
ax4.set_title('Merge Sort')
ax4.set_xlabel('n')
ax4.set_ylabel('Time [s]')

plt.tight_layout()
plt.show()

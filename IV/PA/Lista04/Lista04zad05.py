import numpy as np
from random import randint
from timeit import timeit
from matplotlib import pyplot as plt
from Lista04zad01 import find_max_number, find_second_max_number, \
    find_avg_of_list
from Lista04zad02 import multiplication_comprehensions
from Lista04zad03 import subset_sum


"""--------------------------------- Input ---------------------------------"""

print("\n" + 26*"-" + " Zad 1 " + 26*"-" + "\n")

start = int(input("Enter the start of the range: "))
stop = int(input("Enter the stop of the range: "))
interval = int(input("Enter the desired number of samples: "))
iterations = int(input("Enter the number of iterations to time: "))
span = np.linspace(start=start, stop=stop, num=interval)

print("\n" + 25*"-" + " Zad 2 & 3 " + 25*"-" + "\n")
start_1 = int(input("Enter the start of the range: "))
stop_1 = int(input("Enter the stop of the range: "))
interval_1 = int(input("Enter the desired number of samples: "))
iterations_1 = int(input("Enter the number of iterations to time: "))
span_1 = np.linspace(start=start_1, stop=stop_1, num=interval_1)

print("\n" + 60*"-")

"""----------------------------- Computations -----------------------------"""

times_1_1, times_1_2, times_1_3, times_2, times_3 = [], [], [], [], []
for n in span:
    n = int(n)
    if n == 0:
        continue

    input_list = [randint(0, 100) for _ in range(n)]
    times_1_1.append(timeit(lambda: find_max_number(input_list),
                            number=iterations) / iterations)
    times_1_2.append(timeit(lambda: find_second_max_number(input_list),
                            number=iterations) / iterations)
    times_1_3.append(timeit(lambda: find_avg_of_list(input_list),
                            number=iterations) / iterations)


for n in span_1:
    n = int(n)
    if n == 0:
        continue

    matrix_1 = [[randint(0, 100) for _ in range(n)] for _ in range(n)]
    matrix_2 = [[randint(0, 100) for _ in range(n)] for _ in range(n)]
    times_2.append(timeit(
        lambda: multiplication_comprehensions(matrix_1, matrix_2),
        number=iterations) / iterations)

    numbers_set = [randint(0, 100) for _ in range(n)]
    times_3.append(timeit(
        lambda: subset_sum(set_=numbers_set, n=n, sum_=0),
        number=iterations) / iterations)


"""------------------------------- Plotting -------------------------------"""

fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(2, 3, 1)
ax1.plot(span, times_1_1)
ax1.set_title('find_max_number')
ax1.set_xlabel('n')
ax1.set_ylabel('Time [s]')

ax2 = fig.add_subplot(2, 3, 2)
ax2.plot(span, times_1_2)
ax2.set_title('find_second_max_number')
ax2.set_xlabel('n')
ax2.set_ylabel('Time [s]')

ax3 = fig.add_subplot(2, 3, 3)
ax3.plot(span, times_1_3)
ax3.set_title('input_list_avg')
ax3.set_xlabel('n')
ax3.set_ylabel('Time [s]')

ax4 = fig.add_subplot(2, 3, 4)
ax4.plot(span_1, times_2)
ax4.set_title('multiplication_comprehensions')
ax4.set_xlabel('n')
ax4.set_ylabel('Time [s]')

ax5 = fig.add_subplot(2, 3, 5)
ax5.plot(span_1, times_3)
ax5.set_title('subset_sum')
ax5.set_xlabel('n')
ax5.set_ylabel('Time [s]')

plt.tight_layout()
plt.show()

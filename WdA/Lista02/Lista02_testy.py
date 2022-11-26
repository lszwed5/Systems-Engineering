from Lista02zad01 import generate_random_array, bubble_sort, insertion_sort, selection_sort
import time
from math import log10


n = [10, 100, 1000]


def abbreviation(sorting_algorithm):
    print()
    for i in n:
        arr = generate_random_array(i)
        start = time.time()
        sorting_algorithm(arr)
        end = time.time() - start

        try:
            result = i * log10(i) / end
        except ZeroDivisionError:
            result = 0

        print(f"n = {i}\n"
              f"t(n) = {end}\n"
              f"(nlogn/t(n)) = {result}")
        print()
    print(50*"-")


print(50*"-")
print("Bubble sort: ")
abbreviation(bubble_sort)
print("Insertion sort: ")
abbreviation(insertion_sort)
print("Selection sort: ")
abbreviation(selection_sort)

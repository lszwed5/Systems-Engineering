from random import randint
from timeit import timeit
import Lista04zad01, Lista04zad02, Lista04zad03


n = int(input("Enter the length of the list to be generated: "))
iterations = int(input("Enter the number of iterations to time: "))

"""--------------------------------- Zad 1 ---------------------------------"""

input_list = [randint(0, 100) for _ in range(n)]


print("\n" + 26*"-" + " Zad 1 " + 26*"-")

print("\nThe average time of find_max_number execution:")
print(timeit(
    lambda: Lista04zad01.find_max_number(input_list),
    number=iterations) / iterations)

print("\nThe average time of find_second_max_number execution:")
print(timeit(
    lambda: Lista04zad01.find_second_max_number(input_list),
    number=iterations) / iterations)

print("\nThe average time of input_list_avg execution:")
print(timeit(
    lambda: Lista04zad01.find_avg_of_list(input_list),
    number=iterations) / iterations)

"""--------------------------------- Zad 2 ---------------------------------"""

matrix_1 = [[randint(0, 100) for _ in range(n)] for _ in range(n)]
matrix_2 = [[randint(0, 100) for _ in range(n)] for _ in range(n)]


print("\n" + 26*"-" + " Zad 2 " + 26*"-")

print("\nThe average time of list comprehension multiplication:")
print(timeit(
    lambda: Lista04zad02.multiplication_comprehensions(matrix_1, matrix_2),
    number=iterations) / iterations)

"""--------------------------------- Zad 3 ---------------------------------"""

numbers_set = [randint(0, 100) for _ in range(n)]


print("\n" + 26*"-" + " Zad 3 " + 26*"-")

print("\nThe average time of finding a subset:")
print(timeit(
    lambda: Lista04zad03.subset_sum(set_=numbers_set, n=n, sum_=0),
    number=iterations) / iterations)

print("\n" + 60*"-")

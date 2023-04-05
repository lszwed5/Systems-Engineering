import numpy as np
from numpy.random import randint


def recursive_max_val(arr):
    n = len(arr)

    if n == 1:
        return arr[0]
    else:
        divider = n // 2
        left_half = arr[0:divider]
        right_half = arr[divider:]

    if recursive_max_val(left_half) > recursive_max_val(right_half):
        return recursive_max_val(left_half)

    return recursive_max_val(right_half)

    # Time complexity: O(nlog n) / O(n)


def recursive_second_max_val(arr):
    max_val = recursive_max_val(arr)

    if len(arr) > 1:
        arr.remove(max_val)
    else:
        return arr[0]

    return recursive_max_val(arr)

    # Time complexity: O(2nlog n) = O(nlog n) / O(2n) = O(n)


def recursive_average(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    else:
        divider = n // 2
        left_half = arr[0:divider]
        right_half = arr[divider:]
        return (divider * recursive_average(left_half)
                + (n - divider) * recursive_average(right_half)) / n

    # Time complexity: O(nlog n)


if __name__ == '__main__':
    input_list = input("Enter a list of numbers separated by single space:\n")
    input_list = [float(number) for number in input_list.split(" ")]

    print(recursive_max_val(input_list))
    print(recursive_second_max_val(input_list))
    print(recursive_average(input_list))

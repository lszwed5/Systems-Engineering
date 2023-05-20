import matplotlib.pyplot as plt
from random import randint
from copy import deepcopy


start = 0
stop = 1000
number_of_indexes = 100
to_sort = [randint(start, stop) for _ in range(number_of_indexes)]
n = len(to_sort)
for_heap = deepcopy(to_sort)
for_quick = deepcopy(to_sort)

fig = plt.figure(figsize=(12, 4))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        ax1.cla()
        ax1.set_title('Heap Sort')
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
        ax1.bar(range(len(arr)), arr)
        plt.pause(0.01)


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


def partition(arr, low, high):
    ax2.cla()
    ax2.set_title('Quick Sort')
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            plt.cla()
            ax2.set_title('Quick Sort')
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            ax2.bar(range(len(arr)), arr)
            plt.pause(0.01)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    ax2.bar(range(len(arr)), arr)
    plt.pause(0.01)

    return i + 1


heap_sort(for_heap)
ax1.bar(range(len(for_heap)), for_heap, color='green')
quicksort(for_quick, 0, n - 1)
ax2.bar(range(len(for_quick)), for_quick, color='green')
plt.show()

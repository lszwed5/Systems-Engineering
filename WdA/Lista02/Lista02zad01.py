from matplotlib import pyplot as plt
import random
import time


def generate_random_array(n):
    """Generates an array of random integers between 0 and 1000"""
    list_ = []
    for _ in range(n):
        list_.append(random.randint(0, 1001))
    return list_


def bubble_sort(array):
    """Returns an ascending sorted array using bubble sort"""
    arr = array[:]
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


def insertion_sort(array):
    """Returns an ascending sorted array using insertion sort"""
    arr = array[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(array):
    """Returns an ascending sorted array using selection sort"""
    arr = array[:]
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


def bubble_sort_mod_1(array):
    """Returns an ascending sorted array using bubble sort with a stopper"""
    arr = array[:]
    for i in range(len(arr)):
        stopper = False
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                stopper = True
        if not stopper:
            break
    return arr


def bubble_sort_mod_2(array):
    """Returns an ascending sorted array using bubble sort with full traversing"""
    arr = array[:]
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


def measure_sort_time(function, n):
    """Measures the execution time of a given sort function on a given array with n values and returns
    the longest and the average time"""
    times = []
    for _ in range(10):
        arr = generate_random_array(n)
        start = time.time()
        function(arr)
        times.append(time.time() - start)
    avg_time = sum(times) / len(times)
    max_time = max(times)
    return avg_time, max_time


if __name__ == "__main__":
    x_labels = [10, 20, 50, 100, 200, 500, 1000]
    bubble_avgs, bubble_maxes = [], []
    insertion_avgs, insertion_maxes = [], []
    selection_avgs, selection_maxes = [], []

    for n in x_labels:
        bubble_maxes.append(measure_sort_time(bubble_sort, n)[0])
        bubble_avgs.append(measure_sort_time(bubble_sort, n)[1])

        insertion_avgs.append(measure_sort_time(insertion_sort, n)[0])
        insertion_maxes.append(measure_sort_time(insertion_sort, n)[1])

        selection_avgs.append(measure_sort_time(selection_sort, n)[0])
        selection_maxes.append(measure_sort_time(selection_sort, n)[1])

    averages = [bubble_avgs, insertion_avgs, selection_avgs]
    maxes = [bubble_maxes, insertion_maxes, selection_maxes]

    chart = plt.subplot()
    for i in zip(enumerate(["Bubble sort", "Insertion sort", "Selection sort"]), ["red", "green", "blue"]):
        chart.plot(x_labels, averages[int(i[0][0])], color=i[1], label=i[0][1])
        chart.legend()
    plt.xlabel("Długość sortowanej listy")
    plt.ylabel("Czas w sekundach")
    plt.title("Średni czas działania algorytmów sortowania")
    plt.show()

    chart = plt.subplot()
    for i in zip(enumerate(["Bubble sort", "Insertion sort", "Selection sort"]), ["red", "green", "blue"]):
        chart.plot(x_labels, maxes[int(i[0][0])], color=i[1], label=i[0][1])
        chart.legend()
    plt.xlabel("Długość sortowanej listy")
    plt.ylabel("Czas w sekundach")
    plt.title("Maksymalny czas działania algorytmów sortowania")
    plt.show()


    pure_bubble_avgs, pure_bubble_maxes = [], []
    bubble_mod_1_avgs, bubble_mod_1_maxes = [], []
    bubble_mod_2_avgs, bubble_mod_2_maxes = [], []

    for n in x_labels:
        pure_bubble_avgs.append(measure_sort_time(bubble_sort, n)[0])
        pure_bubble_maxes.append(measure_sort_time(bubble_sort, n)[1])

        bubble_mod_1_avgs.append(measure_sort_time(bubble_sort_mod_1, n)[0])
        bubble_mod_1_maxes.append(measure_sort_time(bubble_sort_mod_1, n)[1])

        bubble_mod_2_avgs.append(measure_sort_time(bubble_sort_mod_2, n)[0])
        bubble_mod_2_maxes.append(measure_sort_time(bubble_sort_mod_2, n)[1])

    averages_bubble = [pure_bubble_avgs, bubble_mod_1_avgs, bubble_mod_2_avgs]
    maxes_bubble = [bubble_maxes, bubble_mod_1_maxes, bubble_mod_2_maxes]

    chart = plt.subplot()
    for i in zip(enumerate(["Pure bubble sort", "Bubble sort mod 1", "Bubble sort mod 2"]), ["red", "green", "blue"]):
        chart.plot(x_labels, averages_bubble[int(i[0][0])], color=i[1], label=i[0][1])
        chart.legend()
    plt.xlabel("Długość sortowanej listy")
    plt.ylabel("Czas w sekundach")
    plt.title("Średni czas działania różnych wersji sortowania bąbelkowego")
    plt.show()

    chart = plt.subplot()
    for i in zip(enumerate(["Pure bubble sort", "Bubble sort mod 1", "Bubble sort mod 2"]), ["red", "green", "blue"]):
        chart.plot(x_labels, maxes_bubble[int(i[0][0])], color=i[1], label=i[0][1])
        chart.legend()
    plt.xlabel("Długość sortowanej listy")
    plt.ylabel("Czas w sekundach")
    plt.title("Maksymalny czas działania różnych wersji sortowania bąbelkowego")
    plt.show()

avg, max_ = measure_sort_time(bubble_sort, 1000)
print(avg, max_)

avg, max_ = measure_sort_time(insertion_sort, 1000)
print(avg, max_)

avg, max_ = measure_sort_time(selection_sort, 1000)
print(avg, max_)

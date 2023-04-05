def merge_sort(array):
    if len(array) > 1:
        divider = len(array) // 2

        left_array = array[:divider]
        right_array = array[divider:]

        merge_sort(left_array)
        merge_sort(right_array)

        l = r = k = 0

        while l < len(left_array) and r < len(right_array):
            if left_array[l] <= right_array[r]:
                array[k] = left_array[l]
                l += 1
            else:
                array[k] = right_array[r]
                r += 1
            k += 1

        while l < len(left_array):
            array[k] = left_array[l]
            l += 1
            k += 1

        while r < len(right_array):
            array[k] = right_array[r]
            r += 1
            k += 1


if __name__ == '__main__':

    input_list = input("Enter a list of numbers separated by single space:\n")
    input_list = [int(number) for number in input_list.split(" ")]

    print("\nOriginal:")
    [print(x, end=" ") for x in input_list]
    merge_sort(input_list)
    print("\n\nSorted:")
    [print(x, end=" ") for x in input_list]
    print()

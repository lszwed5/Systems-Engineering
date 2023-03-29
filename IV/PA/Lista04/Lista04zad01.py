"""----------------------------------- 1 -----------------------------------"""


def find_max_number(input_list):
    max_number = input_list[0]
    for number in input_list:
        max_number = number if number > max_number else max_number

    return max_number

# Time complexity - O(n)


"""----------------------------------- 2 -----------------------------------"""


def find_second_max_number(input_list):
    max_number = input_list[0]
    second_max_number = input_list[0]
    for number in input_list:
        max_number = number if number > max_number else max_number

    for number in input_list:
        if max_number > number > second_max_number:
            second_max_number = number

    return second_max_number

# Time complexity - T(2n) ==> O(n)


"""----------------------------------- 3 -----------------------------------"""


def find_avg_of_list(input_list):
    length = 0
    total_sum = 0
    for number in input_list:
        total_sum += number
        length += 1

    input_list_avg = total_sum / length

    return input_list_avg

# Time complexity - T(n + 1) ==> O(n)


"""-------------------------------- Driver --------------------------------"""

if __name__ == '__main__':
    input_list = input("Enter a list of numbers separated by single space:\n")
    input_list = [float(number) for number in input_list.split(" ")]

    print(f"\nGreatest number: {find_max_number(input_list)}")
    print(f"Second greatest number: {find_second_max_number(input_list)}")
    print(f"Average of list: {find_avg_of_list(input_list)}")

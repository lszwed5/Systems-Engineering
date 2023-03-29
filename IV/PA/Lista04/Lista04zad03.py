def subset_sum(set_, n, sum_):
    if n == 0:
        return False

    if set_[n - 1] > sum_:
        return subset_sum(set_, n - 1, sum_)

    if set_[n - 1] == sum_:
        return True

    return subset_sum(
        set_, n - 1, sum_) or subset_sum(
        set_, n - 1, sum_ - set_[n - 1])


if __name__ == '__main__':
    print("Enter a set of numbers: ")
    numbers = input()
    numbers_set = [float(num) for num in numbers.split(" ")]

    n = len(numbers_set)
    sum_ = 0
    if subset_sum(numbers_set, n, sum_):
        print("Found a subset with given sum")
    else:
        print("No subset with given sum")

    # Time complexity - O(n!)

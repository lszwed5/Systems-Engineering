def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(matrix):
    rows = len(matrix)
    if rows <= 1:
        return matrix

    cols = len(matrix[0])

    max_val = max(matrix[0])
    for i in range(1, rows):
        max_val = max(max_val, max(matrix[i]))

    exp = 1
    while max_val // exp > 0:
        for i in range(cols - 1, -1, -1):
            arr = [row[i] for row in matrix]
            counting_sort(arr, exp)
            for j in range(rows):
                matrix[j][i] = arr[j]
        exp *= 10

    return matrix


size = [int(x) for x in
        input("Enter the size of the matrix as MxN: ").split("x")]
matrix = [[0] * size[1]] * size[0]
print("Enter the matrix to be sorted:")
for M in range(size[0]):
    matrix[M] = [int(val) for val in input().split(" ")]

sorted_matrix = radix_sort(matrix)
print("\nSorted array:")
print(*sorted_matrix, sep="\n")

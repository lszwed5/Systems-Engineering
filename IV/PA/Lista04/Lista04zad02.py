import numpy as np


def multiplication_for(matrix_1, matrix_2):
    result_matrix = [[0 for _ in range(shape)] for _ in range(shape)]
    for i in range(len(matrix_1)):
        for j in range(len(matrix_2[0])):
            for k in range(len(matrix_2)):
                result_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]

    return result_matrix


def multiplication_comprehensions(matrix_1, matrix_2):
    result = [[sum(a * b for a, b in zip(A_row, B_col))
               for B_col in zip(*matrix_2)] for A_row in matrix_1]

    return result


if __name__ == '__main__':
    shape = int(input("Enter the number of columns (rows): "))

    print("\nEnter the first matrix:")
    matrix_1 = [[float(num) for num in input().split(" ")] for _ in
                range(shape)]

    print("\nEnter the second matrix:")
    matrix_2 = [[float(num) for num in input().split(" ")] for _ in
                range(shape)]

    result_matrix = multiplication_for(matrix_1, matrix_2)
    result = multiplication_for(matrix_1, matrix_2)

    print("\n\nThe result is: ")
    print(np.array(result))

    # Verification
    matrix_1, matrix_2 = np.array(matrix_1), np.array(matrix_2)
    result_matrix_np = matrix_1 @ matrix_2

    if np.array([[d == e == f for d, e, f in zip(a, b, c)] for a, b, c
                 in zip(result, result_matrix, result_matrix_np)]).all():
        print("\nResult is correct")
    else:
        print("\nResult is wrong")

    # Time complexity - O(n^3)

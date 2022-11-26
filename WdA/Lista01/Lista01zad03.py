# Nie działa
import numpy as np


def gauss(matrix):
    """Turns the given matrix into an upper-triangular one using the Gauss elimination Method"""
    matrix = np.array(matrix)
    rows, columns = np.shape(matrix)
    for i in range(rows):
        if matrix[i][i] != 0:
            for j in range(i + 1, rows):
                if matrix[j][i] != 0:
                    temp = matrix[j][i]
                    if temp != 0:
                        for k in range(columns):
                            matrix[j][k] = matrix[j][k] - (matrix[i][i]/(matrix[i][i]/temp))
                    else:
                        continue
    print(matrix)


gauss([[1, -2, 1, 0],
       [2, 1, -3, 5],
       [4, -7, 1, -1]])

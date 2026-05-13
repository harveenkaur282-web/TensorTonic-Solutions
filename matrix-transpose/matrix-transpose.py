import numpy as np

def matrix_transpose(A):
    rows = len(A)
    columns = len(A[0])
    transpose = []

    for j in range(columns):
        new_row = []
        for i in range(rows):
            new_row.append(A[i][j])
        transpose.append(new_row)
    transpose = np.array(transpose)
    return transpose



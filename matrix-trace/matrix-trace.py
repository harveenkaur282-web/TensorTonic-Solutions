import numpy as np

def matrix_trace(A):
    A = np.array(A)
    if len(A) != len(A[0]):
        raise ValueError("the matrices should be in the form of n *n")
    trace = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                trace += A[i][j]
    return trace
    pass

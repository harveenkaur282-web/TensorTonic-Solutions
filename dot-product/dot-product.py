import numpy as np

def dot_product(x, y):
    x = np.array(x)
    y = np.array(y)

    if len(x) != len(y):
        raise ValueError("vectors need to have the same length")

    return float(np.dot(x, y))
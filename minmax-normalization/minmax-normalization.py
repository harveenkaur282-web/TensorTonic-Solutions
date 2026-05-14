import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    X = np.array(X)
    minimum_val = np.min(X, axis = axis, keepdims = True)
    maximum_value = np.max(X, axis = axis, keepdims = True)
    minmax_value = (X - minimum_val)/(maximum_value - minimum_val + eps)
    return minmax_value
    pass
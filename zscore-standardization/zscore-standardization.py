import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    X = np.array(X)
    mean = np.mean(X, axis = axis, keepdims = True)
    std = np.std(X, axis = axis, keepdims = True)
    standardized_score = (X-mean)/(std + eps)
#it can also be std = np.maximum(std, eps)
    return standardized_score
    pass
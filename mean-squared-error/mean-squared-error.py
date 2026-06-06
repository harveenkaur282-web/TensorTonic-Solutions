import numpy as np

def mean_squared_error(y_pred, y_true):
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    if len(y_pred) != len(y_true) :
        return None
    N = len(y_pred)
    mean_s_e = (1 / N) * np.sum((y_pred - y_true) ** 2)
    return float(mean_s_e)

import numpy as np

def tanh(x):
    x = np.array(x)

    exp_x = np.exp(x)
    exp_neg_x = np.exp(-x)

    numerator = exp_x - exp_neg_x
    denominator = exp_x + exp_neg_x

    result = numerator / denominator

    if result.shape == ():
        return float(result)

    return result
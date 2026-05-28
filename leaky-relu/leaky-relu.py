import numpy as np

def leaky_relu(x, alpha=0.01):
    x = np.array(x)
    result = []
    for i in range(len(x)):
        if x[i] >= 0:
            result.append(x[i])
        elif x[i] < 0:
            result.append(alpha*x[i])
    result = np.array(result)
    return result
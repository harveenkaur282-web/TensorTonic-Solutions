import numpy as np

def sigmoid(x):
    x = np.array(x)
    return (1/(1+np.exp(-x)))
x = [0, 2, -2]
sigmoid(x)
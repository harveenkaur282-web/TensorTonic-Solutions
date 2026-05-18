import numpy as np

def manhattan_distance(x, y):
    x = np.array(x)
    y = np.array(y)

    if len(x) != len(y):
        raise ValueError("both need to have same no.of elements")

    total = 0
    for i in range(len(x)):
        dist = np.abs(x[i]-y[i])
        total += dist
    distance = float(total)
    return distance
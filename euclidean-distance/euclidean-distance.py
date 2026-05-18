import numpy as np

def euclidean_distance(x, y):
    x = np.array(x)
    y = np.array(y)

    if len(x) != len(y):
        raise ValueError("both should hv same no.of elements")
        
    total = 0
    for i in range(len(x)): 
        dist = np.pow((x[i]-y[i]), 2)
        total += dist
    distance = np.sqrt(total)
    return distance

import numpy as np

def cosine_similarity(a, b):
    if len(a) != len(b):
        return None
    a = np.array(a)
    b = np.array(b)
    dot_prod = np.dot(a,b)
    norm_denominator = np.linalg.norm(a) * np.linalg.norm(b)
    if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
        return 0
    cosine_similarity = dot_prod/norm_denominator
    
    return float(cosine_similarity)
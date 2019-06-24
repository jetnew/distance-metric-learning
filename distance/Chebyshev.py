import numpy as np
from scipy.spatial import distance

def Chebyshev(y1, y2, verbose=False):
    """
    Chebyshev distance between 2 vectors.
    
    Input:
        y1 - list-like object
        y2 - list-like object
    Output:
        distance - sum of absolute difference

    Example:
        y1 = [1,3,5,7]
        y2 = [1,3,7,9]
        Chebyshev(y1, y2, verbose=True)
        =>  y1: [1 3 5 7]
            y2: [1 4 7 10]
            Chebyshev Distance: 3
    """
    y1 = np.asarray(y1)
    y2 = np.asarray(y2)
    dist = distance.chebyshev(y1, y2)
    
    if verbose:
        print("y1:", y1)
        print("y2:", y2)
        print("Chebyshev Distance:", dist)

    return dist
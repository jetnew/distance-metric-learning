import numpy as np
from scipy.spatial import distance

def Euclidean(y1, y2, verbose=False):
    """
    Euclidean distance between 2 vectors.
    
    Input:
        y1 - list-like object
        y2 - list-like object
    Output:
        distance - Euclidean distance

    Example:
        y1 = [1,2,3,4]
        y2 = [1,2,4,6]
        Euclidean(y1, y2, verbose=True)
        =>  y1: [1 2 3 4]
            y2: [1 2 4 6]
            Euclidean Distance: 2.23606797749979
    """
    y1 = np.asarray(y1)
    y2 = np.asarray(y2)
    dist = distance.euclidean(y1, y2)
    
    if verbose:
        print("y1:", y1)
        print("y2:", y2)
        print("Euclidean Distance:", dist)

    return dist

L2_Norm = Euclidean

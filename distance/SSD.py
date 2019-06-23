import numpy as np

def SSD(y1, y2, verbose=False):
    """
    Sum of squared difference between 2 vectors.
    
    Input:
        y1 - list-like object
        y2 - list-like object
    Output:
        distance - sum of squared difference

    Example:
        y1 = [1,3,5,7]
        y2 = [1,3,7,9]
        SSD(y1, y2, verbose=True)
        =>  y1: [1 3 5 7]
            y2: [1 3 7 9]
            Sum of Absolute Difference: 8
    """
    y1 = np.asarray(y1)
    y2 = np.asarray(y2)
    dist = np.sum(np.abs(y1-y2)**2)
    
    print("y1:", y1)
    print("y2:", y2)
    print("Sum of Squared Difference:", dist)

    return dist

Squared_L2_Norm = SSD
Euclidean_Norm = SSD
Squared_Euclidean = SSD
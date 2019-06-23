import numpy as np

def SAD(y1, y2, verbose=False):
    """
    Sum of absolute difference between 2 vectors.
    
    Input:
        y1 - list-like object
        y2 - list-like object
    Output:
        distance - sum of absolute difference

    Example:
        y1 = [1,3,5,7]
        y2 = [1,3,7,9]
        SAD(y1, y2, verbose=True)
        =>  y1: [1 3 5 7]
            y2: [1 3 7 9]
            Sum of Absolute Difference: 4
    """
    y1 = np.asarray(y1)
    y2 = np.asarray(y2)
    dist = np.sum(np.abs(y1-y2))
    
    print("y1:", y1)
    print("y2:", y2)
    print("Sum of Absolute Difference:", dist)

    return dist

L1_Norm = SAD
Manhattan_Norm = SAD
Taxicab_Norm = SAD
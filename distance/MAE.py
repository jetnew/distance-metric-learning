import numpy as np
from sklearn.metrics import mean_absolute_error

def MAE(y1, y2, verbose=False):
    """
    Mean absolute error between 2 vectors.
    
    Input:
        y1 - list-like object
        y2 - list-like object
    Output:
        distance - mean absolute error

    Example:
        y1 = [1,2,3,4]
        y2 = [1,2,4,6]
        MAE(y1, y2, verbose=True)
        =>  y1: [1 2 3 4]
            y2: [1 2 4 6]
            Mean Absolute Error: 0.75
    """
    y1 = np.asarray(y1)
    y2 = np.asarray(y2)
    dist = mean_absolute_error(y1, y2)
    
    if verbose:
        print("y1:", y1)
        print("y2:", y2)
        print("Mean Absolute Error:", dist)

    return dist
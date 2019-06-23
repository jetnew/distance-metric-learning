import numpy as np
from sklearn.metrics import mean_squared_error

def MSE(y1, y2, verbose=False):
    """
    Mean squared error between 2 vectors.
    
    Input:
        y1 - list-like object
        y2 - list-like object
    Output:
        distance - mean squared error

    Example:
        y1 = [1,2,3,4]
        y2 = [1,2,4,6]
        SSD(y1, y2, verbose=True)
        =>  y1: [1 2 3 4]
            y2: [1 2 4 6]
            Mean Squared Error: 1.25
    """
    y1 = np.asarray(y1)
    y2 = np.asarray(y2)
    dist = mean_squared_error(y1, y2)
    
    print("y1:", y1)
    print("y2:", y2)
    print("Mean Squared Error:", dist)

    return dist
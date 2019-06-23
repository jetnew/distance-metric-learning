# Distance Metric Learning

Compilation of distance measures in Python.

## Libraries

* [Scikit-learn (Pairwise Metrics)](https://scikit-learn.org/stable/modules/classes.html#pairwise-metrics)
* [SciPy (Distance Computations)](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html)
* [NumPy (Linear Algebra)](https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)

## List of Distances

* Sum of Absolute Difference
* Sum of Squared Difference
* Mean Absolute Error
* Mean Squared Error
* Euclidean Distance
* Manhattan Distance
* Chebyshev distance
* Minkowski Distance
* Canberra Distance
* Cosine Distance
* Pearson's Distance
* Hamming Distance

## Distances

Sum of Absolute Difference (SAD)

* L1-norm
* Manhattan- or Taxicab-norm
* [Code](distance/SAD.py)

Sum of Squared Difference (SSD)

* Squared L2-norm
* Euclidean norm
* Squared Euclidean distance
* [Code](distance/SSD.py)

Mean Absolute Error (MAE)

* 1/n * Sum of Absolute Difference
* [Code](distance/MAE.py)

Mean Squared Error (MSE)

* 1/n * Sum of Squared Difference
* [Code](distance/MSE.py)

Euclidean Distance

* L2-norm
* Natural distance in a geometric interpretation
* [Code](distance/Euclidean.py)

Manhattan Distance

* L1-norm
* Sum of Absolute Difference
* Minkowski distance with p=1

Chebyshev Distance

* L-infinity norm
* Minkowski distance with p=infinity

Minkowski Distance

* Lp-norm

Canberra Distance

* Weighted Manhattan distance

Cosine Distance

* Dot product scaled by product of Euclidean distances from the origin
* Represents angular distance of 2 vectors, ignoring scale

Pearson's Distance

* Correlation distance based on Pearson's product-momentum correlation coefficient of 2 sample vectors
* Measures linear relationship between 2 vectors

Hamming Distance

* No. of entries in 2 vectors which are different
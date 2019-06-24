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
* Chebyshev distance
* Minkowski Distance
* Canberra Distance
* Cosine Distance
* Pearson's Distance
* Hamming Distance

## Distances

Sum of Absolute Differences (SAD)

* L1-norm
* Manhattan- or Taxicab-norm
* Minkowski distance with p=1
* Formula: &sum; |<i>p</i><sub>i</sub> - <i>q</i><sub>i</sub>|
* Code: [SAD.py](distance/SAD.py)

Mean Absolute Error (MAE)

* 1/n * Sum of Absolute Difference
* Formula: <sup>1</sup>&frasl;<sub>n</sub> * &sum; |<i>p</i><sub>i</sub> - <i>q</i><sub>i</sub>|
* Code: [MAE.py](distance/MAE.py)

Sum of Squared Differences (SSD)

* Squared L2-norm
* Euclidean norm
* Squared Euclidean distance
* Formula: &sum; |<i>p</i><sub>i</sub> - <i>q</i><sub>i</sub>|<sup>2</sup>
* Code: [SSD.py](distance/SSD.py)

Mean Squared Error (MSE)

* 1/n * Sum of Squared Difference
* Formula: <sup>1</sup>&frasl;<sub>n</sub> * &sum; |<i>p</i><sub>i</sub> - <i>q</i><sub>i</sub>|<sup>2</sup>
* Code: [MSE.py](distance/MSE.py)

Euclidean Distance

* L2-norm
* Natural distance in a geometric interpretation
* Formula: &radic; &sum; |<i>p</i><sub>i</sub> - <i>q</i><sub>i</sub>|<sup>2</sup>
* Code: [Euclidean.py](distance/Euclidean.py)

Chebyshev Distance

* L-infinity norm
* Minkowski distance with p=infinity
* Formula: <i>max</i> |<i>p</i><sub>i</sub> - <i>q</i><sub>i</sub>|
* Code: [Chebyshev.py](distance/Chebyshev.py)

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
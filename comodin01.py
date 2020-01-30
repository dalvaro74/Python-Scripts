import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
X = np.arange(6).reshape(3, 2)
X



poly = PolynomialFeatures(2)
poly.fit_transform(X)



poly = PolynomialFeatures(interaction_only=True)
poly.fit_transform(X)

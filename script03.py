import numpy as np
import pandas as pd

x0 = np.arange(9.0)
x1 = np.arange(9.0).reshape((3, 3))
x1
x2 = np.arange(3.0)
# Suma le array x2 al x1 (primer elemento al primero, segundo al segundo, etc..) 
x3 = np.add(x1, x2)
x3

# Añade el nuevo elemento a l
x1 = np.append(x1,x2.reshape((1, 3)), axis=0)
x1
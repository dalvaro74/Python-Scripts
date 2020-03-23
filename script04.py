import numpy as np
import pandas as pd
a = np.arange(10).reshape(2,5)
b = np.arange(10, 20).reshape(2,5)
pp = pd.DataFrame({'foo':[42,51], 'arr':[a,b]})

pp
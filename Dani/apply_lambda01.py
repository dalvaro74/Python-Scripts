import numpy as np 
import pandas as pd

df = pd.DataFrame(np.random.randn(5, 3), columns=['a', 'b', 'c'])

df2 = df[df.apply(lambda x: x['a']>x['c'], axis=1)]
df2
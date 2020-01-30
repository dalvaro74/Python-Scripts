import numpy as np 
import pandas as pd

data = [[1.461711, -0.404452, 0.722502],[-2.169377, 1.131037, 0.232047],
[0.009450, -0.868753, 0.598470,],[0.60246, 0.299249, 0.474564],
[-0.675339, -0.816702, 0.799289]]
df = pd.DataFrame(data, columns=['mass1', 'mass2', 'velocity'])
df

mask = (np.sin(df.velocity) / df.iloc[:, 0:2].prod(axis=1)) > 0

mask

df2 = df[mask]

df2
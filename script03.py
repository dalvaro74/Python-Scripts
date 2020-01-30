import numpy as np
import pandas as pd

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
    index=['cobra', 'viper', 'sidewinder'],
    columns=['max_speed', 'shield'])

df

df.loc['viper']

df.loc[['viper', 'sidewinder']]

df.loc['cobra', 'shield']
df.iloc[0,1]
df.iat[0,1]



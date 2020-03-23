import pandas as pd
import numpy as np 

df = pd.DataFrame(np.arange(12).reshape(3, 4),
                  columns=['A', 'B', 'C', 'D'])

df
df_tmp = df.drop(['B', 'C'], axis=1)
df_tmp

df_tmp2 = df.drop([0,1]) # es lo mismo que df.drop([0,1], axis=0) o df.drop([0,1],0)
df_tmp2
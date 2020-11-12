import numpy as np 
import pandas as pd

mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]

df = pd.DataFrame(mydict)
df
df['a'][1]
# Con un escalar
type(df.iloc[0])
print(df.iloc[0])
print(df.iloc[0,1])

# Con un vector
# Estas dos son lo mismo
print(df.iloc[[0,1]])
print(df.iloc[0:2])

# With a callable, useful in method chains. The x passed to the lambda 
# is the DataFrame being sliced. This selects the rows whose index label even.
print(df.iloc[lambda x: x.index % 2 == 0])

# With lists of integers.
print(df.iloc[[0, 2], [1, 3]])

# With slice objects.
print(df.iloc[1:3, 0:3])

# With a boolean array whose length matches the columns.
print(df.iloc[:, [True, False, True, False]])

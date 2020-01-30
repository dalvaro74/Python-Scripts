import pandas as pd
import numpy as np 

data = {'Temp': ['Hot', 'Cold', 'Very Hot', 'Warm', 'Hot', 'Warm', 'Warm', 'Hot', 'Hot', 'Cold'],
    'Color': ['Red', 'Yellow', 'Blue', 'Blue', 'Red', 'Yellow', 'Red', 'Yellow', 'Yellow', 'Yellow'],
    'Target': [1,1,1,0,1,0,1,0,1,1]}

df = pd.DataFrame(data)

#get_dummies
#df_dummies =
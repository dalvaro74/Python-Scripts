import numpy as np
import pandas as pd

np_array1 = np.array([1,2,3,4,5])
np_array1.shape

np_array2 = np.array([[1,2,3,4,5]])
np_array2.shape

np_array3 = np.array([[1,2,3,4,5], [6,7,8,9]])
np_array3.shape

np_test = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
np_test.shape


# Con esto (dos corchetes) es suficiente ara que el shape tenga la dimension adecuada
dic_data = {'Id': ['img1', 'img2'], 'Features': [[3.0, 2., 1.0, 0.0],[7.0,6.0,5.0,4.0]]}
mi_df = pd.DataFrame.from_dict(dic_data)
mi_df
mi_df['Features']

np_array_features = mi_df['Features'].values

array_model = np.zeros((11761,512))
j=0
i=0
for elem1 in np_array_features:
    array_tmp = np.zeros(512)
    for elem2 in elem1:
        array_tmp[i] = elem2
        i+=1
        print(elem2)
    array_model[j] =  array_tmp
    i=0
    j+=1

array_total

type(mi_df['Features'].values)
data = mi_df['Features'].values
data_reshape = data.reshape(2,4)

data.shape

data_reshape.shape
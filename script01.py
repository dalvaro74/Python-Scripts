import numpy as np
import pandas as pd

# List of Tuples
empoyees = [('jack', 34, 'Sydney', 5) ,
('Riti', 31, 'Delhi' , 7) ,
('Aadi', 16, 'New York', 11)
]
# Create a DataFrame object
#con index manual
#empDfObj = pd.DataFrame(empoyees, columns=['Name', 'Age', 'City', 'Experience'], index=['a', 'b', 'c'])
#sin index
empDfObj = pd.DataFrame(empoyees, columns=['Name', 'Age', 'City', 'Experience'])
print(empDfObj)

# Yields a tuple of index label and series for each row in the datafra,e
for (index_label, row_series) in empDfObj.iterrows():
    print('Row Index label : ', index_label)
    print('Row Content as Series : ', row_series.values)

# Iterate over the Dataframe rows as named tuples
for namedTuple in empDfObj.itertuples():
    #Print row contents inside the named tuple
    print(namedTuple)

print(namedTuple[1])

# Iterate over the Dataframe rows as named tuples without index
for namedTuple in empDfObj.itertuples(index=False):
    # Print row contents inside the named tuple
    print(namedTuple)
print(namedTuple[0])

empDfObj

type(empDfObj[['Name', 'City', 'Experience']])

print(empDfObj.columns[[True,True,False,True]])
print(empDfObj.columns[2:])
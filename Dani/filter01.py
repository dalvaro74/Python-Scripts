#MULTIPLE CONDITIONS

import numpy as np 
import pandas as pd

df=pd.DataFrame({'Name':['JOHN','ALLEN','BOB','NIKI','CHARLIE','CHANG'],
              'Age':[35,42,63,29,47,51],
              'Salary_in_1000':[100,93,78,120,64,115],
             'FT_Team':['STEELERS','SEAHAWKS','FALCONS','FALCONS','PATRIOTS','STEELERS']})
df

#Using loc with multiple conditions
df2 = df.loc[(df['Salary_in_1000']>=100) & (df['Age']< 60) & (df['FT_Team'].str.startswith('S')),['Name','FT_Team']]
df2

#Using np.where with multiple conditions
idx = np.where((df['Salary_in_1000']>=100) & (df['Age']< 60) & (df['FT_Team'].str.startswith('S')))

 df3 = df.loc[idx]
 df3

 #Using Query with multiple Conditions
 df.query('Salary_in_1000>=100 & Age<60 & FT_Team.str.startswith("S").values')

 #pandas boolean indexing multiple conditions
 df[(df['Salary_in_1000']>=100) & (df['Age']<60) & df['FT_Team'].str.startswith('S')][['Name','Age','Salary_in_1000']]

 #Pandas Eval multiple conditions
 df[df.eval("Salary_in_1000>=100 & (Age<60) & FT_Team.str.startswith('S').values")]
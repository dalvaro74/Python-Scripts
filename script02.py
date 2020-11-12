import numpy as np
import pandas as pd
mydict = [{'x': 1, 'y': 2, 'z': 3, 'w': 4},
          {'x': 100, 'y': 200, 'z': 300, 'w': 400},
          {'x': 1000, 'y': 2000, 'z': 3000, 'w': 4000 }]

      
#con index
df = pd.DataFrame(mydict, index=['a', 'b', 'c'])
#sin index (pone automaticamente del 0 al numero de filas)
df = pd.DataFrame(mydict)
#Para
df.index.names = ['Letras']
df
df['a']
#df.iloc[1] (escalar)es un pandas.Series es como un diccionario donde las keys
# son los nombres de las columnas y los valores son los valores del dataframe
# para esa fila
print(df.iloc[1].values)
#df['y] es un pandas.Series, en este caso tambien es como un diccionario 
# donde la keys son los indexdel dtaframe (si los tiene, sino del cero al 
# numero de filas) y los valores son los de esa columna
print(df['y'].values)

print(type(df.iloc[0]))
print(type(df['x']))

#Otros ejemplos con iloc

print("\n***************\n")

#df.iloc[1] (vector)es un pandas.DataFrame con los valores de la fila
print(df.iloc[[1]])
print(type(df.iloc[[0]]))
print(df.iloc[[0,1]])

#con slice
#esto devuelve un DataFrame
print(df.iloc[:3])
print(type(df.iloc[:3]))

#Esto devuelve un Series
print(df.iloc[:,3])
print(type(df.iloc[:,3]))

#con boolean mask
print(df.iloc[[True, False, True]])

#con lambdas
print(df.iloc[lambda x: x.index % 2 == 0])
df['y'].apply(lambda y: 1111 if y == 100 else 5555)

#para obtener los nombres de las columnas de un DF:
print(df.columns)
#Lo de arriba es un pandas.Index

#Para que quede limpio
print(df.columns.tolist())
#Lo de arriba es un list

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

x = np.linspace(0,20,20)

pendiente = 2
abscisa_origen =10
error = 0.8

np.random.seed(5)
epsilon = np.random.randn(20) *error

y = pendiente*x + abscisa_origen +epsilon

x
x.reshape(-1,1)
y
lr = LinearRegression().fit(x.reshape(-1,1), y)
y_hat = lr.predict(x.reshape(-1,1))


plt.plot(x,y,'b.',label='y')
plt.plot(x,y_hat,'r',label='y_hat')
plt.legend()
plt.show

w0 = lr.intercept_
w = lr.coef_

degree = 1
print(f'w0: {w0}')

coef_names = ['w' + str(i) + ':' for i in range(1, degree+1)]

for f,wi in zip(coef_names,w):
    print(f,wi)

mse = np.mean((y-y_hat)**2)

print(f'El error de mi regresion es: {mse}')
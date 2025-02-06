# CS 1101 - Week 11 - Exercise 06

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

X = [1, 2, 3, 4, 5, 6, 7]
Y = [7.1, 9.8, 45, 90, 163, 274.6, 424]

# polyfit
coeff = np.polyfit(X, Y, deg=2)
print(coeff)

f = np.poly1d(coeff)
print(f)

XX = np.linspace(0, 8, 1000)
YY = f(XX)
plt.scatter(X, Y, c='black', s=100, label='data points')
plt.legend()
plt.plot(XX, YY, c='blue')
plt.show()

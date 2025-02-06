# CS 1101 - Week 11 - Exercise 06

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.array([1, 2, 3, 4, 5])
y = np.array([5.9, 7.5, 10.4, 11.2, 15.5])

coeff = np.polyfit(x, y, deg=2)
f = np.poly1d(coeff)

XX = np.linspace(0, 5, 1000)
YY = f(XX)
plt.scatter(x, y, label='data points')
plt.legend()
plt.grid(True)
plt.plot(XX, YY, c='blue')
plt.show()

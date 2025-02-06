# CS 1101 - Week 11 - Exercise 05

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.array([1, 2, 3, 4, 5])
y = np.array([5.9, 7.5, 10.4, 11.2, 15.5])

plt.scatter(
    x,
    y,
)

coeffs = np.polyfit(x, y, 2)
print(coeffs)
p = np.poly1d(coeffs)
x_fit = linspace(0,100,1000)
y_fit = p(x)
plt.plot(x, y_fit,linestyle='--', color='r')
plt.title('Best Fitted Line')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
plt.xticks(x)
plt.show()

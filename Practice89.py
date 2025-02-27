# CS Week 14 - CS 1101 - Exercise 04

# Importing External Libraries for Data Analysis Functions
import numpy as np  # For Handling Mathematical Functions
import matplotlib.pyplot as plt  # For Plotting Graphs
import pandas as pd  # For Importing Files


# Define The Function
def f(y):
    return y

XX = np.linspace(0, 10, 100)
y_actual = np.exp(XX)

plt.scatter(XX, y_actual, color='blue')
plt.plot(XX, y_actual, label='actual fit', color='red')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.legend()
plt.show()

'''
y0 = 1
x0 = 0

n = 100000
X = np.linspace(0, 10, n)
h = (10 - 0)/(n-1)

y1 = y0 + h * (f(y0))
print(y1)
print(np.exp(1))
'''

n = 100000
y_new = np.zeros(n)
H = (10 - 0) / (n - 1)
X = np.linspace(0, 10, n)
y_new[0] = 1

for i in range(n-1):
    y_new[i+1] = y_new[i] + H * (f(y_new[i]))

plt.figure()
plt.scatter(XX, y_actual, color='blue')
plt.plot(X, y_new, label='approximate fit', color='red')
plt.show()
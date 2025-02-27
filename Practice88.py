# CS Week 14 - CS 1101 - Exercise 03

# Importing External Libraries for Data Analysis Functions
import numpy as np               # For Handling Mathematical Functions
import matplotlib.pyplot as plt  # For Plotting Graphs
import pandas as pd              # For Importing Files

# Time Array
X = [0.99, 2.10, 3.22, 4.40, 5.70, 7.12, 8.01, 8.37, 9.32, 9.98]
XX = np.array(X)

# Velocity Array
Y = [4.90, 5.70, 4.20, 7.04, 8.31, 7.82, 5.97, 7.01, 6.68, 4.79]
YY = np.array(Y)

# Finding the Function
coefficients = np.polyfit(XX, YY, 2)
f = np.poly1d(coefficients)
print(f)

# Find the Displacement
step_size = [5, 10, 20, 30, 40, 50]
value = []

for i in step_size:
    N = (i+1)
    H = (10-0) / (N - 1)
    XX = np.linspace(0, 10, N)
    Y = f(XX)
    U = np.sum(Y[1:-1])
    integral = (H/2) * (Y[0] + Y[-1] + 2 * U)
    print(integral)
    value.append(integral)

plt.figure()
plt.scatter(step_size, value, color='b')
plt.plot(step_size, value, color='g', linestyle='--')
plt.xlabel('')
plt.ylabel('Area Value')
plt.title('Trapezoidal Rule')
plt.show()
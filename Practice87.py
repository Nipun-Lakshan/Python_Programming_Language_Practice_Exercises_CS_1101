# CS Week 14 - CS 1101 - Exercise 02

# Importing External Libraries for Data Analysis Functions
import numpy as np               # For Handling Mathematical Functions
import matplotlib.pyplot as plt  # For Plotting Graphs
import pandas as pd              # For Importing Files

def f(X):
    return X*X

'''
X = np.linspace(0, 10, 100)
Y = f(X)
plt.plot(X, Y)
plt.show()
'''

step_size = [10, 20, 50, 100, 500, 1000]
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
plt.xlabel('Step Size')
plt.ylabel('Area Value')
plt.title('Trapezoidal Rule')
plt.show()

# 10 20 50 100 500 1000
# X - Step Size
# Y - Value

'''
N = 101
XX = np.linspace(0, 10, N)
Area = 0
print(XX)

for i in range(0, N-1):
    H = XX[i+1] - XX[i]
    L = (f(XX[i+1]) + f(XX[i]))/2
    A = L * H
    Area = Area + A

print(Area)
'''

# import numpy as np

# # Define the function f(x)
# def f(x):
#     return x**2  # Example function (change as needed)

# N = 10
# XX = np.linspace(0, 10, N)  # Creates 10 points, 9 gaps
# Area = 0

# # Loop to calculate the area using the Trapezoidal Rule
# for i in range(N-1):  # Iterate from 0 to 8 (N-1 = 9)
#     H = XX[i+1] - XX[i]  # Step size
#     L = (f(XX[i+1]) + f(XX[i])) / 2  # Average height
#     A = L * H  # Trapezoid area
#     Area += A  # Accumulate the area

# print("Approximate Area:", Area)
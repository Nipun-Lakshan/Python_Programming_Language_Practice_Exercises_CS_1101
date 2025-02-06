# CS 1101 - Week 11 - Exercise 03

# Import the Matplotlib Library
import matplotlib.pyplot as plt

x_vals = [1, 2, 3, 4, 5]
y_vals = [5, 4, 6, 8, 2]
# plt.plot(x_vals,y_vals)
# plt.plot(x_vals,y_vals, color='r', linestyle='--')
plt.plot(x_vals, y_vals, color='r', linestyle='--', label='hi')
plt.legend()
plt.show()

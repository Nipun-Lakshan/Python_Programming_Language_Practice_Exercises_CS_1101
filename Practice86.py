# CS Week 14 - CS 1101 - Exercise 01

# Importing External Libraries for Data Analysis Functions
import numpy as np               # For Handling Mathematical Functions
import matplotlib.pyplot as plt  # For Plotting Graphs
import pandas as pd              # For Importing Files

# Creating Data Frame Data Structure
file_path = r"A:\03. CS 1101 - Temp\07. CSV Files\Displacement.csv"  # File Path as a String
df = pd.read_csv(file_path)

# Extracting Data as Columns from CSV File Following DataFrame Structure
X = np.array(df['time'])
Y = np.array(df['position'])

# Calculating Data For Plot Best Fitted Line
XX = np.linspace(min(X), max(X), 100)
degree = []
rmsval = []

# Plot Graphs Using a Loop [Best Fitted Line Graph / Residuals]
for i in range(1, 4):
    coefficients = np.polyfit(X, Y, i)
    f = np.poly1d(coefficients)
    YP = f(XX)
    yres = f(X) - Y
    rmse = np.sqrt(np.mean(np.square(yres)))
    rmsval.append(rmse)
    degree.append(i)
    
    plt.figure()
    plt.subplot(1,2,1)
    plt.scatter(X, Y, s=20, color='r', marker='o', label='Original Data')
    plt.plot(XX, YP, color='g', label='Best Fitted Line')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.legend()
    
    plt.subplot(1,2,2)
    plt.scatter(X, yres, s=20, color='r', marker='o', label='Residual Values')
    plt.xlabel('Time (s)')
    plt.ylabel('Residual')
    plt.legend()

plt.figure()
plt.scatter([1,2,3], rmsval, color='red')
plt.plot([1,2,3], rmsval, color='blue', linestyle='--')
plt.title('Order vs RMSE')
plt.xlabel('Order')
plt.ylabel('RMSE')
plt.grid(True)

coefficients = np.polyfit(X, Y, 2)
f = np.poly1d(coefficients)
print(f)
# S = 1/2at^2 + ut + k

plt.show()
'''
# Creating a RMSE List
rmse_list = []

# Calculating Data For Each Graph
for order in range(1, 4):
    coefficient_fit = np.polyfit(T, S, deg=order)
    f = np.poly1d(coefficient_fit)
    XX = np.linspace(min(T), max(S), 1000)
    Y1 = f(XX)
    plt.figure()
    plt.subplot(1,2,1)
    plt.scatter(T, S, color='red', label='T')
    plt.plot(XX, Y1, linestyle='--', color='blue', label='Order' + str(order))
    plt.legend()
    plt.title('T vs S')
    plt.xlabel('Time (T)')
    plt.ylabel('Displacement (S)')
    plt.grid(True)

    rmse = np.sqrt(np.mean((S - f(T))**2))
    rmse_list.append(rmse)

    residual = S - f(T)
    plt.subplot(1,2,2)
    plt.scatter(T, residual, color='green', label='T')
    plt.legend()
    plt.title('X vs Residuals For Order 0' + str(order))
    plt.xlabel('T')
    plt.ylabel('S')
    plt.grid(True)

print(rmse_list)
plt.figure()
plt.scatter([1,2,3,4,5], rmse_list, color='red')
plt.plot([1,2,3,4,5], rmse_list, color='blue', linestyle='--')
plt.title('Order vs RMSE')
plt.xlabel('Order')
plt.ylabel('RMSE')
plt.grid(True)
plt.show()
'''
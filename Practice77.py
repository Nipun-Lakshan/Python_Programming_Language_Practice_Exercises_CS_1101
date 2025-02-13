# Introduction to File
'''
File Name           : Pendulum Data Set
Registration Number : 2023s20371
Index Number        : s17618
'''

# Importing External Libraries for Data Analysis Functions
import numpy as np               # For Handling Mathematical Functions
import matplotlib.pyplot as plt  # For Plotting Graphs
import pandas as pd              # For Importing Files

# Creating Data Frame Data Structure
file_path = r"A:\03. CS 1101 - Temp\07. CSV Files\pendulum_L_T.csv"  # File Path as a String
df = pd.read_csv(file_path)

# Extracting Data as Columns from CSV File Following DataFrame Structure
L = list(df['L'])
T = list(df['T'])

# Creating a RMSE List
rmse_list = []

for order in range(1, 6):
    coefficient_fit = np.polyfit(L, T, deg=order)
    f = np.poly1d(coefficient_fit)
    XX = np.linspace(min(L), max(L), 1000)
    Y1 = f(XX)
    plt.figure()
    plt.subplot(1,2,1)
    plt.scatter(L, T, color='blue', label='T')
    plt.plot(XX, Y1, linestyle='--', color='cyan', label='Order' + str(order))
    plt.legend()
    plt.title('L vs T - s17618')
    plt.xlabel('L')
    plt.ylabel('T')
    plt.grid(True)

    rmse = np.sqrt(np.mean((T - f(L))**2))
    rmse_list.append(rmse)

    residual = T - f(L)
    plt.subplot(1,2,2)
    plt.scatter(L, residual, color='green', label='T')
    plt.legend()
    plt.title('X vs Residuals For Order 0' + str(order) + ' - s17618')
    plt.xlabel('L')
    plt.ylabel('T')
    plt.grid(True)
    print(f'RMSE For Order 0{order} : {rmse}')

plt.figure()
plt.scatter([1,2,3,4,5], rmse_list, color='red')
plt.plot([1,2,3,4,5], rmse_list, color='blue', linestyle='--')
plt.title('Order vs RMSE - s17618')
plt.xlabel('Order')
plt.ylabel('RMSE')
plt.grid(True)
plt.show()
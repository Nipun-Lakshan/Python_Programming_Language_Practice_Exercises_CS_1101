# CS 1101 - Week 12 - Exercise 02

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

# Finding Best-Fitted Lines Using Linear Regression
coefficient_fit_1 = np.polyfit(L, T, deg=1)
f1 = np.poly1d(coefficient_fit_1)

coefficient_fit_2 = np.polyfit(L, T, deg=2)
f2 = np.poly1d(coefficient_fit_2)

coefficient_fit_3 = np.polyfit(L, T, deg=3)
f3 = np.poly1d(coefficient_fit_3)

coefficient_fit_4 = np.polyfit(L, T, deg=4)
f4 = np.poly1d(coefficient_fit_4)

coefficient_fit_5 = np.polyfit(L, T, deg=5)
f5 = np.poly1d(coefficient_fit_5)

# Generating X Values for Plotting the Regression Lines
XX = np.linspace(min(L), max(L), 1000)
Y1 = f1(XX)
Y2 = f2(XX)
Y3 = f3(XX)
Y4 = f4(XX)
Y5 = f5(XX)

# Calculating Residual Points
residual_1 = T - f1(L)
residual_2 = T - f2(L)
residual_3 = T - f3(L)
residual_4 = T - f4(L)
residual_5 = T - f5(L)

# RMSE Calculations

rmse_list = []

rmse_1 = np.sqrt(np.mean((T - f1(L))**2))
rmse_list.append(rmse_1)
rmse_2 = np.sqrt(np.mean((T - f2(L))**2))
rmse_list.append(rmse_2)
rmse_3 = np.sqrt(np.mean((T - f3(L))**2))
rmse_list.append(rmse_3)
rmse_4 = np.sqrt(np.mean((T - f4(L))**2))
rmse_list.append(rmse_4)
rmse_5 = np.sqrt(np.mean((T - f5(L))**2))
rmse_list.append(rmse_5)

print(rmse_list)
plt.figure()
plt.scatter([1,2,3,4,5], rmse_list, color='red')
plt.plot([1,2,3,4,5], rmse_list, color='blue', linestyle='--')
plt.legend()
plt.title('Order vs RMSE')
plt.xlabel('Order')
plt.ylabel('RMSE')
plt.grid(True)

# Plotting the Graph - Figure 01
plt.figure()
plt.subplot(1,2,1)
plt.scatter(L, T, color='red', label='T')
plt.plot(XX, Y1, linestyle='--', color='blue', label='Order 1')
plt.legend()
plt.title('L vs T')
plt.xlabel('L')
plt.ylabel('T')
plt.grid(True)

plt.subplot(1,2,2)
plt.scatter(L, residual_1, color='green', label='T')
plt.legend()
plt.title('X vs Residuals For Order 01')
plt.xlabel('L')
plt.ylabel('T')
plt.grid(True)

# Plotting the Graph - Figure 02
plt.figure()
plt.subplot(1,2,1)
plt.scatter(L, T, color='red', label='T')
plt.plot(XX, Y2, linestyle='--', color='blue', label='Order 2')
plt.legend()
plt.title('L vs T')
plt.xlabel('L')
plt.ylabel('T')
plt.grid(True)

plt.subplot(1,2,2)
plt.scatter(L, residual_2, color='green', label='T')
plt.legend()
plt.title('X vs Residuals For Order 02')
plt.xlabel('L')
plt.ylabel('T')
plt.grid(True)

# Plotting the Graph - Figure 03
plt.figure()
plt.subplot(1,2,1)
plt.scatter(L, T, color='red', label='T')
plt.plot(XX, Y3, linestyle='--', color='blue', label='Order 3')
plt.legend()
plt.title('L vs T')
plt.xlabel('L')
plt.ylabel('T')
plt.grid(True)

plt.subplot(1,2,2)
plt.scatter(L, residual_3, color='green', label='T')
plt.legend()
plt.title('X vs Residuals For Order 03')
plt.xlabel('L')
plt.ylabel('T')
plt.grid(True)

# Plotting the Graph - Figure 04
plt.figure()
plt.subplot(1,2,1)
plt.scatter(L, T, color='red', label='T')
plt.plot(XX, Y4, linestyle='--', color='blue', label='Order 4')
plt.legend()
plt.title('L vs T')
plt.xlabel('L')
plt.ylabel('T')
plt.grid(True)

plt.subplot(1,2,2)
plt.scatter(L, residual_4, color='green', label='T')
plt.legend()
plt.title('X vs Residuals For Order 04')
plt.xlabel('L')
plt.ylabel('T')
plt.grid(True)

# Plotting the Graph - Figure 05
plt.figure()
plt.subplot(1,2,1)
plt.scatter(L, T, color='red', label='T')
plt.plot(XX, Y5, linestyle='--', color='blue', label='Order 5')
plt.legend()
plt.title('L vs T')
plt.xlabel('L')
plt.ylabel('T')
plt.grid(True)

plt.subplot(1,2,2)
plt.scatter(L, residual_5, color='green', label='T')
plt.legend()
plt.title('X vs Residuals For Order 05')
plt.xlabel('L')
plt.ylabel('T')
plt.grid(True)

# Display the Graph
plt.show()
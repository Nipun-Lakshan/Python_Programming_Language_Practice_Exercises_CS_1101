# CS 1101 - Week 12 - Exercise 01

# Importing External Libraries for Data Analysis Functions
import numpy as np               # For Handling Mathematical Functions
import matplotlib.pyplot as plt  # For Plotting Graphs
import pandas as pd              # For Importing Files

# Creating Data Frame Data Structure
file_path = r"A:\03. CS 1101 - Temp\07. CSV Files\pendulum_L_T.csv" # File Path as a String
df = pd.read_csv(file_path)

# Extracting Data as Columns from CSV File Following DataFrame Structure
L = list(df['L'])
T = list(df['T'])

# Finding Best-Fitted Lines Using Linear Regression
coefficient_fit = np.polyfit(L, T, deg=1)
f1 = np.poly1d(coefficient_fit)

# Generating X Values for Plotting the Regression Lines
XX = np.linspace(0, 1, 1000)
Y1 = f1(XX)

# Plotting the Graph
plt.scatter(L, T, color='red', label='T')
plt.plot(XX, Y1, linestyle='--', color='blue', label='fit - T')

# Adding Labels and Legend
plt.legend()
plt.title('L vs T')
plt.xlabel('L')
plt.ylabel('T')
plt.grid(True)

# Display the Graph
plt.show()

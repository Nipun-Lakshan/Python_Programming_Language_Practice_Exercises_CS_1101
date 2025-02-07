# Introduction to File
'''
File Name           : Assignment 01 - Insurance Data Set
Registration Number : 2023s20371
Index Number        : s17618
'''

# Importing External Libraries for Data Analysis Functions
import numpy as np               # For Handling Mathematical Functions
import matplotlib.pyplot as plt  # For Plotting Graphs
import pandas as pd              # For Importing Files

# Creating Data Frame Data Structure
file_path = r"A:\03. CS 1101 - Temp\07. CSV Files\Insurance_data.csv" # File Path as a String
df = pd.read_csv(file_path)                                           # Reading the CSV File

# Extracting Data as Columns from CSV File Following DataFrame Structure
bmi_smoker_list = np.array((df[df['smoker'] == 'yes'])['bmi'])             # BMI values of Smokers
charges_smoker_list = np.array((df[df['smoker'] == 'yes'])['charges'])     # Insurance Premium for Smokers

bmi_non_smoker_list = np.array((df[df['smoker'] == 'no'])['bmi'])          # BMI values of non - Smokers
charges_non_smoker_list = np.array((df[df['smoker'] == 'no'])['charges'])  # Insurance Premium for non - Smokers

# Finding Best-Fitted Lines Using Linear Regression
coefficient_fit_smoker = np.polyfit(bmi_smoker_list, charges_smoker_list, deg=1) # Finding the Slope and Intersection Point of The Best Fitted Line for Smokers
f1 = np.poly1d(coefficient_fit_smoker)                                           # Make a function from above coefficients

coefficient_fit_non_smoker = np.polyfit(bmi_non_smoker_list, charges_non_smoker_list, deg=1) # Finding the Slope and Intersection Point of The Best Fitted Line for non - Smokers.
f2 = np.poly1d(coefficient_fit_non_smoker)                                                   # Make a function from above coefficients

# Generating X Values for Plotting the Regression Lines
XX = np.linspace(15, 50, 1000)
Y1 = f1(XX)
Y2 = f2(XX)

# Plotting the Graph
plt.scatter(bmi_smoker_list, charges_smoker_list, color='blue', label='Smoker')
plt.scatter(bmi_non_smoker_list, charges_non_smoker_list, color='red', label='Non - Smoker')
plt.plot(XX, Y1, linestyle='--', color='blue', label='fit - Smoker')
plt.plot(XX, Y2, linestyle='--', color='green', label='fit - Non - Smoker')

# Adding Labels and Legend
plt.legend()
plt.title('BMI vs. Insurance Premium: Linear Trends for Smokers and Non-Smokers')
plt.xlabel('BMI')
plt.ylabel('Premium')

# Display the Graph
plt.show()
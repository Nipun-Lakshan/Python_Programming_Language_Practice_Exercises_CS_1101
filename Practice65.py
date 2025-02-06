# CS 1101 - Week 11 - Exercise 01

# Import the Pandas Library
import pandas as pd

# Creating Data Frame Data Structure
df = pd.read_csv(r"A:\03. CS 1101 - Temp\07. CSV Files\temp_data.csv")
'''
# To load specific columns from the dataset
df = pd.read_csv(r"A:\03. CS 1101 - Temp\07. CSV Files\temp_data.csv",
                 usecols=[0, 3, 4])
df = pd.read_csv(r"A:\03. CS 1101 - Temp\07. CSV Files\temp_data.csv",
                 usecols=['time'])

# CSV - Comma Separated Values / # df - data frame
'''

# Load the summary of the dataset
print(df)

# Load the Full Data Set
print(df.to_string())

# Load the Dataset Columns
print(df.columns)

# Get a Slice from the dataset
print((df['city'].to_string()))

# Get a Slice From Dataset (True / False)
print(df['city'] == 'Colombo')

# Get a Slice From Dataset and Print them using Boolean
print(set(df['city']))

# Print the number of cities
print(len(set(df['city'])))
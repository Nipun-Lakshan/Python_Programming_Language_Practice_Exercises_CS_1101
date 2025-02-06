# CS 1101 - Week 11 - Exercise 02

# Import the Pandas Library
import pandas as pd

# Import the Matplotlib Library
import matplotlib.pyplot as plt

# Creating Data Frame Data Structure
df = pd.read_csv(r"A:\03. CS 1101 - Temp\07. CSV Files\temp_data.csv")

# Filtering Data
filtered_df = df[(df['city'] == 'Colombo') & (df['time'] < '2010-03-01')]

# Print filtered Data
print(filtered_df)

# df.to_csv(output_file, index=False) -> To save filtered data

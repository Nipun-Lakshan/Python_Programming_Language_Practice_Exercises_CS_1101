# CS 1101 - Week 13 - Exercise 05

# Importing External Libraries for Data Analysis Functions
import numpy as np               # For Handling Mathematical Functions
import matplotlib.pyplot as plt  # For Plotting Graphs
import pandas as pd              # For Importing Files

# Creating Data Frame Data Structure
file_path = r"A:\03. CS 1101 - Temp\07. CSV Files\actors.csv"  # File Path as a String
df = pd.read_csv(file_path)

actors = list(set(df['actor']))
print()
#print(actors)

print("===========================")
print("Actors List Of The Dataset")
print("===========================\n")

i = 1
for actor in actors:
    if(i <10):
        print("0" + str(i) + ".", end=" ")
    else:
        print(str(i) + ".", end=" ")
    print(actor)
    i = i + 1
    
#print(df.head())
#print(df.columns)
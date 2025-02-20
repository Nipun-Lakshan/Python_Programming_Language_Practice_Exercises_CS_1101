# CS 1101 - Week 13 - Exercise 06

# Importing External Libraries for Data Analysis Functions
import numpy as np               # For Handling Mathematical Functions
import matplotlib.pyplot as plt  # For Plotting Graphs
import pandas as pd              # For Importing Files

# Import Decision Tree Classifier Algorithm
from sklearn.tree import DecisionTreeClassifier

# Creating Data Frame Data Structure
file_path = r"A:\03. CS 1101 - Temp\07. CSV Files\actors.csv"  # File Path as a String
df = pd.read_csv(file_path)

# Use the Algorithm
model = DecisionTreeClassifier()
X = (df.drop(columns=['actor']))
y = list(df['actor'])
model.fit(X, y)

# Predicts
predictions = model.predict([[22, 0], [22, 1]])
print(predictions)
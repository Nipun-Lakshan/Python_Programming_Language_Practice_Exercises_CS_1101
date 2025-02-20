# CS 1101 - Week 13 - Exercise 08

# Importing External Libraries for Data Analysis Functions
import pandas as pd              # For Importing Files

# Import Decision Tree Classifier Algorithm
from sklearn.tree import DecisionTreeClassifier

# Import Train Test Split Algorithm
from sklearn.model_selection import train_test_split

# Import Algorithm to Check The accuracy of the train model
from sklearn.metrics import accuracy_score

import seaborn as sns
import matplotlib.pyplot as plt

# Creating Data Frame Data Structure
file_path = r"A:\03. CS 1101 - Temp\07. CSV Files\iris_data.csv"  # File Path as a String
df = pd.read_csv(file_path)

print(df.head())
print(df.describe)

X = (df.drop(columns=['target']))
y = list(df['target'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(X_test)
print(predictions.reshape(-1, 1))

accuracy = accuracy_score(y_test, predictions)
print(accuracy)

sns.pairplot(df, hue='target')
plt.show()
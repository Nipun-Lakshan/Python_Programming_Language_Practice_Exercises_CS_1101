# CS 1101 - Week 11 Videos - Pandas

import pandas as pd

df = pd.read_csv(r"A:\03. CS 1101 - Temp\07. CSV Files\temp_data.csv",
                 header=None,
                 names=[
                     'Time', 'Min Temperature', 'Max Temperature', 'City',
                     'Weather Code'
                 ])
print(df)
print(df.info())
print(df.head())
print()
print(df.shape)
print(df.columns)

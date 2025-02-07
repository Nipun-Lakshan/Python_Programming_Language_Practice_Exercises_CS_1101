# CS 1101 - Week 11 - Exercise 07

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Creating Data Frame Data Structure
df = pd.read_csv(r"A:\03. CS 1101 - Temp\07. CSV Files\temp_data.csv")

#Convert 'time' column to datetime
df['time'] = pd.to_datetime(df['time'])

# Filter DataFrame for 'Hambantota' city before '2010-07-01'
filtered_df_h = df[(df['city'] == 'Hambantota') & (df['time'] < '2010-07-01')]
filtered_df_c = df[(df['city'] == 'Colombo') & (df['time'] < '2010-07-01')]
filtered_df_g = df[(df['city'] == 'Galle') & (df['time'] < '2010-07-01')]
filtered_df_k = df[(df['city'] == 'Kurunegala') & (df['time'] < '2010-07-01')]

# Extract required columns as simple lists
filtered_list1 = filtered_df_h['time'].tolist()  # x-axis: Dates
# y-axis: Temperature
filtered_list2 = filtered_df_h['temperature_2m_mean'].tolist()  
filtered_list3 = filtered_df_c['temperature_2m_mean'].tolist()  
filtered_list4 = filtered_df_g['temperature_2m_mean'].tolist()  
filtered_list5 = filtered_df_k['temperature_2m_mean'].tolist()  

# Plotting the Data
#plt.figure(figsize=(10, 5))  # Optional: Adjust figure size
plt.plot(filtered_list1, filtered_list2, linestyle='-', color='b', label="Hambanthota")
plt.plot(filtered_list1, filtered_list3, linestyle='-', color='g', label="Colombo")
plt.plot(filtered_list1, filtered_list4, linestyle='-', color='y', label="Galle")
plt.plot(filtered_list1, filtered_list5, linestyle='-', color='c', label="Kurunegala")

# Formatting plot
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Temperature Trend in Four Cities")
#plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend()
plt.grid(True)

# Show plot
plt.show()

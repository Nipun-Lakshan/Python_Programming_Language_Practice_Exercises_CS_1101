# CS 1101 - Week 10 - Exercise 06 - Predator - Prey Model

import matplotlib.pyplot as plt

# Parameters
alpha = 1.1 # Prey Growth Rate
beta = 0.4  # Predation Rate
delta = 0.1 # Predator Growth Rate
gamma = 0.4 # Predator Death Rate

# Initial Populations
x0 = 10 # Initial Pray Population
y0 = 5  # Initial Predator

# Data
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 20]

# Create the plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label="Line")

# Labels and Title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Graph")

# Show Legend
plt.legend()

# Display the plot
plt.show()

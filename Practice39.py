# CS 1101 - Week 10 - Exercise 06 - Predator - Prey Model

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters
alpha = 1.1 # Prey Growth Rate
beta = 0.4  # Predation Rate
delta = 0.1 # Predator Growth Rate
gamma = 0.4 # Predator Death Rate

# Initial Populations
x0 = 10 # Initial Pray Population
y0 = 5  # Initial Predator

initial_conditions = [x0, y0]

# Time Span
t = np.linspace(0, 50, 1000)  # Simulate for 50 time units

# Lotka-Volterra Equations
def predator_prey_system(variables, t, alpha, beta, delta, gamma):
    x, y = variables
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

# Solve the system using odeint
solution = odeint(predator_prey_system, initial_conditions, t, args=(alpha, beta, delta, gamma))
prey_population, predator_population = solution.T

# Plot Population Dynamics
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t, prey_population, label="Prey (x)", color='blue')
plt.plot(t, predator_population, label="Predator (y)", color='red')
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Predator-Prey Population Dynamics")
plt.legend()
plt.grid()

# Plot Phase Space (Trajectory)
plt.subplot(1, 2, 2)
plt.plot(prey_population, predator_population, color='green')
plt.xlabel("Prey Population (x)")
plt.ylabel("Predator Population (y)")
plt.title("Phase Space Trajectory")
plt.grid()

plt.tight_layout()
plt.show()


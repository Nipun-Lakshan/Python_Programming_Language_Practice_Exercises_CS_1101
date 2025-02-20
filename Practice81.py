# CS 1101 - Week 13 - Exercise 04

# Import Clustering Algorithm
from sklearn.cluster import KMeans

# Import Matplotlib Library For Plotting Graphs
import matplotlib.pyplot as plt

# X axis points
x = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]

# Y axis points
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# Combine x and y coordinates into a list of tuples [Each point as (x, y)]
data = list(zip(x, y))

# List of Inertia
inertia = []

# Running a Loop to Calculate Inertia From Cluster 1 to 10 and Create a List of Inertia
for cluster in range(1, 11):
    kmeans = KMeans(n_clusters= cluster)
    kmeans.fit(data)
    inertia.append(kmeans.inertia_)

# Plot the Graph
plt.scatter(list(range(1, 11)), inertia)
plt.plot(list(range(1, 11)), inertia, color='r')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.xticks(range(1, 11))
plt.grid(True)
plt.show()
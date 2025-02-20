# CS 1101 - Week 13 - Exercise 04

# Import Clustering Algorithm
from sklearn.cluster import KMeans

# Import Matplotlib Library For Potting Graphs
import matplotlib.pyplot as plt

# X axis points
x = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]

# Y axis points
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# Combine x and y coordinates into a list of tuples [each point as (x, y)]
data = list(zip(x, y))

# Create a KMeans clustering model with 2 clusters
kmeans = KMeans(n_clusters= 2)

# Fit the KMeans model to the data [Perform Clustering]
kmeans.fit(data)

print(kmeans.inertia_)

# Scatter plot the data points, coloring them based on their cluster labels
plt.scatter(x, y, c=kmeans.labels_)

# Print the cluster labels assigned to each data point
print(kmeans.labels_)

# Print the coordinates of the cluster centroids (Center points of each cluster)
print(kmeans.cluster_centers_)

# Display the scatter plot
plt.show()
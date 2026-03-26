# Customer Segmentation using K-Means

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample dataset (Age vs Spending Score)
data = np.array([
    [22, 20],
    [25, 25],
    [30, 30],
    [35, 60],
    [40, 65],
    [45, 70]
])

# Applying K-Means
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

# Cluster labels
labels = kmeans.labels_

# Plotting clusters
plt.scatter(data[:, 0], data[:, 1], c=labels)
plt.xlabel("Age")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()
from sklearn.datasets import make_blobs

from sklearn.cluster import AgglomerativeClustering

import matplotlib.pyplot as plt

import scipy.cluster.hierarchy as sch

x,y = make_blobs(n_samples=100, centers= 4, cluster_std=0.6, random_state=42)

plt.figure(figsize=(10, 6))
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
plt.title("Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")
plt.show()

agglo = AgglomerativeClustering(n_clusters=4, affinity="euclidean", linkage="ward")

y_pred = agglo.fit_predict(x)

plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='rainbow')
plt.title("Agglomerative Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

import matplotlib.pyplot as plt

X,y_true =make_blobs(n_samples= 300, centers= 4,
                      cluster_std= 0.60, random_state=0)

kmeans = KMeans(n_clusters= 4, random_state=0)

kmeans.fit(X)

y_kmeans  = kmeans.predict(X)


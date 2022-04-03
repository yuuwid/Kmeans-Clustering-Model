from cluster.kmeans import Kmeans
from cluster.plot_kmeans import PlotKmeans

import pandas as pd

# Input Data
data = pd.read_csv('dataset.csv').values
init_cent = [[0, 1], [9, 6]]

# Init and Train Kmeans
kmeans = Kmeans(data, n_cluster=2)


# plotting Kmeans
pk = PlotKmeans(kmeans)
pk.plots()
pk.show()
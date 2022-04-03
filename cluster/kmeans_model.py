from copy import deepcopy
import random
import numpy as np
import matplotlib.pyplot as plt

from cluster.distance import Distance

class kmeans_model(Distance):
    

    def __init__(self, data, n_cluster=3, init_centroid=[]):
        self._data = np.array(data)
        
        if len(init_centroid) > 0:
            self._n_cluster = len(init_centroid)
        else:
            self._n_cluster = n_cluster
        
        self._init_centroid_(init_centroid)
        
        self._distance_all_data_()
        
    def _init_centroid_(self, sample_centroid):
        if len(sample_centroid) < self._n_cluster:
            # random centroid
            sample_centroid = self.__rand_centroid_(sample_centroid)
        elif len(sample_centroid) > self._n_cluster:
            sample_centroid = sample_centroid[:self._n_cluster]
        
        self._init_centroid = deepcopy(sample_centroid)

    def __rand_centroid_(self, sample_centroid):
        n_cluster = self._n_cluster        
        data = self._data
        i = 0
        while (i != n_cluster):
            temp = []
            for j in range(len(data[0])):
                Min, Max = self.__get_min_max(data, j)
                temp.append(random.randint(Min, Max))
            
            if temp not in sample_centroid:
                sample_centroid.append(temp)
                i += 1
        
        self._first_centroid = deepcopy(sample_centroid)
        return sample_centroid
        
    def __get_min_max(self, data, index):
        Min = min(data[:, index])
        Max = max(data[:, index])
        
        return Min, Max
        
    def getSumofDistance(self):
        dist_list = self._distance_list
        n = len(dist_list)
        error = 0
        for i in range(n):
            index = self._index_list[i]
            error = error + dist_list[i][index]
        
        return error
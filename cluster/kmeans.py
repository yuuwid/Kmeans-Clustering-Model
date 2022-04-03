from cluster.kmeans_model import kmeans_model
import numpy as np

class Kmeans(kmeans_model):
    _error = []
    
    def __init__(self, data, n_cluster=3, init_centroid=[], max_iter=100):
        super().__init__(data, n_cluster, init_centroid)
        self._max_iter = max_iter

        self._learning_()
    
    def _learning_(self):
        n = self._max_iter

        old_error = -1
        new_error = 0
        
        i = 0
        while old_error != new_error:
            if i == n:
                break
            i += 1
            
            old_error = new_error
            
            new_error = kmeans_model.getSumofDistance(self)
            self._init_centroid_(self._get_new_centroid_())
            self._distance_all_data_()
            
            self._error.append(new_error)

    
    def _get_new_centroid_(self):        
        clus = self._n_cluster
        
        indexes = self._index_list
        data = self._data
        n_d = len(data)
        
        new_centroid = []
        
        for j in range(clus):
            sum_data = np.zeros(2)
            n_data = 0
            for i in range(n_d):
                if indexes[i] == j:
                    sum_data += np.array(data[i])
                    n_data += 1
            new_centroid.append( (sum_data/n_data).tolist() )    
        
        return new_centroid
    
    
    def get_data(self):
        return self._data
    
    def get_centroid(self):
        return self._init_centroid
    
    def get_first_centroid(self):
        return self._first_centroid
    
    def get_error(self):
        return self._error
        
    def get_cluster(self):
        return self._index_list
    
    def get_distance(self):
        return self._distance_list
    
    
    def get_data_cluster(self):
        data = self._data
        index = self._index_list
        
        data_cluster = []
        
        n = self._n_cluster
        
        for i in range(n):
            temp = []
            for j in range(len(data)):
                if i == index[j]:
                    temp.append(data[j])
            data_cluster.append(temp)
            
        return data_cluster
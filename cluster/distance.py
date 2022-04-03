import math
import numpy as np


class Distance:
    
    def __distance(self, data, centroid):        
        n = len(data)        
        total = 0
        for i in range(n):
            total = total + math.pow( (data[i] - centroid[i]) , 2)
        return math.sqrt(total)
        
    def _distance_all_data_(self):
        data = self._data
        n = len(data)
        
        distance_list = []
        index_list = []
        
        for i in range(n):
            dist = self._distance_data_to_centroid_(data[i])
            
            distance_list.append(dist)
            index_list.append(self.__get_index_centroid_(dist))
            
        self._distance_list = distance_list
        self._index_list = index_list
                    
        
    def _distance_data_to_centroid_(self, data):
        centroid = self._init_centroid
        n = len(centroid)
        
        dist = []
        for i in range(n):
            dist.append(self.__distance(data, centroid[i]))
        
        return dist
        
    def __get_index_centroid_(self, distance):
        n = len(distance)
        index = 0
        distMin = distance[index]
        for i in range(1, n):
            if distMin > distance[i]:
                index = i
                distMin = distance[i]
        
        return index
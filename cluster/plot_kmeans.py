from cluster.kmeans import Kmeans
import matplotlib.pyplot as plt

import numpy as np
import random

class PlotKmeans:
    kmeans = None
    
    def __init__(self, kmeans: Kmeans):
        self.kmeans = kmeans
        
    def plot_error(self):
        plt.plot(self.kmeans.get_error())
    
    def scatter_data(self):
        x = self.kmeans.get_data_cluster()
        for i in range(len(x)):
            temp = np.array(x[i])
            
            color = self.__generate_color_()
            plt.scatter(temp[:, 0], temp[:, 1], c=color)
        
        self._scatter_centroid_()
        
    def plots(self, figsize=(10, 4)):
        plt.figure(figsize=figsize)
        plt.subplot(1, 2, 1)
        self.plot_error()
        plt.title('Error')
        
        plt.subplot(1, 2, 2)
        self.scatter_data()
        plt.title('Data')
        
        

    def show(self):
        plt.show()

    def _scatter_centroid_(self):
        centroid = np.array(self.kmeans.get_centroid())
        
        plt.scatter(centroid[:, 0], centroid[:, 1], c='black', marker='x')
        
    def __generate_color_(self):
        color = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
        return color  
    
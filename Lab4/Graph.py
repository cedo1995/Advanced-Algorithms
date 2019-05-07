from Cluster import Cluster
from Shire import Shire
import numpy as np
import sys
class Graph:

    def __init__(self, number_of_shires, shires):
        self.number_of_shires = number_of_shires
        self.shires = shires
        #for i in range(number_of_shires):
        #    self.shires.append(Shire(shires[i].id, shires[i].posX, shires[i].posY, shires[i].population, shires[i].cancer_risk))


    def hierarchicalClustering(self, k):
        """
        :param k: numero di cluster richiesti
        :return: un insieme di k cluster che partizionano le contee
        """
        n = self.number_of_shires
        cluster = []    # lista di cluster
        for i in range(n):      # aggiungo gli n cluster, ciascuno contenente solo il centroide
            cluster.append(Cluster(self.shires[i]))    # costruttore con l'elemento completo

        distances = []  # matrice delle distanze fra ciascun cluster identificati dall'indice
        while len(cluster) > k:
            distances = self.createDistanceMatrix(cluster)
            #print(distances)
            #print("Creata la matrice")
            minimum = self.searchMinimumDistance(distances)      # tripla della forma (distance, i, j) in cui è minima la distanza tra il cluster[i] e il  cluster[j]
            minimum = minimum[0]
            cluster[minimum[1]].unionCluster(cluster[minimum[2]])
            cluster.pop(minimum[2])     # rimuovo il cluster con indice j perchè già stato unito a quello con indice i
        return cluster      # ritorno la lista dei cluster

    def createDistanceMatrix(self, cluster):
        distances = np.ones((len(cluster), len(cluster)))
        for i in range(len(cluster) - 1):
            for j in range(i + 1, len(cluster)):
                distances[i][j] = cluster[i].distanceBetweenCluster(cluster[j])  # calcolo la distanza fra due cluster
                distances[j][i] = distances[i][j]  # matrice simmetrica
        return distances

    def searchMinimumDistance(self, distances):
        res = [(distances[i][j], i, j) for i in range(len(distances[0]) - 1) for j in range(i + 1, len(distances[0]))]
        res = sorted(res, key=lambda t: t[0])
        return res

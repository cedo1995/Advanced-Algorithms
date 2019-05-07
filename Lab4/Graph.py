from Cluster import Cluster
import numpy as np
import sys
class Graph:

    def __init__(self, number_of_shires, shires):
        self.number_of_shires = number_of_shires
        self.shires = shires


    def hierarchicalClustering(self, k):
        """
        :param k: numero di cluster richiesti
        :return: un insieme di k cluster che partizionano le contee
        """
        n = self.number_of_shires
        cluster = []    # lista di cluster
        for i in range(n):      # aggiungo gli n cluster, ciascuno contenente solo il centroide
            cluster.append(Cluster(self.shires[i]))     # costruttore con l'elemento completo
        # todo valutare se aggiungere il centroide alla lista degli elementi del cluster oppure lasciarlo esterno

        distances = []  # matrice delle distanze fra ciascun cluster identificati dall'indice
        while len(cluster) > k:
            distances = self.createDistanceMatrix(cluster)
            print(distances)
            print("Creata la matrice")
            minimum = self.searchMinimumDistance(distances)      # tripla della forma (distance, i, j) in cui è minima la distanza tra il cluster[i] e il  cluster[j]
            minimum = minimum[0]
            # print(minimum)

            new_cluster = Cluster(cluster[int(minimum[1])].unionCluster(cluster[int(minimum[2])]))     # creo un nuovo cluster dato dall'unione dei cluster che rendono minima la funzione distanza
            print("STAMPATO")
            cluster.pop(minimum[1])     # rimuovo il cluster con indice i
            cluster.pop(minimum[2])     # e con indice j
            cluster.append(new_cluster)         # aggiungo il nuovo cluster alla lista dei cluster

        return cluster      # ritorno la lista dei cluster

    def createDistanceMatrix(self, cluster):
        distances = np.ones((self.number_of_shires, self.number_of_shires))
        for i in range(self.number_of_shires - 1):
            for j in range(i + 1, self.number_of_shires):
                distances[i][j] = cluster[i].distanceBetweenCluster(cluster[j])  # calcolo la distanza fra due cluster
                distances[j][i] = distances[i][j]  # matrice simmetrica
        return distances

    def searchMinimumDistance(self, distances):
        res = [(distances[i][j], i, j) for i in range(self.number_of_shires - 1) for j in range(i + 1, self.number_of_shires)]
        res = sorted(res, key=lambda t: t[0])
        return res

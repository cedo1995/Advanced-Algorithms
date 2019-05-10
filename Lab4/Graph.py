from Cluster import Cluster
from Shire import Shire
import numpy as np
import sys
import copy
import time

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

        cluster = {}   # lista di cluster
        for i in range(n):      # aggiungo gli n cluster, ciascuno contenente solo il centroide
            #cluster.append(Cluster(self.shires[i]))    # costruttore con l'elemento completo
            cluster[Cluster(self.shires[i]).centroid] = Cluster(self.shires[i])
        #print(cluster)
        #distances = self.createDistanceMatrix(cluster)

        ordered_distances = self.createMinList(cluster)

        while len(cluster) > k:         # todo Controllare se si riesce ad eseguire la ricerca del minimo solo una volta e non per ogni ciclo, O(n) ogni ciclo
            # ordered_distances = self.searchMinimumDistance(distances)      # tripla della forma (distance, i, j) in cui è minima la distanza tra il cluster[i] e il  cluster[j]
            print(len(cluster))
            minimum = self.findMinimum(ordered_distances)
            #print(" minimum ", minimum)

            cluster[minimum[0]].unionCluster(cluster[minimum[1]])
            new_key = cluster[minimum[0]].centroid
            ora = time.time()
            #cluster.pop(minimum[1])     # rimuovo il cluster con indice j perchè già stato unito a quello con indice i
            del cluster[minimum[1]]
            cluster[new_key] = cluster[minimum[0]]
            del cluster[minimum[0]]
            print(time.time()-ora)
            #print("distances prima \n", distances)
            #distances = self.updateDistanceMatrix(distances, cluster, minimum[1], minimum[2])
            #print(" distances dopo \n", distances)
            #print("ordered distances prima \n", ordered_distances)
            ordered_distances = self.updateDistanceList(distances)
            #print("ordered distances dopo\n ", ordered_distances)
        return cluster      # ritorno la lista dei cluster

    def findMinimum(self, res):
        min_item = [None, None, sys.maxsize]
        for i in res:
            if i[1]<min_item[2]:
                min_item = i
        return min_item




    def createMinList(self, cluster):     #todo: valutare se tenere come range len(distances) oppure mettere len(cluster)

        res = []
        tempCluster = cluster
        for key in cluster:
            for chiave in tempCluster:
                if chiave != key:
                    res.append([key, chiave, cluster[key].distanceBetweenCluster(cluster[chiave])])
                #res[cluster[i].centroid] = [cluster[j].centroid, cluster[i].distanceBetweenCluster(cluster[j])
            del tempCluster[key]



        #res = sorted(res, key=lambda t: t[0])
        return res

    def updateDistanceList(self, cluster, distances, ordered_distances, minimum):
        """
        :param distances: matrice delle distanze
        :param ordered_distances: lista di triple (distanza, i, j) ove i, j sono gli indici dei cluster e distanza è la distanza fra il cluster i e il cluster j
        :param minimum: tripla della forma (distanza, i, j), rappresenta l'istanza con minima distanza trovata
        :return: ordered_distances aggiornata con i nuovi valori in seguito all'unione fra i cluster
        """
        for key in res:
            if key == index_to_delete or res[key][0] == index_to_delete or key == index_to_modify or res[key][0] == index_to_modify:
                del res[key]

        for key in cluster:
            if key != new_index:
                res[new_index] = cluster[new_index].distanceBetweenCluster(cluster[res[key][0]])
                res[key][1] = cluster[key].distanceBetweenCluster(cluster[res[key][0]])





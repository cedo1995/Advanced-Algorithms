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
        # for i in range(number_of_shires):
        #    self.shires.append(Shire(shires[i].id, shires[i].posX, shires[i].posY, shires[i].population, shires[i].cancer_risk))

    def hierarchicalClustering(self, k):
        """
        :param k: numero di cluster richiesti
        :return: un insieme di k cluster che partizionano le contee
        """
        n = self.number_of_shires

        clusters = {}   # lista di cluster
        for i in range(n):      # aggiungo gli n cluster, ciascuno contenente solo il centroide,  nella mappa
            cluster = Cluster(self.shires[i])
            clusters[cluster.id] = cluster

        min_list = self.createMinList(clusters)

        while len(clusters) > k:  # TODO: Controllare se si riesce ad eseguire la ricerca del minimo solo una volta e non per ogni ciclo, O(n) ogni ciclo
            print(len(clusters))
            minimum = self.findMinimum(min_list)

            newCluster = minimum[0]
            delCluster = minimum[1]

            clusters[newCluster].unionCluster(clusters[delCluster])

            min_list = self.updateDistanceList(min_list, clusters, newCluster, delCluster)
            del clusters[delCluster]

        return clusters      # ritorno la lista dei cluster

    def createMinList(self, clusters):
        minList = []
        tempClusters = copy.deepcopy(clusters)
        for id1 in clusters:
            for id2 in tempClusters:
                if id1 != id2:
                    minList.append([id1, id2, clusters[id1].distanceBetweenCluster(clusters[id2])])
            del tempClusters[id1]
        return minList

    def findMinimum(self, list):
        min_item = [None, None, sys.maxsize]
        for i in list:
            if i[2] < min_item[2]:
                min_item = i
        return min_item

    def updateDistanceList(self, min_list, clusters, new_cluster, del_cluster):
        """
        :param min_list:  lista di triple (i, j, distanza) dove i, j sono gli id dei cluster e distanza è la distanza fra il cluster i e il cluster j
        :param clusters: mappa dei cluster
        :param new_cluster: id del Cluster unione
        :param del_cluster: id del Cluster da eliminare
        :return: ordered_distances aggiornata con i nuovi valori in seguito all'unione fra i cluster
        """
        list = copy.deepcopy(min_list)
        for dist in list:
            if (del_cluster == dist[0]) | (del_cluster == dist[1]):
                min_list.remove(dist)
            if new_cluster == dist[0]:
                dist[2] = clusters[dist[0]].distanceBetweenCluster(clusters[dist[1]])
            if new_cluster == dist[1]:
                dist[2] = clusters[dist[1]].distanceBetweenCluster(clusters[dist[0]])
        return min_list

    def kMeansClustering(self, k, iter):
        """
        :param k: numero di cluster richiesti
        :param iter: numero di iterazioni da effettuare
        :return: un insieme di k cluster che partizionano le contee
        """

        n = self.number_of_shires

        ordered_shire = sorted(self.shires, reverse=True, key=self.sortSecond)
        top_shires = ordered_shire[0:k] # k contee con popolazione più elevata

        clusters = {}  # lista di cluster
        for i in range(k):  # aggiungo k cluster, ciascuno con una delle k contee con più popolazione
            cluster = Cluster(top_shires[i])
            clusters[cluster.id] = cluster

        # for i in range(iter):

    def sortSecond(self, val):
        return int(val.population)
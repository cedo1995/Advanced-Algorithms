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
            #print(len(clusters))
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

    def kMeansClustering(self, k, iter, points):
        """
        :param k: numero di cluster richiesti
        :param iter: numero di iterazioni da effettuare
        :param points: lista di contee
        :return: un insieme di k cluster che partizionano le contee
        """

        n = self.number_of_shires

        ordered_shire = sorted(self.shires, reverse=True, key=self.sortSecond)
        top_shires = ordered_shire[0:k]  # k contee con popolazione più elevata
        centroids = []
        for i in range(k):          # creo i k centroidi iniziali
            centroids.append([top_shires[i].posX, top_shires[i].posY])

        for i in range(iter):   # aggiungo k cluster, ciascuno con una delle k contee con più popolazione
            clusters = {}           # lista di cluster in del tipo (id_cluster: cluster) TODO LASCIAMOLO DENTRO
            #cluster = Cluster(top_shires[i])  # creo l'istanza di cluster corrente
            #clusters[cluster.id] = cluster     TODO Forse non servono
            for j in range(n):
                minimum = sys.maxsize

                for f in range(k):
                    if minimum > self.distanceBetweenPoints(centroids[f], [points[j].posX, points[j].posY]):
                        minimum = self.distanceBetweenPoints(centroids[f], [points[j].posX, points[j].posY])
                        l = f       # assegno l'indice del centroide avente distanza minima dal punto

                if l not in clusters.keys():

                    clusters[l] = Cluster(points[j])
                else:

                    clusters[l].addElementToCluster(points[j])        # aggiungo al cluster con indice l il punto j
            for index in range(k):
                clusters[index].updateCentroids()
                centroids[index] = [clusters[index].pos_x, clusters[index].pos_y]
                #print(centroids[index])


        return clusters


    def sortSecond(self, val):
        return int(val.population)

    def distanceBetweenPoints(self, centroid, point):
        """
        :param centroid: punto di partenza iniziale nella forma [posX, posY]
        :param point: punto di arrivo nella forma [posX, posY]
        :return :
        """
        return float(((centroid[0] - point[0])**2 + (centroid[1] - point[1])**2)**0.5)

from Cluster import Cluster
from Shire import Shire
import numpy as np
import sys
import copy
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

        distances = self.createDistanceMatrix(cluster)
        ordered_distances = self.searchMinimumDistance(distances)
        print(ordered_distances[0], ordered_distances[1])
        minimum = []
        while len(cluster) > k:         # todo Controllare se si riesce ad eseguire la ricerca del minimo solo una volta e non per ogni ciclo, O(n) ogni ciclo
            # ordered_distances = self.searchMinimumDistance(distances)      # tripla della forma (distance, i, j) in cui è minima la distanza tra il cluster[i] e il  cluster[j]
            minimum = ordered_distances[0]
            cluster[minimum[1]].unionCluster(cluster[minimum[2]])
            cluster.pop(minimum[2])     # rimuovo il cluster con indice j perchè già stato unito a quello con indice i
            distances = self.updateDistanceMatrix(distances, cluster, minimum[1], minimum[2])
            ordered_distances = self.updateMinimumDistance(cluster, distances, ordered_distances, minimum)
        return cluster      # ritorno la lista dei cluster

    def createDistanceMatrix(self, cluster):
        distances = np.ones((len(cluster), len(cluster)))*sys.maxsize
        for i in range(len(cluster) - 1):
            for j in range(i + 1, len(cluster)):
                distances[i][j] = cluster[i].distanceBetweenCluster(cluster[j])  # calcolo la distanza fra due cluster
                distances[j][i] = distances[i][j]  # matrice simmetrica
        return distances

    def updateDistanceMatrix(self, distances, cluster, row_to_keep, row_to_remove):
        distances = np.delete(distances, int(row_to_remove), 0)     # np.delete rimuove dall'oggetto distances gli elementi della riga(per questo lo zero alla fine) con indice row_to_remove
        distances = np.delete(distances, int(row_to_remove), 1)     # rimuove da distances gli elementi della colonna(per questo l' 1 alla fine) con indice row_to_distances
        for i in range(len(cluster)):
            if row_to_keep != i:     # se non sto calcolando la distanza fra il cluster e sè stesso
                distances[i][row_to_keep] = cluster[i].distanceBetweenCluster(cluster[row_to_keep])     # aggiorno la matrice distances con i valori aggiornati
                distances[row_to_keep][i] = distances[i][row_to_keep]           # aggiorno distances con i valori corretti
        return distances

    def searchMinimumDistance(self, distances):     #todo: valutare se tenere come range len(distances) oppure mettere len(cluster)
        res = [(distances[i][j], i, j) for i in range(len(distances[0]) - 1) for j in range(i + 1, len(distances[0]))]
        res = sorted(res, key=lambda t: t[0])
        return res

    def updateMinimumDistance(self, cluster, distances, ordered_distances, minimum):
        """
        :param distances: matrice delle distanze
        :param ordered_distances: lista di triple (distanza, i, j) ove i, j sono gli indici dei cluster e distanza è la distanza fra il cluster i e il cluster j
        :param minimum: tripla della forma (distanza, i, j), rappresenta l'istanza con minima distanza trovata
        :return: ordered_distances aggiornata con i nuovi valori in seguito all'unione fra i cluster
        """
        for i, val in enumerate(ordered_distances):
            if val[1] == minimum[1] or val[2] == minimum[2] or val[1] == minimum[2] or val[2] == minimum[1]:
                ordered_distances.pop(i)

        for i in range(len(cluster)):
            ordered_distances.append((distances[i][minimum[1]], i, minimum[1]))
        ordered_distances = sorted(ordered_distances, key=lambda t: t[0])
        return ordered_distances


    def insertValueInOrderedDistances(self, ordered_distances, value):
        """
        :param ordered_distances: lista di tuple della forma(distanza, i, j) ordinate in modo crescente rispetto alla distanza
        :param value: tupla dalla forma (distanza, i, j)
        :return ordered_distances aggiornata con la tupla value inserita al posto giusto
        """
        for i in range(len(ordered_distances)):
            if value[0] < ordered_distances[i][0]:
                # inserisco la tupla prima dell'iesima tupla di ordered_value e faccio shift di tutto il resto a destra
                ordered_distances.insert(i, value)      # inserisco la tupla nella posizione corretta
                return ordered_distances
        return ordered_distances

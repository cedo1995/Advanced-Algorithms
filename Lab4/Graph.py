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

    def hierarchicalClustering(self, points, k):
        """
        :param k: numero di cluster richiesti
        :return: un insieme di k cluster che partizionano le contee
        """

        P = points[points[:, 0].argsort()]
        S = points[points[:, 1].argsort()]
        #print(P)
        clusters = [Cluster(i[0], i[1], k) for k, i in enumerate(P)]
        #print(clusters)


        while len(clusters) > k:
            print(len(clusters))

            minimum = self.fastClosestPair(P, S)
            #print(minimum)
            #print("ciao")
            newCluster = minimum[1]
            delCluster = minimum[2]     # l'indice corrisponde all'id del cluster

            clusters[newCluster].unionCluster(clusters[delCluster])     # unisco i due cluster mettendo tutti gli elementi di clusters[delCluster] in clusters[newCluster]
            clusters.pop(delCluster)
            np.delete(P, delCluster, axis=0)
            for i, cl in enumerate(clusters):
                P[i] = [cl.pos_x, cl.pos_y]
            P = P[P[:, 0].argsort()]
            S = P[P[:, 1].argsort()]






        return clusters      # ritorno la lista dei cluster

    def fastClosestPair(self, P, S):
        '''
        :param P: lista di n cluster in cui ogni cluster ha un id e una coppia x,y ordinati per x crescente
        :param S: lista di indici dei punti P ordinati per y crescente
        :return: tripla minima
        '''
        n = len(P)
        tripla_minima = [sys.maxsize, -1, -1]
        if n <= 3:
            return self.slowClosestPair(P)
        else:
            m = int(n/2)
            P_l = P[0:m]    # filtro i valori di P con la condizione che ogni elemento sia in range(m)
            P_r = P[m:]    #     filtro i valori di P con la condizione che ogni elemento sia in range(m, n)
            S_l, S_r = self.split(S, P_l, P_r)
            tripla_minima_l = self.fastClosestPair(P_l, S_l)
            tripla_minima_r = self.fastClosestPair(P_r, S_r)
            if tripla_minima_l[0] <= tripla_minima_r[0]:
                tripla_minima = tripla_minima_l
            else:
                tripla_minima = tripla_minima_r
            mid = 0.5 * (P[m-1][0] + P[m][0])
            if tripla_minima[0] <= self.closestPairStrip(S, mid, tripla_minima[0], P)[0]:
                return tripla_minima
            else:
                return self.closestPairStrip(S, mid, tripla_minima[0], P)


    def closestPairStrip(self, S, mid, d, P):
        '''
        :param S: lista di n indici di punti ordinati per y crescente
        :param mid: valore reale
        :param d: valore reale positivo
        :param P: lista di cluster
        :return:
        '''
        n = len(S)
        S_ = []
        k = 0

        for i in range(n):
            if abs(S[i][0] - mid) < d:
                S_.append(S[i])
                k += 1
        tripla_minima = [sys.maxsize, -1, -1]

        for u in range(k-1):         #TODO: CONTROLLAMI L'intervallo

            for v in range(u+1, min(u + 5, n - 1) + 1 ):
                #print(S_)

                if v < len(S_) and tripla_minima[0] > self.distanceBetweenPoints(S_[u], S_[v]):
                    tripla_minima = [self.distanceBetweenPoints(S_[u], S_[v]), u, v]
        return tripla_minima

    def slowClosestPair(self, clusters):
        '''
        :param clusters: una lista di clusters dove sono importanti gli id dei cluster e le coordinate X e Y
        :return:
        '''
        tripla_minima = [sys.maxsize, -1, -1]
        for i, p_u in enumerate(clusters):
            for j, p_v in enumerate(clusters):
                if j > i:    # cioè considero la matrice triangolare superiore
                    min_dist = tripla_minima[0]
                    if self.distanceBetweenPoints(p_u, p_v) < min_dist:
                        tripla_minima = [self.distanceBetweenPoints(p_u, p_v), i, j]
        return tripla_minima


    def split(self, S, P_l, P_r):
        '''
        :param S: lista contenente gli indici da 0 a n-1 ordinati per y crescente
        :param P_l: lista di cluster contentente partizione dell'inisieme dei centroidi
        :param P_r: lista di cluster contenente partizione dell'inisieme dei centroidi
        :return: due vettori ordinati che contengono gli elementi in P_l e P_r
        '''
        n = len(S)
        S_l, S_r = [], []
        j, k = 0, 0
        for i in range(n):
            if S[i] in P_l:
                S_l.append(S[i])
                j += 1
            else:
                S_r.append(S[i])
                k += 1
        return S_l, S_r



    def updateDistanceList(self, min_list, clusters, new_cluster, del_cluster):     #FIXME: mettimi a posto i commenti
        """
        :param min_list:  lista di triple (i, j, distanza) dove i, j sono gli id dei cluster e distanza è la distanza fra il cluster i e il cluster j
        :param clusters: mappa dei cluster
        :param new_cluster: id del Cluster unione
        :param del_cluster: id del Cluster da eliminare
        :return: ordered_distances aggiornata con i nuovi valori in seguito all'unione fra i cluster
        """
        #list = copy.deepcopy(min_list)
        ora = time.time()
        for i, dist in enumerate(min_list):

            if new_cluster == dist[0]:
                min_list[i][2] = clusters[dist[0]].distanceBetweenCluster(clusters[dist[1]])

            if new_cluster == dist[1]:
                min_list[i][2] = clusters[dist[1]].distanceBetweenCluster(clusters[dist[0]])

        print("tempo primo ciclo -> ", time.time() - ora)

        list = copy.deepcopy(min_list)

        ora = time.time()
        print(len(list))
        counter = 0
        for dist in list:   # FIXME: O(n^2)
            if (del_cluster == dist[0]) or (del_cluster == dist[1]):
                counter += 1
                #print("->", dist)
                min_list.remove(dist)   # FIXME: O(n)
        print("ho rimosso ",counter, " elementi")
        print("tempo secondo ciclo -> ", time.time() - ora)

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

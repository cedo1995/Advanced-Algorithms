import math
import numpy as np
import sys
import copy
import time

from Distance import Distance


class Graph:
    def __init__(self, name, dimension, coord_type, coordinates):
        """
        :param name: nome del grafo che si sta analizzando
        :param dimension: numero dei nodi del grafo
        :param coord_type: tipo di coordinate utilizzate
        :param coordinates: lista di tutte le coordinate
        :param count_to_coordinates: dizionario che relaziona la posizione della coordinata nel file rispetto ai valori
        """
        self.name = name
        self.num_nodes = int(dimension)
        self.coord_type = coord_type
        self.coordinates = coordinates
        self.num_edges = 0          # numero di archi del grafo
        self.matr_adj = np.zeros(shape=(self.num_nodes, self.num_nodes))

        # aggiunta di tutti gli archi al grafo in modo da creare un grafo completo
        for i in range(self.num_nodes-1):
            for j in range(i+1, self.num_nodes):
                self.num_edges += 1
                self.matr_adj[i][j] = self.calculateWeight(self.coordinates[i], self.coordinates[j])
                self.matr_adj[j][i] = self.matr_adj[i][j]





    def printG(self):
        print("Il grafo", self.name, "ha ", self.num_nodes, "nodi e ", self.num_edges, "archi")
        print(self.matr_adj)


    def calculateWeight(self, coordinates1, coordinates2):
        if self.coord_type != "GEO\n":
            x = abs(coordinates1[0] - coordinates2[0])
            y = abs(coordinates1[1] - coordinates2[1])
            return round((x**2 + y**2)**0.5)
        else:
            RRR = 6378.388

            q1 = math.cos(coordinates1[1] - coordinates2[1])
            q2 = math.cos(coordinates1[0] - coordinates2[0])
            q3 = math.cos(coordinates1[0] + coordinates2[0])
            return round(RRR * math.acos(0.5 * ((1.0 + q1) * q2 - (1.0 - q1) * q3)) + 1.0)

    def hkVisit(self, v, subset_nodes, distances, previous, start_time, stop):
        """
        :param v: nodo destinazione
        :param subset_nodes: sottoinsieme di nodi in cui viene calcolato il peso del cammino minimo
        :return: peso del cammino minimo da 0 a v che visita tutti i vertici in subset_nodes
        """
        #print("HK_VISIT", v, subset_nodes)

        if len(subset_nodes) == 1 and subset_nodes[0] == v:
            if distances[v] == -1:  # se distances in v non è ancora definito
                #print("entrato nel caso in cui ho un solo elemento in subset_nodes")
                distances[v] = Distance(v, subset_nodes, self.matr_adj[0][v])  # creo l'istanza di Distance con un distance item con il valore minimo trovato
            #print(self.matr_adj[0][v], v)
            #print(subset_nodes)
            return self.matr_adj[0][v], distances, previous, stop

        elif distances[v] != -1 and distances[v].has_subset_items(subset_nodes)[0]:
            #print("SCR>i", v, subset_nodes)
            return distances[v].value, distances, previous, stop
        else:

            min_dist = sys.maxsize
            min_prec = -1
            subset = copy.copy(subset_nodes)
            subset.remove(v)
            """
            print("SUBSET:")
            for i in subset:
                print(i)
            print("SUBSET_NODES:")
            for i in subset_nodes:
                print(i)
            #print("SUBSET=", subset_nodes)
            """

            for vertex in subset_nodes:
                if stop:
                    break

                if vertex != v:
                    dist, distances, previous, stop = self.hkVisit(vertex, subset, distances, previous, start_time, stop)

                    if dist + self.matr_adj[vertex][v] < min_dist:
                        min_dist = dist + self.matr_adj[vertex][v]
                        min_prec = vertex
            if time.time() - start_time > 20:
                stop = True
                return min_dist, distances, previous, stop


            if distances[v] == -1:        # se distances in v non è ancora definito
                distances[v] = Distance(v, subset_nodes, min_dist)        # creo l'istanza di Distance con un distance item con il valore minimo trovato

            if previous[v] == -1:        # se previous in v non è ancora definito
                previous[v] = Distance(v, subset_nodes, min_prec)        # creo il predecessore di v rispetto


            if distances[v].has_subset_items(subset_nodes)[0]:
                distances[v].value = min_dist
            else:
                distances[v].addDistanceItem(subset_nodes, min_dist)

            if previous[v].has_subset_items(subset_nodes)[0]:
                previous[v].value = min_prec
            else:
                previous[v].addDistanceItem(subset_nodes, min_prec)

            return min_dist, distances, previous, stop



    def hkTsp(self, start_time):
        distances = [-1 for x in range(self.num_nodes)]          # lista di Distance in cui ogni elemento è un DistanceItem con valore la distanza
        previous = [-1 for x in range(self.num_nodes)]           # lista di Distance in cui ogni elemento è un DistanceItem con valore dell'id del predecessore
        vertices = [x for x in range(self.num_nodes)]
        return self.hkVisit(0, vertices, distances, previous, start_time, False)








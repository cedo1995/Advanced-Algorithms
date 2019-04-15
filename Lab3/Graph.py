import math
import numpy as np
import sys

from AdvAlg.Lab3.Distance import Distance


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

    def hkVisit(self, v, subset_nodes, distances, previous):
        """
        :param v: nodo destinazione
        :param subset_nodes: sottoinsieme di nodi in cui viene calcolato il peso del cammino minimo
        :return: peso del cammino minimo da 0 a v che visita tutti i vertici in subset_nodes
        """
        if len(subset_nodes) == 1 and subset_nodes[0] == v:
            return self.matr_adj[0, v], distances, previous
        elif distances[v] is not None and distances[v].has_subset_items(subset_nodes)[0]:
            return distances[v].has_subset_items(subset_nodes)[1].value, distances, previous
        else:
            min_dist = sys.maxsize
            min_prec = None
            subset_nodes.remove(v)
            for vertex in subset_nodes:
                dist = self.hkVisit(vertex, subset_nodes, distances, previous)
                if dist + self.matr_adj[vertex][v] < min_dist:
                    min_dist = dist + self.matr_adj[vertex][v]
                    min_prec = vertex

            if distances[v] is None:        # se distances in v non è ancora definito
                distances[v] = Distance(v, subset_nodes, min_dist)        # creo l'istanza di Distance con un distance item con il valore minimo trovato

            if distances[v].has_subset_items(subset_nodes)[0]:
                distances[v].has_subset_items(subset_nodes)[1].value = min_dist
            else:
                distances[v].addDistanceItem(subset_nodes, min_dist)

            previous[(v, subset_nodes)] = min_prec

            return min_dist, distances, previous



    def hkTsp(self):
        distances = []          # lista di Distance in cui ogni elemento è un DistanceItem con valore la distanza
        previous = []           # lista di Distance in cui ogni elemento è un DistanceItem con valore dell'id del predecessore
        vertices = [x for x in range(self.num_nodes)]
        return self.hkVisit(0, vertices, distances, previous)








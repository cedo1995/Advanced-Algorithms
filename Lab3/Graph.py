import math
import numpy as np

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
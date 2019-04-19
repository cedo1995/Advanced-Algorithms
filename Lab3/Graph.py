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

    def hkVisit(self, v, subset_nodes, distances, previous, start_time, stop, mymap, count):
        """
        :param v: nodo destinazione
        :param subset_nodes: sottoinsieme di nodi in cui viene calcolato il peso del cammino minimo
        :return: peso del cammino minimo da 0 a v che visita tutti i vertici in subset_nodes
        """
        #print("HK_VISIT", v, subset_nodes)
        if len(subset_nodes) == 1 and subset_nodes[0] == v:
            count += 1
            return self.matr_adj[0][v], distances, previous, stop, count

        elif distances[v][mymap[tuple(subset_nodes)]] != -1:
            # print("ENTRATO!")
            return distances[v][mymap[tuple(subset_nodes)]], distances, previous, stop, count
        else:
            min_dist = sys.maxsize
            min_prec = -1
            subset = copy.deepcopy(subset_nodes)
            subset.remove(v)

            for vertex in subset:
                if stop:
                    break
                dist, distances, previous, stop, count = self.hkVisit(vertex, subset, distances, previous, start_time, stop, mymap, count )

                if dist + self.matr_adj[vertex][v] < min_dist:
                    min_dist = dist + self.matr_adj[vertex][v]
                    min_prec = vertex
            if time.time() - start_time > 180:
                stop = True
                return min_dist, distances, previous, stop, count

            distances[v][mymap[tuple(subset_nodes)]] = min_dist

            #print(count)
            return min_dist, distances, previous, stop, count



    def hkTsp(self, start_time):
        column = []  # lista di Distance in cui ogni elemento è un DistanceItem con valore la distanza
        mymap = {}
        counter = 0
        for i in range(self.num_nodes):
            column_copia = copy.deepcopy(column)
            #print(column_copia)
            column.append([i])
            mymap[tuple([i])] = counter
            counter += 1
            for j in range(0, len(column_copia)):
                #print(i)
                column_copia[j].append(i)
                #print(column_copia[j])
                mymap[tuple(column_copia[j])] = counter
                column.append(column_copia[j])
                counter += 1
        #print(column)
        distances = np.full((self.num_nodes, len(column)), -1, dtype=float)

        previous = [-1 for x in range(self.num_nodes)]           # lista di Distance in cui ogni elemento è un DistanceItem con valore dell'id del predecessore
        vertices = [x for x in range(self.num_nodes)]
        count = 0
        return self.hkVisit(0, vertices, distances, previous, start_time, False, mymap, count)








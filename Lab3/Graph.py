import math
import numpy as np
import sys
import copy
import time
from Tree import Tree
from Distance import Distance
from Node import Node
from Edge import Edge
sys.setrecursionlimit(10000)

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
            return int(RRR * math.acos(0.5 * ((1.0 + q1) * q2 - (1.0 - q1) * q3)) + 1.0)

    def hkVisit(self, v, subset_nodes, distances, previous, start_time, stop, mymap):
        """
        :param v: nodo destinazione
        :param subset_nodes: sottoinsieme di nodi in cui viene calcolato il peso del cammino minimo
        :return: peso del cammino minimo da 0 a v che visita tutti i vertici in subset_nodes
        """
        #print("HK_VISIT", v, subset_nodes)
        g = tuple(subset_nodes)

        if len(subset_nodes) == 1 and subset_nodes[0] == v:
            return self.matr_adj[0][v], distances, previous, stop

        elif (v, g) in distances:
            #print("ENTRATO!",distances[v][g])
            return distances[v, g], distances, previous, stop
        else:
            min_dist = sys.maxsize
            min_prec = -1
            subset = copy.deepcopy(subset_nodes)
            subset.remove(v)

            for vertex in subset_nodes:
                if stop:
                    break

                if vertex != v:
                    dist, distances, previous, stop = self.hkVisit(vertex, subset, distances, previous, start_time, stop, mymap)

                    if dist + self.matr_adj[vertex][v] < min_dist:
                        min_dist = dist + self.matr_adj[vertex][v]
                        min_prec = vertex
            if time.time() - start_time > 20*60:
                stop = True
                return min_dist, distances, previous, stop

            # distances[0][tuple(subset_nodes)] = 10

            distances.update({(v, g): min_dist})
            #print(v, g)
            #print(distances[v,g])

            #distances[v][tuple(subset_nodes)] = min_dist

            return min_dist, distances, previous, stop



    def hkTsp(self, start_time):
        column = []  # lista di Distance in cui ogni elemento è un DistanceItem con valore la distanza
        mymap = {}
        counter = 0
        """
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
        """
        distances = {}
        previous = [-1 for x in range(self.num_nodes)]           # lista di Distance in cui ogni elemento è un DistanceItem con valore dell'id del predecessore
        vertices = [x for x in range(self.num_nodes)]
        return self.hkVisit(0, vertices, distances, previous, start_time, False, mymap)


    def nearestNeighbor(self):
        circuit = []
        total_circuit_length = 0
        circuit.append(0)
        visited_nodes = [False for x in range(self.num_nodes)]
        visited_nodes[0] = True
        for i in range(1, self.num_nodes):
            min_dist = sys.maxsize
            choosen_index = -1
            for index, val in enumerate(self.matr_adj[circuit[-1]]):
                if val < min_dist and not visited_nodes[index]:
                    min_dist = val
                    choosen_index = index

            circuit.append(choosen_index)
            visited_nodes[choosen_index] = True
            total_circuit_length += min_dist

        total_circuit_length += self.matr_adj[0][circuit[-1]]       #aggiungo la distanza fra l'ultimo nodo trovato e il nodo sorgente
        circuit.append(0)
        return circuit, total_circuit_length        # Todo Togliere il ritorno di circuit che non serve

    def createArraysOfEdges(self):      # Controllato, ritorna un array di due dimensioni in cui ciascuna riga è una tupla di 3 valori ordinata secondo il primo valore
        res = [(self.matr_adj[i][j], i, j)
               for i in range(self.num_nodes - 1)
               for j in range(i+1, self.num_nodes)]

        res = sorted(res, key=lambda t: t[0])

        return res

    def kruskalMST(self):
        couples = []
        for i in range(self.num_nodes):
            couples.append(Node(i))
        #arr_sets = []
        set_tree = Tree(self.num_nodes)
        for i in range(self.num_nodes):
            set_tree.makeSet(i)
        edges = self.createArraysOfEdges()  # todo crea la funzione che crea gli archi ordinati di peso crescente
        #print("uscito")
        for val in edges:
            #print(val[0])
            if set_tree.findSet(val[1]) != set_tree.findSet(val[2]):
                #print("entrato")
                couples[val[1]].addEdgeToNode(Edge(val[1], val[2], val[0]))
                couples[val[2]].addEdgeToNode(Edge(val[2], val[1], val[0]))
                set_tree.union(val[1], val[2])

        already_inserted = [False for x in range(self.num_nodes)]
        dictionary = {}
        counter = 0
        start_node = couples[0]
        counter, graph_enumeration = self.deptFirstSearch(couples, counter, dictionary, start_node, already_inserted)
        graph_enumeration[counter] = couples[0].id
        dist = self.calculate_distance_MST(graph_enumeration)
        return dist

    def deptFirstSearch(self, couples, counter, dictionary, start_node, already_inserted):
        """
        :param couples: array di nodi con la lista di adiacenza per ciascun nodo
        :param counter: contatore per la numerazione dei nodi
        :param dictionary: dizionario che associa la numerazione dei nodi all'id del nodo nel grafo originale(self)
        :param start_node: nodo di partenzaarr_sets = []
        :return: dict finale
        """
        #print("deptFirstSearch")
        dictionary[counter] = start_node.id
        already_inserted[start_node.id] = True
        counter += 1
        for edge in start_node.adj_arr:
            if not already_inserted[edge.arrival_node]:
                counter, dictionary = self.deptFirstSearch(couples, counter, dictionary, couples[edge.arrival_node],
                                                           already_inserted)

        return counter, dictionary

    def calculate_distance_MST(self, graph_enumeration):
        dist = 0
        #print("calculate_distance_MST")
        for i in range(self.num_nodes):
            dist += self.matr_adj[graph_enumeration[i]][graph_enumeration[i+1]]
        return dist















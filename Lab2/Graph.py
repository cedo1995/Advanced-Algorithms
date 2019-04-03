from Node import Node
from Edge import Edge
from BinaryHeap import BinaryHeap
import sys

class Graph:
    def __init__(self):
        self.id_to_number = {}
        self.nodes_number = 0
        self.nodes_list = []  #lista di nodi contenuti nel grafo
        self.edges_number = 0       #contatore degli archi
        self.number_to_id = {}    #associa il count all'id_stazione e al suo nome

    def ReturnIdToNumber(self):
        return self.id_to_number

    def ReturnNumberToId(self):
        return self.number_to_id

    def PrintG(self):   #stampa le informazioni principali del grafo
        print("Grafo con ", self.nodes_number, " nodi e ", self.edges_number, " archi.")

    def AddNode(self, id_station, name_station, count):
        id_station = int(id_station)
        self.id_to_number[id_station] = count
        self.nodes_number += 1
        self.nodes_list.append(Node(id_station))
        self.number_to_id[count] = id_station

    def AddEdge(self, edge):
        self.edges_number += 1
        i = self.id_to_number[edge.id_departure_station]
        self.nodes_list[i].AddEdgeToNode(edge)

    def Relax(self, u, v, previous_nodes, distances, edge, timetables):  # u e v sono indici dei nodi da rilassare
        timetables[v] = edge.arrival_time
        distances[v] = distances[u] + edge.MinutesCounter(timetables[u], edge.arrival_time)
        previous_nodes[v] = u
        return distances, previous_nodes, timetables

    def Dijkstra(self, id_start_node, min_departure_time):
        distances = []
        heap = BinaryHeap()
        previous_nodes = []
        timetables = []
        for i, x in enumerate(self.nodes_list):
            distances.append(sys.maxsize)
            previous_nodes.append(-1)
            timetables.append("-1")
            heap.Add(x.id, distances[self.id_to_number[x.id]])
        distances[self.id_to_number[id_start_node]] = 0
        timetables[self.id_to_number[id_start_node]] = min_departure_time
        heap.DecreaseKey(id_start_node, 0)       #decremento il valore della heap ad indice idToNumber[startNodeId] a 0 in modo da essere la sorgente
        while len(heap.list_vertices) > 0:
            u = heap.ExtractMin()
            if timetables[self.id_to_number[u.id]] != "-1":
                for edge in self.nodes_list[self.id_to_number[u.id]].adj_arr:
                    if int(edge.departure_time) >= int(timetables[self.id_to_number[u.id]]) and distances[self.id_to_number[u.id]] + edge.MinutesCounter(timetables[self.id_to_number[u.id]], edge.arrival_time) < distances[self.id_to_number[edge.id_arrival_station]]:  # poichè la partenza da una stazione deve essere dopo l'orario di arrivo nella stazione precedente cioè se arrivo alle 13 non posso partire alle 12.55
                        distances, previous_nodes, timetables = self.Relax(self.id_to_number[u.id], self.id_to_number[edge.id_arrival_station], previous_nodes, distances, edge, timetables)
                        heap.DecreaseKey(edge.id_arrival_station, distances[self.id_to_number[edge.id_arrival_station]])



        return distances, previous_nodes, timetables












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

    def returnIdToNumber(self):
        return self.id_to_number

    def returnNumberToId(self):
        return self.number_to_id

    def printG(self):   #stampa le informazioni principali del grafo
        print("Grafo con ", self.nodes_number, " nodi e ", self.edges_number, " archi.")

    def addNode(self, id_station, name_station, count):
        id_station = int(id_station)
        self.id_to_number[id_station] = count
        self.nodes_number += 1
        self.nodes_list.append(Node(id_station))
        self.number_to_id[count] = id_station

    def addEdge(self, edge):
        self.edges_number += 1
        i = self.id_to_number[edge.id_departure_station]
        self.nodes_list[i].addEdgeToNode(edge)

    def relax(self, u, v, previous_nodes, distances, edge, timetables, run_id_list, line_id_list, time_departures):  # u e v sono indici dei nodi da rilassare
        timetables[v] = edge.arrival_time
        distances[v] = distances[u] + (self.CEDO(timetables[u], edge.arrival_time) + (self.orario(edge.arrival_time) - self.orario(edge.departure_time)))
        run_id_list[v] = edge.run_id
        line_id_list[v] = edge.id_line
        previous_nodes[v] = u
        time_departures[v] = edge.departure_time
        return distances, previous_nodes, timetables, run_id_list, line_id_list, time_departures

    def dijkstra(self, id_start_node, min_departure_time):
        distances = []
        heap = BinaryHeap()
        previous_nodes = []
        timetables = []
        time_departures = []

        run_id_list = []
        line_id_list = []

        for i, x in enumerate(self.nodes_list):
            distances.append(sys.maxsize)
            previous_nodes.append(-1)
            timetables.append("-1")
            run_id_list.append("-1")
            line_id_list.append("-1")
            time_departures.append("-1")
            heap.add(x.id, distances[self.id_to_number[x.id]])
        distances[self.id_to_number[id_start_node]] = 0
        timetables[self.id_to_number[id_start_node]] = min_departure_time
        heap.decreaseKey(id_start_node, 0)       #decremento il valore della heap ad indice idToNumber[startNodeId] a 0 in modo da essere la sorgente
        while len(heap.list_vertices) > 0:
            u = heap.extractMin()
            if timetables[self.id_to_number[u.id]] != "-1":
                for edge in self.nodes_list[self.id_to_number[u.id]].adj_arr:
                    if distances[self.id_to_number[u.id]] + (self.CEDO(timetables[self.id_to_number[u.id]], edge.departure_time) + (self.orario(edge.arrival_time) - self.orario(edge.departure_time))) < distances[self.id_to_number[edge.id_arrival_station]]:
                    # if  distances[self.id_to_number[u.id]] + edge.minutesCounter(timetables[self.id_to_number[u.id]], edge.arrival_time, edge.departure_time) < distances[self.id_to_number[edge.id_arrival_station]] :  # poichè la partenza da una stazione deve essere dopo l'orario di arrivo nella stazione precedente cioè se arrivo alle 13 non posso partire alle 12.55
                        distances, previous_nodes, timetables, run_id_list, line_id_list, time_departures = self.relax(self.id_to_number[u.id], self.id_to_number[edge.id_arrival_station], previous_nodes, distances, edge, timetables, run_id_list, line_id_list, time_departures)
                        heap.decreaseKey(edge.id_arrival_station, distances[self.id_to_number[edge.id_arrival_station]])



        return distances, previous_nodes, timetables, run_id_list, line_id_list, time_departures

    def extractTime(self, orario):
        return orario[0:2], orario[2:]

    def CEDO(self, arrivo, partenza):
        arr_ore, arr_minuti = self.extractTime(arrivo[1:])
        part_ore, part_minuti = self.extractTime(partenza[1:])

        arrivo_in_min = int(arr_ore) * 60 + int(arr_minuti)
        partenza_in_min = int(part_ore) * 60 + int(part_minuti)

        if arrivo_in_min >= 24*60:
            arrivo_in_min = abs(24*60 - arrivo_in_min)

        if partenza_in_min >= 24 * 60:
            partenza_in_min = abs(24 * 60 - arrivo_in_min)

        if partenza_in_min - arrivo_in_min >= 0:
            return partenza_in_min - arrivo_in_min
        else:
            return 24*60 + partenza_in_min - arrivo_in_min


    def orario(self, string):
        ore, minuti = self.extractTime(string[1:])
        return int(ore) * 60 + int(minuti)





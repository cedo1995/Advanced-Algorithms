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
        distances[v] = distances[u] + (self.attendanceTime(timetables[u], edge.arrival_time) + (self.time(edge.arrival_time) - self.time(edge.departure_time)))
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
                    if distances[self.id_to_number[u.id]] + (self.attendanceTime(timetables[self.id_to_number[u.id]], edge.departure_time) + (self.time(edge.arrival_time) - self.time(edge.departure_time))) < distances[self.id_to_number[edge.id_arrival_station]]:
                    # if  distances[self.id_to_number[u.id]] + edge.minutesCounter(timetables[self.id_to_number[u.id]], edge.arrival_time, edge.departure_time) < distances[self.id_to_number[edge.id_arrival_station]] :  # poichè la partenza da una stazione deve essere dopo l'time di arrivo nella stazione precedente cioè se arrivo alle 13 non posso partire alle 12.55
                        distances, previous_nodes, timetables, run_id_list, line_id_list, time_departures = self.relax(self.id_to_number[u.id], self.id_to_number[edge.id_arrival_station], previous_nodes, distances, edge, timetables, run_id_list, line_id_list, time_departures)
                        heap.decreaseKey(edge.id_arrival_station, distances[self.id_to_number[edge.id_arrival_station]])



        return distances, previous_nodes, timetables, run_id_list, line_id_list, time_departures

    def extractTime(self, time):
        return time[0:2], time[2:]

    def attendanceTime(self, arriving_time, departure_time):
        arriving_hours, arriving_minutes = self.extractTime(arriving_time[1:])
        departure_hours, departure_minutes = self.extractTime(departure_time[1:])

        arriving_time_minutes = int(arriving_hours) * 60 + int(arriving_minutes)
        departure_time_minutes = int(departure_hours) * 60 + int(departure_minutes)

        if arriving_time_minutes >= 24 * 60:
            arriving_time_minutes = abs(24 * 60 - arriving_time_minutes)

        if departure_time_minutes >= 24 * 60:
            departure_time_minutes = abs(24 * 60 - arriving_time_minutes)

        if departure_time_minutes - arriving_time_minutes >= 0:
            return departure_time_minutes - arriving_time_minutes
        else:
            return 24*60 + departure_time_minutes - arriving_time_minutes


    def time(self, string):
        hours, minutes = self.extractTime(string[1:])
        return int(hours) * 60 + int(minutes)





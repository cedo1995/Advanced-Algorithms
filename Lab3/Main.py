import numpy as np
import codecs
from Graph import Graph
import math
import time
import sys

def main():
    path_info_array = ["./Files/burma14.tsp", "./Files/d493.tsp", "./Files/dsj1000.tsp", "./Files/eil51.tsp", "./Files/gr229.tsp", "./Files/kroD100.tsp", "./Files/ulysses22.tsp"]

    #path_info = ["./Files/piccolo_esempio.tsp"]
    graph_list = []
    #path_info = ["./Files/ulysses22.tsp"]

    for i in range(len(path_info_array)):
        name = ""       # nome del grafo
        dimension = -1      # numero dei nodi
        coord_type = ""     # tipo di coordinate
        coordinates = []    # lista di tuple della forma (coordinata1, coordinata2)
        next_are_coords = False     # se è True significa che sto parsando le coordinate
        line = ""       # inizializzazione della linea che verrà utilizzata per scorrere il file

        with codecs.open(path_info_array[i]) as f:    # apertura dei file
            line = f.readline()         # lettura della prima riga
            while line != "EOF\n":      # finchè non vi è EOF
                if not next_are_coords:     # se la linea è riferita all'intestazione del file

                    a = line.split(":")     # divido la linea rispetto al carattere :
                    if a[0] == "NAME" or a[0] == "NAME ":
                        name = a[1].replace(" ", "")[:-1]   # salvo il nome del grafo

                    if a[0] == "DIMENSION" or a[0] == "DIMENSION ":
                        dimension = int(a[1].replace(" ", ""))     # salvo la dimensione dei nodi del grafo
                    if a[0] == "EDGE_WEIGHT_TYPE" or a[0] == "EDGE_WEIGHT_TYPE ":
                        coord_type = a[1].replace(" ", "")   # salvo il tipo di coordinate
                    if a[0] == "NODE_COORD_SECTION\n":
                        next_are_coords = True      # le prossime righe del file saranno coordinate

                else:
                    a = line.split(" ")     # divido la linea rispetto agli spazi
                    a = [i for i in a if i != ""]
                    if coord_type == "EUC_2D\n":      # se sono euclidee
                        #print("STAMPO", a[1])
                        coordinates.append((float(a[1]), float(a[2][:-1])))      # float gestisce la codifica numerica esponenziale

                    else:
                        deg = int(float(a[1]))
                        #print(deg)
                        min = float(a[1]) - deg
                        radX = math.pi * (deg + 5.0 * min / 3.0) / 180.0

                        deg = int(float(a[2][:-1]))
                        min = float(a[2][:-1]) - deg
                        radY = math.pi * (deg + 5.0 * min / 3.0) / 180.0

                        coordinates.append((radX, radY))    # aggiungo le coordinate alla lista

                line = f.readline()     # passo alla linea successiva
        graph_list.append(Graph(name, dimension, coord_type, coordinates))

    for graph in graph_list:
        print(graph.name)
        start_time = time.time()
        min_dist, distances, previous, stop = graph.hkTsp(start_time)
        print("Minima distanza algoritmo esatto = ", min_dist)
        print("tempo algoritmo esatto =", time.time() - start_time)

        start_time = time.time()
        circuit, min_dist = graph.nearestNeighbor()
        print("Minima distanza euristica nearestNeighbor = ", min_dist)
        print("tempo nearestNeighbor =", time.time() - start_time)

        start_time = time.time()
        dist = graph.kruskalMST()
        print("Minima distanza 2 approssimata = ", dist)
        print("tempo 2 approssimata =", time.time() - start_time)





if __name__ == '__main__':
        main()

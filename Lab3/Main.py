import fileinput
import errno
import codecs
from Graph import Graph
import sys

def main():
    # sys.setrecursionlimit(sys.maxsize)
    path_info = ["./Files/burma14.tsp", "./Files/d493.tsp", "./Files/dsj1000.tsp", "./Files/eil51.tsp",
                 "./Files/gr229.tsp", "./Files/kroD100.tsp", "./Files/ulysses22.tsp"]
    for i in range(len(path_info)):
        name = ""       # nome del grafo
        dimension = -1      # numero dei nodi
        coord_type = ""     # tipo di coordinate
        coordinates = []    # lista di tuple della forma (coordinata1, coordinata2)
        count = 1           # contatore dei nodi
        count_to_coordinates = {}       # dizionario che associa il numero del nodo alle rispettive coordinate
        next_are_coords = False     # se è True significa che sto parsando le coordinate
        line = ""       # inizializzazione della linea che verrà utilizzata per scorrere il file

        with codecs.open(path_info[i]) as f:    # apertura dei file
            line = f.readline()         # lettura della prima riga
            while line != "EOF\n":      # finchè non vi è EOF
                if not next_are_coords:     # se la linea è riferita all'intestazione del file

                    a = line.split(":")     # divido la linea rispetto al carattere :
                    if a[0] == "NAME" or a[0] == "NAME ":
                        name = a[1].split(" ")[0]   # salvo il nome del grafo
                    if a[0] == "DIMENSION" or a[0] == "DIMENSION ":
                        dimension = int(a[1].split(" ")[1])     # salvo la dimensione dei nodi del grafo
                    if a[0] == "EDGE_WEIGHT_TYPE" or a[0] == "EDGE_WEIGHT_TYPE ":
                        coord_type = a[1].split(" ")[0]     # salvo il tipo di coordinate
                    if a[0] == "NODE_COORD_SECTION\n":
                        next_are_coords = True      # le prossime righe del file saranno coordinate

                else:
                    a = line.split(" ")     # divido la linea rispetto agli spazi
                    if coord_type == "EUC_2D":      # se sono euclidee
                        coordinates.append((float(a[1]), float(a[2])))      # float gestisce la codifica numerica esponenziale
                        count_to_coordinates[count] = coordinates[-1]       # indice della coordinata--> coordinate

                    else:
                        coordinates.append((a[1], a[2]))    # aggiungo le coordinate alla lista
                        count_to_coordinates[count] = coordinates[-1]       # indice della coordinata--> coordinate

                    count += 1          # incremento l'indice

                line = f.readline()     # passo alla linea successiva

            graph = Graph(name, dimension, coord_type, coordinates, count_to_coordinates)   # todo da decidere se tenere count_to_coord qui o crearlo in Graph
            graph.printG()

if __name__ == '__main__':
        main()

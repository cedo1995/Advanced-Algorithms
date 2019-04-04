import fileinput
import glob
import errno
import codecs
from Graph import Graph
from Node import Node
from Edge import Edge

def main():
    path_info = "./Files/Info/"
    file_stations = path_info + "bahnhof"       #percorso in cui vi è il file delle stazioni
    id_station = 0          #inizializzazione dell'id e del nome della stazione
    name_station = ""
    graph = Graph()         #creazione del grafo
    with codecs.open(file_stations, encoding='cp1250') as f:    #apertura del file delle stazioni
        f.readline()            #salto la prima riga
        line = f.readline()
        count = 0               #contatore delle stazioni
        while line:    #finchè il file non finisce
            id_station = line[0:9]      #trovo l'id della stazione
            name_station = line[14:34]  #trovo il nome della stazione
            graph.addNode(id_station, name_station, count)      #aggiungo la stazione al grafo
            line = f.readline()     #passo alla linea successiva
            count += 1              #incremento il contatore delle stazioni che corrisponderà ad un nuovo id

    path_lines = "./Files/Linee/*.LIN"      #mi posiziono sulle linee

    files = glob.glob(path_lines)
    i = 0       #contatore dei files

    for name in files:      #per ciascun file presente nella cartella Linee
        i += 1
        with codecs.open(name, encoding='cp1250') as f:    #FONDAMENTALE la codifica del file
            line = f.readline()     #leggo la prima riga
            run_id = ""     #inizializzo l'id della corsa
            line_id = ""    #inizializzo l'id della linea
            j = 0           #alla prima fermata sarà a 0, poi sarà un contatore
            arrival_time = []       #lista che conterrà tutti gli orari di arrivo in una determinata stazione
            departure_time = []     #lista che conterrà tutti gli orari di partenza da una determinata stazione
            name_station = []       #lista dei nomi di tutte le stazioni
            id_station = []         #lista degli id delle stazioni

            restart = False         #mi serve per capire se creare un arco oppure no

            while line:        #finchè non finisce il file
                if line.startswith("*"):
                    restart = True
                    if line.startswith("*Z"):       #identifica le righe che danno informazioni sulla corsa
                        run_id = line[3:8]        #utile per l'edge
                        line_id = line[9:15]

                else:        #se è una riga che contiene informazioni riguardo alle fermate
                    id_station.append(line[0:9])          #inserisco l'id
                    name_station.append(line[10:30])      #inserisco il nome

                    if not (line[32:].startswith(" ") and line[32:].startswith("-")):
                        arrival_time.append(line[32:37])

                    departure_time.append(line[39:44])

                    if restart:
                        restart = False
                    elif int(j) >= 1:
                        edge = Edge(departure_time[j-1], arrival_time[j], run_id, line_id, int(id_station[j-1]), int(id_station[j]))
                        graph.addEdge(edge)


                    j += 1    # incremento j

                line = f.readline()

    graph.printG()
    distances = []
    previous_nodes = []
    run_id_list = []
    time_departures = []
    '''
    for nodo in graph.nodes_list:
        print("Nodo: ", nodo.id)
        for arco in nodo.adj_arr:
            print("arco da ", arco.id_departure_station, " a ", arco.id_arrival_station, "\tOrario partenza: ",
                  arco.departure_time, "\tOrario Arrivo: ", arco.arrival_time)
    '''

    distances, previous_nodes, timetables, run_id_list, time_departures = graph.dijkstra(500000079, "01300")

    id_to_number = graph.returnIdToNumber()
    number_to_id = graph.returnNumberToId()

    print(distances[id_to_number[300000044]])

    previous_path = []
    previous_path = rebuildPreviousNodes(previous_nodes, id_to_number[300000044], id_to_number, previous_path, 500000079)
    print("ora di partenza: ", timetables[id_to_number[500000079]])
    print("Ora di arrivo: ", timetables[id_to_number[300000044]])
    for i, val in enumerate(reversed(previous_path)):
        print(time_departures[val], )
        # print(val, previous_path[len(previous_path)-1-i], "\t", number_to_id[val], "\t", run_id_list[val], time_departures[val])

import fileinput
import glob
import errno
import codecs
from Graph import Graph
from Node import Node
from Edge import Edge

def main():
    path_info = "./Files/Info/"
    file_stations = path_info + "bahnhof"       #percorso in cui vi è il file delle stazioni
    id_station = 0          #inizializzazione dell'id e del nome della stazione
    name_station = ""
    graph = Graph()         #creazione del grafo
    with codecs.open(file_stations, encoding='cp1250') as f:    #apertura del file delle stazioni
        f.readline()            #salto la prima riga
        line = f.readline()
        count = 0               #contatore delle stazioni
        while line:    #finchè il file non finisce
            id_station = line[0:9]      #trovo l'id della stazione
            name_station = line[14:34]  #trovo il nome della stazione
            graph.addNode(id_station, name_station, count)      #aggiungo la stazione al grafo
            line = f.readline()     #passo alla linea successiva
            count += 1              #incremento il contatore delle stazioni che corrisponderà ad un nuovo id

    path_lines = "./Files/Linee/*.LIN"      #mi posiziono sulle linee

    files = glob.glob(path_lines)
    i = 0       #contatore dei files

    for name in files:      #per ciascun file presente nella cartella Linee
        i += 1
        with codecs.open(name, encoding='cp1250') as f:    #FONDAMENTALE la codifica del file
            line = f.readline()     #leggo la prima riga
            run_id = ""     #inizializzo l'id della corsa
            line_id = ""    #inizializzo l'id della linea
            j = 0           #alla prima fermata sarà a 0, poi sarà un contatore
            arrival_time = []       #lista che conterrà tutti gli orari di arrivo in una determinata stazione
            departure_time = []     #lista che conterrà tutti gli orari di partenza da una determinata stazione
            name_station = []       #lista dei nomi di tutte le stazioni
            id_station = []         #lista degli id delle stazioni

            restart = False         #mi serve per capire se creare un arco oppure no

            while line:        #finchè non finisce il file
                if line.startswith("*"):
                    restart = True
                    if line.startswith("*Z"):       #identifica le righe che danno informazioni sulla corsa
                        run_id = line[3:8]        #utile per l'edge
                        line_id = line[9:15]

                else:        #se è una riga che contiene informazioni riguardo alle fermate
                    id_station.append(line[0:9])          #inserisco l'id
                    name_station.append(line[10:30])      #inserisco il nome

                    if not (line[32:].startswith(" ") and line[32:].startswith("-")):
                        arrival_time.append(line[32:37])

                    departure_time.append(line[39:44])

                    if restart:
                        restart = False
                    elif int(j) >= 1:
                        edge = Edge(departure_time[j-1], arrival_time[j], run_id, line_id, int(id_station[j-1]), int(id_station[j]))
                        graph.addEdge(edge)


                    j += 1    # incremento j

                line = f.readline()

    graph.printG()
    distances = []
    previous_nodes = []
    run_id_list = []
    time_departures = []
    line_id_list = []
    '''
    for nodo in graph.nodes_list:
        print("Nodo: ", nodo.id)
        for arco in nodo.adj_arr:
            print("arco da ", arco.id_departure_station, " a ", arco.id_arrival_station, "\tOrario partenza: ",
                  arco.departure_time, "\tOrario Arrivo: ", arco.arrival_time)
    '''

    distances, previous_nodes, timetables, run_id_list, line_id_list, time_departures = graph.dijkstra(500000079, "01300")

    id_to_number = graph.returnIdToNumber()
    number_to_id = graph.returnNumberToId()

    print(distances[id_to_number[300000044]])

    previous_path = []
    previous_path = rebuildPreviousNodes(previous_nodes, id_to_number[300000044], id_to_number, previous_path, 500000079)
    print("ora di partenza: ", timetables[id_to_number[500000079]])
    print("Ora di arrivo: ", timetables[id_to_number[300000044]])
    j = previous_path[-1]
    for i, val in enumerate(reversed(previous_path)):
        if i == 0:
            pass
        else:
            print(time_departures[val], ": corsa ", run_id_list[val], " ", line_id_list[val], " da ", number_to_id[j], " a ", number_to_id[val])
            j = val

        # print(val, previous_path[len(previous_path)-1-i], "\t", number_to_id[val], "\t", run_id_list[val], time_departures[val])


def rebuildPreviousNodes(previous_nodes, node, id_to_number, previous_path, start_node):
    """
    :param previous_nodes: array ritornato dall'algoritmo di Dijkstra
    :param node: nodo destinazione
    :param id_to_number: dizionario originale che associa gli id delle stazioni agli id dei nodi
    :param previous_path: array del cammino minimo
    :param start_node: id del nodo di partenza
    :return previous_path: array del cammino minimo
    """
    if node == id_to_number[start_node]:
        previous_path.append(node)
        return previous_path
    else:
        previous_path.append(node)
        return rebuildPreviousNodes(previous_nodes, previous_nodes[node], id_to_number, previous_path, start_node)




if __name__ == '__main__':
        main()

import fileinput
import glob
import errno
import codecs
from Graph import Graph
from Node import Node
from Edge import Edge

def main():
    path_info = "./Files/Info/"
    file_stations = path_info + "bahnhof"
    id_station = 0
    name_station = ""
    graph = Graph()
    with codecs.open(file_stations, encoding='cp1250') as f:
        f.readline()        #salto la prima riga
        line = f.readline()
        count = 0       #contatore delle stazioni
        while line:    #finchè il file non finisce
            id_station = line[0:9]
            name_station = line[14:34]
            graph.AddNode(id_station, name_station, count)
            line = f.readline()     #passo alla linea successiva
            count += 1

    #path_lines = "./piccolo_esempio/Linee/*.LIN"
    path_lines = "./Files/Linee/*.LIN"

    files = glob.glob(path_lines)
    i = 0

    for name in files:      #per ciascun file presente nella cartella Linee
        i += 1
        with codecs.open(name, encoding='cp1250') as f:    #FONDAMENTALE la codifica del file
            line = f.readline()     #leggo la prima riga
            run_id = ""
            line_id = ""
            j = 0           #alla prima fermata sarà a 0, poi sarà un contatore
            arrival_time = []
            departure_time = []
            name_station = []
            id_station = []
            count = 0
            restart = False
            while line:        #finchè non finisce il file
                count += 1
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
                    #print("Orario partenza: ", str(departure_time[j])," ",count)
                    if restart:
                        restart = False
                    elif int(j) >= 1:
                        edge = Edge(departure_time[j-1], arrival_time[j], run_id, line_id, int(id_station[j-1]), int(id_station[j]))
                        graph.AddEdge(edge)


                    j += 1    # incremento j

                line = f.readline()

    graph.PrintG()
    distances = []
    previous_nodes = []
    '''
    for nodo in graph.nodes_list:
        print("Nodo: ", nodo.id)
        for arco in nodo.adj_arr:
            print("arco da ", arco.id_departure_station, " a ", arco.id_arrival_station, "\tOrario partenza: ",
                  arco.departure_time, "\tOrario Arrivo: ", arco.arrival_time)
    '''

    distances, previous_nodes, timetables = graph.Dijkstra(500000079, "01300")

    id_to_number = graph.ReturnIdToNumber()
    number_to_id = graph.ReturnNumberToId()

    print(distances[id_to_number[300000044]])

    previous_path = []
    previous_path = RebuildPreviousNodes(previous_nodes, id_to_number[300000044], id_to_number, previous_path, 500000079)
    for i in previous_path:
        print(i, "\t", number_to_id[i], "\t", timetables[i])


def RebuildPreviousNodes(previous_nodes, node, id_to_number, previous_path, start_node):
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
        return RebuildPreviousNodes(previous_nodes, previous_nodes[node], id_to_number, previous_path, start_node)




if __name__ == '__main__':
        main()

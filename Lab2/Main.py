import fileinput
import glob
import errno
import codecs
from Graph import Graph
from Node import Node
from Edge import Edge

def main():
    #pathInfo = "./piccolo_esempio/Info/"      #da vedere il formato del file
    pathInfo = "./Files/Info/"  # da vedere il formato del file
    fileStazioni = pathInfo + "bahnhof"
    stazioni = {}
    id_staz = 0
    nome_staz = ""
    matrice = []
    grafo = Graph()
    with codecs.open(fileStazioni, encoding = 'cp1250') as f:
        f.readline()    #salto la prima riga
        line = f.readline()
        count = 0       #contatore delle stazioni
        while(line):    #finchè il file non finisce
            id_staz = line[0:9]
            nome_staz = line[14:34]     #salta in tutti i modi la scritta CdT o CtF.. va bene?
            #stazioni[id_staz] = [count, nome_staz]     togliere se usiamo la classe grafo
            grafo.addNode(id_staz, nome_staz, count)
            line = f.readline()     #passo alla linea successiva
            count += 1

    #pathLinee = "./piccolo_esempio/Linee/*.LIN"
    pathLinee = "./Files/Linee/*.LIN"

    files = glob.glob(pathLinee)
    i = 0

    for name in files:      #per ciascun file presente nella cartella Linee
        i += 1
        #print("NOME DEL FILE: ", name, "\t File numero", i)      #primo file letto
        with codecs.open(name, encoding='cp1250') as f:    #FONDAMENTALE la codifica del file
            line = f.readline()     #leggo la prima riga
            id_corsa = ""
            id_linea = ""
            j = 0           #alla prima fermata sarà a 0, poi sarà un contatore
            orario_arrivo = []
            orario_partenza = []
            nome_stazione = []
            id_stazione = []
            count=0
            restart = False
            while(line):        #finchè non finisce il file
                #print(line)
                count += 1

                if line.startswith("*"):
                    restart = True
                    if line.startswith("*Z"):       #identifica le righe che danno informazioni sulla corsa

                        id_corsa = line[3:8]        #utile per l'arco
                        id_linea = line[9:15]

                else:        #se è una riga che contiene informazioni riguardo alle fermate
                    #print(line[0:9])
                    id_stazione.append(line[0:9])          #inserisco l'id
                    #print("ID: ", id_stazione[j])
                    nome_stazione.append(line[10:30])      #inserisco il nome
                    #print("\t", nome_stazione[j])
                    if not (line[32:].startswith(" ") and line[32:].startswith("-")):
                        orario_arrivo.append(line[32:37])
                        #print("Orario arrivo: ", str(orario_arrivo[j])," ",count)

                    orario_partenza.append(line[39:44])
                    #print("Orario partenza: ", str(orario_partenza[j])," ",count)
                    if restart==True:
                        restart = False
                    elif int(j) >= 1:
                        arco = Edge(orario_partenza[j-1], orario_arrivo[j], id_corsa, id_linea, int(id_stazione[j-1]), int(id_stazione[j]))
                        grafo.addEdge(arco)


                    j += 1    # incremento j

                line = f.readline()

    grafo.printG()
    distanze = []
    predecessori = []
    """
    for nodo in grafo.arrNodes:
        print("Nodo: ",nodo.id)
        for arco in nodo.adjArr:
            print("arco da ", arco.idStazionePartenza, " a ", arco.idStazioneArrivo,"\tOrario partenza: ",arco.orarioPartenza,"\tOrario Arrivo: ",arco.orarioArrivo)
    """
    distanze, predecessori = grafo.Dijkstra(200415016, "00931")
    #print("primo nodo", grafo.arrNodes[0].id, distanze[0], predecessori[0])
    #print("   secondo nodo", grafo.arrNodes[1].id, distanze[1], predecessori[1])
    #print(grafo.arrNodes[2].id)

    idToNumber = grafo.ReturnidToNumber()

    numberToId = grafo.ReturnNumberToId()

    print(distanze[idToNumber[200405005]])
    #print(predecessori[5])
    cammino = []
    #cammino = ricostruisciPredecessore(predecessori, idToNumber[200417023], idToNumber, cammino, 200415016 )
    #for _ in cammino:
        #print(_,"\t",numberToId[_][0],"\t",numberToId[_][1])
    '''
    for i in grafo.arrNodes:
        for e in i.adjArr:
            print("nodo", i.id," arco ad ", e.idStazioneArrivo)
    '''

    #print("   secondo nodo", grafo.arrNodes[100].id, distanze[100], predecessori[100])
    '''
    for i in grafo.arrNodes[2456].adjArr: # prova per controllare id stazione 200415016 che è Hollerich, AVL Porta venga trattato in maniera corretta
        print("partenza da ",i.idStazionePartenza," alle ",i.orarioPartenza," arrivo a ", i.idStazioneArrivo, " alle ", i.orarioArrivo)
    distanze = []
    predecessori = []
    distanze, predecessori = grafo.Dijkstra(0)
    for i in distanze:
        print(i)
    print("primo nodo", grafo.arrNodes[0].id, distanze[0])
    print("   secondo nodo", grafo.arrNodes[1].id, distanze[1])
    '''

def ricostruisciPredecessore(predecessori, nodo, idToNumber, cammino, start_node):
    """
    :param predecessori: array ritornato dall'algoritmo di Dijkstra
    :param nodo:
    :param idToNumber: dizionario che associa gli id delle stazioni agli id dei nodi
    :param cammino: array del cammino minimo
    :return: array del cammino minimo
    """
    if predecessori[nodo] == idToNumber[start_node]:
        cammino.append(predecessori[nodo])
        return cammino
    else:
        cammino.append(nodo)
        return ricostruisciPredecessore(predecessori, predecessori[nodo], idToNumber, cammino, start_node)




if __name__ == '__main__':
        main()

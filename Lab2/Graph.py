from Node import Node
from Edge import Edge
from HeapBinaria import HeapBinaria
import sys

class Graph:
    def __init__(self):
        self.idToNumber = {}
        self.numNodes = 0
        self.arrNodes = []  #lista di nodi contenuti nel grafo
        self.numEdges = 0       #contatore degli archi
        self.numberToId = {}    #associa il count all'id_stazione e al suo nome
    def ReturnidToNumber(self):
        return self.idToNumber

    def ReturnNumberToId(self):
        return self.numberToId

    def printG(self):   #stampa le informazioni principali del grafo
        print("Grafo con ", self.numNodes, " nodi e ", self.numEdges, " archi.")

    def addNode(self, id_stazione, nome_stazione, count ):
        id_stazione = int(id_stazione)
        self.idToNumber[id_stazione] = count
        self.numNodes += 1
        self.arrNodes.append(Node(id_stazione))
        self.numberToId[count] = (id_stazione, nome_stazione)         ##todo VERIFICARE SE FUNZIONA

    def addEdge(self, arco):
        self.numEdges += 1
        i = self.idToNumber[arco.idStazionePartenza]
        self.arrNodes[i].addEdgeToNode(arco)

    def Relax(self, u, v, predecessori, distanze, arco,orario_stazione):  # u e v sono indici dei nodi da rilassare
        print("arco ", arco.idStazionePartenza, arco.idStazioneArrivo)
        print(arco.orarioPartenza, arco.orarioArrivo)
        print(distanze[u], " + ",arco.minutesCounter(orario_stazione, arco.orarioArrivo))
        distanze[v] = distanze[u] + arco.minutesCounter(orario_stazione, arco.orarioArrivo)
        print(" ",distanze[v])
        predecessori[v] = u
        return distanze, predecessori

    def Dijkstra(self, startNodeId, orario):
        predecessori = []
        distanze = []
        for i in range(len(self.arrNodes)):
            distanze.append(998999)
            predecessori.append(-1)
        distanze[self.idToNumber[startNodeId]] = 0
        heap = HeapBinaria()
        heap.Add(startNodeId, 0)
        orario_stazione = orario




        while len(heap.arrVertex) > 0:
            u = heap.ExtractMin()
            delta_tempo = 9999
            first = True
            #TODO Dichiarare arco_temp = qualcosa
            #print(u.id)
            for arco in self.arrNodes[self.idToNumber[u.id]].adjArr:
                if first:
                    arco_temp = arco
                    first = False
                if arco.minutesCounter(orario_stazione, arco.orarioArrivo) > 0 and distanze[self.idToNumber[u.id]] + arco.minutesCounter(orario_stazione, arco.orarioArrivo) < distanze[self.idToNumber[arco.idStazioneArrivo]]:

                    heap.Add(arco.idStazioneArrivo, arco.minutesCounter(orario_stazione, arco.orarioArrivo))
                    distanze, predecessori = self.Relax(self.idToNumber[u.id], self.idToNumber[arco.idStazioneArrivo], predecessori, distanze, arco, orario_stazione)

                    #print(arco.idStazionePartenza, arco.idStazioneArrivo, arco.orarioPartenza, arco.orarioArrivo, arco.minutesCounter(arco.orarioPartenza, arco.orarioArrivo))
                    if(arco.minutesCounter(orario_stazione, arco.orarioArrivo) < delta_tempo):
                        delta_tempo = arco.minutesCounter(orario_stazione, arco.orarioArrivo)
                        arco_temp = arco
                    heap.DecreaseKey(self.idToNumber[arco.idStazioneArrivo], distanze[self.idToNumber[arco.idStazioneArrivo]])
            orario_stazione = arco_temp.orarioArrivo        #TODO capire come gestire questo assegnamento
                #print(len(heap.arrVertex))
        return distanze, predecessori












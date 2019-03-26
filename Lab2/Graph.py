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

    def printG(self):   #stampa le informazioni principali del grafo
        print("Grafo con ", self.numNodes, " nodi e ", self.numEdges, " archi.")

    def addNode(self, id_stazione, nome_stazione, count ):
        self.idToNumber[id_stazione] = count
        self.numNodes += 1
        self.arrNodes.append(Node(id_stazione))

    def addEdge(self, arco):
        self.numEdges += 1
        i = self.idToNumber[arco.idStazionePartenza]
        self.arrNodes[i].addEdgeToNode(arco)

    def Relax(self, u, v, predecessori, distanze, arco):  # u e v sono indici dei nodi da rilassare
        distanze[v] = distanze[u] + arco.minutesCounter(arco.orarioPartenza, arco.orarioArrivo)
        predecessori[v] = u
        return distanze, predecessori

    def Dijkstra(self, startNodeId):
        predecessori = []
        distanze = []
        for i in range(len(self.arrNodes)):
            distanze.append(998999)
            predecessori.append(-1)
        distanze[0] = 0
        heap = HeapBinaria(self.arrNodes)
        while len(heap.arrVertex) > 0:
            u = heap.ExtractMin()

            for arco in self.arrNodes[self.idToNumber[u.id]].adjArr:
                if distanze[self.idToNumber[u.id]] + arco.minutesCounter(arco.orarioPartenza, arco.orarioArrivo) < distanze[self.idToNumber[arco.idStazioneArrivo]]:
                    distanze, predecessori = self.Relax(self.idToNumber[u.id], self.idToNumber[arco.idStazioneArrivo], predecessori, distanze, arco)
                    #print(self.idToNumber[arco.idStazioneArrivo])
                    heap.DecreaseKey(self.idToNumber[arco.idStazioneArrivo], distanze[self.idToNumber[arco.idStazioneArrivo]])
        return distanze, predecessori












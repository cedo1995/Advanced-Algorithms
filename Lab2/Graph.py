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
        self.numberToId[count] = id_stazione         ##todo VERIFICARE SE FUNZIONA

    def addEdge(self, arco):
        self.numEdges += 1
        i = self.idToNumber[arco.idStazionePartenza]
        self.arrNodes[i].addEdgeToNode(arco)

    def Relax(self, u, v, predecessori, distanze, arco, orario_stazione):  # u e v sono indici dei nodi da rilassare
        #print("arco ", arco.idStazionePartenza, arco.idStazioneArrivo)
        #print(arco.orarioPartenza, arco.orarioArrivo)
        #print(distanze[u], " + ",arco.minutesCounter(orario_stazione, arco.orarioArrivo))
        distanze[v] = distanze[u] + arco.minutesCounter(orario_stazione, arco.orarioArrivo)
        #print(" ",distanze[v])
        predecessori[v] = u
        return distanze, predecessori

    def Dijkstra(self, startNodeId, orario):
        distanze = []
        heap = HeapBinaria()
        predecessori = []
        for i, x in enumerate(self.arrNodes):
            distanze.append(sys.maxsize)
            predecessori.append(-1)
            heap.Add(x.id, distanze[self.idToNumber[x.id]])
        heap.DecreaseKey(self.idToNumber[startNodeId], 0)       #decremento il valore della heap ad indice idToNumber[startNodeId] a 0 in modo da essere la sorgente
        



        return distanze, predecessori












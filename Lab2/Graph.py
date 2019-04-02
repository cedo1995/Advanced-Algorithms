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

    def Relax(self, u, v, predecessori, distanze, arco, orario):  # u e v sono indici dei nodi da rilassare
        orario[v] = arco.orarioArrivo
        distanze[v] = distanze[u] + arco.minutesCounter(orario[u], arco.orarioArrivo)
        #print(" ",distanze[v])
        predecessori[v] = u
        return distanze, predecessori, orario

    def Dijkstra(self, startNodeId, orario_minima_partenza):
        distanze = []
        heap = HeapBinaria()
        predecessori = []
        orario = []
        for i, x in enumerate(self.arrNodes):
            distanze.append(sys.maxsize)
            predecessori.append(-1)
            orario.append("-1")
            heap.Add(x.id, distanze[self.idToNumber[x.id]])
        distanze[self.idToNumber[startNodeId]] = 0
        orario[self.idToNumber[startNodeId]] = orario_minima_partenza
        heap.DecreaseKey(startNodeId, 0)       #decremento il valore della heap ad indice idToNumber[startNodeId] a 0 in modo da essere la sorgente
        while len(heap.arrVertex) > 0:
            u = heap.ExtractMin()
            if orario[self.idToNumber[u.id]] != "-1":
                print(u.id)
                for arco in self.arrNodes[self.idToNumber[u.id]].adjArr:
                    #print(u.id, self.idToNumber[u.id], arco.idStazioneArrivo)
                    if distanze[self.idToNumber[u.id]] + arco.minutesCounter(orario[self.idToNumber[u.id]], arco.orarioArrivo) < distanze[self.idToNumber[arco.idStazioneArrivo]]:

                        distanze, predecessori, orario = self.Relax(self.idToNumber[u.id], self.idToNumber[arco.idStazioneArrivo], predecessori, distanze, arco, orario)
                        heap.DecreaseKey(arco.idStazioneArrivo, distanze[self.idToNumber[arco.idStazioneArrivo]])



        return distanze, predecessori












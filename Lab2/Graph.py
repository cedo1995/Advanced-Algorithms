from Node import Node
from Edge import Edge
class Graph:
    def __init__(self):
        self.numNodes = 0
        self.arrNodes = []  #lista di nodi contenuti nel grafo
        self.numEdges = 0       #contatore degli archi
        self.arrEdges = []

    def printG(self):   #stampa le informazioni principali del grafo
        print("Grafo con ", self.numNodes, " nodi e ", self.numEdges, " archi.")

    def addNode(self, id_stazione, nome_stazione, count ):
        self.numNodes += 1
        self.arrNodes.append(Node(id_stazione))     #siamo convinti abbia senso usare un count?

    def addEdge(self, arco):
        self.numEdges += 1
        self.arrEdges.append(arco)

    




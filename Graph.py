import random as random
import numpy as np
np.set_printoptions(threshold=np.inf)
from enum import Enum



class Color(Enum):
    White = int(0)
    Gray = int(1)
    Black = int(2)


# Classe base da cui derivano le tre classi ERGraph, UPAGraph e DataGraph
class Graph:
    def __init__(self):
        self.nodes = 0
        self.arches = []  # Contiene le tuple con i vertici collegati SOLO UNA VOLTA dato che parliamo di grafi non orientati
        self.adjArr = []  # Array di adiacenza, qui entrambe le coppie sono settate a 1 (sta a noi prendere solo metà array)

    def printG(self):
        print("Grafo con", self.nodes, "nodi e", len(self.arches), "archi.")

    def addNode(self, node):
        self.nodes += 1

    def addEdge(self, node1, node2):
        self.arches.append(node1,node2)
        self.adjArr[node1][node2] = 1
        self.adjArr[node2][node1] = 1

    def DFS_Visited(self, u, visited,idToColor):
        idToColor[u] = Color.Gray
        visited.append(u)
        #print(self.adjArr[u])
        for i, v in enumerate(self.adjArr[u]):  #ogni v contiene gli ID dei vertici che hanno un arco con u

            if v == 1:

                if idToColor[i] == Color.White:

                    #print(i)

                    self.DFS_Visited(i, visited, idToColor)


        idToColor[u] = Color.Black

        return visited

    def connectedComponents(self):
        idToColor = [Color.White]*self.nodes        #coloro tutti i nodi di bianco

        ## TODO: valutare se mettere CC=vuoto
        CC= []                                      #array di componenti connesse
        for v in range(self.nodes):
            if idToColor[v] == Color.White:
                #print(v)
                visited = []
                comp = self.DFS_Visited(v, visited,idToColor)
                #print(comp)
                CC.append(comp)
        return CC


class ERGraph(Graph):
    def __init__(self, n, p):
        """
        :param n: number of nodes
        :param p: probability to generate an edge
        """
        super().__init__()
        random.seed(2)
        self.nodes = n
        self.adjArr = np.zeros((n, n))
        for row in range(n):
            for col in range(n):
                a = random.uniform(0, 1)
                # FIXME
                # con G[col][row] != 1 non considero i doppi archi avendo un grafo non orientato
                if a < p and self.adjArr[col][row] != 1 and row != col:
                    # Setto a 1 entrambe le celle (così sarà una matrice simmetrica) ma conto solo un arco
                    self.adjArr[row][col] = 1
                    self.adjArr[col][row] = 1
                    self.arches.append((row, col))


class UPAGraph(Graph):
    def __init__(self, n, m):
        """
        :param n: number of nodes
        :param m: 0 <= 1 <= m number of nodes already in the graph
        """
        super().__init__()
        self.nodes = m
        self.adjArr = np.zeros((n, n))

        jar = []  # Urna da cui pescare, sarebbe nodeNumbers del libro ma quel nome mi faceva confusione

        # Inizializza grafo completo con m nodi
        for row in range(m):
            for col in range(row+1, m):
                self.adjArr[row][col] = 1
                self.adjArr[col][row] = 1
        # da valutare se necessario
                self.arches.append((row, col))

        #UPATRIAL:
        # Aggiunge m volte ognuno degli m nodi a jar
        for i in range(0, self.nodes):
            for j in range(0, self.nodes):
                jar.append(i)

        # Per ogni ulteriore nodo faccio m estrazioni
        for u in range(m, n):
            jar, extraction = self.RunTrial(m, u, jar)
            for num in extraction:
                # Setto a 1 entrambe le celle (così sarà una matrice simmetrica) ma conto solo un arco
                if self.adjArr[u][num] != 1 and u != num and self.adjArr[num][u] != 1: # perchè devo controllare di non contare di nuovo archi dove li ho già nè devo mettere cappi
                    self.adjArr[u][num] = 1
                    self.adjArr[num][u] = 1
                    self.arches.append((u, num))

    def RunTrial(self, m, num_node, jar):
        extraction = []
        for i in range(0, m):
            u = np.random.randint(len(jar))
            extraction.append(jar[u])
        jar.append(self.nodes)  # PSEUDO CODICE SBAGLIATO ?!?!?!?!?!??!!?
        jar.extend(extraction)
        self.nodes += 1
        return jar, extraction


# NB: definisco i numeri che hanno i nodi nel file fornito dal professore come "Old_ID"
#     mentre i numeri che vanno da 1 a 6474 come gli "ID" dei nodi (che ora voglio aggiungere io)

class DataGraph(Graph):
    def __init__(self, n, file):
        super().__init__()
        self.nodes = n
        self.adjArr = np.zeros((n, n))
        data = np.loadtxt(file, delimiter='\t', dtype=int)
        startingNode = data[:, 0]
        endingNode = data[:, 1]
        IDtoNumber = set(startingNode)
        IDtoNumberArr=list(IDtoNumber)      # IDtoNumber contiene tutti i gli Old_ID una presenti una sola volta ciascuno (in totale ha lunghezza 6474)
        IDtoNumberArr.sort()
        #print(IDtoNumberArr[2])
        #print(startingNode)
        IdDictionary={}
        for i in range(n):
            IdDictionary[IDtoNumberArr[i]] = i      # dizionario che associa ad ogni valore degli Old_ID il valore ID (intero incrementale da 0 a 6473)


        for i in range(len(startingNode)):

            if startingNode[i] != endingNode[i] and self.adjArr[IdDictionary[startingNode[i]]][IdDictionary[endingNode[i]]] != 1:

                #print(startingNode[1]," - ",endingNode[1])
                #print(IdDictionary[startingNode[1]], " - ", IdDictionary[endingNode[1]])
                self.adjArr[IdDictionary[startingNode[i]]][IdDictionary[endingNode[i]]] = 1     # leggendo gli Old_ID utilizzo il dizionario per capire a quale ID si riferiscono cosi da poter associare archi
                self.adjArr[IdDictionary[endingNode[i]]][IdDictionary[startingNode[i]]] = 1
                self.arches.append((IdDictionary[startingNode[i]], IdDictionary[endingNode[i]]))

import random as random
import numpy as np

# Classe base da cui derivano le tre classi ERGraph, UPAGraph e DataGraph
class Graph:
    def __init__(self):
        self.nodes = 0
        self.arches = []  # Contiene le tuple con i vertici collegati SOLO UNA VOLTA dato che parliamo di grafi non orientati
        self.adjArr = []  # Array di adiacenza, qui entrambe le coppie sono settate a 1 (sta a noi prendere solo metà array)

    def printG(self):
        print("Grafo con", self.nodes, "nodi e", len(self.arches), "archi.")


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
                self.adjArr[u][num] = 1
                self.adjArr[num][u] = 1
                self.arches.append((u, num))

    def RunTrial(self, m, num_node, jar):
        extraction = []
        for i in range(0, m):
            u = random.randint(0, len(jar)-1)
            extraction.append(jar[u])
        jar.append(num_node)
        jar.extend(extraction)
        self.nodes += 1
        return jar, extraction


class DataGraph(Graph):
    def __init__(self, n, file):
        super().__init__()
        self.nodes = n
        self.adjArr = np.zeros((n, n))
        data = np.loadtxt(file, delimiter='\t', dtype=int)
        startingNode = data[:, 0]
        endingNode = data[:, 1]
        IDtoNumber = set(startingNode)
        IDtoNumberArr
        for i in range(len(IDtoNumber)):
        	IDtoNumberArr.append()
        IdDictionary={}
        for i in range(n):
        	IdDictionary[IDtoNumber[i]] = i
        #print(numberToID)

        new_data = []	#array di tuple
        for i in range(len(startingNode)):
            if startingNode[i] != endingNode[i] and self.adjArr[IdDictionary[startingNode[i]][IdDictionary[endingNode[i]]]] != 1:

                self.adjArr[IdDictionary[startingNode[i]][IdDictionary[endingNode[i]]]] = 1
                self.adjArr[IdDictionary[endingNode[i]]][IdDictionary[startingNode[i]]] = 1
                #self.arches.append((startingNode, endingNode))


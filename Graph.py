import random as random
import numpy as np


class Graph:
    def __init__(self):
        self.nodes = 0
        self.arches = []
        self.adjArr = []

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
                    self.adjArr[row][col] = 1
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

        node_numbers = []  # "Contenitore" da cui pescare

        # Inizializza grafo completo con m nodi
        for row in range(m):
            for col in range(row+1, m):
                self.adjArr[row][col] = 1
                self.arches.append((row, col))

        # Aggiunge m volte ognuno degli m nodi a node_numbers
        for i in range(0, self.nodes):
            for j in range(0, self.nodes):
                node_numbers.append(i)

        # Per ogni ulteriore nodo faccio un'estrazione
        for u in range(m, n):
            node_numbers = self.RunTrial(m, u, node_numbers)
            for row in range(m):
                for col in range(row+1, m):
                    self.adjArr[row][col] = 1
                    self.arches.append((row, col))

    # TODO: verificarne il corretto funzionamento
    def RunTrial(self, m, num_node, nodeNumbers):
        extraction = []
        for i in range(0, m):
            u = random.randint(0, len(nodeNumbers)-1)
            extraction.append(nodeNumbers[u])
        nodeNumbers.append(num_node)
        nodeNumbers.append(extraction)
        self.nodes += 1
        return nodeNumbers


class DataGraph(Graph):
    def __init__(self):
        super().__init__()
        print("Inizializzato un nuovo grafo dai Dati")
        # TODO

from Node import *
import random as random
import numpy as np
from enum import Enum
import matplotlib.pyplot as plt


class Color(Enum):
    White = int(0)
    Gray = int(1)
    Black = int(2)


class Graph:
    def __init__(self, n):
        self.numNodes = n
        self.arrNodes = []
        for i in range(n):
            self.arrNodes.append( Node(i) )
        self.numEdges = 0

    def printG(self):
        print("Grafo con ", self.numNodes, " nodi e ", self.numEdges, " archi.")

    def DFS_Visited(self, u, visited, idToColor):
        idToColor[u] = Color.Gray
        visited.append(u)
        for i in self.arrNodes[u].adjArr:
            if idToColor[i] == Color.White:
                self.DFS_Visited(i, visited, idToColor)

        idToColor[u] = Color.Black
        return visited

    def connectedComponents(self):
        idToColor = [Color.White]*self.numNodes
        CC = []
        for v in range(self.numNodes):
            if idToColor[v] == Color.White:
                visited = []
                comp = self.DFS_Visited(v, visited, idToColor)
                CC.append(comp)
        return CC

    def removeNode(self, index_node):
        for vertex in range(len(self.arrNodes)):
            num1 = len(self.arrNodes[vertex].adjArr)
            self.arrNodes[vertex].adjArr = [x for x in self.arrNodes[vertex].adjArr if x != index_node]
            num2 = len(self.arrNodes[vertex].adjArr)
            if num2 < num1:
                self.numEdges -= 1

        del self.arrNodes[index_node]
        self.numNodes -= 1

        for i in range(len(self.arrNodes)):
            for j in range(len(self.arrNodes[i].adjArr)):
                if self.arrNodes[i].adjArr[j] > index_node:
                    self.arrNodes[i].adjArr[j] -= 1
            if self.arrNodes[i].id > index_node:
                self.arrNodes[i].id -= 1

    def getResilience(self):
        CC = self.connectedComponents()
        max = 0
        for index in CC:
            if len(index) > max:
                max = len(index)
        return max

    def resilienceCalculator(self, seed):
        random.seed(seed)
        resilience = []
        while self.numNodes != 0:
            index_node = random.randint(0, self.numNodes-1)
            self.removeNode(index_node)
            resilience.append(self.getResilience())
        return resilience

    def intelligentSelectionResilienceCalculator(self):
        resilience = []
        while self.numNodes != 0:
            max_deg = 0  # grado massimo
            index_max = 0  # indice del nodo con grado massimo
            for i in range(len(self.arrNodes)):
                if max_deg < len(self.arrNodes[i].adjArr):
                    max_deg = len(self.arrNodes[i].adjArr)
                    index_max = i
            self.removeNode(index_max)
            resilience.append(self.getResilience())
        return resilience


class ERGraph(Graph):
    """
    :param n: num of nodes
    :param p: prob to generate a node
    :param seed: seed of random values
    """
    def __init__(self, n, p, seed):
        super().__init__(n)
        random.seed(seed)
        self.numNodes = n
        for i in range(self.numNodes):
            for j in range(self.numNodes):
                a = random.uniform(0, 1)
                if a < p and i != j and not (self.arrNodes[j].getAdjArr().__contains__(i) and self.arrNodes[i].getAdjArr().__contains__(j) ):
                    self.arrNodes[i].addNodeToAdj(j)
                    self.arrNodes[j].addNodeToAdj(i)
                    self.numEdges += 1


class UPAGraph(Graph):
    def __init__(self, n, m):
        """
        :param n: num of nodes
        :param m: num of nodes already in the jar
        """
        super().__init__(n)
        self.numNodes = m

        jar = []    # Attualmente teniamo solo gli ID dei nodi presenti nell'urna

        for i in range(m):
            for j in range(i+1, m):
                self.arrNodes[i].addNodeToAdj(j)
                self.arrNodes[j].addNodeToAdj(i)
                self.numEdges += 1

        #UPATrial
        for i in range(self.numNodes):
            for j in range(self.numNodes):
                jar.append(i)

        for u in range(m, n):
            jar, extraction = self.RunTrial(m, u, jar)
            for num in extraction:
                #Aggiungo i nodi alle rispettive liste di adj
                #da valutare se aggiungere if c'è gia un arco fra u e num e il contrario
                self.arrNodes[u].addNodeToAdj(num)
                self.arrNodes[num].addNodeToAdj(u)
                self.numEdges += 1

    def RunTrial(self, m, num_node, jar):
        extraction = []
        for i in range(m):
            u = random.randint(0, len(jar) - 1)
            extraction.append(jar[u])
        jar.append(num_node)
        jar.extend(extraction)
        self.numNodes += 1
        return jar, extraction


class DATAGraph(Graph):
    def __init__(self, n, file):
        super().__init__(n)
        self.numNodes = n
        data = np.loadtxt(file, delimiter='\t', dtype=int)
        startingNode = data[:, 0]
        endingNode = data[:, 1]

        IdToNumberArr = list(set(startingNode))
        IdToNumberArr.sort()

        IdDictionary = {}

        for i in range(n):
            IdDictionary[IdToNumberArr[i]] = i
        for i in range(len(startingNode)):
            if startingNode[i] != endingNode[i] and not self.arrNodes[IdDictionary[endingNode[i]]].adjArr.__contains__(IdDictionary[startingNode[i]]) and not self.arrNodes[IdDictionary[startingNode[i]]].adjArr.__contains__(IdDictionary[endingNode[i]]):
                self.arrNodes[IdDictionary[startingNode[i]]].addNodeToAdj(IdDictionary[endingNode[i]])
                self.arrNodes[IdDictionary[endingNode[i]]].addNodeToAdj(IdDictionary[startingNode[i]])
                self.numEdges += 1


def printPlotRandom(ArrResilD, ArrResilER, ArrResilUPA, numNodes, fileName):
    t = np.arange(numNodes)
    fig, ax = plt.subplots()
    ax.set(xlabel="Nr. nodi disattivati",
           ylabel="Dimensione componente connessa più grande",
           title="Resilienze dopo attacchi casuali")

    ax.plot(t, ArrResilD, "r", label="Grafo dati reali")
    ax.plot(t, ArrResilER, "b", label="Grafo ER")
    ax.plot(t, ArrResilUPA, "g", label="Grafo UPA")

    ax.legend(loc="upper right", shadow=True, fontsize="medium")
   
    fig.savefig(fileName)
    plt.show()


def printPlotRandom_masked(ArrResilD, ArrResilER, ArrResilUPA, numNodes, fileName):
    t = np.arange(numNodes)
    fig, ax = plt.subplots()
    ax.set(xlabel="Nr. nodi disattivati",
           ylabel="Dimensione componente connessa più grande",
           title="Resilienze dopo attacchi casuali")

    ax.plot(t, ArrResilD, "#ff6666", label="Grafo dati reali", linewidth=0.75)
    ax.plot(t, ArrResilER, "#8080ff", label="Grafo ER", linewidth=0.75)
    ax.plot(t, ArrResilUPA, "#66ff66", label="Grafo UPA", linewidth=0.75)

    ax.legend(loc="upper right", shadow=True, fontsize="medium")

    y_threshold = numNodes*0.75
    x_threshold = numNodes*0.2

    yE = []
    yU = []
    yD = []
    cE = 0
    cU = 0
    cD = 0
    for i in ArrResilER:
        if i >= y_threshold:
            yE.append(i)
            cE += 1
    for i in ArrResilUPA:
        if i >= y_threshold:
            yU.append(i)
            cU += 1
    for i in ArrResilD:
        if i >= y_threshold:
            yD.append(i)
            cD += 1

    ax.plot(np.arange(cE), yE, "#000066", linewidth=0.75)
    ax.plot(np.arange(cU), yU, "#003300", linewidth=0.75)
    ax.plot(np.arange(cD), yD, "#660000", linewidth=0.75)

    ax.axhline(y=y_threshold, linewidth=0.5, color="k")
    ax.axvline(x=x_threshold, linewidth=0.5, color="k")

    fig.savefig(fileName)
    plt.show()

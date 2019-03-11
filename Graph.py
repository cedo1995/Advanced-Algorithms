from Node import *
import random as random
import numpy as np



class Graph:
    def __init__(self, n):
        self.numNodes = n
        self.arrNodes = []
        for i in range(n):
            self.arrNodes.append( Node(i) )
        self.numEdges = 0
    def printG(self):
        print("Grafo con ", self.numNodes, " nodi e ", self.numEdges, " archi.")

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
            if startingNode[i] != endingNode[i] and not self.arrNodes[IdDictionary[endingNode[i]]].adjArr.__contains__(IdDictionary[startingNode[i]]):


import numpy as np
import random as random
import sys as sys
from Graph import UPAGraph, ERGraph, DataGraph


def ER(n, p):
    """
    :param n: number of nodes
    :param p: probability to generate an edge
    :return: Graph
    """
    random.seed(2)
    G = np.zeros((n, n))
    count = 0
    for row in range(n):
        for col in range(n):
            a = random.uniform(0, 1)
            # FIXME
            # con G[col][row] != 1 non considero i doppi archi avendo un grafo non orientato
            if a < p and G[col][row] != 1 and row != col:
                G[row][col] = 1
                count += 1
    return G, count


"""
def findP(G):
    for p in np.arange(0.000314, 0.0003198, 0.000001):
        G, count = ER(6474, p)
        print("{} \t {}".format(p, count))
"""

"""
def bisectionMethod(a,b,tolerance):
    G1, count1 = ER(6474, a)

    if (abs(count1 - 13233) > tolerance):
        G2, count2 = ER(6474, b)

        if (abs(count2 - 13233) > tolerance):
                    m = (a+b) / 2
                    if abs(count1-13233) < abs(count2-13233):
                        print(" intervallo",a," ",m)
                        return bisectionMethod(a, m, scarto)
                    else:
                        print(" intervallo",m," ",b)
                        return bisectionMethod(m, b, scarto)
        else:
            return Decimal(b)
    else:
        return Decimal(a)
"""


# TODO: verificarne il corretto funzionamento
def UPATrial(m, numNodes, nodeNumbers):
    numNodes = m
    nodeNumbers = []
    for i in range(0, numNodes):
        for j in range(0, m):
            nodeNumbers.append( i )
    # TODO: Controllare se serve anche numNodes
    # TODO: Ottimizzare con dizionario {indice: numero occorrenze}
    return nodeNumbers


# TODO: verificarne il corretto funzionamento
def RunTrial(m, numNodes, nodeNumbers):
    V_2 = []
    for i in range(0,m):
        u = RandomChoice(nodeNumbers)
        V_2.append(u)
    nodeNumbers.append(numNodes)
    nodeNumbers.append(V_2)
    numNodes += 1
    return V_2


# TODO: verificarne il corretto funzionamento
def UPA(n, m):
    """
    :param n: number of nodes
    :param m: 0<=1<=m number of nodes already in the graph
    """
    V = np.zeros((m))
    G = np.zeros((m, m))

    # TODO: Capire se è corretto settarli a zero
    numNodes = 0
    nodeNumbers = 0

    # Inizializza grafo completo con m nodi
    for row in range(m):
        for col in range(row+1, m):
            G[row][col] = 1

    nodeNumbers = UPATrial(m, numNodes, nodeNumbers)

    for u in range(m, n):
        V_2 = RunTrial(m, numNodes, nodeNumbers)
        V.append(u)
        for row in range(m):
            for col in range(row+1, m):
                G[row][col] = 1
    # TODO: Controllare se giusto
    return G


def main():
    # Da valutare se va usato
    """a=float(0.0)
    b=float(1.0)
    tolerance = 20      ##da valutare se cambiarlo
    p= Decimal(bisectionMethod(a,b,tolerance))
    print("probability: ",p)
    """

    """
    #calcolo di p ideale
    numNodes = 6474
    numEdges = 13233
    p = numEdges / (numNodes**2)
    G, count = ER(numNodes, p)
    print(count,p)
    """
    # TODO: porre m uguale al grado medio dei nodi entranti

    """
    # read data from file
    data = np.loadtxt('./as20000102.txt', delimiter='\t', dtype=int)
    startingNode = data[:, 0]
    endingNode = data[:, 1]
    new_data = []
    dict = {}
    # TODO: compattare new_data in codice più efficiente
    for i in range(len(startingNode)):
        if startingNode[i] != endingNode[i] and not new_data.__contains__((startingNode[i],endingNode[i])):
            new_data.append((startingNode[i], endingNode[i]))
            new_data.append((endingNode[i], startingNode[i]))

    # print("new_data=",np.size(new_data))
    """
    """for i,j in new_data:
        print("{}\t{}".format(i,j))
    """

    # Ciao amici :) La parte che va con le classi parte da qui..
    # se decidete che vi piace con le classi fate un po' di pulizia sopra
    numNodes = 6474
    numEdges = 12572

    #numNodes = 4

    p = numEdges / (numNodes**2)
    m = int(round(numEdges/numNodes))  # numero intero più vicino al grado medio dei vertici della rete reale
    sys.setrecursionlimit(10000)
    # Genero un grafo con il processo ER
    graph_er = ERGraph(numNodes, p)
    graph_er.printG()
    CCEr = graph_er.connectedComponents()

    # Genero un grafo con il processo UPA
    graph_upa = UPAGraph(numNodes, m)
    graph_upa.printG()
    CCUpa = graph_upa.connectedComponents()

    #Genero un grafo dal file
    graph_Dati = DataGraph(numNodes, './as20000102.txt')
    graph_Dati.printG()
    CCDati = graph_Dati.connectedComponents()
    #print(len(CCDati[0]))

    #graph_Dati = DataGraph(numNodes, './piccolo_esempietto.txt')
    # print(graph_Dati.adjArr)





if __name__ == '__main__':
    main()

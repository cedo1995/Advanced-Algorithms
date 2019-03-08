import numpy as np
import random as random
import sys as sys
from Graph import UPAGraph, ERGraph, DataGraph



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

    # TODO: porre m uguale al grado medio dei nodi entranti


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

    for i,j in new_data:
        print("{}\t{}".format(i,j))
    """

    # Ciao amici :) La parte che va con le classi parte da qui..
    # se decidete che vi piace con le classi fate un po' di pulizia sopra
    numNodes = 6474
    numEdges = 12572
    seed=2
    #numNodes = 2

    p = numEdges / (numNodes**2)
    m = int(round(numEdges/numNodes)) #se m=2 il numero di archi risulta giusto, se usiamo invece 2*numEdges/numNodes allora no.


    sys.setrecursionlimit(10000)

    # Genero un grafo con il processo ER
    print("ERGraph:")
    graph_er = ERGraph(numNodes, p, seed)
    graph_er.printG()
    CCEr = graph_er.connectedComponents()
    print(len(CCEr),"\n\n")

    # Genero un grafo con il processo UPA
    print("UPAGraph:")
    graph_upa = UPAGraph(numNodes, m)
    graph_upa.printG()
    CCUpa = graph_upa.connectedComponents()
    print(len(CCUpa),"\n\n")

    #Genero un grafo dal file
    print("DataGraph:")
    graph_Dati = DataGraph(numNodes, './as20000102.txt')
    graph_Dati.printG()
    CCDati = graph_Dati.connectedComponents()
    print(len(CCDati),"\n\n")

    #graph_Dati = DataGraph(numNodes, './piccolo_esempietto.txt')
    # print(graph_Dati.adjArr)
    

    # Genero un grafo con il processo UPA
    graph_upa = UPAGraph(numNodes, m)
    graph_upa.printG()
    #CCUpa = graph_upa.connectedComponents()





if __name__ == '__main__':
    main()

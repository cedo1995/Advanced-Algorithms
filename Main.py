from Graph import *
import sys


def main():
    numNodes = 6474
    numEdges = 12572
    #numNodes = 4
    sys.setrecursionlimit(10000)
    seed = 1
    p = numEdges / (numNodes ** 2)
    m = int(round(numEdges / numNodes))

    print("ER Graph:")
    graph_er = ERGraph(numNodes, p, seed)
    graph_er.printG()
    #CCEr = graph_er.connectedComponents()
    #print(CCEr)
    arrResilienceEr = graph_er.resilienceCalculator(seed)
    print("Resilienza random", arrResilienceEr)
    graph_er = ERGraph(numNodes, p, seed)
    intSelResilienceEr = graph_er.intelligentSelectionResilienceCalculator()
    print("Resilienza grado massimo", intSelResilienceEr)

    print("UPA Graph:")
    graph_UPA = UPAGraph(numNodes, m)
    graph_UPA.printG()
    # CCEr = graph_er.connectedComponents()
    # print(CCEr)
    arrResilienceUPA = graph_UPA.resilienceCalculator(seed)
    print("Resilienza random", arrResilienceUPA)
    graph_UPA = UPAGraph(numNodes, m)
    intSelResilienceUPA = graph_UPA.intelligentSelectionResilienceCalculator()
    print("Resilienza grado massimo", intSelResilienceUPA)
    
    print("DataGraph:")
    data_graph = DATAGraph(numNodes, './as20000102.txt')
    data_graph.printG()
    #for i in data_graph.arrNodes:
        #print(i.getID(), "\t", i.getAdjArr())

    #CCDati = data_graph.connectedComponents()
    #print(len(CCDati[0]))

    arrResilienceDATA = data_graph.resilienceCalculator(seed)
    print("Resilienza random", arrResilienceDATA)
    data_graph = DATAGraph(numNodes, './as20000102.txt')
    intSelResilienceDATA = data_graph.intelligentSelectionResilienceCalculator()
    print("Resilienza grado massimo", intSelResilienceDATA)





if __name__ == '__main__':
        main()
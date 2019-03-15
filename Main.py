from Graph import *
import sys
import copy

def main():
    numNodes = 6474
    numEdges = 12572
    #numNodes = 4
    sys.setrecursionlimit(10000)
    seed = 1
    p = numEdges / (numNodes ** 2)
    m = int(round(numEdges / numNodes))


    # DOMANDA 1
    print("ER Graph:")
    graph_er = ERGraph(numNodes, p, seed)
    graph_er.printG()

    graph_er_copy = copy.deepcopy(graph_er)
    arrResilienceEr = graph_er_copy.resilienceCalculator(seed)
    print("Resilienza random", arrResilienceEr)

    # intSelResilienceEr = graph_er.intelligentSelectionResilienceCalculator()
    # print("Resilienza grado massimo", intSelResilienceEr)

    print("UPA Graph:")
    graph_UPA = UPAGraph(numNodes, m)
    graph_UPA.printG()

    graph_UPA_copy = copy.deepcopy()
    arrResilienceUPA = graph_UPA_copy.resilienceCalculator(seed)
    print("Resilienza random", arrResilienceUPA)

    # intSelResilienceUPA = graph_UPA.intelligentSelectionResilienceCalculator()
    # print("Resilienza grado massimo", intSelResilienceUPA)


    print("DataGraph:")
    data_graph = DATAGraph(numNodes, './as20000102.txt')
    data_graph.printG()

    data_graph_copy = copy.deepcopy()
    arrResilienceDATA = data_graph_copy.resilienceCalculator(seed)
    print("Resilienza random", arrResilienceDATA)

    # intSelResilienceDATA = data_graph.intelligentSelectionResilienceCalculator()
    # print("Resilienza grado massimo", intSelResilienceDATA)

    # printPlotRandom(arrResilienceDATA, arrResilienceEr, arrResilienceUPA, numNodes)

    # DOMANDA 2
    printPlotRandom_masked(arrResilienceDATA, arrResilienceEr, arrResilienceUPA, numNodes)

if __name__ == '__main__':
        main()

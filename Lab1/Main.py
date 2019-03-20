from Graph import *
import sys
import copy

def main():
    numNodes = 6474
    numEdges = 12572

    sys.setrecursionlimit(10000)
    seed = 1
    #p = numEdges / (numNodes ** 2)
    p = 0.0006
    m = int(round(numEdges / numNodes))

    print("ER Graph:")
    graph_er = ERGraph(numNodes, p, seed)
    graph_er.printG()
    graph_er_copy = copy.deepcopy(graph_er)
    arrResilienceEr = graph_er_copy.resilienceCalculator(seed)
   
    intSelResilienceEr = graph_er.intelligentSelectionResilienceCalculator()
    

    print("UPA Graph:")
    graph_UPA = UPAGraph(numNodes, m)
    graph_UPA.printG()
    graph_UPA_copy = copy.deepcopy(graph_UPA)
    arrResilienceUPA = graph_UPA_copy.resilienceCalculator(seed)
    
    intSelResilienceUPA = graph_UPA.intelligentSelectionResilienceCalculator()
    


    print("DataGraph:")
    data_graph = DATAGraph(numNodes, './as20000102.txt')
    data_graph.printG()
    data_graph_copy = copy.deepcopy(data_graph)
    arrResilienceDATA = data_graph_copy.resilienceCalculator(seed)
    
    intSelResilienceDATA = data_graph.intelligentSelectionResilienceCalculator()
    

    # DOMANDA 1
    printPlotRandom(arrResilienceDATA,
                    arrResilienceEr,
                    arrResilienceUPA,
                    numNodes,
                    "Fig1_resilienze_attacchi_casuali")

    # DOMANDA 2
    printPlotRandom_masked(arrResilienceDATA,
                           arrResilienceEr,
                           arrResilienceUPA,
                           numNodes,
                           "Fig2_resilienze_attacchi_casuali_masked")

    # DOMANDA 3
    printPlotRandom(intSelResilienceDATA,
                    intSelResilienceEr,
                    intSelResilienceUPA,
                    numNodes,
                    "Fig3_resilienze_attacchi_intelligenti")

    # DOMANDA 4
    printPlotRandom_masked(intSelResilienceDATA,
                           intSelResilienceEr,
                           intSelResilienceUPA,
                           numNodes,
                           "Fig4_resilienze_attacchi_intelligenti_masked")


if __name__ == '__main__':
        main()

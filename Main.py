from Graph import *



def main():
    numNodes = 6474
    numEdges = 12572
    #numNodes = 4

    seed = 1
    p = numEdges / (numNodes ** 2)
    m = int(round(numEdges / numNodes))
    """
    print("ER Graph:")
    graph_er = ERGraph(numNodes, p, seed)
    graph_er.printG()
    
    
    print("UPA Graph:")
    graph_UPA = UPAGraph(numNodes, m)
    graph_UPA.printG()
    """

    print("DataGraph:")
    data_graph = DATAGraph(numNodes, './as20000102.txt')
    data_graph.printG()
    #for i in data_graph.arrNodes:
        #print(i.getID(), "\t", i.getAdjArr())

    #CCDati = data_graph.connectedComponents()
    #print(len(CCDati[0]))

    arrResilience = data_graph.resilienceCalculator(seed)
    print(arrResilience)




if __name__ == '__main__':
        main()
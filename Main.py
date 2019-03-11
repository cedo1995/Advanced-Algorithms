from Graph import ERGraph, UPAGraph, DATAGraph





def main():
    numNodes = 6474
    numEdges = 12572
    seed = 1
    p = numEdges / (numNodes ** 2)
    m = int(round(numEdges / numNodes))
    """
    print("ER Graph:")
    graph_er = ERGraph(numNodes, p, seed)
    graph_er.printG()
    print(graph_er.arrNodes[0].adjArr)
    print(graph_er.arrNodes[3918].adjArr)
    
    print("UPA Graph:")
    graph_UPA = UPAGraph(numNodes, m)
    graph_UPA.printG()
    """
    print("DataGraph:")
    data_graph = DATAGraph(numNodes, './as20000102.txt')
    data_graph.printG()




if __name__ == '__main__':
        main()
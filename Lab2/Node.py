class Node:
    def __init__(self, id):
        self.id = id
        self.adj_arr = [] # lista di archi

    def addEdgeToNode(self, arco):
        self.adj_arr.append(arco)

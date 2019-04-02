class Node:
    def __init__(self, id):
        self.id = id
        self.adj_arr = [] # lista di archi

    def AddEdgeToNode(self, arco):
        self.adj_arr.append(arco)

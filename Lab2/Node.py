class Node:
    def __init__(self, id):
        self.id = id
        self.adjArr = [] # lista di archi

    def getID(self):
        return self.id

    def addEdgeToNode(self, arco):
        self.adjArr.append(arco)

    def print(self):
        print("Nodo:", self.id, "Adj:", self.adjArr)

    def getAdjArr(self):
        return self.adjArr
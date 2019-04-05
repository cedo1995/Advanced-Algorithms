class Node:
    def __init__(self, id):
        self.id = id
        self.adj_arr = []    # lista di archi
        self.posX = 0
        self.posY = 0

    def addEdgeToNode(self, arco):
        self.adj_arr.append(arco)

    def setPosX(self, posX):
        self.posX = posX

    def setPosY(self, posY):
        self.posY = posY

    def setCoordinates(self, posX, posY):
        self.setPosX(posX)
        self.setPosY(posY)



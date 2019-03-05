class Node:
    def __init__(self, value, color):
       self.value = value       #ID of the node
       self.color = color

    def printNode(self):
        print("Nodo: ",self.value,"\tColore: ",self.color)

    def addNode(self,value,color):


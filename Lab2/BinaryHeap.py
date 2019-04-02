from Node import Node
from Edge import Edge
import sys

class Tuple:
    def __init__(self, id, value):
        self.id = id  # id della stazione a cui corrisponde il nodo
        self.value = value

class BinaryHeap:
    def __init__(self):
        self.list_vertices = []  #lista di nodi contenuti nella heap binaria ogni elemento è una Tupla (valore, id stazione)

    def Add(self, id, value):
        self.list_vertices.append(Tuple(id, value))
        n = len(self.list_vertices)
        self.BubbleUp(n-1)

    def BuildHeap(self, n):
        for i in range(int(n/2)-1, 0, -1):
            self.TrickleDown(i)

    def Left(self, i):
        return (2*i)+1

    def Right(self, i):
        return (2*i)+2

    def Parent(self, i):
        return int((i-1)/2)

    def BubbleUp(self, i):
        p = self.Parent(i)
        while i > 0 and self.list_vertices[i].value < self.list_vertices[p].value:
            temp = self.list_vertices[p]
            self.list_vertices[p] = self.list_vertices[i]
            self.list_vertices[i] = temp  # scambio A[i] con A[p]
            i = p
            p = self.Parent(i)

    def DecreaseKey(self, nodeId, value):
        """
        :param nodeId: NON è un IdToNumber
        :param value: è la distanza dallo starting node al nodo con id = nodeId
        :return:
        """
        for i, x in enumerate(self.list_vertices):
            if x.id == nodeId and self.list_vertices[i].value > value:
                self.list_vertices[i].value = value
                self.BubbleUp(i)
                return True
        return False

    def TrickleDown(self, i):
        l = self.Left(i)
        r = self.Right(i)
        n = len(self.list_vertices)
        smallest = i
        if l < n and self.list_vertices[l].value < self.list_vertices[i].value:
            smallest = l
        if r < n and self.list_vertices[r].value < self.list_vertices[smallest].value:
            smallest = r
        if smallest != i:
            temp = self.list_vertices[smallest]
            self.list_vertices[smallest] = self.list_vertices[i]
            self.list_vertices[i] = temp
            self.TrickleDown(smallest)

    def ExtractMin(self):
        min = self.list_vertices[0]
        n = len(self.list_vertices)
        self.list_vertices[0] = self.list_vertices[n - 1]
        self.list_vertices.pop(n - 1)  # elimina l'elemento copiato in cima (duplicato)
        self.TrickleDown(0)
        return min





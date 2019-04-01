from Node import Node
from Edge import Edge
import sys

class Tupla:
    def __init__(self,id, valore):
        self.valore = valore
        self.id = id  # id della stazione a cui corrisponde il nodo

class HeapBinaria:
    def __init__(self):
        self.arrVertex = []  #lista di nodi contenuti nella heap binaria ogni elemento è una Tupla (valore, id stazione)
        #for i in arrNodi:
            #self.arrVertex.append(Tupla(i.id))  # inizializzo priority queue con id delle stazioni e distanza infinito

    def Add(self, x, valore):
        self.arrVertex.append(Tupla(x, valore))
        n = len(self.arrVertex)
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
        while i > 0 and self.arrVertex[i].valore < self.arrVertex[p].valore:
            temp = self.arrVertex[p]
            self.arrVertex[p] = self.arrVertex[i]
            self.arrVertex[i] = temp  # scambio A[i] con A[p]
            i = p
            p = self.Parent(i)

    def DecreaseKey(self, nodeId, value):  # sostituisco alla tupla in posizione "i" il valore "value"
        for i, x in enumerate(self.arrVertex):
            if x.id == nodeId and self.arrVertex[i].valore > value:
                self.arrVertex[i].valore = value
                self.BubbleUp(i)
                return True
        return False

    def TrickleDown(self, i):
        l = self.Left(i)
        r = self.Right(i)
        n = len(self.arrVertex)
        smallest = i
        if l<n and self.arrVertex[l].valore < self.arrVertex[i].valore:
            smallest = l
        if r<n and self.arrVertex[r].valore < self.arrVertex[smallest].valore:
            smallest = r
        if smallest != i:
            temp = self.arrVertex[smallest]
            self.arrVertex[smallest] = self.arrVertex[i]
            self.arrVertex[i] = temp
            self.TrickleDown(smallest)

    def ExtractMin(self):
        min = self.arrVertex[0]
        n = len(self.arrVertex)
        self.arrVertex[0] = self.arrVertex[n-1]
        self.arrVertex.pop(n-1)  # elimina l'elemento copiato in cima (duplicato)
        self.TrickleDown(0)
        return min





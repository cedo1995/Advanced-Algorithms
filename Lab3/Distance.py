import sys


class DistanceItem:
    subset_nodes = []
    value = sys.maxsize

    def __init__(self, subset_nodes, value):
        self.subset_nodes = subset_nodes
        self.value = value


class Distance:
    id_vertex = 0
    subset_nodes = []
    value = sys.maxsize

    def __init__(self, id_vertex, subset_nodes, value):
        self.id_vertex = id_vertex
        self.subset_nodes = subset_nodes
        self.value = value

    def addDistanceItem(self, subset_nodes, value):
        is_the_same = True
        if len(subset_nodes) != len(self.subset_nodes):
            self.subset_nodes = subset_nodes
            self.value = value
            return
        for i, val in enumerate(self.subset_nodes):
            if val != subset_nodes[i]:
                is_the_same = False
                break

        if not is_the_same:
            self.subset_nodes = subset_nodes
            self.value = value

    def has_subset_items(self, subset_node):  # controlla se la lista di distance_items e uguale
        if len(subset_node) != len(self.subset_nodes):
            return False,-1
        for i,val in enumerate(self.subset_nodes):
            if val != subset_node[i]:
                return False, i
        return True, -1
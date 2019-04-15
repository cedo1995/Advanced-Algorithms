import sys


class DistanceItem:
    subset_nodes = {}
    value = sys.maxsize

    def __init__(self, subset_nodes, value):
        self.subset_nodes = subset_nodes
        self.value = value


class Distance:
    id_vertex = 0
    distance_items_list = []

    def __init__(self, id_vertex, subset_nodes,value):
        self.id_vertex = id_vertex
        self.distance_items_list.append(DistanceItem(subset_nodes, value))

    def addDistanceItem(self, subset_nodes, value):
        is_the_same = False
        for i in self.distance_items_list:
            if i.subset_nodes == subset_nodes:
                i.value = value
                is_the_same = True
                break

        if not is_the_same:
            self.distance_items_list.append(DistanceItem(subset_nodes, value))

    def has_subset_items(self, subset_node):
        for i in self.distance_items_list:
            if i.subset_nodes == subset_node:
                return True, i
        return False, -1
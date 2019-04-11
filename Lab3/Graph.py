

class Graph:
    def __init__(self, name, dimension, coord_type, coordinates, count_to_coordinates):
        """
        :param name: nome del grafo che si sta analizzando
        :param dimension: numero dei nodi del grafo
        :param coord_type: tipo di coordinate utilizzate
        :param coordinates: lista di tutte le coordinate
        :param count_to_coordinates: dizionario che relaziona la posizione della coordinata nel file rispetto ai valori
        """
        self.name = name
        self.num_nodes = int(dimension)
        self.coord_type = coord_type
        self.coordinates = coordinates
        self.count_to_coordinates = count_to_coordinates        # dizionario indice--> coordinate
        self.num_edges = 0          # numero di archi del grafo
        self.edges = []             # archi del grafo

        # aggiunta di tutti gli archi al grafo in modo da creare un grafo completo
        for i in range(self.num_nodes-1):
            for j in range(i+1, self.num_nodes):
                self.num_edges += 1
                self.edges.append((self.coordinates[i], self.coordinates[j]))



    def printG(self):
        print("Il grafo", self.name, "ha ", self.num_nodes, "nodi e ", self.num_edges, "archi")

from Shire import Shire


class Cluster:

    def __init__(self, centroid):
        """
        :param centroid: tuple of 2 coordinates(x,y)
        """
        self.pos_x = centroid.posX
        self.pos_y = centroid.posY
        self.centroid = []
        self.setCentroid(self.pos_x, self.pos_y)
        self.elements = []
        self.addElementToCluster(centroid)

    def setCentroid(self, pos_x, pos_y):
        self.centroid = [pos_x, pos_y]


    def printCluster(self):
        print("Cluster con centroide in posizione ", self.centroid[0], self.centroid[1], "con elementi:")
        for el in self.elements:
            print(el.id)

    def addElementToCluster(self, el):
        self.elements.append(el)     # todo da togliere gli elementi dal cluster shire

    def unionCluster(self, cluster):
        self.calculateNewCentroid(self.pos_x, self.pos_y, cluster.pos_x, cluster.pos_y)   # a livello teorico non devo neanche eliminare la posizione vecchia del centroide
        #print("Sto per aggiungere gli elementi al cluster ", self.centroid)
        for el in cluster.elements:
            #print(el)
            self.addElementToCluster(el)

    def calculateNewCentroid(self, pos_x, pos_y, pos2_x, pos2_y):
        new_pos_x = float(abs(float(pos2_x) - float(pos_x)) / 2)
        new_pos_y = float(abs(float(pos2_y) - float(pos_y)) / 2)
        self.setCentroid(new_pos_x, new_pos_y)

    def distanceBetweenCluster(self, cluster_2):
        """
        :param cluster_2:  cluster da confrontare
        :return: calcola la distanza euclidea fra il centroide del cluster stesso e il centroide del cluster2
        """
        return float(float(float(float(self.pos_x) - float(cluster_2.pos_x))**2 +
                           float(float(self.pos_y) - float(cluster_2.pos_y))**2) ** 0.5)


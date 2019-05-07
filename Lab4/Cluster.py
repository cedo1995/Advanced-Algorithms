class Cluster:

    def __init__(self, centroid):
        """
        :param centroid: tuple of 2 coordinates(x,y)
        """
        self.centroid = [centroid.posX, centroid.posY]       # ha la forma: (posX e posY)
        self.elements = []

    def printCluster(self):
        print("Cluster con centroide in posizione ", self.centroid[0], self.centroid[1], "con elementi:", self.elements)

    def addElementToCluster(self, shire):
        self.elements.append(shire)     # todo da togliere gli elementi dal cluster shire

    def unionCluster(self, shire2):
        posx, posy = self.calculateNewCentroid(shire2)
        new_pos = (posx, posy)
        cluster = Cluster(new_pos)
        for element in shire2.elements:
            self.addElementToCluster(element)
        cluster.elements = self.elements
        return cluster

    def calculateNewCentroid(self, shire2):
        pos_x = float(abs(float(shire2.centroid[0]) - float(self.centroid[0])) / 2)
        pos_y = float(abs(float(shire2.centroid[1]) - float(self.centroid[1])) / 2)
        return pos_x, pos_y

    def distanceBetweenCluster(self, cluster_2):
        """
        :param cluster_2:  cluster da confrontare
        :return: calcola la distanza euclidea fra il centroide del cluster stesso e il centroide del cluster2
        """
        return float(float(float(float(self.centroid[0]) - float(cluster_2.centroid[0]))**2 +
                           float(float(self.centroid[1]) - float(cluster_2.centroid[1]))**2) ** 0.5)



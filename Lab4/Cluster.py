class Cluster:

    def __init__(self, centroid):
        self.centroid = centroid
        self.elements = []

    def addElementToCluster(self, county):
        self.elements.append(county)

    def unionCluster(self, county1, county2):
        pass
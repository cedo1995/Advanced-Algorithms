class Graph:

    def __init__(self, number_of_counties, counties):
        self.number_of_counties = number_of_counties
        self.counties = counties

    def hierarchicalClustering(self, k):
        """
        :param k: numero di cluster richiesti
        :return: un insieme di k cluster che partizionano le contee
        """
        n = self.number_of_counties
        cluster = {}    # dizionario con chiave l'indice(id) del cluster e valori una lista di liste con
        for i in range(n):
            pass

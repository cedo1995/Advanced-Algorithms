from Shire import Shire
from Graph import Graph
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm


def main():
    path_file = ["./unifiedCancerData_212.csv", "./unifiedCancerData_562.csv", "./unifiedCancerData_1041.csv",
                 "./unifiedCancerData_3108.csv"]
    #path_file = ["./unifiedCancerData_3108.csv"]
    #path_file = ["./unifiedCancerData_562.csv"]
    #path_file = ["./piccolo_esempietto.csv"]
    points = np.loadtxt(path_file[1], delimiter=",", usecols=(1, 2))
    for file in path_file:
        shire_list = []  # contiene tutte le contee presenti nel file
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                line_count += 1
                shire = Shire(row[0], float(row[1]), float(row[2]), row[3], row[4])
                shire_list.append(shire)

        graph = Graph(len(shire_list), shire_list)
        #print(points)

        clusters = graph.hierarchicalClustering(points, 15)

        #clusters = graph.kMeansClustering(15, 5, shire_list)

        """
        for cl in clusters:
            clusters[cl].printCluster()
        """
        x = [x for x in range(15)]
        colors = matplotlib.cm.rainbow(np.linspace(0, 1, 15))
        i = 0
        for cl in clusters:
            shires_x = [x[0] for x in cl.elements]
            shires_y = [x[1] for x in cl.elements]
            plt.scatter(shires_x, shires_y, c=colors[i], s=1, marker="o")
            i += 1
        plt.gca().invert_yaxis()

        plt.show()






if __name__ == '__main__':
    main()

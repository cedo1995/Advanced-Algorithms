from Shire import Shire
from Graph import Graph
import csv


def main():
    path_file = ["./unifiedCancerData_212.csv", "./unifiedCancerData_562.csv", "./unifiedCancerData_1041.csv",
                 "./unifiedCancerData_3108.csv"]
    path_file = ["piccolo_esempietto.csv"]
    path_file = ["./unifiedCancerData_212.csv"]
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

        clusters = graph.hierarchicalClustering(15)

        # clusters = graph.kMeansClustering(15, 5)

        for cl in clusters:
            clusters[cl].printCluster()




























if __name__ == '__main__':
    main()

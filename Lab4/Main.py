from Shire import Shire
from Graph import Graph
import csv


def main():
    path_file = ["./unifiedCancerData_212.csv", "./unifiedCancerData_562.csv", "./unifiedCancerData_1041.csv",
                 "./unifiedCancerData_3108.csv"]
    path_file = ["./unifiedCancerData_212.csv"]
    for file in path_file:
        shire_list = []  # contiene tutte le contee presenti nel file
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                line_count += 1
                shire = Shire(row[0], row[1], row[2], row[3], row[4])
                shire_list.append(shire)
        # print(shire_list[0].posX, shire_list[0].posY)
        graph = Graph(len(shire_list), shire_list)
        cluster = graph.hierarchicalClustering(15)
        """for cl in cluster:
            cl.printCluster()
        #print(file_shires_element)
        """



























if __name__ == '__main__':
    main()

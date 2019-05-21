from Shire import Shire
from Graph import Graph
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm
from sklearn.cluster import AgglomerativeClustering

def main():
    path_file = ["./unifiedCancerData_212.csv", "./unifiedCancerData_562.csv", "./unifiedCancerData_1041.csv",
                 "./unifiedCancerData_3108.csv"]
    #path_file = ["./unifiedCancerData_3108.csv"]
    #path_file = ["./unifiedCancerData_562.csv"]
    #path_file = ["./piccolo_esempietto.csv"]

    for file in path_file:
        points = np.loadtxt(file, delimiter=",", usecols=(0, 1, 2))
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

        clustersH = -1
        clustersK = -1
        clustersH = graph.hierarchicalClustering(points, 15)
        # SERVE PER PROVA PER CAPIRE SE I CLUSTER SONO GIUSTI
        '''  
        data_set = np.loadtxt(fname="./unifiedCancerData_3108.csv",  delimiter=",", usecols=(1, 2))
        clustersH = graph.hierarchicalClustering(points, 15)
        cluster = AgglomerativeClustering(n_clusters=15, affinity='euclidean', linkage='ward')
        cluster.fit_predict(data_set)
        plt.scatter(data_set[:, 0], data_set[:, 1], c=cluster.labels_, cmap='rainbow', alpha=0.5)
        plt.gca().invert_yaxis()
        plt.show()
        '''
        if clustersH != -1:
            colors = matplotlib.cm.rainbow(np.linspace(0, 1, 15))
            i = 0
            img = plt.imread("./USA_Counties.png")
            fig, ax = plt.subplots()
            for cl in clustersH:
                shires_x = [x[0] for x in clustersH[cl].elements]
                shires_y = [x[1] for x in clustersH[cl].elements]


                ax.plot(clustersH[cl].pos_x, clustersH[cl].pos_y, 'o', markersize=4, c=colors[i])
                for el in clustersH[cl].elements:
                    ax.plot([clustersH[cl].pos_x, el[0]], [clustersH[cl].pos_y, el[1]], 'o-', c=colors[i], lw=0.2, markersize=2)
                i += 1
            ax.invert_yaxis()
            ax.imshow(img)
            plt.show()


        clustersK = graph.kMeansClustering(15, 5, shire_list)

        if clustersK != -1:
            colors = matplotlib.cm.rainbow(np.linspace(0, 1, 15))
            i = 0
            img = plt.imread("./USA_Counties.png")
            fig, ax = plt.subplots()
            for cl in clustersK:
                ax.plot(cl.pos_x, cl.pos_y, 'o', markersize=4, c=colors[i])
                for k in cl.elements:
                    ax.plot([cl.pos_x, k[0]], [cl.pos_y, k[1]], 'o-', c=colors[i], lw=0.2, markersize=2)
                i += 1
            ax.invert_yaxis()
            ax.imshow(img)
            plt.show()







if __name__ == '__main__':
    main()

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveTask;
import java.util.concurrent.TimeUnit;

class KMeans{

    public List<Cluster> serialKMeans(List<City> cities, int k, int num_it){
        int n = cities.size();

        List<City> firstFifty = cities.subList(0, k);

        // Creo la lista dei centroidi
        List<Point> centroids = new ArrayList<Point>();
        for (int i = 0; i < k; i++) {
            centroids.add(firstFifty.get(i).coordinates);
        }

        List<Cluster> clusters = new ArrayList<Cluster>();
        for (int i=0; i<num_it; i++) {
            clusters = new ArrayList<Cluster>();

            // Creo n cluster vuoti (solo con i centroidi)
            for (Point a:centroids){
                clusters.add(new Cluster(a, new ArrayList<City>()));
            }

            // Trovo per ogni città il centroide più vicino
            for(int j = 0; j < n; j++) {
                int nearestCentroidIndex = findNearestIndexOfCentroid(cities.get(j), centroids);
                clusters.get(nearestCentroidIndex).addElementToCluster(cities.get(j));
            }

            // Aggiorno tutti i centroidi dopo l'aggiunta degli elementi ai cluster
            for (int j = 0; j < k ; j++){
                Point newCentroid = clusters.get(j).updateCentroid();
                centroids.set(j, newCentroid);
            }
        }
        return clusters;
    }

    private int findNearestIndexOfCentroid(City nodo, List<Point> centroids) {
        double minDistFound = 1000000000;
        int indexMinCentroid = -1;
        int count = 0;

        for (Point a : centroids) {
            double distance = a.getDistance(nodo.coordinates);
            if (distance < minDistFound) {
                minDistFound = distance;
                indexMinCentroid = count;
            }
            count += 1;
        }
        return indexMinCentroid;
    }

    // PROBLEMA:
    // ogni ciclo for da parallelizzare è dentro un invoke sul pool
    // Ma il codice scritto dopo gli invoke continua ad essere fatto senza aspettare che i cicli paralleli finiscano,
    // quindi si mescola tutto e succede un casino!
    public List<Cluster> parallelKMeans(List<City> cities, int k, int num_it) throws InterruptedException {
        int n = cities.size();

        List<City> firstFifty = cities.subList(0, k);


        List<Point> centroids = new ArrayList<Point>(k);
        //ForkJoinPool pool = new ForkJoinPool(100);
        ForkJoinPool.commonPool().invoke(new ForEach(centroids, firstFifty, 0, k)); // In realtà ci mette di più

        List<Cluster> clusters = new ArrayList<Cluster>();
        for (int i=0; i<1; i++){
            clusters = new ArrayList<Cluster>(k);

            // Creo n cluster vuoti (solo con i centroidi)
            ForkJoinPool.commonPool().invoke(new ForEach2(clusters, centroids, 0, centroids.size()));

            // Trovo per ogni città il centroide più vicino
            ForkJoinPool.commonPool().invoke(new ForEach3(clusters, cities, centroids, 0, n));

            // Aggiorno tutti i centroidi dopo l'aggiunta degli elementi ai cluster
            ForkJoinPool.commonPool().invoke(new ForEach4(clusters, centroids, 0, k));

        }
        return clusters;
    }
}
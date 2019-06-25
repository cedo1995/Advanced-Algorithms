import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveTask;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.function.Consumer;

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

    public List<Cluster> parallelKMeans(List<City> cities, int k, int num_it) throws InterruptedException {
        int n = cities.size();

        List<City> firstFifty = cities.subList(0, k);

        // Creo la lista dei centroidi
        List<Point> centroids = new CopyOnWriteArrayList<Point>();

        List<Cluster> clusters = new CopyOnWriteArrayList<Cluster>();

        for (int i = 0; i < k; i++) {
            centroids.add(firstFifty.get(i).coordinates);
            clusters.add(i,new Cluster(centroids.get(i), new  CopyOnWriteArrayList<City>()));
        }


        for (int i=0; i<num_it; i++) {
            // clusters = new CopyOnWriteArrayList<Cluster>();

            // Creo n cluster vuoti (solo con i centroidi)
            for (int w=0; w < centroids.size(); w++){
                clusters.set(w, new Cluster(centroids.get(w), new  CopyOnWriteArrayList<City>()));
            }

            ForkJoinPool pool = new ForkJoinPool();
            AtomicInteger a = new AtomicInteger(n);
            for (int j = 0; j < n; j++) {
                pool.invoke(new ParallelAction(a, j,
                        new Consumer<Integer>() {
                            @Override
                            public void accept(Integer integer) {
                                int nearestCentroidIndex = findNearestIndexOfCentroid(cities.get(integer), centroids);
                                clusters.get(nearestCentroidIndex).addElementToCluster(cities.get(integer));
                            }
                        }
                ));
            }

            while( a.get() > 0 ) {
                Thread.yield();
            }

            // Aggiorno tutti i centroidi dopo l'aggiunta degli elementi ai cluster
            for (int j = 0; j < k ; j++){
                Point newCentroid = clusters.get(j).updateCentroid();
                centroids.set(j, newCentroid);
            }
        }
        return clusters;
    }
}
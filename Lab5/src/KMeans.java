import java.sql.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.concurrent.*;
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

    private int findNearestIndexOfCentroidWow(ForkJoinPool pool, City nodo, List<Point> centroids) throws InterruptedException {
        CountDownLatch c = new CountDownLatch(centroids.size());

        ConcurrentLinkedQueue<ArrayList<Double>> distances = new ConcurrentLinkedQueue<ArrayList<Double>>();

        for (int a = 0; a < centroids.size(); a++) {
            final int index = a;
            pool.execute(new Runnable() {
                @Override
                public void run() {
                    ArrayList<Double> array = new ArrayList<Double>();
                    array.add((double)index);
                    array.add(centroids.get(index).getDistance(nodo.coordinates));
                    distances.add(array);
                    c.countDown();
                }
            });
        }
        c.await();

        ArrayList<Double> min = null;
        for(ArrayList<Double> d : distances)
        {
            min = (min==null|| d.get(0)<min.get(0)?d:min);
        }
        return min.get(0).intValue();
    }

    public List<Cluster> parallelKMeans(List<City> cities, int k, int num_it) throws InterruptedException {
        ForkJoinPool pool = new ForkJoinPool();
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

            AtomicInteger a = new AtomicInteger(n);
            for (int j = 0; j < n; j++) {
                final int integer = j;
                pool.execute(new Runnable() {
                    @Override
                    public void run() {
                        int nearestCentroidIndex = 0;

                        nearestCentroidIndex = findNearestIndexOfCentroid(cities.get(integer), centroids);

                        clusters.get(nearestCentroidIndex).addElementToCluster(cities.get(integer));
                        a.decrementAndGet();
                    }
                });
//                pool.execute(new ParallelAction(a, j,
//                    new Consumer<Integer>() {
//                        @Override
//                        public void accept(Integer integer) {
//                            int nearestCentroidIndex = 0;
//                            try {
//                                nearestCentroidIndex = findNearestIndexOfCentroidWow(pool, cities.get(integer), centroids);
//                            } catch (InterruptedException e) {
//                                e.printStackTrace();
//                            }
//                            clusters.get(nearestCentroidIndex).addElementToCluster(cities.get(integer));
//                        }
//                    }
//                ));
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
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.RecursiveAction;

class ForEach3 extends RecursiveAction {

    private List<Cluster> arrayCluster;
    private List<City> arrayCity;
    private List<Point> arrayCentroidi;
    private int from;
    private int to;

    public final static int TASK_LEN = 5000;

    public ForEach3(List<Cluster> arrayCluster, List<City> arrayCity, List<Point> arrayCentroidi, int from, int to) {
        this.arrayCluster = arrayCluster;
        this.arrayCity = arrayCity;
        this.arrayCentroidi = arrayCentroidi;
        this.from = from;
        this.to = to;
    }

    @Override
    protected void compute() {
        int len = to - from;
        if (len < TASK_LEN) {
            work(arrayCluster, arrayCity, arrayCentroidi, from, to);
        } else {
            int mid = (from + to) >>> 1;
            new ForEach3(arrayCluster, arrayCity, arrayCentroidi, from, mid).fork();
            new ForEach3(arrayCluster, arrayCity, arrayCentroidi, mid, to).fork();
        }
    }

    private void work(List<Cluster> arrayCluster, List<City> arrayCity, List<Point> arrayCentroidi, int from, int to) {
        System.out.println("C");
        for (int j = from; j < to; j++) {
            int nearestCentroidIndex = findNearestIndexOfCentroid(arrayCity.get(j), arrayCentroidi);
            arrayCluster.get(nearestCentroidIndex).addElementToCluster(arrayCity.get(j));
        }
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
}

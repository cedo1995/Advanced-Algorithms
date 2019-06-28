import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.RecursiveAction;
import java.util.concurrent.atomic.AtomicInteger;

class ParallelFor3 extends RecursiveAction {

    private Map<Integer, Cluster> arrayConteniore;
    Map<Integer, Point> arrayDaAggiungere;
    private List<City> arrayCity;
    private int from;
    private int to;
    private AtomicInteger a;

    public final static int TASK_LEN = 20;

    public ParallelFor3(Map<Integer, Cluster> arrayConteniore, Map<Integer, Point> arrayDaAggiungere, List<City> arrayCity, int from, int to, AtomicInteger a) {
        this.arrayConteniore = arrayConteniore;
        this.arrayDaAggiungere = arrayDaAggiungere;
        this.arrayCity = arrayCity;
        this.from = from;
        this.to = to;
        this.a = a;
    }

    @Override
    protected void compute() {
        int len = to - from;
        if (len < TASK_LEN) {
            work(arrayConteniore, arrayDaAggiungere, arrayCity, from, to);
        } else {
            int mid = (from + to) / 2;
            invokeAll(new ParallelFor3(arrayConteniore, arrayDaAggiungere, arrayCity, from, mid, a),
                    new ParallelFor3(arrayConteniore, arrayDaAggiungere, arrayCity, mid, to, a));
        }

    }

    private void work(Map<Integer, Cluster> arrayConteniore, Map<Integer, Point> arrayDaAggiungere, List<City> arrayCity, int from, int to) {
        for (int j = from; j < to; j++) {
            int nearestCentroidIndex = findNearestIndexOfCentroid(arrayCity.get(j), arrayDaAggiungere);
            arrayConteniore.get(nearestCentroidIndex).addElementToCluster(arrayCity.get(j));
            a.decrementAndGet();
        }
    }

    private int findNearestIndexOfCentroid(City nodo, Map<Integer, Point> centroids) {
        double minDistFound = 1000000000;
        int indexMinCentroid = -1;

        for(Map.Entry<Integer, Point> a : centroids.entrySet()) {
            double distance = a.getValue().getDistance(nodo.coordinates);
            if (distance < minDistFound) {
                minDistFound = distance;
                indexMinCentroid = a.getKey();
            }
        }
        return indexMinCentroid;
    }
}


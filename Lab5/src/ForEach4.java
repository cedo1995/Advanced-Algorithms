import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.RecursiveAction;

class ForEach4 extends RecursiveAction {

    private List<Cluster> arrayCluster;
    private List<Point> arrayCentroidi;
    private int from;
    private int to;

    public final static int TASK_LEN = 5000;

    public ForEach4(List<Cluster> arrayCluster, List<Point> arrayCentroidi, int from, int to) {
        this.arrayCluster = arrayCluster;
        this.arrayCentroidi = arrayCentroidi;
        this.from = from;
        this.to = to;
    }

    @Override
    protected void compute() {
        int len = to - from;
        if (len < TASK_LEN) {
            work(arrayCluster, arrayCentroidi, from, to);
        } else {
            int mid = (from + to) >>> 1;
            new ForEach4(arrayCluster, arrayCentroidi, from, mid).fork();
            new ForEach4(arrayCluster, arrayCentroidi, mid, to).fork();
        }
    }

    private void work(List<Cluster> arrayCluster, List<Point> arrayCentroidi, int from, int to) {
        System.out.println("D");
        for (int j = from; j < to; j++) {
            Point newCentroid = arrayCluster.get(j).updateCentroid();
            arrayCentroidi.add(j, newCentroid);
        }
    }
}

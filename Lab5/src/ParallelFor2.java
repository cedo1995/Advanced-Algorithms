import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.RecursiveAction;
import java.util.concurrent.atomic.AtomicInteger;

class ParallelFor2 extends RecursiveAction {

    private Map<Integer, Cluster> arrayConteniore;
    Map<Integer, Point> arrayDaAggiungere;
    private int from;
    private int to;
    private AtomicInteger a;

    public final static int TASK_LEN = 20;

    public ParallelFor2(Map<Integer, Cluster> arrayConteniore, Map<Integer, Point> arrayDaAggiungere, int from, int to, AtomicInteger a) {
        this.arrayConteniore = arrayConteniore;
        this.arrayDaAggiungere = arrayDaAggiungere;
        this.from = from;
        this.to = to;
        this.a = a;
    }

    @Override
    protected void compute() {
        int len = to - from;
        if (len < TASK_LEN) {
            work(arrayConteniore, arrayDaAggiungere, from, to);
        } else {
            int mid = (from + to) / 2;
           invokeAll(new ParallelFor2(arrayConteniore, arrayDaAggiungere, from, mid, a),
            new ParallelFor2(arrayConteniore, arrayDaAggiungere, mid, to, a));
        }

    }

    private void work(Map<Integer, Cluster> arrayConteniore, Map<Integer, Point> arrayDaAggiungere, int from, int to) {
        for (int j = from; j < to; j++) {
            arrayConteniore.put(j, new Cluster(arrayDaAggiungere.get(j), new ArrayList<City>()));
            a.decrementAndGet();
        }
    }
}
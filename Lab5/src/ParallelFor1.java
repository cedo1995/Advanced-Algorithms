import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveAction;
import java.util.concurrent.RecursiveTask;
import java.util.concurrent.atomic.AtomicInteger;

class ParallelFor1 extends RecursiveAction {

    private Map<Integer, Point> arrayConteniore;
    private List<City> arrayDaAggiungere;
    private int from;
    private int to;
    AtomicInteger a;

    public final static int TASK_LEN = 20;

    public ParallelFor1(Map<Integer, Point> arrayConteniore, List<City> arrayDaAggiungere, int from, int to, AtomicInteger a) {
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
            invokeAll(new ParallelFor1(arrayConteniore, arrayDaAggiungere, from, mid, a),
            new ParallelFor1(arrayConteniore, arrayDaAggiungere, mid, to, a));
        }
    }

    private void work(Map<Integer, Point>arrayConteniore, List<City> arrayDaAggiungere, int from, int to) {
        for (int j = from; j < to; j++) {
            arrayConteniore.put(j, arrayDaAggiungere.get(j).coordinates);
            a.decrementAndGet();
        }
    }
}
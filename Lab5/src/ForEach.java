import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveAction;
import java.util.concurrent.RecursiveTask;

class ForEach extends RecursiveAction {

    private List<Point> arrayConteniore;
    private List<City> arrayDaAggiungere;
    private int from;
    private int to;

    public final static int TASK_LEN = 5000;

    public ForEach(List<Point> arrayConteniore, List<City> arrayDaAggiungere, int from, int to) {
        this.arrayConteniore = arrayConteniore;
        this.arrayDaAggiungere = arrayDaAggiungere;
        this.from = from;
        this.to = to;
    }

    @Override
    protected void compute() {
        int len = to - from;
        if (len < TASK_LEN) {
            work(arrayConteniore, arrayDaAggiungere, from, to);
        } else {
            int mid = (from + to) >>> 1;
            new ForEach(arrayConteniore, arrayDaAggiungere, from, mid).fork();
            new ForEach(arrayConteniore, arrayDaAggiungere, mid, to).fork();
        }
    }

    private void work(List<Point> arrayConteniore, List<City> arrayDaAggiungere, int from, int to) {
        System.out.println("A");
        for (int j = from; j < to; j++) {
            arrayConteniore.add(j, arrayDaAggiungere.get(j).coordinates);
        }
    }
}

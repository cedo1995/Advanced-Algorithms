import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.RecursiveAction;

class ForEach2 extends RecursiveAction {

    private List<Cluster> arrayConteniore;
    private List<Point> arrayDaAggiungere;
    private int from;
    private int to;

    public final static int TASK_LEN = 5000;

    public ForEach2(List<Cluster> arrayConteniore, List<Point> arrayDaAggiungere, int from, int to) {
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
            new ForEach2(arrayConteniore, arrayDaAggiungere, from, mid).fork();
            new ForEach2(arrayConteniore, arrayDaAggiungere, mid, to).fork();
        }

    }

    private void work(List<Cluster> arrayContenitore, List<Point> arrayDaAggiungere, int from, int to) {
        System.out.println("B");
        for (int j = from; j < to; j++) {
            arrayContenitore.add(j, new Cluster(arrayDaAggiungere.get(j), new ArrayList<City>()));
        }
    }
}

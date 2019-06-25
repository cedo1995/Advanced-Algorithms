import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveAction;
import java.util.concurrent.RecursiveTask;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.function.Consumer;

class ParallelAction extends RecursiveAction {

    private AtomicInteger a;
    int k;
    private Consumer<Integer> consumer;

    public ParallelAction(AtomicInteger a, int k, Consumer<Integer> consumer)  {
        this.a = a;
        this.k = k;
        this.consumer = consumer;
    }

    @Override
    protected void compute() {
        consumer.accept(k);
        a.decrementAndGet();
//        if( 0 == a.decrementAndGet())
//        {
//            //a.notify();
//        }
    }

}

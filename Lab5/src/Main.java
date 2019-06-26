import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.ForkJoinPool;

public class Main {

    private static final String SAMPLE_CSV_FILE_PATH = "./src/cities-and-towns-of-usa.csv";

    public static void main(String[] args) {
        List<City> citiesList = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(SAMPLE_CSV_FILE_PATH))) {
            String line;
            br.readLine();
            while ((line = br.readLine()) != null) {
                String[] values = line.split(",");
                City city = new City(values);
                citiesList.add(city);
            }

            // Parametri
            ArrayList<Integer> threshold = new ArrayList<Integer>();
            threshold.add(-1);
            threshold.add(250);
            threshold.add(2000);
            threshold.add(5000);
            threshold.add(15000);
            threshold.add(50000);
            threshold.add(100000);

            int k = 50;

            int iter = 100; // iterazioni

            KMeans kmeans = new KMeans();

            //Prova
            // Seriale
            long startS = System.currentTimeMillis();
            List<Cluster> S = kmeans.serialKMeans(citiesList, k, iter);
            long timeS = System.currentTimeMillis() - startS;
            System.out.println(timeS);

            // Parallelo
            long startP = System.currentTimeMillis();
            List<Cluster> P = kmeans.parallelKMeans(citiesList, k, iter);
            long timeP = System.currentTimeMillis() - startP;
            System.out.println(timeP);

            // DOMANDA 1
//            ArrayList<Long> serialTimeD1 = new ArrayList<Long>();
//            ArrayList<Long> parallelTimeD1 = new ArrayList<Long>();
//
//            // Ordinamento città
//            citiesList.sort((a, b)-> a.getPopulation() - b.getPopulation());
//            Collections.reverse(citiesList);
//            int index_threshold = citiesList.size();
//
//            List<City> cities = new ArrayList<>(citiesList);
//            List<Cluster> test = kmeans.serialKMeans(cities, k, iter);
//            for (int tr: threshold) {
//
//                if(tr != -1) {
//                    for (int i = 0; i < citiesList.size(); i++) {
//                        if ((tr != -1) && citiesList.get(i).getPopulation() < tr) {
//                            index_threshold = i;
//                            break;
//                        }
//                    }
//                    cities = citiesList.subList(0, index_threshold);
//                }
//
//                // Seriale
//                long startD1S = System.currentTimeMillis();
//                List<Cluster> D1S = kmeans.serialKMeans(cities, k, iter);
//                long timeD1S = System.currentTimeMillis() - startD1S;
//                serialTimeD1.add(timeD1S);
//
//                // Parallelo
//                long startD1P = System.currentTimeMillis();
//                List<Cluster> D1P = kmeans.parallelKMeans(cities, k, iter);
//                long timeD1P = System.currentTimeMillis() - startD1P;
//                parallelTimeD1.add(timeD1P);
//            }
//            System.out.println("~~~~ Domanda 1: variare del dataset (sempre più piccolo)");
//            System.out.print("KMeans seriale: \n\t");
//            for (long time: serialTimeD1) {
//                System.out.print(time + " ");
//            }
//            System.out.print("\nKMeans parallelo: \n\t");
//            for (long time: parallelTimeD1) {
//                System.out.print(time + " ");
//            }
//
//
//
//            // DOMANDA 2
//            ArrayList<Long> serialTimeD2 = new ArrayList<Long>();
//            ArrayList<Long> parallelTimeD2 = new ArrayList<Long>();
//
//
//            for (int kappa=10; kappa <101; kappa++) {
//
//                // Seriale
//                long startD2S = System.currentTimeMillis();
//                List<Cluster> D2S = kmeans.serialKMeans(citiesList, kappa, iter);
//                long timeD2S = System.currentTimeMillis() - startD2S;
//                serialTimeD2.add(timeD2S);
//
//                // Parallelo
//                long startD2P = System.currentTimeMillis();
//                List<Cluster> D2P = kmeans.parallelKMeans(citiesList, kappa, iter);
//                long timeD2P = System.currentTimeMillis() - startD2P;
//                parallelTimeD2.add(timeD2P);
//            }
//            System.out.println("\n\n~~~~ Domanda 2: variare del numero di cluster (sempre più grande)");
//            System.out.print("KMeans seriale: \n\t");
//            for (long time: serialTimeD2) {
//                System.out.print(time + " ");
//            }
//            System.out.print("\nKMeans parallelo: \n\t");
//            for (long time: parallelTimeD2) {
//                System.out.print(time + " ");
//            }
//
//            // DOMANDA 3
//            ArrayList<Long> serialTimeD3 = new ArrayList<Long>();
//            ArrayList<Long> parallelTimeD3 = new ArrayList<Long>();
//
//
//            for (int iterazioni=10;  iterazioni<1000; iterazioni++) {
//
//                // Seriale
//                long startD3S = System.currentTimeMillis();
//                List<Cluster> D3S = kmeans.serialKMeans(citiesList, k, iterazioni);
//                long timeD3S = System.currentTimeMillis() - startD3S;
//                serialTimeD3.add(timeD3S);
//
//                // Parallelo
//                long startD3P = System.currentTimeMillis();
//                List<Cluster> D3P = kmeans.parallelKMeans(citiesList, k, iterazioni);
//                long timeD3P = System.currentTimeMillis() - startD3P;
//                parallelTimeD3.add(timeD3P);
//            }
//            System.out.println("\n\n~~~~ Domanda 3: variare del numero di iterazioni (sempre più grande)");
//            System.out.print("KMeans seriale: \n\t");
//            for (long time: serialTimeD3) {
//                System.out.print(time + " ");
//            }
//            System.out.print("\nKMeans parallelo: \n\t");
//            for (long time: parallelTimeD3) {
//                System.out.print(time + " ");
//            }


        }
        catch(Exception e) {
            System.out.println(e);
        }

    }
}

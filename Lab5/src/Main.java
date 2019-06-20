import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

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
            int threshold = 250; // popolazione minima
            int k = 50; // numero cluster
            int iter = 100; // iterazioni

            // Ordinamento e selezione delle città
            citiesList.sort((a, b)-> a.getPopulation() - b.getPopulation());
            Collections.reverse(citiesList);
            int index_threshold = citiesList.size();
            for(int i = 0; i< citiesList.size(); i++){
                if (citiesList.get(i).getPopulation()<threshold){
                    index_threshold = i;
                    break;
                }
            }
            System.out.println("Nr. totale città: " + citiesList.size());
            List<City> cities = citiesList.subList(0, index_threshold);
            System.out.println("Nr. città selezionate: " + cities.size());

            KMeans kmeans = new KMeans();

            // Non mi spiego perchè ma la prima volta che fa il seriaKMeans o il parallelKMeans ci mette di più,
            // Così se confronto subito un serial e un parallel il primo mi viene sballato..
            // sarà qualcosa sull'allocazione di memoria?
            List<Cluster> test = kmeans.serialKMeans(cities, k, iter);

            long startSer = System.currentTimeMillis();
            List<Cluster> serialClusters = kmeans.serialKMeans(cities, k, iter);
            long serialTime = System.currentTimeMillis() - startSer;

            long startPar = System.currentTimeMillis();
            List<Cluster> parallelClusters = kmeans.parallelKMeans(cities, k, iter);
            long parallelTime = System.currentTimeMillis() - startPar;

            System.out.println("Tempo K_Means seriale: "+ serialTime);
            System.out.println("Tempo K_Means parallelo: "+ parallelTime);

        }
        catch(Exception e) {
            System.out.println(e);
        }

    }
}

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
                //System.out.println(city);
                citiesList.add(city);
            }
            int threshold = 250;
            citiesList.sort((a,b )-> a.getPopulation() - b.getPopulation());
            Collections.reverse(citiesList);
            int index_threshold = citiesList.size();
            //TODO Da commentare il ciclo se viene fatto l'algoritmo senza soglia minima
            for(int i = 0; i< citiesList.size(); i++){
                if (citiesList.get(i).getPopulation()<threshold){
                    index_threshold = i;
                    break;
                }
            }
            System.out.println("Dimensione originale"+citiesList.size());
            List<City> cities = citiesList.subList(0,index_threshold);
            System.out.println("Dimensione dopo la rimozione"+cities.size());
            KMeans a =new KMeans();
            long start = System.currentTimeMillis();
            List<Cluster> clusters = a.serialKMeans(cities, 50, 100);
            long serialTime = System.currentTimeMillis()-start;
            System.out.println("Tempo K_Means seriale: "+ serialTime);

        }
        catch(Exception e) {
            System.out.println(e);
        }

    }
}
